# -*- coding: UTF-8 -*-
import sys
from CTPUserApiStruct import *
from ctypes import *
from CallBackDecorater import *
import ConfigParser
from eventlet import sleep
import logging
import copy
import threading

from MarketDataCenter import MdDll, TdDll, FrameDll

__author__ = 'jebin'



Orders = {}

def OnConnect(pApi, pRspUserLogin, result):
    print 'User %x status: %d' % (pApi, result)
def OnDisconnect(pApi, pRspInfo, step):
    print 'User %x status: %d' % (pApi, step)

def OnRspError(pApi, pRspInfo, nRequestID, bIsLast):
    pass
def OnRspOrderInsert(pTraderApi, pInputOrder, pRspInfo, nRequestID, bIsLast):
    print 'User %x insert order %s' % (pTraderApi, pInputOrder.contents.OrderRef)
    
def OnRspOrderAction(pTraderApi, pInputOrderAction, pRspInfo, nRequestID, bIsLast):
    if pRspInfo.contents.ErrorID == 0:
        print 'User %x cancel order %s' % (pTraderApi, pInputOrderAction.contents.OrderRef)
    else:
        print pRspInfo.contents.ErrorMsg.encode('utf-8')
def OnRspQryInstrumentCommissionRate(pTraderApi, pInstrumentCommissionRate, pRspInfo, nRequestID, bIsLast):
    pass
def OnRspQryInvestorPosition(pTraderApi, pInvestorPosition, pRspInfo, nRequestID, bIsLast):
    pass
def OnRspQryInvestorPositionDetail(pTraderApi, pInvestorPositionDetail, pRspInfo, nRequestID, bIsLast):
    pass
def OnRspQryOrder(pTraderApi, pOrder, pRspInfo, nRequestID, bIsLast):
    pass
def OnRspQryTrade(pTraderApi, pTrade, pRspInfo, nRequestID, bIsLast):
    pass
def OnRtnInstrumentStatus(pTraderApi, pInstrumentStatus):
    pass
def OnRspQryTradingAccount(pTraderApi, pTradingAccount, pRspInfo, nRequestID, bIsLast):
    pass

def OnRtnOrder(pTraderApi, pOrder):
    Orders[int(pOrder.contents.OrderRef)] = copy.deepcopy(pOrder.contents)
    print 'User %x \'s order %s status %s' % (pTraderApi, pOrder.contents.OrderRef, pOrder.contents.OrderStatus)
    
def OnRtnTrade(pTraderApi, pTrade):
    pass

