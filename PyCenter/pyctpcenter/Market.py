#-*- coding=utf-8 -*-
"market api"
from ctp.futures import ApiStruct, MdApi
import threading
import logging
import copy
import time
import os
class Market(MdApi):
    def __init__(self, marketname, brokerid,
                 investorid, password, mdserver, *args,**kwargs):
        self.requestid=0
        self.requestlock = threading.Lock()
        self.name = marketname
        self.brokerid =brokerid
        self.investorid = investorid
        self.password = password
        self.mdserver = mdserver
        self.connectevent = threading.Event()
        
        self.logger = logging.getLogger('market[%s]'%self.name)
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
    def IsError(self, info):
        return info != None and info.ErrorID != 0
    def Connect(self):
        '''连接'''
        #创建log目录
        if not os.path.exists('log'):
            os.makedirs('log')
        if not os.path.exists('log\\%s'%self.name):
            os.makedirs('log\\%s'%self.name)
        self.Create('log\\%s'%self.name + '\\')
        for i in self.mdserver:
            self.RegisterFront(i)
        self.Init()
        
    def OnFrontConnected(self):
        self.logger.info('OnFrontConnected')
        self.Login(self.brokerid, self.investorid, self.password)
        
    def Login(self, brokerid, investorid, password):
        '''登陆行情端'''
        UserInfo = ApiStruct.ReqUserLogin(BrokerID=brokerid, UserID=investorid, Password=password)
        self.IncReqid()
        self.ReqUserLogin(UserInfo, self.requestid)
    def OnRspUserLogin(self, pRspUserLogin, pRspInfo, nRequestID, bIsLast):
        if self.IsError(pRspInfo):
            self.logger.error('OnRspUserLogin[%s]'%pRspInfo.ErrorMsg.encode('utf-8'))
        else:
            self.logger.info('OnRspUserLogin[%s]'%self.name)
            self.userinfo = copy.deepcopy(pRspUserLogin)
            self.connectevent.set()
    def WaitForConnected(self, timeout=10):
        '''等待连接'''
        return self.connectevent.wait(timeout)
    
    def Subscribe(self, instruments):
        self.SubscribeMarketData(instruments)
    def OnRtnDepthMarketData(self, pDepthMarketData):
        self.logger.info('%s: %f'%(pDepthMarketData.InstrumentID, pDepthMarketData.LastPrice))

def main():
    market = Market(marketname='market1', brokerid='1019',
                 investorid='00000002', password='123456', mdserver=['tcp://183.129.188.37:41213'])
    market2 = Market(marketname='market2', brokerid='1019',
                 investorid='00000003', password='123456', mdserver=['tcp://183.129.188.37:41213'])
    market.Connect()
    market.WaitForConnected()
    market.Subscribe(['IF1501', 'IF1502'])
    market2.Connect()
    market2.WaitForConnected()
    market2.Subscribe(['IF1501', 'IF1502'])
    
    market.Join()
    market2.Join()

if __name__ == '__main__': main()
