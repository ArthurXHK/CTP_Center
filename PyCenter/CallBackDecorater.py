from CTPUserApiStruct import *
import threading


InstrumentList = []
InstrumentAllGetedEvent = threading.Event()
OnRtnMarketDataDec = WINFUNCTYPE(None, c_void_p, POINTER(CThostFtdcDepthMarketDataField))

def OnRtnMarketData(md, marketdata):
    print marketdata.contents.InstrumentID
    print marketdata.contents.LastPrice
OnRspQryInstrumentDec = WINFUNCTYPE(None, c_void_p, POINTER(CThostFtdcInstrumentField), POINTER(CThostFtdcRspInfoField), c_int, c_bool)
def OnRspQryInstrument(td, pInstrument, pRspInfo, nRequestID, bIsLast):
    print pInstrument.contents.InstrumentID
    InstrumentList.append(pInstrument.contents.InstrumentID)
    if bIsLast:
        InstrumentAllGetedEvent.set()