class Trader(object):
    
    def __init__(self, inifile = '../server.ini', section = 'SimServer'):
        self.__inifile = inifile
        self.__section = section
        config = ConfigParser.ConfigParser()
        config.read(inifile)
        self.__brokerid = config.get(section, 'brokerid')
        self.__mdserver = config.get(section, 'mdserver')
        self.__tdserver = config.get(section, 'tdserver')
        self.__investorid = config.get(section, 'investorid')
        self.__password = config.get(section, 'password')
        self.__streampath = config.get(section, 'streampath')
        self.__logpath = config.get(section, 'logpath')
        self.__mongoip = config.get(section, 'mongoip')
        self.__database = config.get(section, 'database')
        self.__md = FrameDll.MD_CreateMdApi()
        self.__td = FrameDll.TD_CreateTdApi()
        self.__msgQueue = FrameDll.CTP_CreateMsgQueue()
        FrameDll.MD_RegMsgQueue2MdApi(self.__md, self.__msgQueue)
        FrameDll.TD_RegMsgQueue2TdApi(self.__td, self.__msgQueue)
        FrameDll.CTP_StartMsgQueue(self.__msgQueue)
        # set logger
        self.__logger = logging.getLogger('Trader')
        self.__logger.setLevel(logging.DEBUG)
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        ch.setFormatter(formatter)
        self.__logger.addHandler(ch)
        self.__RegisterCallback()
        self.__logger.info('init finished')
        
    def __RegisterCallback(self):
        self.__pOnConnect = fnOnConnectDec(OnConnect)
        FrameDll.CTP_RegOnConnect(self.__msgQueue, self.__pOnConnect)
        self.__pOnDisConnect = fnOnDisconnectDec(OnDisconnect)
        FrameDll.CTP_RegOnDisconnect(self.__msgQueue, self.__pOnDisConnect)
        self.__pOnRspOrderAction = fnOnRspOrderActionDec(OnRspOrderAction)
        FrameDll.CTP_RegOnRspOrderAction(self.__msgQueue, self.__pOnRspOrderAction)
        self.__pOnRspOrderInsert = fnOnRspOrderInsertDec(OnRspOrderInsert)
        FrameDll.CTP_RegOnRspOrderInsert(self.__msgQueue, self.__pOnRspOrderInsert)
        self.__pOnRspQryInvestorPosition = fnOnRspQryInvestorPositionDec(OnRspQryInvestorPosition)
        FrameDll.CTP_RegOnRspQryInvestorPosition(self.__msgQueue, self.__pOnRspQryInvestorPosition)
        self.__pOnRspQryInvestorPositionDetail = fnOnRspQryInvestorPositionDetailDec(OnRspQryInvestorPositionDetail)
        FrameDll.CTP_RegOnRspQryInvestorPositionDetail(self.__msgQueue, self.__pOnRspQryInvestorPositionDetail)
        self.__pOnRspQryOrder = fnOnRspQryOrderDec(OnRspQryOrder)
        FrameDll.CTP_RegOnRspQryOrder(self.__msgQueue, self.__pOnRspQryOrder)
        self.__pOnRspQryTradingAccount = fnOnRspQryTradingAccountDec(OnRspQryTradingAccount)
        FrameDll.CTP_RegOnRspQryTradingAccount(self.__msgQueue, self.__pOnRspQryTradingAccount)
        self.__pOnRtnOrder = fnOnRtnOrderDec(OnRtnOrder)
        FrameDll.CTP_RegOnRtnOrder(self.__msgQueue, self.__pOnRtnOrder)
        self.__pOnRtnTrade = fnOnRtnTradeDec(OnRtnTrade)
        FrameDll.CTP_RegOnRtnTrade(self.__msgQueue, self.__pOnRtnTrade)
        
    def Connect(self):
        FrameDll.MD_Connect(self.__md,
                            self.__streampath, 
                            self.__mdserver, 
                            self.__brokerid, 
                            self.__investorid, 
                            self.__password)
        
        FrameDll.TD_Connect(self.__td,
                            self.__streampath, 
                            self.__tdserver, 
                            self.__brokerid, 
                            self.__investorid, 
                            self.__password,
                            THOST_TERT_QUICK,
                            '', '')
        if 1 == FrameDll.MD_WaitForConnected(self.__md): 
            print 'md is connected' 
        else: return False
        if 1 == FrameDll.TD_WaitForConnected(self.__td): 
            print 'td is connected'
        else: return False
        return True

    def Release(self):
        FrameDll.TD_ReleaseTdApi(self.__td)
        FrameDll.MD_ReleaseMdApi(self.__md)
        FrameDll.CTP_ReleaseMsgQueue(self.__msgQueue)
        
    def SendOrder(self, instrument, direction, OffsetFlag, volume, price):
        FrameDll.TD_SendOrder(self.__td, -1, instrument, '', 
                              c_char(direction), 
                              OffsetFlag, '1', c_int(volume), 
                              c_double(price), 
                              c_char(THOST_FTDC_OPT_LimitPrice), 
                              c_char(THOST_FTDC_TC_GFD), 
                              c_char(THOST_FTDC_CC_Immediately), 
                              c_double(0), 
                              c_char(THOST_FTDC_VC_AV))
    def CancelOrder(self, orderref):
        
        if orderref in Orders:
            FrameDll.TD_CancelOrder(self.__td, byref(Orders[orderref]))
        else:
            self.__logger.warn('orderref %d not found' % orderref)


def main():
    trader = Trader()
    while trader.Connect() == False:
        pass
    
    while True:
        msg = raw_input()
        if msg == 'get':
            trader.SendOrder('IF1412', '0', '0', 2, 3390)
        elif msg == 'cancel':
            trader.CancelOrder(1)
        elif msg == 'end':
            trader.Release()
            print 'end now'
            break
if __name__ == '__main__':
    main()
        