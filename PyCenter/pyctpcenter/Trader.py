#-*- coding=utf-8 -*-
"trader api"
from ctp.futures import ApiStruct, TraderApi
import threading
import logging
import copy
import time
import os
from time import sleep

OrderStatus = {'0': 'OST_AllTraded', 
               '1': 'OST_PartTradedQueueing', 
               '2': 'OST_PartTradedNotQueueing', 
               '3': 'OST_NoTradeQueueing', 
               '4': 'OST_NoTradeNotQueueing',
               '5': 'OST_Canceled',
               'a': 'OST_Unknown',
               'b': 'OST_NotTouched',
               'c': 'OST_Touched'}

class Trader(TraderApi):
    def __init__(self, tradername, brokerid,
                 investorid, password, tdserver, *args,**kwargs):
        #tradername: 交易者名,会显示到log中
        
        self.name = tradername
        self.brokerid =brokerid
        self.investorid = investorid
        self.password = password
        self.tdserver = tdserver
        
        self.requestid=0
        self.requestlock = threading.Lock()
        self.settlementevent = threading.Event()
        self.maxorderref = 0
        self.maxorderreflock = threading.Lock()
        self.orders = {}
        self.orderslock = threading.Lock()
        self.instruments = {}
        self.instrumentlock = threading.Lock()
        self.instrumentgeted = threading.Event()
        self.position = {}
        self.positionlock = threading.Lock()
        
        #logger设置
        self.logger = logging.getLogger('trader[%s]'%self.name)
        self.logger.setLevel(logging.DEBUG)
        #输出到当前日期log文件
        self.time = time.strftime('%Y%m%d', time.localtime(time.time()))
        if not os.path.exists('log'):
            os.makedirs('log')
        if not os.path.exists('log\\log'):
            os.makedirs('log\\log')
        fh = logging.FileHandler('log\\log\\%s.log'%self.time)
        fh.setLevel(logging.DEBUG)
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)
    def IncReqid(self):
        '''增加requestid'''
        with self.requestlock:
            self.requestid+=1
    def Connect(self):
        '''连接'''
        #创建log目录
        if not os.path.exists('log'):
            os.makedirs('log')
        if not os.path.exists('log\\%s'%self.name):
            os.makedirs('log\\%s'%self.name)
        self.Create('log\\%s'%self.name + '\\')
        for i in self.tdserver:
            self.RegisterFront(i)
        self.SubscribePrivateTopic(ApiStruct.TERT_QUICK)
        self.SubscribePublicTopic(ApiStruct.TERT_QUICK)
        self.Init()
    def OnFrontConnected(self):
        self.logger.info('OnFrontConnected')
        self.Login(self.brokerid, self.investorid, self.password)
    def OnFrontDisConnected(self, reason):
        self.logger.info('OnFrontDisConnected[%s]'%str(reason))
    def OnHeartBeatWarning(self, time):
        self.logger.error(str(time))
        
    def OnRspError(self, info, RequestId, IsLast):
        if self.IsNoError(info):
            self.logger.error()
    def IsError(self, info):
        return info != None and info.ErrorID != 0

    def Login(self, brokerid, investorid, password):
        '''登陆交易端'''
        UserInfo = ApiStruct.ReqUserLogin(BrokerID=brokerid, UserID=investorid, Password=password)
        self.IncReqid()
        self.ReqUserLogin(UserInfo, self.requestid)

    def OnRspUserLogin(self, pRspUserLogin, pRspInfo, nRequestID, bIsLast):
        if self.IsError(pRspInfo):
            self.logger.error('OnRspUserLogin[%s]'%pRspInfo.ErrorMsg.encode('utf-8'))
        else:
            self.logger.info('OnRspUserLogin[%s]'%self.name)
            self.userinfo = copy.deepcopy(pRspUserLogin)
            self.SettlementInfoConfirm()

    def SettlementInfoConfirm(self):
        '''结算确认：需要结算确认才可以进行其他操作'''
        pSettlementInfoConfirm = ApiStruct.SettlementInfoConfirm(self.brokerid, self.investorid)
        self.IncReqid()
        self.ReqSettlementInfoConfirm(pSettlementInfoConfirm, self.requestid)
        
    def OnRspSettlementInfoConfirm(self, pSettlementInfoConfirm, pRspInfo, nRequestID, bIsLast):
        if self.IsError(pRspInfo):
            self.logger.error('OnRspSettlementInfoConfirm[%s]'%pRspInfo.ErrorMsg.encode('utf-8'))
        else:
            self.logger.info('OnRspSettlementInfoConfirm')
            self.settlementevent.set()
    def WaitForConnected(self, timeout=10):
        '''等待连接'''
        return self.settlementevent.wait(timeout)
    def SendOrder(self, instrument, direction, offsetflag, volume, price):
        '''发送报单'''
        if offsetflag != ApiStruct.OF_Open:
            #平仓则判定是否当下session持仓数量是否合法
            with self.positionlock:
                ind = (instrument, str(1 - int(direction)))#转换相反持仓信息index
                if ind not in self.position or len(self.position[ind]) == 0:
                    self.logger.error('SendOrder[%s, %s]: not exist volume'%ind)
                    return
                else:
                    ans = 0
                    for i in self.position[ind]:
                        ans += i.Volume
                    if ans < volume:
                        self.logger.error('SendOrder[%s, %s]: No enough volume'%ind)
                        return
                
        #下单
        with self.maxorderreflock:
            self.maxorderref+=1
            pInputOrder = ApiStruct.InputOrder(
                                           BrokerID=self.brokerid,
                                           InvestorID=self.investorid,
                                           InstrumentID=instrument,
                                           OrderRef=str(self.maxorderref),
                                           OrderPriceType=ApiStruct.OPT_LimitPrice,
                                           Direction=direction,
                                           CombOffsetFlag=offsetflag,
                                           CombHedgeFlag=ApiStruct.HF_Speculation,
                                           LimitPrice=price,
                                           VolumeTotalOriginal=volume,
                                           TimeCondition=ApiStruct.TC_GFD,
                                           VolumeCondition=ApiStruct.VC_AV,
                                           MinVolume=1,
                                           ContingentCondition=ApiStruct.CC_Immediately,
                                           )
            self.IncReqid()
            self.ReqOrderInsert(pInputOrder, self.requestid)
    
    def OnRspOrderInsert(self, pInputOrder, pRspInfo, nRequestID, bIsLast):
        if self.IsError(pRspInfo):
            self.logger.error('Order[%s,%s]: OnRspOrderInsert[%s]'%(pInputOrder.OrderRef, 
                                                                    pInputOrder.InstrumentID, 
                                                                    pRspInfo.ErrorMsg.encode('utf-8')))
    def OnErrRtnOrderInsert(self, pInputOrder, pRspInfo):
        if self.IsError(pRspInfo):
            self.logger.error('Order[%s,%s]: OnErrRtnOrderInsert[%s]'%(pInputOrder.OrderRef, 
                                                                       pInputOrder.InstrumentID, 
                                                                       pRspInfo.ErrorMsg.encode('utf-8')))
        
    def OnRtnOrder(self, pOrder):
        '''过滤非本session报单回报'''
        if self.userinfo.SessionID == pOrder.SessionID:
            self.logger.info('Order[%s,%s] -> status[%s]'%(pOrder.OrderRef, pOrder.InstrumentID, OrderStatus[pOrder.OrderStatus]))
            with self.orderslock:
                self.orders[pOrder.OrderRef] = copy.deepcopy(pOrder)
    def ProcessTrade(self, pTrade):
        '''处理成交信息转换为持仓信息'''
        with self.positionlock:
            if pTrade.Direction == ApiStruct.D_Buy:
                if pTrade.OffsetFlag == ApiStruct.OF_Open:
                    ind = (pTrade.InstrumentID, pTrade.Direction)
                    if ind not in self.position:
                        self.position[ind] = []
                    self.position[ind].append(copy.deepcopy(pTrade))
                else:
                    ind = (pTrade.InstrumentID, str(1 - int(pTrade.Direction)))
                    if ind not in self.position or len(self.position[ind]) == 0:
                        self.logger.error('平卖单仓位不足')
                    while pTrade.Volume != 0:
                        if self.position[ind][0].Volume > pTrade.Volume:
                            self.position[ind][0].Volume -= pTrade.Volume
                            break
                        else:
                            pTrade.Volume -= self.position[ind][0].Volume
                            self.position[ind].pop(0)
                            
            elif pTrade.Direction == ApiStruct.D_Sell:
                if pTrade.OffsetFlag == ApiStruct.OF_Open:
                    ind = (pTrade.InstrumentID, pTrade.Direction)
                    if ind not in self.position:
                        self.position[ind] = []
                    self.position[ind].append(copy.deepcopy(pTrade))
                else:
                    ind = (pTrade.InstrumentID, str(1 - int(pTrade.Direction)))
                    if ind not in self.position or len(self.position[ind]) == 0:
                        self.logger.error('平买单仓位不足')
                    while pTrade.Volume != 0:
                        if self.position[ind][0].Volume > pTrade.Volume:
                            self.position[ind][0].Volume -= pTrade.Volume
                            break
                        else:
                            pTrade.Volume -= self.position[ind][0].Volume
                            self.position[ind].pop(0)
            #显示持仓信息log
            ans = 0
            for i in self.position[(pTrade.InstrumentID, 
                                    pTrade.Direction if pTrade.OffsetFlag == ApiStruct.OF_Open else str(1 - int(pTrade.Direction)))]:
                ans += i.Volume
            self.logger.info('Position[%s, %s]: %d'%(pTrade.InstrumentID,
                                                     pTrade.Direction,
                                                     ans))
    def OnRtnTrade(self, pTrade):
        
        with self.orderslock:
            ref = pTrade.OrderRef
            #过滤非本session成交信息
            if ref in self.orders and self.orders[ref].OrderSysID == pTrade.OrderSysID:
                self.ProcessTrade(pTrade)
    

    def CancelOrder(self, orderref):
        '''撤单：根据当前trader的orderref'''
        with self.orderslock:
            if orderref in self.orders:
                torder = self.orders[orderref]
                order = ApiStruct.InputOrderAction(BrokerID=torder.BrokerID,
                                                   InvestorID=torder.InvestorID,
                                                   OrderRef=torder.OrderRef,
                                                   FrontID=torder.FrontID,
                                                   SessionID=torder.SessionID,
                                                   ExchangeID=torder.ExchangeID,
                                                   OrderSysID=torder.OrderSysID,
                                                   ActionFlag=ApiStruct.AF_Delete,
                                                   InstrumentID=torder.InstrumentID
                                                   )
                self.IncReqid()
                self.ReqOrderAction(order, self.requestid)
                self.logger.info('Order[%s]: CancelOrder sended'%orderref)
            else:
                self.logger.error('Order[%s] not exist'%orderref)
    def OnErrRtnOrderAction(self, pOrderAction, pRspInfo):
        if self.IsError(pRspInfo):
            self.logger.error('Order[%s]: Action error[%s]'%(pOrderAction.OrderRef, pRspInfo.ErrorMsg.encode('utf-8')))
    
    def QryInstrument(self, instrument):
        '''查询合约'''
        inst = ApiStruct.QryInstrument(InstrumentID=instrument)
        self.IncReqid()
        self.ReqQryInstrument(inst, self.requestid)
    def OnRspQryInstrument(self, pInstrument, pRspInfo, nRequestID, bIsLast):
        if self.IsError(pRspInfo):
            self.logger.error('OnRspQryInstrument[%s]'%pRspInfo.ErrorMsg.encode('utf-8'))
        else:
            with self.instrumentlock:
                self.instruments[pInstrument.InstrumentID] = copy.deepcopy(pInstrument)
                if bIsLast:
                    self.instrumentgeted.set()
                    self.logger.info('OnRspQryInstrument[all instruments getted]')
    def WaitForInstrumentGeted(self, timeout=10):
        '''等待QryInstrument回调完成'''
        return self.instrumentgeted.wait(timeout)
    
    def QryInstrumentMarginRate(self, instrument):
        pQryInstrumentMarginRate = ApiStruct.QryInstrumentMarginRate(BrokerID=self.userinfo.BrokerID,
                                                                     InvestorID=self.userinfo.UserID,
                                                                     InstrumentID=instrument,
                                                                     HedgeFlag=ApiStruct.HF_Speculation)
        self.IncReqid()
        self.ReqQryInstrumentMarginRate(pQryInstrumentMarginRate, self.requestid)
    def QryAllInstrumentMarginRate(self):
        ok = self.WaitForInstrumentGeted()
        if ok:
            for i in  self.instruments:
                if len(i) < 8:
                    sleep(0.5)
                    self.QryInstrumentMarginRate(i)
            self.logger.info('QryAllInstrumentMarginRate done')
        else:
            self.logger.error('instruments not getted')
    def OnRspQryInstrumentMarginRate(self, pInstrumentMarginRate, pRspInfo, nRequestID, bIsLast):
        print '%s: %s'%(pInstrumentMarginRate.InstrumentID, pInstrumentMarginRate.LongMarginRatioByMoney)
    
    def QryTradingAccount(self):
        pQryTradingAccount = ApiStruct.QryTradingAccount(BrokerID=self.brokerid, InvestorID=self.investorid)
        self.IncReqid()
        self.ReqQryTradingAccount(pQryTradingAccount, self.requestid)
    def OnRspQryTradingAccount(self, pTradingAccount, pRspInfo, nRequestID, bIsLast):
        pass
    def QryMarketData(self, instrument):
        ok = self.settlementevent.wait(5)
        if ok:
            Instrument = ApiStruct.QryDepthMarketData(instrument)
            self.requestid+=1
            self.ReqQryDepthMarketData(Instrument, self.requestid)
        else:self.logger.error('QryMarketData timeout')
    def OnRspQryDepthMarketData(self, pDepthMarketData, pRspInfo, nRequestID, bIsLast):
        pass
        
def main():
    user = Trader(tradername='t2', brokerid="1019",investorid="00000002",password="123456",tdserver=["tcp://183.129.188.37:41205"])
    user.Connect()
    user.WaitForConnected()
    user.QryInstrument('')
    user.WaitForInstrumentGeted()
    user.QryTradingAccount()
    
    while True:
        user.SendOrder('IF1501', ApiStruct.D_Buy, ApiStruct.OF_Open, 10, 3700)
        sleep(2)
        user.SendOrder('IF1501', ApiStruct.D_Sell, ApiStruct.OF_CloseToday, 10, 3500)
    #user.CancelOrder('1')
    #user.QryAllInstrumentMarginRate()
    user.Join()

if __name__=="__main__": main()
