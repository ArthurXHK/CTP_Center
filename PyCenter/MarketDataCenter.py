# -*- coding: UTF-8 -*-
import sys
from CTPUserApiStruct import *
from ctypes import *
from CallBackDecorater import *
import ConfigParser
from eventlet import sleep
from multiprocessing import Process
import logging
import multiprocessing

__author__ = 'jebin'


MdDll = WinDLL('..\\lib\\thostmduserapi.dll')
TdDll = WinDLL('..\\lib\\thosttraderapi.dll')
FrameDll = WinDLL('..\\lib\\FrameDll.dll')

InstrumentList = []
InstrumentAllGetedEvent = multiprocessing.Event()
MainOverEvent = multiprocessing.Event()

def OnConnect(pApi, pRspUserLogin, result):
    print '%x now: %d' % (pApi, result)
    sys.stdout.flush()
def OnDisconnect(pApi, pRspInfo, step):
    print '%x now: %d' % (pApi, step)
    sys.stdout.flush()

def OnRtnMarketData(pMdUserApi, pDepthMarketData):
    print pDepthMarketData.contents.LastPrice
    sys.stdout.flush()
def OnRspQryInstrument(pTraderApi, pInstrument, pRspInfo, nRequestID, bIsLast):
    InstrumentList.append(pInstrument.contents.InstrumentID)
    if bIsLast:
        InstrumentAllGetedEvent.set()
        
class MarketDataCenter(object):
    '''行情回报中心'''
    def __str__(self):
        res = "PyCtpCenter: "
        config = ConfigParser.ConfigParser()
        config.read(self.__inifile)    
        res += config.items(self.__section).__str__();
        return res
    __repr__ = __str__
    
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
        self.__logger = logging.getLogger('MarketCenter')
        self.__logger.setLevel(logging.DEBUG)
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        ch.setFormatter(formatter)
        self.__logger.addHandler(ch)
        self.__RegisterCallback()
        self.__logger.info('init finished')
    def Release(self):
        FrameDll.TD_ReleaseTdApi(self.__td);
        FrameDll.MD_ReleaseMdApi(self.__md);
        FrameDll.CTP_ReleaseMsgQueue(self.__msgQueue);
    def __RegisterCallback(self):
        self.__pOnRtnMarketData = fnOnRtnMarketDataDec(OnRtnMarketData)
        FrameDll.CTP_RegOnRtnDepthMarketData(self.__msgQueue, self.__pOnRtnMarketData)
        self.__pOnRspQryInstrument = fnOnRspQryInstrumentDec(OnRspQryInstrument)
        FrameDll.CTP_RegOnRspQryInstrument(self.__msgQueue, self.__pOnRspQryInstrument)
        self.__pOnConnect = fnOnConnectDec(OnConnect)
        FrameDll.CTP_RegOnConnect(self.__msgQueue, self.__pOnConnect)
        self.__pOnDisConnect = fnOnDisconnectDec(OnDisconnect)
        FrameDll.CTP_RegOnDisconnect(self.__msgQueue, self.__pOnDisConnect)
        self.__logger.info('register callback finish')
        
    
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
                            THOST_TERT_RESTART,
                            '', '')
        if 1 == FrameDll.MD_WaitForConnected(self.__md): 
            print 'md is connected' 
            sys.stdout.flush()
        else: return False
        if 1 == FrameDll.TD_WaitForConnected(self.__td): 
            print 'td is connected'
            sys.stdout.flush()
        else: return False
        return True
    
    def QryInstrument(self, instruments):
        FrameDll.TD_ReqQryInstrument(self.__td, instruments)
    
        
    def Subscribe(self, instruments):
        FrameDll.MD_Subscribe(self.__md, instruments, '')
    def SubscribeAll(self):
        if InstrumentAllGetedEvent.wait(10):
            for i in InstrumentList: self.Subscribe(i)
        else:
            self.__logger.error('Subscribeall error')
    def run(self):
        while self.Connect() == False:
            self.__logger.error('connect error')
            
        else:
            self.__logger.info('connect success')
            self.QryInstrument('')
            self.__logger.info('qryinstrument finish')
            #self.SubscribeAll()
            self.Subscribe('IF1412')
            self.__logger.info('subscribeall finish')

def main():
    center = MarketDataCenter()
    center.run()
    MainOverEvent.wait()
    center.Release()
    print 'main over'
    sys.stdout.flush()
    
if __name__ == '__main__':
    process = Process(target=main, args=tuple())
    
    while True:
        msg = raw_input('input: ')
        if msg == 'stop':
            MainOverEvent.set()
            sleep(10)
            break
        elif msg == 'start':
            process.start()
        else:
            print 'no operation'
            