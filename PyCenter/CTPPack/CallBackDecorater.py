# -*- coding: UTF-8 -*-
from ctypes import *
from CTPUserApiStruct import *

#行情回报
fnOnRtnMarketDataDec = WINFUNCTYPE(None, c_void_p, POINTER(CThostFtdcDepthMarketDataField))
def OnRtnMarketData(pMdUserApi, pDepthMarketData):
    pass

#查询合约回报
fnOnRspQryInstrumentDec = WINFUNCTYPE(None, c_void_p, POINTER(CThostFtdcInstrumentField), POINTER(CThostFtdcRspInfoField), c_int, c_bool)
def OnRspQryInstrument(pTraderApi, pInstrument, pRspInfo, nRequestID, bIsLast):
    pass

#连接回报
fnOnConnectDec = WINFUNCTYPE(None, c_void_p, POINTER(CThostFtdcRspUserLoginField), c_int)
def OnConnect(pApi, pRspUserLogin, result):
    pass

fnOnDisconnectDec = WINFUNCTYPE(None, c_void_p, POINTER(CThostFtdcRspInfoField), c_int)
def OnDisconnect(pApi, pRspInfo, step):
    pass

fnOnErrRtnOrderActionDec = WINFUNCTYPE(None, c_void_p, POINTER(CThostFtdcOrderActionField), POINTER(CThostFtdcRspInfoField))
def OnErrRtnOrderAction(pTraderApi, pOrderAction, pRspInfo):
    pass

fnOnErrRtnOrderInsertDec = WINFUNCTYPE(None, c_void_p, POINTER(CThostFtdcInputOrderField), POINTER(CThostFtdcRspInfoField))
def OnErrRtnOrderInsert(pTraderApi, pInputOrder, pRspInfo):
    pass

fnOnRspErrorDec = WINFUNCTYPE(None, c_void_p, POINTER(CThostFtdcRspInfoField), c_int, c_bool)
def OnRspError(pApi, pRspInfo, nRequestID, bIsLast):
    pass

fnOnRspOrderActionDec = WINFUNCTYPE(None, c_void_p, POINTER(CThostFtdcInputOrderActionField), POINTER(CThostFtdcRspInfoField), c_int, c_bool)
def OnRspOrderAction(pTraderApi, pInputOrderAction, pRspInfo, nRequestID, bIsLast):
    pass

fnOnRspOrderInsertDec = WINFUNCTYPE(None, c_void_p, POINTER(CThostFtdcInputOrderField), POINTER(CThostFtdcRspInfoField), c_int, c_bool)
def OnRspOrderInsert(pTraderApi, pInputOrder, pRspInfo, nRequestID, bIsLast):
    pass

fnOnRspQryDepthMarketDataDec = WINFUNCTYPE(None, c_void_p, POINTER(CThostFtdcDepthMarketDataField), POINTER(CThostFtdcRspInfoField), c_int, c_bool)
def OnRspQryDepthMarketData(pTraderApi, pDepthMarketData, pRspInfo, nRequestID, bIsLast):
    pass



fnOnRspQryInstrumentCommissionRateDec = WINFUNCTYPE(None, c_void_p, POINTER(CThostFtdcInstrumentCommissionRateField), POINTER(CThostFtdcRspInfoField), c_int, c_bool)
def OnRspQryInstrumentCommissionRate(pTraderApi, pInstrumentCommissionRate, pRspInfo, nRequestID, bIsLast):
    pass


fnOnRspQryInstrumentMarginRateDec = WINFUNCTYPE(None, c_void_p, POINTER(CThostFtdcInstrumentMarginRateField), POINTER(CThostFtdcRspInfoField), c_int, c_bool)
def OnRspQryInstrumentMarginRate(pTraderApi, pInstrumentMarginRate, pRspInfo, nRequestID, bIsLast):
    pass


fnOnRspQryInvestorPositionDec = WINFUNCTYPE(None, c_void_p, POINTER(CThostFtdcInvestorPositionField), POINTER(CThostFtdcRspInfoField), c_int, c_bool)
def OnRspQryInvestorPosition(pTraderApi, pInvestorPosition, pRspInfo, nRequestID, bIsLast):
    pass


fnOnRspQryInvestorPositionDetailDec = WINFUNCTYPE(None, c_void_p, POINTER(CThostFtdcInvestorPositionDetailField), POINTER(CThostFtdcRspInfoField), c_int, c_bool)
def OnRspQryInvestorPositionDetail(pTraderApi, pInvestorPositionDetail, pRspInfo, nRequestID, bIsLast):
    pass


fnOnRspQryOrderDec = WINFUNCTYPE(None, c_void_p, POINTER(CThostFtdcOrderField), POINTER(CThostFtdcRspInfoField), c_int, c_bool)
def OnRspQryOrder(pTraderApi, pOrder, pRspInfo, nRequestID, bIsLast):
    pass


fnOnRspQryTradeDec = WINFUNCTYPE(None, c_void_p, POINTER(CThostFtdcTradeField), POINTER(CThostFtdcRspInfoField), c_int, c_bool)
def OnRspQryTrade(pTraderApi, pTrade, pRspInfo, nRequestID, bIsLast):
    pass

fnOnRspQrySettlementInfoDec = WINFUNCTYPE(None, c_void_p, POINTER(CThostFtdcSettlementInfoField), POINTER(CThostFtdcRspInfoField), c_int, c_bool)
def OnRspQrySettlementInfo(pTraderApi, pSettlementInfo, pRspInfo, nRequestID, bIsLast):
    pass


fnOnRspQryTradingAccountDec = WINFUNCTYPE(None, c_void_p, POINTER(CThostFtdcTradingAccountField), POINTER(CThostFtdcRspInfoField), c_int, c_bool)
def OnRspQryTradingAccount(pTraderApi, pTradingAccount, pRspInfo, nRequestID, bIsLast):
    pass


fnOnRtnInstrumentStatusDec = WINFUNCTYPE(None, c_void_p, POINTER(CThostFtdcInstrumentStatusField))
def OnRtnInstrumentStatus(pTraderApi, pInstrumentStatus):
    pass

fnOnRtnOrderDec = WINFUNCTYPE(None, c_void_p, POINTER(CThostFtdcOrderField))
def OnRtnOrder(pTraderApi, pOrder):
    pass

fnOnRtnTradeDec = WINFUNCTYPE(None, c_void_p, POINTER(CThostFtdcTradeField))
def OnRtnTrade(pTraderApi, pTrade):
    pass
