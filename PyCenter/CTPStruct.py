#-*- coding:utf-8 -*-
from ctypes import *

class CThostFtdcDepthMarketDataField(Structure):
    _fields_ = [('TradingDay', c_char * 9),
               ('InstrumentID', c_char * 31),
               ('ExchangeID', c_char * 9),
               ('ExchangeInstID', c_char * 31),
               ('LastPrice', c_double),
               ('PreSettlementPrice', c_double),
               ('PreClosePrice', c_double),
               ('PreOpenInterest', c_double),
               ('OpenPrice', c_double),
               ('HighestPrice', c_double),
               ('LowestPrice', c_double),
               ('Volume', c_int),
               ('Turnover', c_double),
               ('OpenInterest', c_double),
               ('ClosePrice', c_double),
               ('SettlementPrice', c_double),
               ('UpperLimitPrice', c_double),
               ('LowerLimitPrice', c_double),
               ('PreDelta', c_double),
               ('CurrDelta', c_double),
               ('UpdateTime', c_char * 9),
               ('UpdateMillisec', c_int),
               ('BidPrice1', c_double),
               ('BidVolume1', c_int),
               ('AskPrice1', c_double),
               ('AskVolume1', c_int),
               ('BidPrice2', c_double),
               ('BidVolume2', c_int),
               ('AskPrice2', c_double),
               ('AskVolume2', c_int),
               ('BidPrice3', c_double),
               ('BidVolume3', c_int),
               ('AskPrice3', c_double),
               ('AskVolume3', c_int),
               ('BidPrice4', c_double),
               ('BidVolume4', c_int),
               ('AskPrice4', c_double),
               ('AskVolume4', c_int),
               ('BidPrice5', c_double),
               ('BidVolume5', c_int),
               ('AskPrice5', c_double),
               ('AskVolume5', c_int),
               ('AveragePrice', c_double),
               ('ActionDay', c_char * 9)
               ]
    
class CThostFtdcRspUserLoginField(Structure): 
    _field_ = []
    
    
    
class CThostFtdcRspInfoField(Structure): 
    _field_ = []
class CThostFtdcInputOrderActionField(Structure): 
    _field_ = []
class CThostFtdcInputOrderField(Structure): 
    _field_ = []
class CThostFtdcInstrumentField(Structure): 
    _field_ = []
class CThostFtdcInstrumentMarginRateField(Structure): 
    _field_ = []
class CThostFtdcInvestorPositionField(Structure): 
    _field_ = []
class CThostFtdcInvestorPositionDetailField(Structure): 
    _field_ = []
class CThostFtdcOrderField(Structure): 
    _field_ = []
class CThostFtdcSettlementInfoField(Structure): 
    _field_ = []
class CThostFtdcTradeField(Structure): 
    _field_ = []
class ConnectionStatus(Union): 
    _field_ = []

