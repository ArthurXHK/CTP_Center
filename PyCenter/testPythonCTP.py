# -*- coding : utf-8 -*-

from ctypes import *


MdDll = WinDLL('..\\lib\\thostmduserapi.dll')
TdDll = WinDLL('..\\lib\\thosttraderapi.dll')
FrameDll = WinDLL('..\\lib\\FrameDll.dll')




md = FrameDll.MD_CreateMdApi();
md_msgQueue = FrameDll.CTP_CreateMsgQueue()

FrameDll.MD_RegMsgQueue2MdApi(md, md_msgQueue)

FrameDll.CTP_StartMsgQueue(md_msgQueue)

FrameDll.MD_Connect(md, 'stream', 'tcp://183.129.188.37:41213', '1019', '0000002', '123456');

ok = c_bool(FrameDll.MD_WaitForConnected(md))
print ok
if ok == 1:
    print 'connect seccess'
    
else:
    print 'connect error'