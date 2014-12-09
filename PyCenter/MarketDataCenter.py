# -*- coding: UTF-8 -*-
from CTPUserApiStruct import *
from ctypes import *
from CallBackDecorater import *
import ConfigParser
import threading
from eventlet import sleep

__author__ = 'jebin'


MdDll = WinDLL('..\\lib\\thostmduserapi.dll')
TdDll = WinDLL('..\\lib\\thosttraderapi.dll')
FrameDll = WinDLL('..\\lib\\FrameDll.dll')

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
        self.__RegisterCallback()
        self.__lock = threading.Event()
        
    def __RegisterCallback(self):
        self.__pOnRtnMarketData = fnOnRtnMarketDataDec(OnRtnMarketData)
        FrameDll.CTP_RegOnRtnDepthMarketData(self.__msgQueue, self.__pOnRtnMarketData)
        self.__pOnRspQryInstrument = fnOnRspQryInstrumentDec(OnRspQryInstrument)
        FrameDll.CTP_RegOnRspQryInstrument(self.__msgQueue, self.__pOnRspQryInstrument)
    
    
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
        if 1 == FrameDll.MD_WaitForConnected(self.__md): print 'md is connected'
        else: return False
        if 1 == FrameDll.TD_WaitForConnected(self.__td): print 'td is connected'
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
            print 'error SubscribeAll'

    def Join(self, time = 100):
        sleep(time)

if __name__ == '__main__':
    center = MarketDataCenter()
    print center
    if center.Connect():
        center.QryInstrument('')
        
        center.SubscribeAll()
        
        center.Join()