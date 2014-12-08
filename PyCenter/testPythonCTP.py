#!/usr/bin/env python
# -*- coding: utf-8 -*-

from CTPUserApiStruct import *
from ctypes import *
from time import sleep

MdDll = WinDLL('..\\lib\\thostmduserapi.dll')
TdDll = WinDLL('..\\lib\\thosttraderapi.dll')
FrameDll = WinDLL('..\\lib\\FrameDll.dll')

MARKETDATAFUN = WINFUNCTYPE(None, c_void_p, POINTER(CThostFtdcDepthMarketDataField))

def OnRtnMarketData(pMd, data):
    print data.contents.InstrumentID
    print data.contents.LastPrice
    
pOnRtnMarketData = MARKETDATAFUN(OnRtnMarketData)
print pOnRtnMarketData
md = FrameDll.MD_CreateMdApi();

md_msgQueue = FrameDll.CTP_CreateMsgQueue()

FrameDll.MD_RegMsgQueue2MdApi(md, md_msgQueue)

FrameDll.CTP_StartMsgQueue(md_msgQueue)

FrameDll.MD_Connect(md, 'stream', 'tcp://183.129.188.37:41213', '1019', '0000002', '123456');

FrameDll.CTP_RegOnRtnDepthMarketData(md_msgQueue, pOnRtnMarketData)

ok = FrameDll.MD_WaitForConnected(md)


print ok
if ok == 1:
    print 'connect seccess'
    FrameDll.MD_Subscribe(md, 'IF1412,IF1501,ag1412', '')
    
else:
    print 'connect error'

    
sleep(100)