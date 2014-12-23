from CTPApiDataType import *
class CThostFtdcDisseminationField(Structure):
    _fields_ = [
           ('SequenceSeries', TThostFtdcSequenceSeriesType),
           ('SequenceNo', TThostFtdcSequenceNoType),
           ]
class CThostFtdcReqUserLoginField(Structure):
    _fields_ = [
           ('TradingDay', TThostFtdcDateType),
           ('BrokerID', TThostFtdcBrokerIDType),
           ('UserID', TThostFtdcUserIDType),
           ('Password', TThostFtdcPasswordType),
           ('UserProductInfo', TThostFtdcProductInfoType),
           ('InterfaceProductInfo', TThostFtdcProductInfoType),
           ('ProtocolInfo', TThostFtdcProtocolInfoType),
           ('MacAddress', TThostFtdcMacAddressType),
           ('OneTimePassword', TThostFtdcPasswordType),
           ('ClientIPAddress', TThostFtdcIPAddressType),
           ]
class CThostFtdcRspUserLoginField(Structure):
    _fields_ = [
           ('TradingDay', TThostFtdcDateType),
           ('LoginTime', TThostFtdcTimeType),
           ('BrokerID', TThostFtdcBrokerIDType),
           ('UserID', TThostFtdcUserIDType),
           ('SystemName', TThostFtdcSystemNameType),
           ('FrontID', TThostFtdcFrontIDType),
           ('SessionID', TThostFtdcSessionIDType),
           ('MaxOrderRef', TThostFtdcOrderRefType),
           ('SHFETime', TThostFtdcTimeType),
           ('DCETime', TThostFtdcTimeType),
           ('CZCETime', TThostFtdcTimeType),
           ('FFEXTime', TThostFtdcTimeType),
           ('INETime', TThostFtdcTimeType),
           ]
class CThostFtdcUserLogoutField(Structure):
    _fields_ = [
           ('BrokerID', TThostFtdcBrokerIDType),
           ('UserID', TThostFtdcUserIDType),
           ]
class CThostFtdcForceUserLogoutField(Structure):
    _fields_ = [
           ('BrokerID', TThostFtdcBrokerIDType),
           ('UserID', TThostFtdcUserIDType),
           ]
class CThostFtdcReqAuthenticateField(Structure):
    _fields_ = [
           ('BrokerID', TThostFtdcBrokerIDType),
           ('UserID', TThostFtdcUserIDType),
           ('UserProductInfo', TThostFtdcProductInfoType),
           ('AuthCode', TThostFtdcAuthCodeType),
           ]
class CThostFtdcRspAuthenticateField(Structure):
    _fields_ = [
           ('BrokerID', TThostFtdcBrokerIDType),
           ('UserID', TThostFtdcUserIDType),
           ('UserProductInfo', TThostFtdcProductInfoType),
           ]
class CThostFtdcAuthenticationInfoField(Structure):
    _fields_ = [
           ('BrokerID', TThostFtdcBrokerIDType),
           ('UserID', TThostFtdcUserIDType),
           ('UserProductInfo', TThostFtdcProductInfoType),
           ('AuthInfo', TThostFtdcAuthInfoType),
           ('IsResult', TThostFtdcBoolType),
           ]
class CThostFtdcTransferHeaderField(Structure):
    _fields_ = [
           ('Version', TThostFtdcVersionType),
           ('TradeCode', TThostFtdcTradeCodeType),
           ('TradeDate', TThostFtdcTradeDateType),
           ('TradeTime', TThostFtdcTradeTimeType),
           ('TradeSerial', TThostFtdcTradeSerialType),
           ('FutureID', TThostFtdcFutureIDType),
           ('BankID', TThostFtdcBankIDType),
           ('BankBrchID', TThostFtdcBankBrchIDType),
           ('OperNo', TThostFtdcOperNoType),
           ('DeviceID', TThostFtdcDeviceIDType),
           ('RecordNum', TThostFtdcRecordNumType),
           ('SessionID', TThostFtdcSessionIDType),
           ('RequestID', TThostFtdcRequestIDType),
           ]
class CThostFtdcTransferBankToFutureReqField(Structure):
    _fields_ = [
           ('FutureAccount', TThostFtdcAccountIDType),
           ('FuturePwdFlag', TThostFtdcFuturePwdFlagType),
           ('FutureAccPwd', TThostFtdcFutureAccPwdType),
           ('TradeAmt', TThostFtdcMoneyType),
           ('CustFee', TThostFtdcMoneyType),
           ('CurrencyCode', TThostFtdcCurrencyCodeType),
           ]
class CThostFtdcTransferBankToFutureRspField(Structure):
    _fields_ = [
           ('RetCode', TThostFtdcRetCodeType),
           ('RetInfo', TThostFtdcRetInfoType),
           ('FutureAccount', TThostFtdcAccountIDType),
           ('TradeAmt', TThostFtdcMoneyType),
           ('CustFee', TThostFtdcMoneyType),
           ('CurrencyCode', TThostFtdcCurrencyCodeType),
           ]
class CThostFtdcTransferFutureToBankReqField(Structure):
    _fields_ = [
           ('FutureAccount', TThostFtdcAccountIDType),
           ('FuturePwdFlag', TThostFtdcFuturePwdFlagType),
           ('FutureAccPwd', TThostFtdcFutureAccPwdType),
           ('TradeAmt', TThostFtdcMoneyType),
           ('CustFee', TThostFtdcMoneyType),
           ('CurrencyCode', TThostFtdcCurrencyCodeType),
           ]
class CThostFtdcTransferFutureToBankRspField(Structure):
    _fields_ = [
           ('RetCode', TThostFtdcRetCodeType),
           ('RetInfo', TThostFtdcRetInfoType),
           ('FutureAccount', TThostFtdcAccountIDType),
           ('TradeAmt', TThostFtdcMoneyType),
           ('CustFee', TThostFtdcMoneyType),
           ('CurrencyCode', TThostFtdcCurrencyCodeType),
           ]
class CThostFtdcTransferQryBankReqField(Structure):
    _fields_ = [
           ('FutureAccount', TThostFtdcAccountIDType),
           ('FuturePwdFlag', TThostFtdcFuturePwdFlagType),
           ('FutureAccPwd', TThostFtdcFutureAccPwdType),
           ('CurrencyCode', TThostFtdcCurrencyCodeType),
           ]
class CThostFtdcTransferQryBankRspField(Structure):
    _fields_ = [
           ('RetCode', TThostFtdcRetCodeType),
           ('RetInfo', TThostFtdcRetInfoType),
           ('FutureAccount', TThostFtdcAccountIDType),
           ('TradeAmt', TThostFtdcMoneyType),
           ('UseAmt', TThostFtdcMoneyType),
           ('FetchAmt', TThostFtdcMoneyType),
           ('CurrencyCode', TThostFtdcCurrencyCodeType),
           ]
class CThostFtdcTransferQryDetailReqField(Structure):
    _fields_ = [
           ('FutureAccount', TThostFtdcAccountIDType),
           ]
class CThostFtdcTransferQryDetailRspField(Structure):
    _fields_ = [
           ('TradeDate', TThostFtdcDateType),
           ('TradeTime', TThostFtdcTradeTimeType),
           ('TradeCode', TThostFtdcTradeCodeType),
           ('FutureSerial', TThostFtdcTradeSerialNoType),
           ('FutureID', TThostFtdcFutureIDType),
           ('FutureAccount', TThostFtdcFutureAccountType),
           ('BankSerial', TThostFtdcTradeSerialNoType),
           ('BankID', TThostFtdcBankIDType),
           ('BankBrchID', TThostFtdcBankBrchIDType),
           ('BankAccount', TThostFtdcBankAccountType),
           ('CertCode', TThostFtdcCertCodeType),
           ('CurrencyCode', TThostFtdcCurrencyCodeType),
           ('TxAmount', TThostFtdcMoneyType),
           ('Flag', TThostFtdcTransferValidFlagType),
           ]
class CThostFtdcRspInfoField(Structure):
    _fields_ = [
           ('ErrorID', TThostFtdcErrorIDType),
           ('ErrorMsg', TThostFtdcErrorMsgType),
           ]
class CThostFtdcExchangeField(Structure):
    _fields_ = [
           ('ExchangeID', TThostFtdcExchangeIDType),
           ('ExchangeName', TThostFtdcExchangeNameType),
           ('ExchangeProperty', TThostFtdcExchangePropertyType),
           ]
class CThostFtdcProductField(Structure):
    _fields_ = [
           ('ProductID', TThostFtdcInstrumentIDType),
           ('ProductName', TThostFtdcProductNameType),
           ('ExchangeID', TThostFtdcExchangeIDType),
           ('ProductClass', TThostFtdcProductClassType),
           ('VolumeMultiple', TThostFtdcVolumeMultipleType),
           ('PriceTick', TThostFtdcPriceType),
           ('MaxMarketOrderVolume', TThostFtdcVolumeType),
           ('MinMarketOrderVolume', TThostFtdcVolumeType),
           ('MaxLimitOrderVolume', TThostFtdcVolumeType),
           ('MinLimitOrderVolume', TThostFtdcVolumeType),
           ('PositionType', TThostFtdcPositionTypeType),
           ('PositionDateType', TThostFtdcPositionDateTypeType),
           ('CloseDealType', TThostFtdcCloseDealTypeType),
           ('TradeCurrencyID', TThostFtdcCurrencyIDType),
           ('MortgageFundUseRange', TThostFtdcMortgageFundUseRangeType),
           ('ExchangeProductID', TThostFtdcInstrumentIDType),
           ('UnderlyingMultiple', TThostFtdcUnderlyingMultipleType),
           ]
class CThostFtdcInstrumentField(Structure):
    _fields_ = [
           ('InstrumentID', TThostFtdcInstrumentIDType),
           ('ExchangeID', TThostFtdcExchangeIDType),
           ('InstrumentName', TThostFtdcInstrumentNameType),
           ('ExchangeInstID', TThostFtdcExchangeInstIDType),
           ('ProductID', TThostFtdcInstrumentIDType),
           ('ProductClass', TThostFtdcProductClassType),
           ('DeliveryYear', TThostFtdcYearType),
           ('DeliveryMonth', TThostFtdcMonthType),
           ('MaxMarketOrderVolume', TThostFtdcVolumeType),
           ('MinMarketOrderVolume', TThostFtdcVolumeType),
           ('MaxLimitOrderVolume', TThostFtdcVolumeType),
           ('MinLimitOrderVolume', TThostFtdcVolumeType),
           ('VolumeMultiple', TThostFtdcVolumeMultipleType),
           ('PriceTick', TThostFtdcPriceType),
           ('CreateDate', TThostFtdcDateType),
           ('OpenDate', TThostFtdcDateType),
           ('ExpireDate', TThostFtdcDateType),
           ('StartDelivDate', TThostFtdcDateType),
           ('EndDelivDate', TThostFtdcDateType),
           ('InstLifePhase', TThostFtdcInstLifePhaseType),
           ('IsTrading', TThostFtdcBoolType),
           ('PositionType', TThostFtdcPositionTypeType),
           ('PositionDateType', TThostFtdcPositionDateTypeType),
           ('LongMarginRatio', TThostFtdcRatioType),
           ('ShortMarginRatio', TThostFtdcRatioType),
           ('MaxMarginSideAlgorithm', TThostFtdcMaxMarginSideAlgorithmType),
           ('UnderlyingInstrID', TThostFtdcInstrumentIDType),
           ('StrikePrice', TThostFtdcPriceType),
           ('OptionsType', TThostFtdcOptionsTypeType),
           ('UnderlyingMultiple', TThostFtdcUnderlyingMultipleType),
           ('CombinationType', TThostFtdcCombinationTypeType),
           ]
class CThostFtdcBrokerField(Structure):
    _fields_ = [
           ('BrokerID', TThostFtdcBrokerIDType),
           ('BrokerAbbr', TThostFtdcBrokerAbbrType),
           ('BrokerName', TThostFtdcBrokerNameType),
           ('IsActive', TThostFtdcBoolType),
           ]
class CThostFtdcTraderField(Structure):
    _fields_ = [
           ('ExchangeID', TThostFtdcExchangeIDType),
           ('TraderID', TThostFtdcTraderIDType),
           ('ParticipantID', TThostFtdcParticipantIDType),
           ('Password', TThostFtdcPasswordType),
           ('InstallCount', TThostFtdcInstallCountType),
           ('BrokerID', TThostFtdcBrokerIDType),
           ]
class CThostFtdcInvestorField(Structure):
    _fields_ = [
           ('InvestorID', TThostFtdcInvestorIDType),
           ('BrokerID', TThostFtdcBrokerIDType),
           ('InvestorGroupID', TThostFtdcInvestorIDType),
           ('InvestorName', TThostFtdcPartyNameType),
           ('IdentifiedCardType', TThostFtdcIdCardTypeType),
           ('IdentifiedCardNo', TThostFtdcIdentifiedCardNoType),
           ('IsActive', TThostFtdcBoolType),
           ('Telephone', TThostFtdcTelephoneType),
           ('Address', TThostFtdcAddressType),
           ('OpenDate', TThostFtdcDateType),
           ('Mobile', TThostFtdcMobileType),
           ('CommModelID', TThostFtdcInvestorIDType),
           ('MarginModelID', TThostFtdcInvestorIDType),
           ]
class CThostFtdcTradingCodeField(Structure):
    _fields_ = [
           ('InvestorID', TThostFtdcInvestorIDType),
           ('BrokerID', TThostFtdcBrokerIDType),
           ('ExchangeID', TThostFtdcExchangeIDType),
           ('ClientID', TThostFtdcClientIDType),
           ('IsActive', TThostFtdcBoolType),
           ('ClientIDType', TThostFtdcClientIDTypeType),
           ]
class CThostFtdcPartBrokerField(Structure):
    _fields_ = [
           ('BrokerID', TThostFtdcBrokerIDType),
           ('ExchangeID', TThostFtdcExchangeIDType),
           ('ParticipantID', TThostFtdcParticipantIDType),
           ('IsActive', TThostFtdcBoolType),
           ]
class CThostFtdcSuperUserField(Structure):
    _fields_ = [
           ('UserID', TThostFtdcUserIDType),
           ('UserName', TThostFtdcUserNameType),
           ('Password', TThostFtdcPasswordType),
           ('IsActive', TThostFtdcBoolType),
           ]
class CThostFtdcSuperUserFunctionField(Structure):
    _fields_ = [
           ('UserID', TThostFtdcUserIDType),
           ('FunctionCode', TThostFtdcFunctionCodeType),
           ]
class CThostFtdcInvestorGroupField(Structure):
    _fields_ = [
           ('BrokerID', TThostFtdcBrokerIDType),
           ('InvestorGroupID', TThostFtdcInvestorIDType),
           ('InvestorGroupName', TThostFtdcInvestorGroupNameType),
           ]
class CThostFtdcTradingAccountField(Structure):
    _fields_ = [
           ('BrokerID', TThostFtdcBrokerIDType),
           ('AccountID', TThostFtdcAccountIDType),
           ('PreMortgage', TThostFtdcMoneyType),
           ('PreCredit', TThostFtdcMoneyType),
           ('PreDeposit', TThostFtdcMoneyType),
           ('PreBalance', TThostFtdcMoneyType),
           ('PreMargin', TThostFtdcMoneyType),
           ('InterestBase', TThostFtdcMoneyType),
           ('Interest', TThostFtdcMoneyType),
           ('Deposit', TThostFtdcMoneyType),
           ('Withdraw', TThostFtdcMoneyType),
           ('FrozenMargin', TThostFtdcMoneyType),
           ('FrozenCash', TThostFtdcMoneyType),
           ('FrozenCommission', TThostFtdcMoneyType),
           ('CurrMargin', TThostFtdcMoneyType),
           ('CashIn', TThostFtdcMoneyType),
           ('Commission', TThostFtdcMoneyType),
           ('CloseProfit', TThostFtdcMoneyType),
           ('PositionProfit', TThostFtdcMoneyType),
           ('Balance', TThostFtdcMoneyType),
           ('Available', TThostFtdcMoneyType),
           ('WithdrawQuota', TThostFtdcMoneyType),
           ('Reserve', TThostFtdcMoneyType),
           ('TradingDay', TThostFtdcDateType),
           ('SettlementID', TThostFtdcSettlementIDType),
           ('Credit', TThostFtdcMoneyType),
           ('Mortgage', TThostFtdcMoneyType),
           ('ExchangeMargin', TThostFtdcMoneyType),
           ('DeliveryMargin', TThostFtdcMoneyType),
           ('ExchangeDeliveryMargin', TThostFtdcMoneyType),
           ('ReserveBalance', TThostFtdcMoneyType),
           ('CurrencyID', TThostFtdcCurrencyIDType),
           ('PreFundMortgageIn', TThostFtdcMoneyType),
           ('PreFundMortgageOut', TThostFtdcMoneyType),
           ('FundMortgageIn', TThostFtdcMoneyType),
           ('FundMortgageOut', TThostFtdcMoneyType),
           ('FundMortgageAvailable', TThostFtdcMoneyType),
           ('MortgageableFund', TThostFtdcMoneyType),
           ('SpecProductMargin', TThostFtdcMoneyType),
           ('SpecProductFrozenMargin', TThostFtdcMoneyType),
           ('SpecProductCommission', TThostFtdcMoneyType),
           ('SpecProductFrozenCommission', TThostFtdcMoneyType),
           ('SpecProductPositionProfit', TThostFtdcMoneyType),
           ('SpecProductCloseProfit', TThostFtdcMoneyType),
           ('SpecProductPositionProfitByAlg', TThostFtdcMoneyType),
           ('SpecProductExchangeMargin', TThostFtdcMoneyType),
           ]
class CThostFtdcInvestorPositionField(Structure):
    _fields_ = [
           ('InstrumentID', TThostFtdcInstrumentIDType),
           ('BrokerID', TThostFtdcBrokerIDType),
           ('InvestorID', TThostFtdcInvestorIDType),
           ('PosiDirection', TThostFtdcPosiDirectionType),
           ('HedgeFlag', TThostFtdcHedgeFlagType),
           ('PositionDate', TThostFtdcPositionDateType),
           ('YdPosition', TThostFtdcVolumeType),
           ('Position', TThostFtdcVolumeType),
           ('LongFrozen', TThostFtdcVolumeType),
           ('ShortFrozen', TThostFtdcVolumeType),
           ('LongFrozenAmount', TThostFtdcMoneyType),
           ('ShortFrozenAmount', TThostFtdcMoneyType),
           ('OpenVolume', TThostFtdcVolumeType),
           ('CloseVolume', TThostFtdcVolumeType),
           ('OpenAmount', TThostFtdcMoneyType),
           ('CloseAmount', TThostFtdcMoneyType),
           ('PositionCost', TThostFtdcMoneyType),
           ('PreMargin', TThostFtdcMoneyType),
           ('UseMargin', TThostFtdcMoneyType),
           ('FrozenMargin', TThostFtdcMoneyType),
           ('FrozenCash', TThostFtdcMoneyType),
           ('FrozenCommission', TThostFtdcMoneyType),
           ('CashIn', TThostFtdcMoneyType),
           ('Commission', TThostFtdcMoneyType),
           ('CloseProfit', TThostFtdcMoneyType),
           ('PositionProfit', TThostFtdcMoneyType),
           ('PreSettlementPrice', TThostFtdcPriceType),
           ('SettlementPrice', TThostFtdcPriceType),
           ('TradingDay', TThostFtdcDateType),
           ('SettlementID', TThostFtdcSettlementIDType),
           ('OpenCost', TThostFtdcMoneyType),
           ('ExchangeMargin', TThostFtdcMoneyType),
           ('CombPosition', TThostFtdcVolumeType),
           ('CombLongFrozen', TThostFtdcVolumeType),
           ('CombShortFrozen', TThostFtdcVolumeType),
           ('CloseProfitByDate', TThostFtdcMoneyType),
           ('CloseProfitByTrade', TThostFtdcMoneyType),
           ('TodayPosition', TThostFtdcVolumeType),
           ('MarginRateByMoney', TThostFtdcRatioType),
           ('MarginRateByVolume', TThostFtdcRatioType),
           ('StrikeFrozen', TThostFtdcVolumeType),
           ('StrikeFrozenAmount', TThostFtdcMoneyType),
           ('AbandonFrozen', TThostFtdcVolumeType),
           ]
class CThostFtdcInstrumentMarginRateField(Structure):
    _fields_ = [
           ('InstrumentID', TThostFtdcInstrumentIDType),
           ('InvestorRange', TThostFtdcInvestorRangeType),
           ('BrokerID', TThostFtdcBrokerIDType),
           ('InvestorID', TThostFtdcInvestorIDType),
           ('HedgeFlag', TThostFtdcHedgeFlagType),
           ('LongMarginRatioByMoney', TThostFtdcRatioType),
           ('LongMarginRatioByVolume', TThostFtdcMoneyType),
           ('ShortMarginRatioByMoney', TThostFtdcRatioType),
           ('ShortMarginRatioByVolume', TThostFtdcMoneyType),
           ('IsRelative', TThostFtdcBoolType),
           ]
class CThostFtdcInstrumentCommissionRateField(Structure):
    _fields_ = [
           ('InstrumentID', TThostFtdcInstrumentIDType),
           ('InvestorRange', TThostFtdcInvestorRangeType),
           ('BrokerID', TThostFtdcBrokerIDType),
           ('InvestorID', TThostFtdcInvestorIDType),
           ('OpenRatioByMoney', TThostFtdcRatioType),
           ('OpenRatioByVolume', TThostFtdcRatioType),
           ('CloseRatioByMoney', TThostFtdcRatioType),
           ('CloseRatioByVolume', TThostFtdcRatioType),
           ('CloseTodayRatioByMoney', TThostFtdcRatioType),
           ('CloseTodayRatioByVolume', TThostFtdcRatioType),
           ]
class CThostFtdcDepthMarketDataField(Structure):
    _fields_ = [
           ('TradingDay', TThostFtdcDateType),
           ('InstrumentID', TThostFtdcInstrumentIDType),
           ('ExchangeID', TThostFtdcExchangeIDType),
           ('ExchangeInstID', TThostFtdcExchangeInstIDType),
           ('LastPrice', TThostFtdcPriceType),
           ('PreSettlementPrice', TThostFtdcPriceType),
           ('PreClosePrice', TThostFtdcPriceType),
           ('PreOpenInterest', TThostFtdcLargeVolumeType),
           ('OpenPrice', TThostFtdcPriceType),
           ('HighestPrice', TThostFtdcPriceType),
           ('LowestPrice', TThostFtdcPriceType),
           ('Volume', TThostFtdcVolumeType),
           ('Turnover', TThostFtdcMoneyType),
           ('OpenInterest', TThostFtdcLargeVolumeType),
           ('ClosePrice', TThostFtdcPriceType),
           ('SettlementPrice', TThostFtdcPriceType),
           ('UpperLimitPrice', TThostFtdcPriceType),
           ('LowerLimitPrice', TThostFtdcPriceType),
           ('PreDelta', TThostFtdcRatioType),
           ('CurrDelta', TThostFtdcRatioType),
           ('UpdateTime', TThostFtdcTimeType),
           ('UpdateMillisec', TThostFtdcMillisecType),
           ('BidPrice1', TThostFtdcPriceType),
           ('BidVolume1', TThostFtdcVolumeType),
           ('AskPrice1', TThostFtdcPriceType),
           ('AskVolume1', TThostFtdcVolumeType),
           ('BidPrice2', TThostFtdcPriceType),
           ('BidVolume2', TThostFtdcVolumeType),
           ('AskPrice2', TThostFtdcPriceType),
           ('AskVolume2', TThostFtdcVolumeType),
           ('BidPrice3', TThostFtdcPriceType),
           ('BidVolume3', TThostFtdcVolumeType),
           ('AskPrice3', TThostFtdcPriceType),
           ('AskVolume3', TThostFtdcVolumeType),
           ('BidPrice4', TThostFtdcPriceType),
           ('BidVolume4', TThostFtdcVolumeType),
           ('AskPrice4', TThostFtdcPriceType),
           ('AskVolume4', TThostFtdcVolumeType),
           ('BidPrice5', TThostFtdcPriceType),
           ('BidVolume5', TThostFtdcVolumeType),
           ('AskPrice5', TThostFtdcPriceType),
           ('AskVolume5', TThostFtdcVolumeType),
           ('AveragePrice', TThostFtdcPriceType),
           ('ActionDay', TThostFtdcDateType),
           ]
class CThostFtdcInstrumentTradingRightField(Structure):
    _fields_ = [
           ('InstrumentID', TThostFtdcInstrumentIDType),
           ('InvestorRange', TThostFtdcInvestorRangeType),
           ('BrokerID', TThostFtdcBrokerIDType),
           ('InvestorID', TThostFtdcInvestorIDType),
           ('TradingRight', TThostFtdcTradingRightType),
           ]
class CThostFtdcBrokerUserField(Structure):
    _fields_ = [
           ('BrokerID', TThostFtdcBrokerIDType),
           ('UserID', TThostFtdcUserIDType),
           ('UserName', TThostFtdcUserNameType),
           ('UserType', TThostFtdcUserTypeType),
           ('IsActive', TThostFtdcBoolType),
           ('IsUsingOTP', TThostFtdcBoolType),
           ]
class CThostFtdcBrokerUserPasswordField(Structure):
    _fields_ = [
           ('BrokerID', TThostFtdcBrokerIDType),
           ('UserID', TThostFtdcUserIDType),
           ('Password', TThostFtdcPasswordType),
           ]
class CThostFtdcBrokerUserFunctionField(Structure):
    _fields_ = [
           ('BrokerID', TThostFtdcBrokerIDType),
           ('UserID', TThostFtdcUserIDType),
           ('BrokerFunctionCode', TThostFtdcBrokerFunctionCodeType),
           ]
class CThostFtdcTraderOfferField(Structure):
    _fields_ = [
           ('ExchangeID', TThostFtdcExchangeIDType),
           ('TraderID', TThostFtdcTraderIDType),
           ('ParticipantID', TThostFtdcParticipantIDType),
           ('Password', TThostFtdcPasswordType),
           ('InstallID', TThostFtdcInstallIDType),
           ('OrderLocalID', TThostFtdcOrderLocalIDType),
           ('TraderConnectStatus', TThostFtdcTraderConnectStatusType),
           ('ConnectRequestDate', TThostFtdcDateType),
           ('ConnectRequestTime', TThostFtdcTimeType),
           ('LastReportDate', TThostFtdcDateType),
           ('LastReportTime', TThostFtdcTimeType),
           ('ConnectDate', TThostFtdcDateType),
           ('ConnectTime', TThostFtdcTimeType),
           ('StartDate', TThostFtdcDateType),
           ('StartTime', TThostFtdcTimeType),
           ('TradingDay', TThostFtdcDateType),
           ('BrokerID', TThostFtdcBrokerIDType),
           ('MaxTradeID', TThostFtdcTradeIDType),
           ('MaxOrderMessageReference', TThostFtdcReturnCodeType),
           ]
class CThostFtdcSettlementInfoField(Structure):
    _fields_ = [
           ('TradingDay', TThostFtdcDateType),
           ('SettlementID', TThostFtdcSettlementIDType),
           ('BrokerID', TThostFtdcBrokerIDType),
           ('InvestorID', TThostFtdcInvestorIDType),
           ('SequenceNo', TThostFtdcSequenceNoType),
           ('Content', TThostFtdcContentType),
           ]
class CThostFtdcInstrumentMarginRateAdjustField(Structure):
    _fields_ = [
           ('InstrumentID', TThostFtdcInstrumentIDType),
           ('InvestorRange', TThostFtdcInvestorRangeType),
           ('BrokerID', TThostFtdcBrokerIDType),
           ('InvestorID', TThostFtdcInvestorIDType),
           ('HedgeFlag', TThostFtdcHedgeFlagType),
           ('LongMarginRatioByMoney', TThostFtdcRatioType),
           ('LongMarginRatioByVolume', TThostFtdcMoneyType),
           ('ShortMarginRatioByMoney', TThostFtdcRatioType),
           ('ShortMarginRatioByVolume', TThostFtdcMoneyType),
           ('IsRelative', TThostFtdcBoolType),
           ]
class CThostFtdcExchangeMarginRateField(Structure):
    _fields_ = [
           ('BrokerID', TThostFtdcBrokerIDType),
           ('InstrumentID', TThostFtdcInstrumentIDType),
           ('HedgeFlag', TThostFtdcHedgeFlagType),
           ('LongMarginRatioByMoney', TThostFtdcRatioType),
           ('LongMarginRatioByVolume', TThostFtdcMoneyType),
           ('ShortMarginRatioByMoney', TThostFtdcRatioType),
           ('ShortMarginRatioByVolume', TThostFtdcMoneyType),
           ]
class CThostFtdcExchangeMarginRateAdjustField(Structure):
    _fields_ = [
           ('BrokerID', TThostFtdcBrokerIDType),
           ('InstrumentID', TThostFtdcInstrumentIDType),
           ('HedgeFlag', TThostFtdcHedgeFlagType),
           ('LongMarginRatioByMoney', TThostFtdcRatioType),
           ('LongMarginRatioByVolume', TThostFtdcMoneyType),
           ('ShortMarginRatioByMoney', TThostFtdcRatioType),
           ('ShortMarginRatioByVolume', TThostFtdcMoneyType),
           ('ExchLongMarginRatioByMoney', TThostFtdcRatioType),
           ('ExchLongMarginRatioByVolume', TThostFtdcMoneyType),
           ('ExchShortMarginRatioByMoney', TThostFtdcRatioType),
           ('ExchShortMarginRatioByVolume', TThostFtdcMoneyType),
           ('NoLongMarginRatioByMoney', TThostFtdcRatioType),
           ('NoLongMarginRatioByVolume', TThostFtdcMoneyType),
           ('NoShortMarginRatioByMoney', TThostFtdcRatioType),
           ('NoShortMarginRatioByVolume', TThostFtdcMoneyType),
           ]
class CThostFtdcExchangeRateField(Structure):
    _fields_ = [
           ('BrokerID', TThostFtdcBrokerIDType),
           ('FromCurrencyID', TThostFtdcCurrencyIDType),
           ('FromCurrencyUnit', TThostFtdcCurrencyUnitType),
           ('ToCurrencyID', TThostFtdcCurrencyIDType),
           ('ExchangeRate', TThostFtdcExchangeRateType),
           ]
class CThostFtdcSettlementRefField(Structure):
    _fields_ = [
           ('TradingDay', TThostFtdcDateType),
           ('SettlementID', TThostFtdcSettlementIDType),
           ]
class CThostFtdcCurrentTimeField(Structure):
    _fields_ = [
           ('CurrDate', TThostFtdcDateType),
           ('CurrTime', TThostFtdcTimeType),
           ('CurrMillisec', TThostFtdcMillisecType),
           ('ActionDay', TThostFtdcDateType),
           ]
class CThostFtdcCommPhaseField(Structure):
    _fields_ = [
           ('TradingDay', TThostFtdcDateType),
           ('CommPhaseNo', TThostFtdcCommPhaseNoType),
           ('SystemID', TThostFtdcSystemIDType),
           ]
class CThostFtdcLoginInfoField(Structure):
    _fields_ = [
           ('FrontID', TThostFtdcFrontIDType),
           ('SessionID', TThostFtdcSessionIDType),
           ('BrokerID', TThostFtdcBrokerIDType),
           ('UserID', TThostFtdcUserIDType),
           ('LoginDate', TThostFtdcDateType),
           ('LoginTime', TThostFtdcTimeType),
           ('IPAddress', TThostFtdcIPAddressType),
           ('UserProductInfo', TThostFtdcProductInfoType),
           ('InterfaceProductInfo', TThostFtdcProductInfoType),
           ('ProtocolInfo', TThostFtdcProtocolInfoType),
           ('SystemName', TThostFtdcSystemNameType),
           ('Password', TThostFtdcPasswordType),
           ('MaxOrderRef', TThostFtdcOrderRefType),
           ('SHFETime', TThostFtdcTimeType),
           ('DCETime', TThostFtdcTimeType),
           ('CZCETime', TThostFtdcTimeType),
           ('FFEXTime', TThostFtdcTimeType),
           ('MacAddress', TThostFtdcMacAddressType),
           ('OneTimePassword', TThostFtdcPasswordType),
           ('INETime', TThostFtdcTimeType),
           ]
class CThostFtdcLogoutAllField(Structure):
    _fields_ = [
           ('FrontID', TThostFtdcFrontIDType),
           ('SessionID', TThostFtdcSessionIDType),
           ('SystemName', TThostFtdcSystemNameType),
           ]
class CThostFtdcFrontStatusField(Structure):
    _fields_ = [
           ('FrontID', TThostFtdcFrontIDType),
           ('LastReportDate', TThostFtdcDateType),
           ('LastReportTime', TThostFtdcTimeType),
           ('IsActive', TThostFtdcBoolType),
           ]
class CThostFtdcUserPasswordUpdateField(Structure):
    _fields_ = [
           ('BrokerID', TThostFtdcBrokerIDType),
           ('UserID', TThostFtdcUserIDType),
           ('OldPassword', TThostFtdcPasswordType),
           ('NewPassword', TThostFtdcPasswordType),
           ]
class CThostFtdcInputOrderField(Structure):
    _fields_ = [
           ('BrokerID', TThostFtdcBrokerIDType),
           ('InvestorID', TThostFtdcInvestorIDType),
           ('InstrumentID', TThostFtdcInstrumentIDType),
           ('OrderRef', TThostFtdcOrderRefType),
           ('UserID', TThostFtdcUserIDType),
           ('OrderPriceType', TThostFtdcOrderPriceTypeType),
           ('Direction', TThostFtdcDirectionType),
           ('CombOffsetFlag', TThostFtdcCombOffsetFlagType),
           ('CombHedgeFlag', TThostFtdcCombHedgeFlagType),
           ('LimitPrice', TThostFtdcPriceType),
           ('VolumeTotalOriginal', TThostFtdcVolumeType),
           ('TimeCondition', TThostFtdcTimeConditionType),
           ('GTDDate', TThostFtdcDateType),
           ('VolumeCondition', TThostFtdcVolumeConditionType),
           ('MinVolume', TThostFtdcVolumeType),
           ('ContingentCondition', TThostFtdcContingentConditionType),
           ('StopPrice', TThostFtdcPriceType),
           ('ForceCloseReason', TThostFtdcForceCloseReasonType),
           ('IsAutoSuspend', TThostFtdcBoolType),
           ('BusinessUnit', TThostFtdcBusinessUnitType),
           ('RequestID', TThostFtdcRequestIDType),
           ('UserForceClose', TThostFtdcBoolType),
           ('IsSwapOrder', TThostFtdcBoolType),
           ]
class CThostFtdcOrderField(Structure):
    _fields_ = [
           ('BrokerID', TThostFtdcBrokerIDType),
           ('InvestorID', TThostFtdcInvestorIDType),
           ('InstrumentID', TThostFtdcInstrumentIDType),
           ('OrderRef', TThostFtdcOrderRefType),
           ('UserID', TThostFtdcUserIDType),
           ('OrderPriceType', TThostFtdcOrderPriceTypeType),
           ('Direction', TThostFtdcDirectionType),
           ('CombOffsetFlag', TThostFtdcCombOffsetFlagType),
           ('CombHedgeFlag', TThostFtdcCombHedgeFlagType),
           ('LimitPrice', TThostFtdcPriceType),
           ('VolumeTotalOriginal', TThostFtdcVolumeType),
           ('TimeCondition', TThostFtdcTimeConditionType),
           ('GTDDate', TThostFtdcDateType),
           ('VolumeCondition', TThostFtdcVolumeConditionType),
           ('MinVolume', TThostFtdcVolumeType),
           ('ContingentCondition', TThostFtdcContingentConditionType),
           ('StopPrice', TThostFtdcPriceType),
           ('ForceCloseReason', TThostFtdcForceCloseReasonType),
           ('IsAutoSuspend', TThostFtdcBoolType),
           ('BusinessUnit', TThostFtdcBusinessUnitType),
           ('RequestID', TThostFtdcRequestIDType),
           ('OrderLocalID', TThostFtdcOrderLocalIDType),
           ('ExchangeID', TThostFtdcExchangeIDType),
           ('ParticipantID', TThostFtdcParticipantIDType),
           ('ClientID', TThostFtdcClientIDType),
           ('ExchangeInstID', TThostFtdcExchangeInstIDType),
           ('TraderID', TThostFtdcTraderIDType),
           ('InstallID', TThostFtdcInstallIDType),
           ('OrderSubmitStatus', TThostFtdcOrderSubmitStatusType),
           ('NotifySequence', TThostFtdcSequenceNoType),
           ('TradingDay', TThostFtdcDateType),
           ('SettlementID', TThostFtdcSettlementIDType),
           ('OrderSysID', TThostFtdcOrderSysIDType),
           ('OrderSource', TThostFtdcOrderSourceType),
           ('OrderStatus', TThostFtdcOrderStatusType),
           ('OrderType', TThostFtdcOrderTypeType),
           ('VolumeTraded', TThostFtdcVolumeType),
           ('VolumeTotal', TThostFtdcVolumeType),
           ('InsertDate', TThostFtdcDateType),
           ('InsertTime', TThostFtdcTimeType),
           ('ActiveTime', TThostFtdcTimeType),
           ('SuspendTime', TThostFtdcTimeType),
           ('UpdateTime', TThostFtdcTimeType),
           ('CancelTime', TThostFtdcTimeType),
           ('ActiveTraderID', TThostFtdcTraderIDType),
           ('ClearingPartID', TThostFtdcParticipantIDType),
           ('SequenceNo', TThostFtdcSequenceNoType),
           ('FrontID', TThostFtdcFrontIDType),
           ('SessionID', TThostFtdcSessionIDType),
           ('UserProductInfo', TThostFtdcProductInfoType),
           ('StatusMsg', TThostFtdcErrorMsgType),
           ('UserForceClose', TThostFtdcBoolType),
           ('ActiveUserID', TThostFtdcUserIDType),
           ('BrokerOrderSeq', TThostFtdcSequenceNoType),
           ('RelativeOrderSysID', TThostFtdcOrderSysIDType),
           ('ZCETotalTradedVolume', TThostFtdcVolumeType),
           ('IsSwapOrder', TThostFtdcBoolType),
           ]
class CThostFtdcExchangeOrderField(Structure):
    _fields_ = [
           ('OrderPriceType', TThostFtdcOrderPriceTypeType),
           ('Direction', TThostFtdcDirectionType),
           ('CombOffsetFlag', TThostFtdcCombOffsetFlagType),
           ('CombHedgeFlag', TThostFtdcCombHedgeFlagType),
           ('LimitPrice', TThostFtdcPriceType),
           ('VolumeTotalOriginal', TThostFtdcVolumeType),
           ('TimeCondition', TThostFtdcTimeConditionType),
           ('GTDDate', TThostFtdcDateType),
           ('VolumeCondition', TThostFtdcVolumeConditionType),
           ('MinVolume', TThostFtdcVolumeType),
           ('ContingentCondition', TThostFtdcContingentConditionType),
           ('StopPrice', TThostFtdcPriceType),
           ('ForceCloseReason', TThostFtdcForceCloseReasonType),
           ('IsAutoSuspend', TThostFtdcBoolType),
           ('BusinessUnit', TThostFtdcBusinessUnitType),
           ('RequestID', TThostFtdcRequestIDType),
           ('OrderLocalID', TThostFtdcOrderLocalIDType),
           ('ExchangeID', TThostFtdcExchangeIDType),
           ('ParticipantID', TThostFtdcParticipantIDType),
           ('ClientID', TThostFtdcClientIDType),
           ('ExchangeInstID', TThostFtdcExchangeInstIDType),
           ('TraderID', TThostFtdcTraderIDType),
           ('InstallID', TThostFtdcInstallIDType),
           ('OrderSubmitStatus', TThostFtdcOrderSubmitStatusType),
           ('NotifySequence', TThostFtdcSequenceNoType),
           ('TradingDay', TThostFtdcDateType),
           ('SettlementID', TThostFtdcSettlementIDType),
           ('OrderSysID', TThostFtdcOrderSysIDType),
           ('OrderSource', TThostFtdcOrderSourceType),
           ('OrderStatus', TThostFtdcOrderStatusType),
           ('OrderType', TThostFtdcOrderTypeType),
           ('VolumeTraded', TThostFtdcVolumeType),
           ('VolumeTotal', TThostFtdcVolumeType),
           ('InsertDate', TThostFtdcDateType),
           ('InsertTime', TThostFtdcTimeType),
           ('ActiveTime', TThostFtdcTimeType),
           ('SuspendTime', TThostFtdcTimeType),
           ('UpdateTime', TThostFtdcTimeType),
           ('CancelTime', TThostFtdcTimeType),
           ('ActiveTraderID', TThostFtdcTraderIDType),
           ('ClearingPartID', TThostFtdcParticipantIDType),
           ('SequenceNo', TThostFtdcSequenceNoType),
           ]
class CThostFtdcExchangeOrderInsertErrorField(Structure):
    _fields_ = [
           ('ExchangeID', TThostFtdcExchangeIDType),
           ('ParticipantID', TThostFtdcParticipantIDType),
           ('TraderID', TThostFtdcTraderIDType),
           ('InstallID', TThostFtdcInstallIDType),
           ('OrderLocalID', TThostFtdcOrderLocalIDType),
           ('ErrorID', TThostFtdcErrorIDType),
           ('ErrorMsg', TThostFtdcErrorMsgType),
           ]
class CThostFtdcInputOrderActionField(Structure):
    _fields_ = [
           ('BrokerID', TThostFtdcBrokerIDType),
           ('InvestorID', TThostFtdcInvestorIDType),
           ('OrderActionRef', TThostFtdcOrderActionRefType),
           ('OrderRef', TThostFtdcOrderRefType),
           ('RequestID', TThostFtdcRequestIDType),
           ('FrontID', TThostFtdcFrontIDType),
           ('SessionID', TThostFtdcSessionIDType),
           ('ExchangeID', TThostFtdcExchangeIDType),
           ('OrderSysID', TThostFtdcOrderSysIDType),
           ('ActionFlag', TThostFtdcActionFlagType),
           ('LimitPrice', TThostFtdcPriceType),
           ('VolumeChange', TThostFtdcVolumeType),
           ('UserID', TThostFtdcUserIDType),
           ('InstrumentID', TThostFtdcInstrumentIDType),
           ]
class CThostFtdcOrderActionField(Structure):
    _fields_ = [
           ('BrokerID', TThostFtdcBrokerIDType),
           ('InvestorID', TThostFtdcInvestorIDType),
           ('OrderActionRef', TThostFtdcOrderActionRefType),
           ('OrderRef', TThostFtdcOrderRefType),
           ('RequestID', TThostFtdcRequestIDType),
           ('FrontID', TThostFtdcFrontIDType),
           ('SessionID', TThostFtdcSessionIDType),
           ('ExchangeID', TThostFtdcExchangeIDType),
           ('OrderSysID', TThostFtdcOrderSysIDType),
           ('ActionFlag', TThostFtdcActionFlagType),
           ('LimitPrice', TThostFtdcPriceType),
           ('VolumeChange', TThostFtdcVolumeType),
           ('ActionDate', TThostFtdcDateType),
           ('ActionTime', TThostFtdcTimeType),
           ('TraderID', TThostFtdcTraderIDType),
           ('InstallID', TThostFtdcInstallIDType),
           ('OrderLocalID', TThostFtdcOrderLocalIDType),
           ('ActionLocalID', TThostFtdcOrderLocalIDType),
           ('ParticipantID', TThostFtdcParticipantIDType),
           ('ClientID', TThostFtdcClientIDType),
           ('BusinessUnit', TThostFtdcBusinessUnitType),
           ('OrderActionStatus', TThostFtdcOrderActionStatusType),
           ('UserID', TThostFtdcUserIDType),
           ('StatusMsg', TThostFtdcErrorMsgType),
           ('InstrumentID', TThostFtdcInstrumentIDType),
           ]
class CThostFtdcExchangeOrderActionField(Structure):
    _fields_ = [
           ('ExchangeID', TThostFtdcExchangeIDType),
           ('OrderSysID', TThostFtdcOrderSysIDType),
           ('ActionFlag', TThostFtdcActionFlagType),
           ('LimitPrice', TThostFtdcPriceType),
           ('VolumeChange', TThostFtdcVolumeType),
           ('ActionDate', TThostFtdcDateType),
           ('ActionTime', TThostFtdcTimeType),
           ('TraderID', TThostFtdcTraderIDType),
           ('InstallID', TThostFtdcInstallIDType),
           ('OrderLocalID', TThostFtdcOrderLocalIDType),
           ('ActionLocalID', TThostFtdcOrderLocalIDType),
           ('ParticipantID', TThostFtdcParticipantIDType),
           ('ClientID', TThostFtdcClientIDType),
           ('BusinessUnit', TThostFtdcBusinessUnitType),
           ('OrderActionStatus', TThostFtdcOrderActionStatusType),
           ('UserID', TThostFtdcUserIDType),
           ]
class CThostFtdcExchangeOrderActionErrorField(Structure):
    _fields_ = [
           ('ExchangeID', TThostFtdcExchangeIDType),
           ('OrderSysID', TThostFtdcOrderSysIDType),
           ('TraderID', TThostFtdcTraderIDType),
           ('InstallID', TThostFtdcInstallIDType),
           ('OrderLocalID', TThostFtdcOrderLocalIDType),
           ('ActionLocalID', TThostFtdcOrderLocalIDType),
           ('ErrorID', TThostFtdcErrorIDType),
           ('ErrorMsg', TThostFtdcErrorMsgType),
           ]
class CThostFtdcExchangeTradeField(Structure):
    _fields_ = [
           ('ExchangeID', TThostFtdcExchangeIDType),
           ('TradeID', TThostFtdcTradeIDType),
           ('Direction', TThostFtdcDirectionType),
           ('OrderSysID', TThostFtdcOrderSysIDType),
           ('ParticipantID', TThostFtdcParticipantIDType),
           ('ClientID', TThostFtdcClientIDType),
           ('TradingRole', TThostFtdcTradingRoleType),
           ('ExchangeInstID', TThostFtdcExchangeInstIDType),
           ('OffsetFlag', TThostFtdcOffsetFlagType),
           ('HedgeFlag', TThostFtdcHedgeFlagType),
           ('Price', TThostFtdcPriceType),
           ('Volume', TThostFtdcVolumeType),
           ('TradeDate', TThostFtdcDateType),
           ('TradeTime', TThostFtdcTimeType),
           ('TradeType', TThostFtdcTradeTypeType),
           ('PriceSource', TThostFtdcPriceSourceType),
           ('TraderID', TThostFtdcTraderIDType),
           ('OrderLocalID', TThostFtdcOrderLocalIDType),
           ('ClearingPartID', TThostFtdcParticipantIDType),
           ('BusinessUnit', TThostFtdcBusinessUnitType),
           ('SequenceNo', TThostFtdcSequenceNoType),
           ('TradeSource', TThostFtdcTradeSourceType),
           ]
class CThostFtdcTradeField(Structure):
    _fields_ = [
           ('BrokerID', TThostFtdcBrokerIDType),
           ('InvestorID', TThostFtdcInvestorIDType),
           ('InstrumentID', TThostFtdcInstrumentIDType),
           ('OrderRef', TThostFtdcOrderRefType),
           ('UserID', TThostFtdcUserIDType),
           ('ExchangeID', TThostFtdcExchangeIDType),
           ('TradeID', TThostFtdcTradeIDType),
           ('Direction', TThostFtdcDirectionType),
           ('OrderSysID', TThostFtdcOrderSysIDType),
           ('ParticipantID', TThostFtdcParticipantIDType),
           ('ClientID', TThostFtdcClientIDType),
           ('TradingRole', TThostFtdcTradingRoleType),
           ('ExchangeInstID', TThostFtdcExchangeInstIDType),
           ('OffsetFlag', TThostFtdcOffsetFlagType),
           ('HedgeFlag', TThostFtdcHedgeFlagType),
           ('Price', TThostFtdcPriceType),
           ('Volume', TThostFtdcVolumeType),
           ('TradeDate', TThostFtdcDateType),
           ('TradeTime', TThostFtdcTimeType),
           ('TradeType', TThostFtdcTradeTypeType),
           ('PriceSource', TThostFtdcPriceSourceType),
           ('TraderID', TThostFtdcTraderIDType),
           ('OrderLocalID', TThostFtdcOrderLocalIDType),
           ('ClearingPartID', TThostFtdcParticipantIDType),
           ('BusinessUnit', TThostFtdcBusinessUnitType),
           ('SequenceNo', TThostFtdcSequenceNoType),
           ('TradingDay', TThostFtdcDateType),
           ('SettlementID', TThostFtdcSettlementIDType),
           ('BrokerOrderSeq', TThostFtdcSequenceNoType),
           ('TradeSource', TThostFtdcTradeSourceType),
           ]
class CThostFtdcUserSessionField(Structure):
    _fields_ = [
           ('FrontID', TThostFtdcFrontIDType),
           ('SessionID', TThostFtdcSessionIDType),
           ('BrokerID', TThostFtdcBrokerIDType),
           ('UserID', TThostFtdcUserIDType),
           ('LoginDate', TThostFtdcDateType),
           ('LoginTime', TThostFtdcTimeType),
           ('IPAddress', TThostFtdcIPAddressType),
           ('UserProductInfo', TThostFtdcProductInfoType),
           ('InterfaceProductInfo', TThostFtdcProductInfoType),
           ('ProtocolInfo', TThostFtdcProtocolInfoType),
           ('MacAddress', TThostFtdcMacAddressType),
           ]
class CThostFtdcQueryMaxOrderVolumeField(Structure):
    _fields_ = [
           ('BrokerID', TThostFtdcBrokerIDType),
           ('InvestorID', TThostFtdcInvestorIDType),
           ('InstrumentID', TThostFtdcInstrumentIDType),
           ('Direction', TThostFtdcDirectionType),
           ('OffsetFlag', TThostFtdcOffsetFlagType),
           ('HedgeFlag', TThostFtdcHedgeFlagType),
           ('MaxVolume', TThostFtdcVolumeType),
           ]
class CThostFtdcSettlementInfoConfirmField(Structure):
    _fields_ = [
           ('BrokerID', TThostFtdcBrokerIDType),
           ('InvestorID', TThostFtdcInvestorIDType),
           ('ConfirmDate', TThostFtdcDateType),
           ('ConfirmTime', TThostFtdcTimeType),
           ]
class CThostFtdcSyncDepositField(Structure):
    _fields_ = [
           ('DepositSeqNo', TThostFtdcDepositSeqNoType),
           ('BrokerID', TThostFtdcBrokerIDType),
           ('InvestorID', TThostFtdcInvestorIDType),
           ('Deposit', TThostFtdcMoneyType),
           ('IsForce', TThostFtdcBoolType),
           ('CurrencyID', TThostFtdcCurrencyIDType),
           ]
class CThostFtdcSyncFundMortgageField(Structure):
    _fields_ = [
           ('MortgageSeqNo', TThostFtdcDepositSeqNoType),
           ('BrokerID', TThostFtdcBrokerIDType),
           ('InvestorID', TThostFtdcInvestorIDType),
           ('FromCurrencyID', TThostFtdcCurrencyIDType),
           ('MortgageAmount', TThostFtdcMoneyType),
           ('ToCurrencyID', TThostFtdcCurrencyIDType),
           ]
class CThostFtdcBrokerSyncField(Structure):
    _fields_ = [
           ('BrokerID', TThostFtdcBrokerIDType),
           ]
class CThostFtdcSyncingInvestorField(Structure):
    _fields_ = [
           ('InvestorID', TThostFtdcInvestorIDType),
           ('BrokerID', TThostFtdcBrokerIDType),
           ('InvestorGroupID', TThostFtdcInvestorIDType),
           ('InvestorName', TThostFtdcPartyNameType),
           ('IdentifiedCardType', TThostFtdcIdCardTypeType),
           ('IdentifiedCardNo', TThostFtdcIdentifiedCardNoType),
           ('IsActive', TThostFtdcBoolType),
           ('Telephone', TThostFtdcTelephoneType),
           ('Address', TThostFtdcAddressType),
           ('OpenDate', TThostFtdcDateType),
           ('Mobile', TThostFtdcMobileType),
           ('CommModelID', TThostFtdcInvestorIDType),
           ('MarginModelID', TThostFtdcInvestorIDType),
           ]
class CThostFtdcSyncingTradingCodeField(Structure):
    _fields_ = [
           ('InvestorID', TThostFtdcInvestorIDType),
           ('BrokerID', TThostFtdcBrokerIDType),
           ('ExchangeID', TThostFtdcExchangeIDType),
           ('ClientID', TThostFtdcClientIDType),
           ('IsActive', TThostFtdcBoolType),
           ('ClientIDType', TThostFtdcClientIDTypeType),
           ]
class CThostFtdcSyncingInvestorGroupField(Structure):
    _fields_ = [
           ('BrokerID', TThostFtdcBrokerIDType),
           ('InvestorGroupID', TThostFtdcInvestorIDType),
           ('InvestorGroupName', TThostFtdcInvestorGroupNameType),
           ]
class CThostFtdcSyncingTradingAccountField(Structure):
    _fields_ = [
           ('BrokerID', TThostFtdcBrokerIDType),
           ('AccountID', TThostFtdcAccountIDType),
           ('PreMortgage', TThostFtdcMoneyType),
           ('PreCredit', TThostFtdcMoneyType),
           ('PreDeposit', TThostFtdcMoneyType),
           ('PreBalance', TThostFtdcMoneyType),
           ('PreMargin', TThostFtdcMoneyType),
           ('InterestBase', TThostFtdcMoneyType),
           ('Interest', TThostFtdcMoneyType),
           ('Deposit', TThostFtdcMoneyType),
           ('Withdraw', TThostFtdcMoneyType),
           ('FrozenMargin', TThostFtdcMoneyType),
           ('FrozenCash', TThostFtdcMoneyType),
           ('FrozenCommission', TThostFtdcMoneyType),
           ('CurrMargin', TThostFtdcMoneyType),
           ('CashIn', TThostFtdcMoneyType),
           ('Commission', TThostFtdcMoneyType),
           ('CloseProfit', TThostFtdcMoneyType),
           ('PositionProfit', TThostFtdcMoneyType),
           ('Balance', TThostFtdcMoneyType),
           ('Available', TThostFtdcMoneyType),
           ('WithdrawQuota', TThostFtdcMoneyType),
           ('Reserve', TThostFtdcMoneyType),
           ('TradingDay', TThostFtdcDateType),
           ('SettlementID', TThostFtdcSettlementIDType),
           ('Credit', TThostFtdcMoneyType),
           ('Mortgage', TThostFtdcMoneyType),
           ('ExchangeMargin', TThostFtdcMoneyType),
           ('DeliveryMargin', TThostFtdcMoneyType),
           ('ExchangeDeliveryMargin', TThostFtdcMoneyType),
           ('ReserveBalance', TThostFtdcMoneyType),
           ('CurrencyID', TThostFtdcCurrencyIDType),
           ('PreFundMortgageIn', TThostFtdcMoneyType),
           ('PreFundMortgageOut', TThostFtdcMoneyType),
           ('FundMortgageIn', TThostFtdcMoneyType),
           ('FundMortgageOut', TThostFtdcMoneyType),
           ('FundMortgageAvailable', TThostFtdcMoneyType),
           ('MortgageableFund', TThostFtdcMoneyType),
           ('SpecProductMargin', TThostFtdcMoneyType),
           ('SpecProductFrozenMargin', TThostFtdcMoneyType),
           ('SpecProductCommission', TThostFtdcMoneyType),
           ('SpecProductFrozenCommission', TThostFtdcMoneyType),
           ('SpecProductPositionProfit', TThostFtdcMoneyType),
           ('SpecProductCloseProfit', TThostFtdcMoneyType),
           ('SpecProductPositionProfitByAlg', TThostFtdcMoneyType),
           ('SpecProductExchangeMargin', TThostFtdcMoneyType),
           ]
class CThostFtdcSyncingInvestorPositionField(Structure):
    _fields_ = [
           ('InstrumentID', TThostFtdcInstrumentIDType),
           ('BrokerID', TThostFtdcBrokerIDType),
           ('InvestorID', TThostFtdcInvestorIDType),
           ('PosiDirection', TThostFtdcPosiDirectionType),
           ('HedgeFlag', TThostFtdcHedgeFlagType),
           ('PositionDate', TThostFtdcPositionDateType),
           ('YdPosition', TThostFtdcVolumeType),
           ('Position', TThostFtdcVolumeType),
           ('LongFrozen', TThostFtdcVolumeType),
           ('ShortFrozen', TThostFtdcVolumeType),
           ('LongFrozenAmount', TThostFtdcMoneyType),
           ('ShortFrozenAmount', TThostFtdcMoneyType),
           ('OpenVolume', TThostFtdcVolumeType),
           ('CloseVolume', TThostFtdcVolumeType),
           ('OpenAmount', TThostFtdcMoneyType),
           ('CloseAmount', TThostFtdcMoneyType),
           ('PositionCost', TThostFtdcMoneyType),
           ('PreMargin', TThostFtdcMoneyType),
           ('UseMargin', TThostFtdcMoneyType),
           ('FrozenMargin', TThostFtdcMoneyType),
           ('FrozenCash', TThostFtdcMoneyType),
           ('FrozenCommission', TThostFtdcMoneyType),
           ('CashIn', TThostFtdcMoneyType),
           ('Commission', TThostFtdcMoneyType),
           ('CloseProfit', TThostFtdcMoneyType),
           ('PositionProfit', TThostFtdcMoneyType),
           ('PreSettlementPrice', TThostFtdcPriceType),
           ('SettlementPrice', TThostFtdcPriceType),
           ('TradingDay', TThostFtdcDateType),
           ('SettlementID', TThostFtdcSettlementIDType),
           ('OpenCost', TThostFtdcMoneyType),
           ('ExchangeMargin', TThostFtdcMoneyType),
           ('CombPosition', TThostFtdcVolumeType),
           ('CombLongFrozen', TThostFtdcVolumeType),
           ('CombShortFrozen', TThostFtdcVolumeType),
           ('CloseProfitByDate', TThostFtdcMoneyType),
           ('CloseProfitByTrade', TThostFtdcMoneyType),
           ('TodayPosition', TThostFtdcVolumeType),
           ('MarginRateByMoney', TThostFtdcRatioType),
           ('MarginRateByVolume', TThostFtdcRatioType),
           ('StrikeFrozen', TThostFtdcVolumeType),
           ('StrikeFrozenAmount', TThostFtdcMoneyType),
           ('AbandonFrozen', TThostFtdcVolumeType),
           ]
class CThostFtdcSyncingInstrumentMarginRateField(Structure):
    _fields_ = [
           ('InstrumentID', TThostFtdcInstrumentIDType),
           ('InvestorRange', TThostFtdcInvestorRangeType),
           ('BrokerID', TThostFtdcBrokerIDType),
           ('InvestorID', TThostFtdcInvestorIDType),
           ('HedgeFlag', TThostFtdcHedgeFlagType),
           ('LongMarginRatioByMoney', TThostFtdcRatioType),
           ('LongMarginRatioByVolume', TThostFtdcMoneyType),
           ('ShortMarginRatioByMoney', TThostFtdcRatioType),
           ('ShortMarginRatioByVolume', TThostFtdcMoneyType),
           ('IsRelative', TThostFtdcBoolType),
           ]
class CThostFtdcSyncingInstrumentCommissionRateField(Structure):
    _fields_ = [
           ('InstrumentID', TThostFtdcInstrumentIDType),
           ('InvestorRange', TThostFtdcInvestorRangeType),
           ('BrokerID', TThostFtdcBrokerIDType),
           ('InvestorID', TThostFtdcInvestorIDType),
           ('OpenRatioByMoney', TThostFtdcRatioType),
           ('OpenRatioByVolume', TThostFtdcRatioType),
           ('CloseRatioByMoney', TThostFtdcRatioType),
           ('CloseRatioByVolume', TThostFtdcRatioType),
           ('CloseTodayRatioByMoney', TThostFtdcRatioType),
           ('CloseTodayRatioByVolume', TThostFtdcRatioType),
           ]
class CThostFtdcSyncingInstrumentTradingRightField(Structure):
    _fields_ = [
           ('InstrumentID', TThostFtdcInstrumentIDType),
           ('InvestorRange', TThostFtdcInvestorRangeType),
           ('BrokerID', TThostFtdcBrokerIDType),
           ('InvestorID', TThostFtdcInvestorIDType),
           ('TradingRight', TThostFtdcTradingRightType),
           ]
class CThostFtdcQryOrderField(Structure):
    _fields_ = [
           ('BrokerID', TThostFtdcBrokerIDType),
           ('InvestorID', TThostFtdcInvestorIDType),
           ('InstrumentID', TThostFtdcInstrumentIDType),
           ('ExchangeID', TThostFtdcExchangeIDType),
           ('OrderSysID', TThostFtdcOrderSysIDType),
           ('InsertTimeStart', TThostFtdcTimeType),
           ('InsertTimeEnd', TThostFtdcTimeType),
           ]
class CThostFtdcQryTradeField(Structure):
    _fields_ = [
           ('BrokerID', TThostFtdcBrokerIDType),
           ('InvestorID', TThostFtdcInvestorIDType),
           ('InstrumentID', TThostFtdcInstrumentIDType),
           ('ExchangeID', TThostFtdcExchangeIDType),
           ('TradeID', TThostFtdcTradeIDType),
           ('TradeTimeStart', TThostFtdcTimeType),
           ('TradeTimeEnd', TThostFtdcTimeType),
           ]
class CThostFtdcQryInvestorPositionField(Structure):
    _fields_ = [
           ('BrokerID', TThostFtdcBrokerIDType),
           ('InvestorID', TThostFtdcInvestorIDType),
           ('InstrumentID', TThostFtdcInstrumentIDType),
           ]
class CThostFtdcQryTradingAccountField(Structure):
    _fields_ = [
           ('BrokerID', TThostFtdcBrokerIDType),
           ('InvestorID', TThostFtdcInvestorIDType),
           ('CurrencyID', TThostFtdcCurrencyIDType),
           ]
class CThostFtdcQryInvestorField(Structure):
    _fields_ = [
           ('BrokerID', TThostFtdcBrokerIDType),
           ('InvestorID', TThostFtdcInvestorIDType),
           ]
class CThostFtdcQryTradingCodeField(Structure):
    _fields_ = [
           ('BrokerID', TThostFtdcBrokerIDType),
           ('InvestorID', TThostFtdcInvestorIDType),
           ('ExchangeID', TThostFtdcExchangeIDType),
           ('ClientID', TThostFtdcClientIDType),
           ('ClientIDType', TThostFtdcClientIDTypeType),
           ]
class CThostFtdcQryInvestorGroupField(Structure):
    _fields_ = [
           ('BrokerID', TThostFtdcBrokerIDType),
           ]
class CThostFtdcQryInstrumentMarginRateField(Structure):
    _fields_ = [
           ('BrokerID', TThostFtdcBrokerIDType),
           ('InvestorID', TThostFtdcInvestorIDType),
           ('InstrumentID', TThostFtdcInstrumentIDType),
           ('HedgeFlag', TThostFtdcHedgeFlagType),
           ]
class CThostFtdcQryInstrumentCommissionRateField(Structure):
    _fields_ = [
           ('BrokerID', TThostFtdcBrokerIDType),
           ('InvestorID', TThostFtdcInvestorIDType),
           ('InstrumentID', TThostFtdcInstrumentIDType),
           ]
class CThostFtdcQryInstrumentTradingRightField(Structure):
    _fields_ = [
           ('BrokerID', TThostFtdcBrokerIDType),
           ('InvestorID', TThostFtdcInvestorIDType),
           ('InstrumentID', TThostFtdcInstrumentIDType),
           ]
class CThostFtdcQryBrokerField(Structure):
    _fields_ = [
           ('BrokerID', TThostFtdcBrokerIDType),
           ]
class CThostFtdcQryTraderField(Structure):
    _fields_ = [
           ('ExchangeID', TThostFtdcExchangeIDType),
           ('ParticipantID', TThostFtdcParticipantIDType),
           ('TraderID', TThostFtdcTraderIDType),
           ]
class CThostFtdcQrySuperUserFunctionField(Structure):
    _fields_ = [
           ('UserID', TThostFtdcUserIDType),
           ]
class CThostFtdcQryUserSessionField(Structure):
    _fields_ = [
           ('FrontID', TThostFtdcFrontIDType),
           ('SessionID', TThostFtdcSessionIDType),
           ('BrokerID', TThostFtdcBrokerIDType),
           ('UserID', TThostFtdcUserIDType),
           ]
class CThostFtdcQryPartBrokerField(Structure):
    _fields_ = [
           ('ExchangeID', TThostFtdcExchangeIDType),
           ('BrokerID', TThostFtdcBrokerIDType),
           ('ParticipantID', TThostFtdcParticipantIDType),
           ]
class CThostFtdcQryFrontStatusField(Structure):
    _fields_ = [
           ('FrontID', TThostFtdcFrontIDType),
           ]
class CThostFtdcQryExchangeOrderField(Structure):
    _fields_ = [
           ('ParticipantID', TThostFtdcParticipantIDType),
           ('ClientID', TThostFtdcClientIDType),
           ('ExchangeInstID', TThostFtdcExchangeInstIDType),
           ('ExchangeID', TThostFtdcExchangeIDType),
           ('TraderID', TThostFtdcTraderIDType),
           ]
class CThostFtdcQryOrderActionField(Structure):
    _fields_ = [
           ('BrokerID', TThostFtdcBrokerIDType),
           ('InvestorID', TThostFtdcInvestorIDType),
           ('ExchangeID', TThostFtdcExchangeIDType),
           ]
class CThostFtdcQryExchangeOrderActionField(Structure):
    _fields_ = [
           ('ParticipantID', TThostFtdcParticipantIDType),
           ('ClientID', TThostFtdcClientIDType),
           ('ExchangeID', TThostFtdcExchangeIDType),
           ('TraderID', TThostFtdcTraderIDType),
           ]
class CThostFtdcQrySuperUserField(Structure):
    _fields_ = [
           ('UserID', TThostFtdcUserIDType),
           ]
class CThostFtdcQryExchangeField(Structure):
    _fields_ = [
           ('ExchangeID', TThostFtdcExchangeIDType),
           ]
class CThostFtdcQryProductField(Structure):
    _fields_ = [
           ('ProductID', TThostFtdcInstrumentIDType),
           ('ProductClass', TThostFtdcProductClassType),
           ]
class CThostFtdcQryInstrumentField(Structure):
    _fields_ = [
           ('InstrumentID', TThostFtdcInstrumentIDType),
           ('ExchangeID', TThostFtdcExchangeIDType),
           ('ExchangeInstID', TThostFtdcExchangeInstIDType),
           ('ProductID', TThostFtdcInstrumentIDType),
           ]
class CThostFtdcQryDepthMarketDataField(Structure):
    _fields_ = [
           ('InstrumentID', TThostFtdcInstrumentIDType),
           ]
class CThostFtdcQryBrokerUserField(Structure):
    _fields_ = [
           ('BrokerID', TThostFtdcBrokerIDType),
           ('UserID', TThostFtdcUserIDType),
           ]
class CThostFtdcQryBrokerUserFunctionField(Structure):
    _fields_ = [
           ('BrokerID', TThostFtdcBrokerIDType),
           ('UserID', TThostFtdcUserIDType),
           ]
class CThostFtdcQryTraderOfferField(Structure):
    _fields_ = [
           ('ExchangeID', TThostFtdcExchangeIDType),
           ('ParticipantID', TThostFtdcParticipantIDType),
           ('TraderID', TThostFtdcTraderIDType),
           ]
class CThostFtdcQrySyncDepositField(Structure):
    _fields_ = [
           ('BrokerID', TThostFtdcBrokerIDType),
           ('DepositSeqNo', TThostFtdcDepositSeqNoType),
           ]
class CThostFtdcQrySettlementInfoField(Structure):
    _fields_ = [
           ('BrokerID', TThostFtdcBrokerIDType),
           ('InvestorID', TThostFtdcInvestorIDType),
           ('TradingDay', TThostFtdcDateType),
           ]
class CThostFtdcQryExchangeMarginRateField(Structure):
    _fields_ = [
           ('BrokerID', TThostFtdcBrokerIDType),
           ('InstrumentID', TThostFtdcInstrumentIDType),
           ('HedgeFlag', TThostFtdcHedgeFlagType),
           ]
class CThostFtdcQryExchangeMarginRateAdjustField(Structure):
    _fields_ = [
           ('BrokerID', TThostFtdcBrokerIDType),
           ('InstrumentID', TThostFtdcInstrumentIDType),
           ('HedgeFlag', TThostFtdcHedgeFlagType),
           ]
class CThostFtdcQryExchangeRateField(Structure):
    _fields_ = [
           ('BrokerID', TThostFtdcBrokerIDType),
           ('FromCurrencyID', TThostFtdcCurrencyIDType),
           ('ToCurrencyID', TThostFtdcCurrencyIDType),
           ]
class CThostFtdcQrySyncFundMortgageField(Structure):
    _fields_ = [
           ('BrokerID', TThostFtdcBrokerIDType),
           ('MortgageSeqNo', TThostFtdcDepositSeqNoType),
           ]
class CThostFtdcQryHisOrderField(Structure):
    _fields_ = [
           ('BrokerID', TThostFtdcBrokerIDType),
           ('InvestorID', TThostFtdcInvestorIDType),
           ('InstrumentID', TThostFtdcInstrumentIDType),
           ('ExchangeID', TThostFtdcExchangeIDType),
           ('OrderSysID', TThostFtdcOrderSysIDType),
           ('InsertTimeStart', TThostFtdcTimeType),
           ('InsertTimeEnd', TThostFtdcTimeType),
           ('TradingDay', TThostFtdcDateType),
           ('SettlementID', TThostFtdcSettlementIDType),
           ]
class CThostFtdcOptionInstrMiniMarginField(Structure):
    _fields_ = [
           ('InstrumentID', TThostFtdcInstrumentIDType),
           ('InvestorRange', TThostFtdcInvestorRangeType),
           ('BrokerID', TThostFtdcBrokerIDType),
           ('InvestorID', TThostFtdcInvestorIDType),
           ('MinMargin', TThostFtdcMoneyType),
           ('ValueMethod', TThostFtdcValueMethodType),
           ('IsRelative', TThostFtdcBoolType),
           ]
class CThostFtdcOptionInstrMarginAdjustField(Structure):
    _fields_ = [
           ('InstrumentID', TThostFtdcInstrumentIDType),
           ('InvestorRange', TThostFtdcInvestorRangeType),
           ('BrokerID', TThostFtdcBrokerIDType),
           ('InvestorID', TThostFtdcInvestorIDType),
           ('SShortMarginRatioByMoney', TThostFtdcRatioType),
           ('SShortMarginRatioByVolume', TThostFtdcMoneyType),
           ('HShortMarginRatioByMoney', TThostFtdcRatioType),
           ('HShortMarginRatioByVolume', TThostFtdcMoneyType),
           ('AShortMarginRatioByMoney', TThostFtdcRatioType),
           ('AShortMarginRatioByVolume', TThostFtdcMoneyType),
           ('IsRelative', TThostFtdcBoolType),
           ]
class CThostFtdcOptionInstrCommRateField(Structure):
    _fields_ = [
           ('InstrumentID', TThostFtdcInstrumentIDType),
           ('InvestorRange', TThostFtdcInvestorRangeType),
           ('BrokerID', TThostFtdcBrokerIDType),
           ('InvestorID', TThostFtdcInvestorIDType),
           ('OpenRatioByMoney', TThostFtdcRatioType),
           ('OpenRatioByVolume', TThostFtdcRatioType),
           ('CloseRatioByMoney', TThostFtdcRatioType),
           ('CloseRatioByVolume', TThostFtdcRatioType),
           ('CloseTodayRatioByMoney', TThostFtdcRatioType),
           ('CloseTodayRatioByVolume', TThostFtdcRatioType),
           ('StrikeRatioByMoney', TThostFtdcRatioType),
           ('StrikeRatioByVolume', TThostFtdcRatioType),
           ]
class CThostFtdcOptionInstrTradeCostField(Structure):
    _fields_ = [
           ('BrokerID', TThostFtdcBrokerIDType),
           ('InvestorID', TThostFtdcInvestorIDType),
           ('InstrumentID', TThostFtdcInstrumentIDType),
           ('HedgeFlag', TThostFtdcHedgeFlagType),
           ('FixedMargin', TThostFtdcMoneyType),
           ('MiniMargin', TThostFtdcMoneyType),
           ('Royalty', TThostFtdcMoneyType),
           ('ExchFixedMargin', TThostFtdcMoneyType),
           ('ExchMiniMargin', TThostFtdcMoneyType),
           ]
class CThostFtdcQryOptionInstrTradeCostField(Structure):
    _fields_ = [
           ('BrokerID', TThostFtdcBrokerIDType),
           ('InvestorID', TThostFtdcInvestorIDType),
           ('InstrumentID', TThostFtdcInstrumentIDType),
           ('HedgeFlag', TThostFtdcHedgeFlagType),
           ('InputPrice', TThostFtdcPriceType),
           ('UnderlyingPrice', TThostFtdcPriceType),
           ]
class CThostFtdcQryOptionInstrCommRateField(Structure):
    _fields_ = [
           ('BrokerID', TThostFtdcBrokerIDType),
           ('InvestorID', TThostFtdcInvestorIDType),
           ('InstrumentID', TThostFtdcInstrumentIDType),
           ]
class CThostFtdcIndexPriceField(Structure):
    _fields_ = [
           ('BrokerID', TThostFtdcBrokerIDType),
           ('InstrumentID', TThostFtdcInstrumentIDType),
           ('ClosePrice', TThostFtdcPriceType),
           ]
class CThostFtdcInputExecOrderField(Structure):
    _fields_ = [
           ('BrokerID', TThostFtdcBrokerIDType),
           ('InvestorID', TThostFtdcInvestorIDType),
           ('InstrumentID', TThostFtdcInstrumentIDType),
           ('ExecOrderRef', TThostFtdcOrderRefType),
           ('UserID', TThostFtdcUserIDType),
           ('Volume', TThostFtdcVolumeType),
           ('RequestID', TThostFtdcRequestIDType),
           ('BusinessUnit', TThostFtdcBusinessUnitType),
           ('OffsetFlag', TThostFtdcOffsetFlagType),
           ('HedgeFlag', TThostFtdcHedgeFlagType),
           ('ActionType', TThostFtdcActionTypeType),
           ('PosiDirection', TThostFtdcPosiDirectionType),
           ('ReservePositionFlag', TThostFtdcExecOrderPositionFlagType),
           ('CloseFlag', TThostFtdcExecOrderCloseFlagType),
           ]
class CThostFtdcInputExecOrderActionField(Structure):
    _fields_ = [
           ('BrokerID', TThostFtdcBrokerIDType),
           ('InvestorID', TThostFtdcInvestorIDType),
           ('ExecOrderActionRef', TThostFtdcOrderActionRefType),
           ('ExecOrderRef', TThostFtdcOrderRefType),
           ('RequestID', TThostFtdcRequestIDType),
           ('FrontID', TThostFtdcFrontIDType),
           ('SessionID', TThostFtdcSessionIDType),
           ('ExchangeID', TThostFtdcExchangeIDType),
           ('ExecOrderSysID', TThostFtdcExecOrderSysIDType),
           ('ActionFlag', TThostFtdcActionFlagType),
           ('UserID', TThostFtdcUserIDType),
           ('InstrumentID', TThostFtdcInstrumentIDType),
           ]
class CThostFtdcExecOrderField(Structure):
    _fields_ = [
           ('BrokerID', TThostFtdcBrokerIDType),
           ('InvestorID', TThostFtdcInvestorIDType),
           ('InstrumentID', TThostFtdcInstrumentIDType),
           ('ExecOrderRef', TThostFtdcOrderRefType),
           ('UserID', TThostFtdcUserIDType),
           ('Volume', TThostFtdcVolumeType),
           ('RequestID', TThostFtdcRequestIDType),
           ('BusinessUnit', TThostFtdcBusinessUnitType),
           ('OffsetFlag', TThostFtdcOffsetFlagType),
           ('HedgeFlag', TThostFtdcHedgeFlagType),
           ('ActionType', TThostFtdcActionTypeType),
           ('PosiDirection', TThostFtdcPosiDirectionType),
           ('ReservePositionFlag', TThostFtdcExecOrderPositionFlagType),
           ('CloseFlag', TThostFtdcExecOrderCloseFlagType),
           ('ExecOrderLocalID', TThostFtdcOrderLocalIDType),
           ('ExchangeID', TThostFtdcExchangeIDType),
           ('ParticipantID', TThostFtdcParticipantIDType),
           ('ClientID', TThostFtdcClientIDType),
           ('ExchangeInstID', TThostFtdcExchangeInstIDType),
           ('TraderID', TThostFtdcTraderIDType),
           ('InstallID', TThostFtdcInstallIDType),
           ('OrderSubmitStatus', TThostFtdcOrderSubmitStatusType),
           ('NotifySequence', TThostFtdcSequenceNoType),
           ('TradingDay', TThostFtdcDateType),
           ('SettlementID', TThostFtdcSettlementIDType),
           ('ExecOrderSysID', TThostFtdcExecOrderSysIDType),
           ('InsertDate', TThostFtdcDateType),
           ('InsertTime', TThostFtdcTimeType),
           ('CancelTime', TThostFtdcTimeType),
           ('ExecResult', TThostFtdcExecResultType),
           ('ClearingPartID', TThostFtdcParticipantIDType),
           ('SequenceNo', TThostFtdcSequenceNoType),
           ('FrontID', TThostFtdcFrontIDType),
           ('SessionID', TThostFtdcSessionIDType),
           ('UserProductInfo', TThostFtdcProductInfoType),
           ('StatusMsg', TThostFtdcErrorMsgType),
           ('ActiveUserID', TThostFtdcUserIDType),
           ('BrokerExecOrderSeq', TThostFtdcSequenceNoType),
           ]
class CThostFtdcExecOrderActionField(Structure):
    _fields_ = [
           ('BrokerID', TThostFtdcBrokerIDType),
           ('InvestorID', TThostFtdcInvestorIDType),
           ('ExecOrderActionRef', TThostFtdcOrderActionRefType),
           ('ExecOrderRef', TThostFtdcOrderRefType),
           ('RequestID', TThostFtdcRequestIDType),
           ('FrontID', TThostFtdcFrontIDType),
           ('SessionID', TThostFtdcSessionIDType),
           ('ExchangeID', TThostFtdcExchangeIDType),
           ('ExecOrderSysID', TThostFtdcExecOrderSysIDType),
           ('ActionFlag', TThostFtdcActionFlagType),
           ('ActionDate', TThostFtdcDateType),
           ('ActionTime', TThostFtdcTimeType),
           ('TraderID', TThostFtdcTraderIDType),
           ('InstallID', TThostFtdcInstallIDType),
           ('ExecOrderLocalID', TThostFtdcOrderLocalIDType),
           ('ActionLocalID', TThostFtdcOrderLocalIDType),
           ('ParticipantID', TThostFtdcParticipantIDType),
           ('ClientID', TThostFtdcClientIDType),
           ('BusinessUnit', TThostFtdcBusinessUnitType),
           ('OrderActionStatus', TThostFtdcOrderActionStatusType),
           ('UserID', TThostFtdcUserIDType),
           ('ActionType', TThostFtdcActionTypeType),
           ('StatusMsg', TThostFtdcErrorMsgType),
           ('InstrumentID', TThostFtdcInstrumentIDType),
           ]
class CThostFtdcQryExecOrderField(Structure):
    _fields_ = [
           ('BrokerID', TThostFtdcBrokerIDType),
           ('InvestorID', TThostFtdcInvestorIDType),
           ('InstrumentID', TThostFtdcInstrumentIDType),
           ('ExchangeID', TThostFtdcExchangeIDType),
           ('ExecOrderSysID', TThostFtdcExecOrderSysIDType),
           ('InsertTimeStart', TThostFtdcTimeType),
           ('InsertTimeEnd', TThostFtdcTimeType),
           ]
class CThostFtdcExchangeExecOrderField(Structure):
    _fields_ = [
           ('Volume', TThostFtdcVolumeType),
           ('RequestID', TThostFtdcRequestIDType),
           ('BusinessUnit', TThostFtdcBusinessUnitType),
           ('OffsetFlag', TThostFtdcOffsetFlagType),
           ('HedgeFlag', TThostFtdcHedgeFlagType),
           ('ActionType', TThostFtdcActionTypeType),
           ('PosiDirection', TThostFtdcPosiDirectionType),
           ('ReservePositionFlag', TThostFtdcExecOrderPositionFlagType),
           ('CloseFlag', TThostFtdcExecOrderCloseFlagType),
           ('ExecOrderLocalID', TThostFtdcOrderLocalIDType),
           ('ExchangeID', TThostFtdcExchangeIDType),
           ('ParticipantID', TThostFtdcParticipantIDType),
           ('ClientID', TThostFtdcClientIDType),
           ('ExchangeInstID', TThostFtdcExchangeInstIDType),
           ('TraderID', TThostFtdcTraderIDType),
           ('InstallID', TThostFtdcInstallIDType),
           ('OrderSubmitStatus', TThostFtdcOrderSubmitStatusType),
           ('NotifySequence', TThostFtdcSequenceNoType),
           ('TradingDay', TThostFtdcDateType),
           ('SettlementID', TThostFtdcSettlementIDType),
           ('ExecOrderSysID', TThostFtdcExecOrderSysIDType),
           ('InsertDate', TThostFtdcDateType),
           ('InsertTime', TThostFtdcTimeType),
           ('CancelTime', TThostFtdcTimeType),
           ('ExecResult', TThostFtdcExecResultType),
           ('ClearingPartID', TThostFtdcParticipantIDType),
           ('SequenceNo', TThostFtdcSequenceNoType),
           ]
class CThostFtdcQryExchangeExecOrderField(Structure):
    _fields_ = [
           ('ParticipantID', TThostFtdcParticipantIDType),
           ('ClientID', TThostFtdcClientIDType),
           ('ExchangeInstID', TThostFtdcExchangeInstIDType),
           ('ExchangeID', TThostFtdcExchangeIDType),
           ('TraderID', TThostFtdcTraderIDType),
           ]
class CThostFtdcQryExecOrderActionField(Structure):
    _fields_ = [
           ('BrokerID', TThostFtdcBrokerIDType),
           ('InvestorID', TThostFtdcInvestorIDType),
           ('ExchangeID', TThostFtdcExchangeIDType),
           ]
class CThostFtdcExchangeExecOrderActionField(Structure):
    _fields_ = [
           ('ExchangeID', TThostFtdcExchangeIDType),
           ('ExecOrderSysID', TThostFtdcExecOrderSysIDType),
           ('ActionFlag', TThostFtdcActionFlagType),
           ('ActionDate', TThostFtdcDateType),
           ('ActionTime', TThostFtdcTimeType),
           ('TraderID', TThostFtdcTraderIDType),
           ('InstallID', TThostFtdcInstallIDType),
           ('ExecOrderLocalID', TThostFtdcOrderLocalIDType),
           ('ActionLocalID', TThostFtdcOrderLocalIDType),
           ('ParticipantID', TThostFtdcParticipantIDType),
           ('ClientID', TThostFtdcClientIDType),
           ('BusinessUnit', TThostFtdcBusinessUnitType),
           ('OrderActionStatus', TThostFtdcOrderActionStatusType),
           ('UserID', TThostFtdcUserIDType),
           ('ActionType', TThostFtdcActionTypeType),
           ]
class CThostFtdcQryExchangeExecOrderActionField(Structure):
    _fields_ = [
           ('ParticipantID', TThostFtdcParticipantIDType),
           ('ClientID', TThostFtdcClientIDType),
           ('ExchangeID', TThostFtdcExchangeIDType),
           ('TraderID', TThostFtdcTraderIDType),
           ]
class CThostFtdcErrExecOrderField(Structure):
    _fields_ = [
           ('BrokerID', TThostFtdcBrokerIDType),
           ('InvestorID', TThostFtdcInvestorIDType),
           ('InstrumentID', TThostFtdcInstrumentIDType),
           ('ExecOrderRef', TThostFtdcOrderRefType),
           ('UserID', TThostFtdcUserIDType),
           ('Volume', TThostFtdcVolumeType),
           ('RequestID', TThostFtdcRequestIDType),
           ('BusinessUnit', TThostFtdcBusinessUnitType),
           ('OffsetFlag', TThostFtdcOffsetFlagType),
           ('HedgeFlag', TThostFtdcHedgeFlagType),
           ('ActionType', TThostFtdcActionTypeType),
           ('PosiDirection', TThostFtdcPosiDirectionType),
           ('ReservePositionFlag', TThostFtdcExecOrderPositionFlagType),
           ('CloseFlag', TThostFtdcExecOrderCloseFlagType),
           ('ErrorID', TThostFtdcErrorIDType),
           ('ErrorMsg', TThostFtdcErrorMsgType),
           ]
class CThostFtdcQryErrExecOrderField(Structure):
    _fields_ = [
           ('BrokerID', TThostFtdcBrokerIDType),
           ('InvestorID', TThostFtdcInvestorIDType),
           ]
class CThostFtdcErrExecOrderActionField(Structure):
    _fields_ = [
           ('BrokerID', TThostFtdcBrokerIDType),
           ('InvestorID', TThostFtdcInvestorIDType),
           ('ExecOrderActionRef', TThostFtdcOrderActionRefType),
           ('ExecOrderRef', TThostFtdcOrderRefType),
           ('RequestID', TThostFtdcRequestIDType),
           ('FrontID', TThostFtdcFrontIDType),
           ('SessionID', TThostFtdcSessionIDType),
           ('ExchangeID', TThostFtdcExchangeIDType),
           ('ExecOrderSysID', TThostFtdcExecOrderSysIDType),
           ('ActionFlag', TThostFtdcActionFlagType),
           ('UserID', TThostFtdcUserIDType),
           ('InstrumentID', TThostFtdcInstrumentIDType),
           ('ErrorID', TThostFtdcErrorIDType),
           ('ErrorMsg', TThostFtdcErrorMsgType),
           ]
class CThostFtdcQryErrExecOrderActionField(Structure):
    _fields_ = [
           ('BrokerID', TThostFtdcBrokerIDType),
           ('InvestorID', TThostFtdcInvestorIDType),
           ]
class CThostFtdcOptionInstrTradingRightField(Structure):
    _fields_ = [
           ('InstrumentID', TThostFtdcInstrumentIDType),
           ('InvestorRange', TThostFtdcInvestorRangeType),
           ('BrokerID', TThostFtdcBrokerIDType),
           ('InvestorID', TThostFtdcInvestorIDType),
           ('Direction', TThostFtdcDirectionType),
           ('TradingRight', TThostFtdcTradingRightType),
           ]
class CThostFtdcQryOptionInstrTradingRightField(Structure):
    _fields_ = [
           ('BrokerID', TThostFtdcBrokerIDType),
           ('InvestorID', TThostFtdcInvestorIDType),
           ('InstrumentID', TThostFtdcInstrumentIDType),
           ('Direction', TThostFtdcDirectionType),
           ]
class CThostFtdcInputForQuoteField(Structure):
    _fields_ = [
           ('BrokerID', TThostFtdcBrokerIDType),
           ('InvestorID', TThostFtdcInvestorIDType),
           ('InstrumentID', TThostFtdcInstrumentIDType),
           ('ForQuoteRef', TThostFtdcOrderRefType),
           ('UserID', TThostFtdcUserIDType),
           ]
class CThostFtdcForQuoteField(Structure):
    _fields_ = [
           ('BrokerID', TThostFtdcBrokerIDType),
           ('InvestorID', TThostFtdcInvestorIDType),
           ('InstrumentID', TThostFtdcInstrumentIDType),
           ('ForQuoteRef', TThostFtdcOrderRefType),
           ('UserID', TThostFtdcUserIDType),
           ('ForQuoteLocalID', TThostFtdcOrderLocalIDType),
           ('ExchangeID', TThostFtdcExchangeIDType),
           ('ParticipantID', TThostFtdcParticipantIDType),
           ('ClientID', TThostFtdcClientIDType),
           ('ExchangeInstID', TThostFtdcExchangeInstIDType),
           ('TraderID', TThostFtdcTraderIDType),
           ('InstallID', TThostFtdcInstallIDType),
           ('InsertDate', TThostFtdcDateType),
           ('InsertTime', TThostFtdcTimeType),
           ('ForQuoteStatus', TThostFtdcForQuoteStatusType),
           ('FrontID', TThostFtdcFrontIDType),
           ('SessionID', TThostFtdcSessionIDType),
           ('StatusMsg', TThostFtdcErrorMsgType),
           ('ActiveUserID', TThostFtdcUserIDType),
           ('BrokerForQutoSeq', TThostFtdcSequenceNoType),
           ]
class CThostFtdcQryForQuoteField(Structure):
    _fields_ = [
           ('BrokerID', TThostFtdcBrokerIDType),
           ('InvestorID', TThostFtdcInvestorIDType),
           ('InstrumentID', TThostFtdcInstrumentIDType),
           ('ExchangeID', TThostFtdcExchangeIDType),
           ('InsertTimeStart', TThostFtdcTimeType),
           ('InsertTimeEnd', TThostFtdcTimeType),
           ]
class CThostFtdcExchangeForQuoteField(Structure):
    _fields_ = [
           ('ForQuoteLocalID', TThostFtdcOrderLocalIDType),
           ('ExchangeID', TThostFtdcExchangeIDType),
           ('ParticipantID', TThostFtdcParticipantIDType),
           ('ClientID', TThostFtdcClientIDType),
           ('ExchangeInstID', TThostFtdcExchangeInstIDType),
           ('TraderID', TThostFtdcTraderIDType),
           ('InstallID', TThostFtdcInstallIDType),
           ('InsertDate', TThostFtdcDateType),
           ('InsertTime', TThostFtdcTimeType),
           ('ForQuoteStatus', TThostFtdcForQuoteStatusType),
           ]
class CThostFtdcQryExchangeForQuoteField(Structure):
    _fields_ = [
           ('ParticipantID', TThostFtdcParticipantIDType),
           ('ClientID', TThostFtdcClientIDType),
           ('ExchangeInstID', TThostFtdcExchangeInstIDType),
           ('ExchangeID', TThostFtdcExchangeIDType),
           ('TraderID', TThostFtdcTraderIDType),
           ]
class CThostFtdcInputQuoteField(Structure):
    _fields_ = [
           ('BrokerID', TThostFtdcBrokerIDType),
           ('InvestorID', TThostFtdcInvestorIDType),
           ('InstrumentID', TThostFtdcInstrumentIDType),
           ('QuoteRef', TThostFtdcOrderRefType),
           ('UserID', TThostFtdcUserIDType),
           ('AskPrice', TThostFtdcPriceType),
           ('BidPrice', TThostFtdcPriceType),
           ('AskVolume', TThostFtdcVolumeType),
           ('BidVolume', TThostFtdcVolumeType),
           ('RequestID', TThostFtdcRequestIDType),
           ('BusinessUnit', TThostFtdcBusinessUnitType),
           ('AskOffsetFlag', TThostFtdcOffsetFlagType),
           ('BidOffsetFlag', TThostFtdcOffsetFlagType),
           ('AskHedgeFlag', TThostFtdcHedgeFlagType),
           ('BidHedgeFlag', TThostFtdcHedgeFlagType),
           ('AskOrderRef', TThostFtdcOrderRefType),
           ('BidOrderRef', TThostFtdcOrderRefType),
           ]
class CThostFtdcInputQuoteActionField(Structure):
    _fields_ = [
           ('BrokerID', TThostFtdcBrokerIDType),
           ('InvestorID', TThostFtdcInvestorIDType),
           ('QuoteActionRef', TThostFtdcOrderActionRefType),
           ('QuoteRef', TThostFtdcOrderRefType),
           ('RequestID', TThostFtdcRequestIDType),
           ('FrontID', TThostFtdcFrontIDType),
           ('SessionID', TThostFtdcSessionIDType),
           ('ExchangeID', TThostFtdcExchangeIDType),
           ('QuoteSysID', TThostFtdcOrderSysIDType),
           ('ActionFlag', TThostFtdcActionFlagType),
           ('UserID', TThostFtdcUserIDType),
           ('InstrumentID', TThostFtdcInstrumentIDType),
           ]
class CThostFtdcQuoteField(Structure):
    _fields_ = [
           ('BrokerID', TThostFtdcBrokerIDType),
           ('InvestorID', TThostFtdcInvestorIDType),
           ('InstrumentID', TThostFtdcInstrumentIDType),
           ('QuoteRef', TThostFtdcOrderRefType),
           ('UserID', TThostFtdcUserIDType),
           ('AskPrice', TThostFtdcPriceType),
           ('BidPrice', TThostFtdcPriceType),
           ('AskVolume', TThostFtdcVolumeType),
           ('BidVolume', TThostFtdcVolumeType),
           ('RequestID', TThostFtdcRequestIDType),
           ('BusinessUnit', TThostFtdcBusinessUnitType),
           ('AskOffsetFlag', TThostFtdcOffsetFlagType),
           ('BidOffsetFlag', TThostFtdcOffsetFlagType),
           ('AskHedgeFlag', TThostFtdcHedgeFlagType),
           ('BidHedgeFlag', TThostFtdcHedgeFlagType),
           ('QuoteLocalID', TThostFtdcOrderLocalIDType),
           ('ExchangeID', TThostFtdcExchangeIDType),
           ('ParticipantID', TThostFtdcParticipantIDType),
           ('ClientID', TThostFtdcClientIDType),
           ('ExchangeInstID', TThostFtdcExchangeInstIDType),
           ('TraderID', TThostFtdcTraderIDType),
           ('InstallID', TThostFtdcInstallIDType),
           ('NotifySequence', TThostFtdcSequenceNoType),
           ('OrderSubmitStatus', TThostFtdcOrderSubmitStatusType),
           ('TradingDay', TThostFtdcDateType),
           ('SettlementID', TThostFtdcSettlementIDType),
           ('QuoteSysID', TThostFtdcOrderSysIDType),
           ('InsertDate', TThostFtdcDateType),
           ('InsertTime', TThostFtdcTimeType),
           ('CancelTime', TThostFtdcTimeType),
           ('QuoteStatus', TThostFtdcOrderStatusType),
           ('ClearingPartID', TThostFtdcParticipantIDType),
           ('SequenceNo', TThostFtdcSequenceNoType),
           ('AskOrderSysID', TThostFtdcOrderSysIDType),
           ('BidOrderSysID', TThostFtdcOrderSysIDType),
           ('FrontID', TThostFtdcFrontIDType),
           ('SessionID', TThostFtdcSessionIDType),
           ('UserProductInfo', TThostFtdcProductInfoType),
           ('StatusMsg', TThostFtdcErrorMsgType),
           ('ActiveUserID', TThostFtdcUserIDType),
           ('BrokerQuoteSeq', TThostFtdcSequenceNoType),
           ('AskOrderRef', TThostFtdcOrderRefType),
           ('BidOrderRef', TThostFtdcOrderRefType),
           ]
class CThostFtdcQuoteActionField(Structure):
    _fields_ = [
           ('BrokerID', TThostFtdcBrokerIDType),
           ('InvestorID', TThostFtdcInvestorIDType),
           ('QuoteActionRef', TThostFtdcOrderActionRefType),
           ('QuoteRef', TThostFtdcOrderRefType),
           ('RequestID', TThostFtdcRequestIDType),
           ('FrontID', TThostFtdcFrontIDType),
           ('SessionID', TThostFtdcSessionIDType),
           ('ExchangeID', TThostFtdcExchangeIDType),
           ('QuoteSysID', TThostFtdcOrderSysIDType),
           ('ActionFlag', TThostFtdcActionFlagType),
           ('ActionDate', TThostFtdcDateType),
           ('ActionTime', TThostFtdcTimeType),
           ('TraderID', TThostFtdcTraderIDType),
           ('InstallID', TThostFtdcInstallIDType),
           ('QuoteLocalID', TThostFtdcOrderLocalIDType),
           ('ActionLocalID', TThostFtdcOrderLocalIDType),
           ('ParticipantID', TThostFtdcParticipantIDType),
           ('ClientID', TThostFtdcClientIDType),
           ('BusinessUnit', TThostFtdcBusinessUnitType),
           ('OrderActionStatus', TThostFtdcOrderActionStatusType),
           ('UserID', TThostFtdcUserIDType),
           ('StatusMsg', TThostFtdcErrorMsgType),
           ('InstrumentID', TThostFtdcInstrumentIDType),
           ]
class CThostFtdcQryQuoteField(Structure):
    _fields_ = [
           ('BrokerID', TThostFtdcBrokerIDType),
           ('InvestorID', TThostFtdcInvestorIDType),
           ('InstrumentID', TThostFtdcInstrumentIDType),
           ('ExchangeID', TThostFtdcExchangeIDType),
           ('QuoteSysID', TThostFtdcOrderSysIDType),
           ('InsertTimeStart', TThostFtdcTimeType),
           ('InsertTimeEnd', TThostFtdcTimeType),
           ]
class CThostFtdcExchangeQuoteField(Structure):
    _fields_ = [
           ('AskPrice', TThostFtdcPriceType),
           ('BidPrice', TThostFtdcPriceType),
           ('AskVolume', TThostFtdcVolumeType),
           ('BidVolume', TThostFtdcVolumeType),
           ('RequestID', TThostFtdcRequestIDType),
           ('BusinessUnit', TThostFtdcBusinessUnitType),
           ('AskOffsetFlag', TThostFtdcOffsetFlagType),
           ('BidOffsetFlag', TThostFtdcOffsetFlagType),
           ('AskHedgeFlag', TThostFtdcHedgeFlagType),
           ('BidHedgeFlag', TThostFtdcHedgeFlagType),
           ('QuoteLocalID', TThostFtdcOrderLocalIDType),
           ('ExchangeID', TThostFtdcExchangeIDType),
           ('ParticipantID', TThostFtdcParticipantIDType),
           ('ClientID', TThostFtdcClientIDType),
           ('ExchangeInstID', TThostFtdcExchangeInstIDType),
           ('TraderID', TThostFtdcTraderIDType),
           ('InstallID', TThostFtdcInstallIDType),
           ('NotifySequence', TThostFtdcSequenceNoType),
           ('OrderSubmitStatus', TThostFtdcOrderSubmitStatusType),
           ('TradingDay', TThostFtdcDateType),
           ('SettlementID', TThostFtdcSettlementIDType),
           ('QuoteSysID', TThostFtdcOrderSysIDType),
           ('InsertDate', TThostFtdcDateType),
           ('InsertTime', TThostFtdcTimeType),
           ('CancelTime', TThostFtdcTimeType),
           ('QuoteStatus', TThostFtdcOrderStatusType),
           ('ClearingPartID', TThostFtdcParticipantIDType),
           ('SequenceNo', TThostFtdcSequenceNoType),
           ('AskOrderSysID', TThostFtdcOrderSysIDType),
           ('BidOrderSysID', TThostFtdcOrderSysIDType),
           ]
class CThostFtdcQryExchangeQuoteField(Structure):
    _fields_ = [
           ('ParticipantID', TThostFtdcParticipantIDType),
           ('ClientID', TThostFtdcClientIDType),
           ('ExchangeInstID', TThostFtdcExchangeInstIDType),
           ('ExchangeID', TThostFtdcExchangeIDType),
           ('TraderID', TThostFtdcTraderIDType),
           ]
class CThostFtdcQryQuoteActionField(Structure):
    _fields_ = [
           ('BrokerID', TThostFtdcBrokerIDType),
           ('InvestorID', TThostFtdcInvestorIDType),
           ('ExchangeID', TThostFtdcExchangeIDType),
           ]
class CThostFtdcExchangeQuoteActionField(Structure):
    _fields_ = [
           ('ExchangeID', TThostFtdcExchangeIDType),
           ('QuoteSysID', TThostFtdcOrderSysIDType),
           ('ActionFlag', TThostFtdcActionFlagType),
           ('ActionDate', TThostFtdcDateType),
           ('ActionTime', TThostFtdcTimeType),
           ('TraderID', TThostFtdcTraderIDType),
           ('InstallID', TThostFtdcInstallIDType),
           ('QuoteLocalID', TThostFtdcOrderLocalIDType),
           ('ActionLocalID', TThostFtdcOrderLocalIDType),
           ('ParticipantID', TThostFtdcParticipantIDType),
           ('ClientID', TThostFtdcClientIDType),
           ('BusinessUnit', TThostFtdcBusinessUnitType),
           ('OrderActionStatus', TThostFtdcOrderActionStatusType),
           ('UserID', TThostFtdcUserIDType),
           ]
class CThostFtdcQryExchangeQuoteActionField(Structure):
    _fields_ = [
           ('ParticipantID', TThostFtdcParticipantIDType),
           ('ClientID', TThostFtdcClientIDType),
           ('ExchangeID', TThostFtdcExchangeIDType),
           ('TraderID', TThostFtdcTraderIDType),
           ]
class CThostFtdcOptionInstrDeltaField(Structure):
    _fields_ = [
           ('InstrumentID', TThostFtdcInstrumentIDType),
           ('InvestorRange', TThostFtdcInvestorRangeType),
           ('BrokerID', TThostFtdcBrokerIDType),
           ('InvestorID', TThostFtdcInvestorIDType),
           ('Delta', TThostFtdcRatioType),
           ]
class CThostFtdcForQuoteRspField(Structure):
    _fields_ = [
           ('TradingDay', TThostFtdcDateType),
           ('InstrumentID', TThostFtdcInstrumentIDType),
           ('ForQuoteSysID', TThostFtdcOrderSysIDType),
           ('ForQuoteTime', TThostFtdcTimeType),
           ('ActionDay', TThostFtdcDateType),
           ('ExchangeID', TThostFtdcExchangeIDType),
           ]
class CThostFtdcStrikeOffsetField(Structure):
    _fields_ = [
           ('InstrumentID', TThostFtdcInstrumentIDType),
           ('InvestorRange', TThostFtdcInvestorRangeType),
           ('BrokerID', TThostFtdcBrokerIDType),
           ('InvestorID', TThostFtdcInvestorIDType),
           ('Offset', TThostFtdcMoneyType),
           ]
class CThostFtdcQryStrikeOffsetField(Structure):
    _fields_ = [
           ('BrokerID', TThostFtdcBrokerIDType),
           ('InvestorID', TThostFtdcInvestorIDType),
           ('InstrumentID', TThostFtdcInstrumentIDType),
           ]
class CThostFtdcMarketDataField(Structure):
    _fields_ = [
           ('TradingDay', TThostFtdcDateType),
           ('InstrumentID', TThostFtdcInstrumentIDType),
           ('ExchangeID', TThostFtdcExchangeIDType),
           ('ExchangeInstID', TThostFtdcExchangeInstIDType),
           ('LastPrice', TThostFtdcPriceType),
           ('PreSettlementPrice', TThostFtdcPriceType),
           ('PreClosePrice', TThostFtdcPriceType),
           ('PreOpenInterest', TThostFtdcLargeVolumeType),
           ('OpenPrice', TThostFtdcPriceType),
           ('HighestPrice', TThostFtdcPriceType),
           ('LowestPrice', TThostFtdcPriceType),
           ('Volume', TThostFtdcVolumeType),
           ('Turnover', TThostFtdcMoneyType),
           ('OpenInterest', TThostFtdcLargeVolumeType),
           ('ClosePrice', TThostFtdcPriceType),
           ('SettlementPrice', TThostFtdcPriceType),
           ('UpperLimitPrice', TThostFtdcPriceType),
           ('LowerLimitPrice', TThostFtdcPriceType),
           ('PreDelta', TThostFtdcRatioType),
           ('CurrDelta', TThostFtdcRatioType),
           ('UpdateTime', TThostFtdcTimeType),
           ('UpdateMillisec', TThostFtdcMillisecType),
           ('ActionDay', TThostFtdcDateType),
           ]
class CThostFtdcMarketDataBaseField(Structure):
    _fields_ = [
           ('TradingDay', TThostFtdcDateType),
           ('PreSettlementPrice', TThostFtdcPriceType),
           ('PreClosePrice', TThostFtdcPriceType),
           ('PreOpenInterest', TThostFtdcLargeVolumeType),
           ('PreDelta', TThostFtdcRatioType),
           ]
class CThostFtdcMarketDataStaticField(Structure):
    _fields_ = [
           ('OpenPrice', TThostFtdcPriceType),
           ('HighestPrice', TThostFtdcPriceType),
           ('LowestPrice', TThostFtdcPriceType),
           ('ClosePrice', TThostFtdcPriceType),
           ('UpperLimitPrice', TThostFtdcPriceType),
           ('LowerLimitPrice', TThostFtdcPriceType),
           ('SettlementPrice', TThostFtdcPriceType),
           ('CurrDelta', TThostFtdcRatioType),
           ]
class CThostFtdcMarketDataLastMatchField(Structure):
    _fields_ = [
           ('LastPrice', TThostFtdcPriceType),
           ('Volume', TThostFtdcVolumeType),
           ('Turnover', TThostFtdcMoneyType),
           ('OpenInterest', TThostFtdcLargeVolumeType),
           ]
class CThostFtdcMarketDataBestPriceField(Structure):
    _fields_ = [
           ('BidPrice1', TThostFtdcPriceType),
           ('BidVolume1', TThostFtdcVolumeType),
           ('AskPrice1', TThostFtdcPriceType),
           ('AskVolume1', TThostFtdcVolumeType),
           ]
class CThostFtdcMarketDataBid23Field(Structure):
    _fields_ = [
           ('BidPrice2', TThostFtdcPriceType),
           ('BidVolume2', TThostFtdcVolumeType),
           ('BidPrice3', TThostFtdcPriceType),
           ('BidVolume3', TThostFtdcVolumeType),
           ]
class CThostFtdcMarketDataAsk23Field(Structure):
    _fields_ = [
           ('AskPrice2', TThostFtdcPriceType),
           ('AskVolume2', TThostFtdcVolumeType),
           ('AskPrice3', TThostFtdcPriceType),
           ('AskVolume3', TThostFtdcVolumeType),
           ]
class CThostFtdcMarketDataBid45Field(Structure):
    _fields_ = [
           ('BidPrice4', TThostFtdcPriceType),
           ('BidVolume4', TThostFtdcVolumeType),
           ('BidPrice5', TThostFtdcPriceType),
           ('BidVolume5', TThostFtdcVolumeType),
           ]
class CThostFtdcMarketDataAsk45Field(Structure):
    _fields_ = [
           ('AskPrice4', TThostFtdcPriceType),
           ('AskVolume4', TThostFtdcVolumeType),
           ('AskPrice5', TThostFtdcPriceType),
           ('AskVolume5', TThostFtdcVolumeType),
           ]
class CThostFtdcMarketDataUpdateTimeField(Structure):
    _fields_ = [
           ('InstrumentID', TThostFtdcInstrumentIDType),
           ('UpdateTime', TThostFtdcTimeType),
           ('UpdateMillisec', TThostFtdcMillisecType),
           ('ActionDay', TThostFtdcDateType),
           ]
class CThostFtdcMarketDataExchangeField(Structure):
    _fields_ = [
           ('ExchangeID', TThostFtdcExchangeIDType),
           ]
class CThostFtdcSpecificInstrumentField(Structure):
    _fields_ = [
           ('InstrumentID', TThostFtdcInstrumentIDType),
           ]
class CThostFtdcInstrumentStatusField(Structure):
    _fields_ = [
           ('ExchangeID', TThostFtdcExchangeIDType),
           ('ExchangeInstID', TThostFtdcExchangeInstIDType),
           ('SettlementGroupID', TThostFtdcSettlementGroupIDType),
           ('InstrumentID', TThostFtdcInstrumentIDType),
           ('InstrumentStatus', TThostFtdcInstrumentStatusType),
           ('TradingSegmentSN', TThostFtdcTradingSegmentSNType),
           ('EnterTime', TThostFtdcTimeType),
           ('EnterReason', TThostFtdcInstStatusEnterReasonType),
           ]
class CThostFtdcQryInstrumentStatusField(Structure):
    _fields_ = [
           ('ExchangeID', TThostFtdcExchangeIDType),
           ('ExchangeInstID', TThostFtdcExchangeInstIDType),
           ]
class CThostFtdcInvestorAccountField(Structure):
    _fields_ = [
           ('BrokerID', TThostFtdcBrokerIDType),
           ('InvestorID', TThostFtdcInvestorIDType),
           ('AccountID', TThostFtdcAccountIDType),
           ('CurrencyID', TThostFtdcCurrencyIDType),
           ]
class CThostFtdcPositionProfitAlgorithmField(Structure):
    _fields_ = [
           ('BrokerID', TThostFtdcBrokerIDType),
           ('AccountID', TThostFtdcAccountIDType),
           ('Algorithm', TThostFtdcAlgorithmType),
           ('Memo', TThostFtdcMemoType),
           ('CurrencyID', TThostFtdcCurrencyIDType),
           ]
class CThostFtdcDiscountField(Structure):
    _fields_ = [
           ('BrokerID', TThostFtdcBrokerIDType),
           ('InvestorRange', TThostFtdcInvestorRangeType),
           ('InvestorID', TThostFtdcInvestorIDType),
           ('Discount', TThostFtdcRatioType),
           ]
class CThostFtdcQryTransferBankField(Structure):
    _fields_ = [
           ('BankID', TThostFtdcBankIDType),
           ('BankBrchID', TThostFtdcBankBrchIDType),
           ]
class CThostFtdcTransferBankField(Structure):
    _fields_ = [
           ('BankID', TThostFtdcBankIDType),
           ('BankBrchID', TThostFtdcBankBrchIDType),
           ('BankName', TThostFtdcBankNameType),
           ('IsActive', TThostFtdcBoolType),
           ]
class CThostFtdcQryInvestorPositionDetailField(Structure):
    _fields_ = [
           ('BrokerID', TThostFtdcBrokerIDType),
           ('InvestorID', TThostFtdcInvestorIDType),
           ('InstrumentID', TThostFtdcInstrumentIDType),
           ]
class CThostFtdcInvestorPositionDetailField(Structure):
    _fields_ = [
           ('InstrumentID', TThostFtdcInstrumentIDType),
           ('BrokerID', TThostFtdcBrokerIDType),
           ('InvestorID', TThostFtdcInvestorIDType),
           ('HedgeFlag', TThostFtdcHedgeFlagType),
           ('Direction', TThostFtdcDirectionType),
           ('OpenDate', TThostFtdcDateType),
           ('TradeID', TThostFtdcTradeIDType),
           ('Volume', TThostFtdcVolumeType),
           ('OpenPrice', TThostFtdcPriceType),
           ('TradingDay', TThostFtdcDateType),
           ('SettlementID', TThostFtdcSettlementIDType),
           ('TradeType', TThostFtdcTradeTypeType),
           ('CombInstrumentID', TThostFtdcInstrumentIDType),
           ('ExchangeID', TThostFtdcExchangeIDType),
           ('CloseProfitByDate', TThostFtdcMoneyType),
           ('CloseProfitByTrade', TThostFtdcMoneyType),
           ('PositionProfitByDate', TThostFtdcMoneyType),
           ('PositionProfitByTrade', TThostFtdcMoneyType),
           ('Margin', TThostFtdcMoneyType),
           ('ExchMargin', TThostFtdcMoneyType),
           ('MarginRateByMoney', TThostFtdcRatioType),
           ('MarginRateByVolume', TThostFtdcRatioType),
           ('LastSettlementPrice', TThostFtdcPriceType),
           ('SettlementPrice', TThostFtdcPriceType),
           ('CloseVolume', TThostFtdcVolumeType),
           ('CloseAmount', TThostFtdcMoneyType),
           ]
class CThostFtdcTradingAccountPasswordField(Structure):
    _fields_ = [
           ('BrokerID', TThostFtdcBrokerIDType),
           ('AccountID', TThostFtdcAccountIDType),
           ('Password', TThostFtdcPasswordType),
           ('CurrencyID', TThostFtdcCurrencyIDType),
           ]
class CThostFtdcMDTraderOfferField(Structure):
    _fields_ = [
           ('ExchangeID', TThostFtdcExchangeIDType),
           ('TraderID', TThostFtdcTraderIDType),
           ('ParticipantID', TThostFtdcParticipantIDType),
           ('Password', TThostFtdcPasswordType),
           ('InstallID', TThostFtdcInstallIDType),
           ('OrderLocalID', TThostFtdcOrderLocalIDType),
           ('TraderConnectStatus', TThostFtdcTraderConnectStatusType),
           ('ConnectRequestDate', TThostFtdcDateType),
           ('ConnectRequestTime', TThostFtdcTimeType),
           ('LastReportDate', TThostFtdcDateType),
           ('LastReportTime', TThostFtdcTimeType),
           ('ConnectDate', TThostFtdcDateType),
           ('ConnectTime', TThostFtdcTimeType),
           ('StartDate', TThostFtdcDateType),
           ('StartTime', TThostFtdcTimeType),
           ('TradingDay', TThostFtdcDateType),
           ('BrokerID', TThostFtdcBrokerIDType),
           ('MaxTradeID', TThostFtdcTradeIDType),
           ('MaxOrderMessageReference', TThostFtdcReturnCodeType),
           ]
class CThostFtdcQryMDTraderOfferField(Structure):
    _fields_ = [
           ('ExchangeID', TThostFtdcExchangeIDType),
           ('ParticipantID', TThostFtdcParticipantIDType),
           ('TraderID', TThostFtdcTraderIDType),
           ]
class CThostFtdcQryNoticeField(Structure):
    _fields_ = [
           ('BrokerID', TThostFtdcBrokerIDType),
           ]
class CThostFtdcNoticeField(Structure):
    _fields_ = [
           ('BrokerID', TThostFtdcBrokerIDType),
           ('Content', TThostFtdcContentType),
           ('SequenceLabel', TThostFtdcSequenceLabelType),
           ]
class CThostFtdcUserRightField(Structure):
    _fields_ = [
           ('BrokerID', TThostFtdcBrokerIDType),
           ('UserID', TThostFtdcUserIDType),
           ('UserRightType', TThostFtdcUserRightTypeType),
           ('IsForbidden', TThostFtdcBoolType),
           ]
class CThostFtdcQrySettlementInfoConfirmField(Structure):
    _fields_ = [
           ('BrokerID', TThostFtdcBrokerIDType),
           ('InvestorID', TThostFtdcInvestorIDType),
           ]
class CThostFtdcLoadSettlementInfoField(Structure):
    _fields_ = [
           ('BrokerID', TThostFtdcBrokerIDType),
           ]
class CThostFtdcBrokerWithdrawAlgorithmField(Structure):
    _fields_ = [
           ('BrokerID', TThostFtdcBrokerIDType),
           ('WithdrawAlgorithm', TThostFtdcAlgorithmType),
           ('UsingRatio', TThostFtdcRatioType),
           ('IncludeCloseProfit', TThostFtdcIncludeCloseProfitType),
           ('AllWithoutTrade', TThostFtdcAllWithoutTradeType),
           ('AvailIncludeCloseProfit', TThostFtdcIncludeCloseProfitType),
           ('IsBrokerUserEvent', TThostFtdcBoolType),
           ('CurrencyID', TThostFtdcCurrencyIDType),
           ('FundMortgageRatio', TThostFtdcRatioType),
           ('BalanceAlgorithm', TThostFtdcBalanceAlgorithmType),
           ]
class CThostFtdcTradingAccountPasswordUpdateV1Field(Structure):
    _fields_ = [
           ('BrokerID', TThostFtdcBrokerIDType),
           ('InvestorID', TThostFtdcInvestorIDType),
           ('OldPassword', TThostFtdcPasswordType),
           ('NewPassword', TThostFtdcPasswordType),
           ]
class CThostFtdcTradingAccountPasswordUpdateField(Structure):
    _fields_ = [
           ('BrokerID', TThostFtdcBrokerIDType),
           ('AccountID', TThostFtdcAccountIDType),
           ('OldPassword', TThostFtdcPasswordType),
           ('NewPassword', TThostFtdcPasswordType),
           ('CurrencyID', TThostFtdcCurrencyIDType),
           ]
class CThostFtdcQryCombinationLegField(Structure):
    _fields_ = [
           ('CombInstrumentID', TThostFtdcInstrumentIDType),
           ('LegID', TThostFtdcLegIDType),
           ('LegInstrumentID', TThostFtdcInstrumentIDType),
           ]
class CThostFtdcQrySyncStatusField(Structure):
    _fields_ = [
           ('TradingDay', TThostFtdcDateType),
           ]
class CThostFtdcCombinationLegField(Structure):
    _fields_ = [
           ('CombInstrumentID', TThostFtdcInstrumentIDType),
           ('LegID', TThostFtdcLegIDType),
           ('LegInstrumentID', TThostFtdcInstrumentIDType),
           ('Direction', TThostFtdcDirectionType),
           ('LegMultiple', TThostFtdcLegMultipleType),
           ('ImplyLevel', TThostFtdcImplyLevelType),
           ]
class CThostFtdcSyncStatusField(Structure):
    _fields_ = [
           ('TradingDay', TThostFtdcDateType),
           ('DataSyncStatus', TThostFtdcDataSyncStatusType),
           ]
class CThostFtdcQryLinkManField(Structure):
    _fields_ = [
           ('BrokerID', TThostFtdcBrokerIDType),
           ('InvestorID', TThostFtdcInvestorIDType),
           ]
class CThostFtdcLinkManField(Structure):
    _fields_ = [
           ('BrokerID', TThostFtdcBrokerIDType),
           ('InvestorID', TThostFtdcInvestorIDType),
           ('PersonType', TThostFtdcPersonTypeType),
           ('IdentifiedCardType', TThostFtdcIdCardTypeType),
           ('IdentifiedCardNo', TThostFtdcIdentifiedCardNoType),
           ('PersonName', TThostFtdcPartyNameType),
           ('Telephone', TThostFtdcTelephoneType),
           ('Address', TThostFtdcAddressType),
           ('ZipCode', TThostFtdcZipCodeType),
           ('Priority', TThostFtdcPriorityType),
           ('UOAZipCode', TThostFtdcUOAZipCodeType),
           ('PersonFullName', TThostFtdcInvestorFullNameType),
           ]
class CThostFtdcQryBrokerUserEventField(Structure):
    _fields_ = [
           ('BrokerID', TThostFtdcBrokerIDType),
           ('UserID', TThostFtdcUserIDType),
           ('UserEventType', TThostFtdcUserEventTypeType),
           ]
class CThostFtdcBrokerUserEventField(Structure):
    _fields_ = [
           ('BrokerID', TThostFtdcBrokerIDType),
           ('UserID', TThostFtdcUserIDType),
           ('UserEventType', TThostFtdcUserEventTypeType),
           ('EventSequenceNo', TThostFtdcSequenceNoType),
           ('EventDate', TThostFtdcDateType),
           ('EventTime', TThostFtdcTimeType),
           ('UserEventInfo', TThostFtdcUserEventInfoType),
           ('InvestorID', TThostFtdcInvestorIDType),
           ('InstrumentID', TThostFtdcInstrumentIDType),
           ]
class CThostFtdcQryContractBankField(Structure):
    _fields_ = [
           ('BrokerID', TThostFtdcBrokerIDType),
           ('BankID', TThostFtdcBankIDType),
           ('BankBrchID', TThostFtdcBankBrchIDType),
           ]
class CThostFtdcContractBankField(Structure):
    _fields_ = [
           ('BrokerID', TThostFtdcBrokerIDType),
           ('BankID', TThostFtdcBankIDType),
           ('BankBrchID', TThostFtdcBankBrchIDType),
           ('BankName', TThostFtdcBankNameType),
           ]
class CThostFtdcInvestorPositionCombineDetailField(Structure):
    _fields_ = [
           ('TradingDay', TThostFtdcDateType),
           ('OpenDate', TThostFtdcDateType),
           ('ExchangeID', TThostFtdcExchangeIDType),
           ('SettlementID', TThostFtdcSettlementIDType),
           ('BrokerID', TThostFtdcBrokerIDType),
           ('InvestorID', TThostFtdcInvestorIDType),
           ('ComTradeID', TThostFtdcTradeIDType),
           ('TradeID', TThostFtdcTradeIDType),
           ('InstrumentID', TThostFtdcInstrumentIDType),
           ('HedgeFlag', TThostFtdcHedgeFlagType),
           ('Direction', TThostFtdcDirectionType),
           ('TotalAmt', TThostFtdcVolumeType),
           ('Margin', TThostFtdcMoneyType),
           ('ExchMargin', TThostFtdcMoneyType),
           ('MarginRateByMoney', TThostFtdcRatioType),
           ('MarginRateByVolume', TThostFtdcRatioType),
           ('LegID', TThostFtdcLegIDType),
           ('LegMultiple', TThostFtdcLegMultipleType),
           ('CombInstrumentID', TThostFtdcInstrumentIDType),
           ('TradeGroupID', TThostFtdcTradeGroupIDType),
           ]
class CThostFtdcParkedOrderField(Structure):
    _fields_ = [
           ('BrokerID', TThostFtdcBrokerIDType),
           ('InvestorID', TThostFtdcInvestorIDType),
           ('InstrumentID', TThostFtdcInstrumentIDType),
           ('OrderRef', TThostFtdcOrderRefType),
           ('UserID', TThostFtdcUserIDType),
           ('OrderPriceType', TThostFtdcOrderPriceTypeType),
           ('Direction', TThostFtdcDirectionType),
           ('CombOffsetFlag', TThostFtdcCombOffsetFlagType),
           ('CombHedgeFlag', TThostFtdcCombHedgeFlagType),
           ('LimitPrice', TThostFtdcPriceType),
           ('VolumeTotalOriginal', TThostFtdcVolumeType),
           ('TimeCondition', TThostFtdcTimeConditionType),
           ('GTDDate', TThostFtdcDateType),
           ('VolumeCondition', TThostFtdcVolumeConditionType),
           ('MinVolume', TThostFtdcVolumeType),
           ('ContingentCondition', TThostFtdcContingentConditionType),
           ('StopPrice', TThostFtdcPriceType),
           ('ForceCloseReason', TThostFtdcForceCloseReasonType),
           ('IsAutoSuspend', TThostFtdcBoolType),
           ('BusinessUnit', TThostFtdcBusinessUnitType),
           ('RequestID', TThostFtdcRequestIDType),
           ('UserForceClose', TThostFtdcBoolType),
           ('ExchangeID', TThostFtdcExchangeIDType),
           ('ParkedOrderID', TThostFtdcParkedOrderIDType),
           ('UserType', TThostFtdcUserTypeType),
           ('Status', TThostFtdcParkedOrderStatusType),
           ('ErrorID', TThostFtdcErrorIDType),
           ('ErrorMsg', TThostFtdcErrorMsgType),
           ('IsSwapOrder', TThostFtdcBoolType),
           ]
class CThostFtdcParkedOrderActionField(Structure):
    _fields_ = [
           ('BrokerID', TThostFtdcBrokerIDType),
           ('InvestorID', TThostFtdcInvestorIDType),
           ('OrderActionRef', TThostFtdcOrderActionRefType),
           ('OrderRef', TThostFtdcOrderRefType),
           ('RequestID', TThostFtdcRequestIDType),
           ('FrontID', TThostFtdcFrontIDType),
           ('SessionID', TThostFtdcSessionIDType),
           ('ExchangeID', TThostFtdcExchangeIDType),
           ('OrderSysID', TThostFtdcOrderSysIDType),
           ('ActionFlag', TThostFtdcActionFlagType),
           ('LimitPrice', TThostFtdcPriceType),
           ('VolumeChange', TThostFtdcVolumeType),
           ('UserID', TThostFtdcUserIDType),
           ('InstrumentID', TThostFtdcInstrumentIDType),
           ('ParkedOrderActionID', TThostFtdcParkedOrderActionIDType),
           ('UserType', TThostFtdcUserTypeType),
           ('Status', TThostFtdcParkedOrderStatusType),
           ('ErrorID', TThostFtdcErrorIDType),
           ('ErrorMsg', TThostFtdcErrorMsgType),
           ]
class CThostFtdcQryParkedOrderField(Structure):
    _fields_ = [
           ('BrokerID', TThostFtdcBrokerIDType),
           ('InvestorID', TThostFtdcInvestorIDType),
           ('InstrumentID', TThostFtdcInstrumentIDType),
           ('ExchangeID', TThostFtdcExchangeIDType),
           ]
class CThostFtdcQryParkedOrderActionField(Structure):
    _fields_ = [
           ('BrokerID', TThostFtdcBrokerIDType),
           ('InvestorID', TThostFtdcInvestorIDType),
           ('InstrumentID', TThostFtdcInstrumentIDType),
           ('ExchangeID', TThostFtdcExchangeIDType),
           ]
class CThostFtdcRemoveParkedOrderField(Structure):
    _fields_ = [
           ('BrokerID', TThostFtdcBrokerIDType),
           ('InvestorID', TThostFtdcInvestorIDType),
           ('ParkedOrderID', TThostFtdcParkedOrderIDType),
           ]
class CThostFtdcRemoveParkedOrderActionField(Structure):
    _fields_ = [
           ('BrokerID', TThostFtdcBrokerIDType),
           ('InvestorID', TThostFtdcInvestorIDType),
           ('ParkedOrderActionID', TThostFtdcParkedOrderActionIDType),
           ]
class CThostFtdcInvestorWithdrawAlgorithmField(Structure):
    _fields_ = [
           ('BrokerID', TThostFtdcBrokerIDType),
           ('InvestorRange', TThostFtdcInvestorRangeType),
           ('InvestorID', TThostFtdcInvestorIDType),
           ('UsingRatio', TThostFtdcRatioType),
           ('CurrencyID', TThostFtdcCurrencyIDType),
           ('FundMortgageRatio', TThostFtdcRatioType),
           ]
class CThostFtdcQryInvestorPositionCombineDetailField(Structure):
    _fields_ = [
           ('BrokerID', TThostFtdcBrokerIDType),
           ('InvestorID', TThostFtdcInvestorIDType),
           ('CombInstrumentID', TThostFtdcInstrumentIDType),
           ]
class CThostFtdcMarketDataAveragePriceField(Structure):
    _fields_ = [
           ('AveragePrice', TThostFtdcPriceType),
           ]
class CThostFtdcVerifyInvestorPasswordField(Structure):
    _fields_ = [
           ('BrokerID', TThostFtdcBrokerIDType),
           ('InvestorID', TThostFtdcInvestorIDType),
           ('Password', TThostFtdcPasswordType),
           ]
class CThostFtdcUserIPField(Structure):
    _fields_ = [
           ('BrokerID', TThostFtdcBrokerIDType),
           ('UserID', TThostFtdcUserIDType),
           ('IPAddress', TThostFtdcIPAddressType),
           ('IPMask', TThostFtdcIPAddressType),
           ('MacAddress', TThostFtdcMacAddressType),
           ]
class CThostFtdcTradingNoticeInfoField(Structure):
    _fields_ = [
           ('BrokerID', TThostFtdcBrokerIDType),
           ('InvestorID', TThostFtdcInvestorIDType),
           ('SendTime', TThostFtdcTimeType),
           ('FieldContent', TThostFtdcContentType),
           ('SequenceSeries', TThostFtdcSequenceSeriesType),
           ('SequenceNo', TThostFtdcSequenceNoType),
           ]
class CThostFtdcTradingNoticeField(Structure):
    _fields_ = [
           ('BrokerID', TThostFtdcBrokerIDType),
           ('InvestorRange', TThostFtdcInvestorRangeType),
           ('InvestorID', TThostFtdcInvestorIDType),
           ('SequenceSeries', TThostFtdcSequenceSeriesType),
           ('UserID', TThostFtdcUserIDType),
           ('SendTime', TThostFtdcTimeType),
           ('SequenceNo', TThostFtdcSequenceNoType),
           ('FieldContent', TThostFtdcContentType),
           ]
class CThostFtdcQryTradingNoticeField(Structure):
    _fields_ = [
           ('BrokerID', TThostFtdcBrokerIDType),
           ('InvestorID', TThostFtdcInvestorIDType),
           ]
class CThostFtdcQryErrOrderField(Structure):
    _fields_ = [
           ('BrokerID', TThostFtdcBrokerIDType),
           ('InvestorID', TThostFtdcInvestorIDType),
           ]
class CThostFtdcErrOrderField(Structure):
    _fields_ = [
           ('BrokerID', TThostFtdcBrokerIDType),
           ('InvestorID', TThostFtdcInvestorIDType),
           ('InstrumentID', TThostFtdcInstrumentIDType),
           ('OrderRef', TThostFtdcOrderRefType),
           ('UserID', TThostFtdcUserIDType),
           ('OrderPriceType', TThostFtdcOrderPriceTypeType),
           ('Direction', TThostFtdcDirectionType),
           ('CombOffsetFlag', TThostFtdcCombOffsetFlagType),
           ('CombHedgeFlag', TThostFtdcCombHedgeFlagType),
           ('LimitPrice', TThostFtdcPriceType),
           ('VolumeTotalOriginal', TThostFtdcVolumeType),
           ('TimeCondition', TThostFtdcTimeConditionType),
           ('GTDDate', TThostFtdcDateType),
           ('VolumeCondition', TThostFtdcVolumeConditionType),
           ('MinVolume', TThostFtdcVolumeType),
           ('ContingentCondition', TThostFtdcContingentConditionType),
           ('StopPrice', TThostFtdcPriceType),
           ('ForceCloseReason', TThostFtdcForceCloseReasonType),
           ('IsAutoSuspend', TThostFtdcBoolType),
           ('BusinessUnit', TThostFtdcBusinessUnitType),
           ('RequestID', TThostFtdcRequestIDType),
           ('UserForceClose', TThostFtdcBoolType),
           ('ErrorID', TThostFtdcErrorIDType),
           ('ErrorMsg', TThostFtdcErrorMsgType),
           ('IsSwapOrder', TThostFtdcBoolType),
           ]
class CThostFtdcErrorConditionalOrderField(Structure):
    _fields_ = [
           ('BrokerID', TThostFtdcBrokerIDType),
           ('InvestorID', TThostFtdcInvestorIDType),
           ('InstrumentID', TThostFtdcInstrumentIDType),
           ('OrderRef', TThostFtdcOrderRefType),
           ('UserID', TThostFtdcUserIDType),
           ('OrderPriceType', TThostFtdcOrderPriceTypeType),
           ('Direction', TThostFtdcDirectionType),
           ('CombOffsetFlag', TThostFtdcCombOffsetFlagType),
           ('CombHedgeFlag', TThostFtdcCombHedgeFlagType),
           ('LimitPrice', TThostFtdcPriceType),
           ('VolumeTotalOriginal', TThostFtdcVolumeType),
           ('TimeCondition', TThostFtdcTimeConditionType),
           ('GTDDate', TThostFtdcDateType),
           ('VolumeCondition', TThostFtdcVolumeConditionType),
           ('MinVolume', TThostFtdcVolumeType),
           ('ContingentCondition', TThostFtdcContingentConditionType),
           ('StopPrice', TThostFtdcPriceType),
           ('ForceCloseReason', TThostFtdcForceCloseReasonType),
           ('IsAutoSuspend', TThostFtdcBoolType),
           ('BusinessUnit', TThostFtdcBusinessUnitType),
           ('RequestID', TThostFtdcRequestIDType),
           ('OrderLocalID', TThostFtdcOrderLocalIDType),
           ('ExchangeID', TThostFtdcExchangeIDType),
           ('ParticipantID', TThostFtdcParticipantIDType),
           ('ClientID', TThostFtdcClientIDType),
           ('ExchangeInstID', TThostFtdcExchangeInstIDType),
           ('TraderID', TThostFtdcTraderIDType),
           ('InstallID', TThostFtdcInstallIDType),
           ('OrderSubmitStatus', TThostFtdcOrderSubmitStatusType),
           ('NotifySequence', TThostFtdcSequenceNoType),
           ('TradingDay', TThostFtdcDateType),
           ('SettlementID', TThostFtdcSettlementIDType),
           ('OrderSysID', TThostFtdcOrderSysIDType),
           ('OrderSource', TThostFtdcOrderSourceType),
           ('OrderStatus', TThostFtdcOrderStatusType),
           ('OrderType', TThostFtdcOrderTypeType),
           ('VolumeTraded', TThostFtdcVolumeType),
           ('VolumeTotal', TThostFtdcVolumeType),
           ('InsertDate', TThostFtdcDateType),
           ('InsertTime', TThostFtdcTimeType),
           ('ActiveTime', TThostFtdcTimeType),
           ('SuspendTime', TThostFtdcTimeType),
           ('UpdateTime', TThostFtdcTimeType),
           ('CancelTime', TThostFtdcTimeType),
           ('ActiveTraderID', TThostFtdcTraderIDType),
           ('ClearingPartID', TThostFtdcParticipantIDType),
           ('SequenceNo', TThostFtdcSequenceNoType),
           ('FrontID', TThostFtdcFrontIDType),
           ('SessionID', TThostFtdcSessionIDType),
           ('UserProductInfo', TThostFtdcProductInfoType),
           ('StatusMsg', TThostFtdcErrorMsgType),
           ('UserForceClose', TThostFtdcBoolType),
           ('ActiveUserID', TThostFtdcUserIDType),
           ('BrokerOrderSeq', TThostFtdcSequenceNoType),
           ('RelativeOrderSysID', TThostFtdcOrderSysIDType),
           ('ZCETotalTradedVolume', TThostFtdcVolumeType),
           ('ErrorID', TThostFtdcErrorIDType),
           ('ErrorMsg', TThostFtdcErrorMsgType),
           ('IsSwapOrder', TThostFtdcBoolType),
           ]
class CThostFtdcQryErrOrderActionField(Structure):
    _fields_ = [
           ('BrokerID', TThostFtdcBrokerIDType),
           ('InvestorID', TThostFtdcInvestorIDType),
           ]
class CThostFtdcErrOrderActionField(Structure):
    _fields_ = [
           ('BrokerID', TThostFtdcBrokerIDType),
           ('InvestorID', TThostFtdcInvestorIDType),
           ('OrderActionRef', TThostFtdcOrderActionRefType),
           ('OrderRef', TThostFtdcOrderRefType),
           ('RequestID', TThostFtdcRequestIDType),
           ('FrontID', TThostFtdcFrontIDType),
           ('SessionID', TThostFtdcSessionIDType),
           ('ExchangeID', TThostFtdcExchangeIDType),
           ('OrderSysID', TThostFtdcOrderSysIDType),
           ('ActionFlag', TThostFtdcActionFlagType),
           ('LimitPrice', TThostFtdcPriceType),
           ('VolumeChange', TThostFtdcVolumeType),
           ('ActionDate', TThostFtdcDateType),
           ('ActionTime', TThostFtdcTimeType),
           ('TraderID', TThostFtdcTraderIDType),
           ('InstallID', TThostFtdcInstallIDType),
           ('OrderLocalID', TThostFtdcOrderLocalIDType),
           ('ActionLocalID', TThostFtdcOrderLocalIDType),
           ('ParticipantID', TThostFtdcParticipantIDType),
           ('ClientID', TThostFtdcClientIDType),
           ('BusinessUnit', TThostFtdcBusinessUnitType),
           ('OrderActionStatus', TThostFtdcOrderActionStatusType),
           ('UserID', TThostFtdcUserIDType),
           ('StatusMsg', TThostFtdcErrorMsgType),
           ('InstrumentID', TThostFtdcInstrumentIDType),
           ('ErrorID', TThostFtdcErrorIDType),
           ('ErrorMsg', TThostFtdcErrorMsgType),
           ]
class CThostFtdcQryExchangeSequenceField(Structure):
    _fields_ = [
           ('ExchangeID', TThostFtdcExchangeIDType),
           ]
class CThostFtdcExchangeSequenceField(Structure):
    _fields_ = [
           ('ExchangeID', TThostFtdcExchangeIDType),
           ('SequenceNo', TThostFtdcSequenceNoType),
           ('MarketStatus', TThostFtdcInstrumentStatusType),
           ]
class CThostFtdcQueryMaxOrderVolumeWithPriceField(Structure):
    _fields_ = [
           ('BrokerID', TThostFtdcBrokerIDType),
           ('InvestorID', TThostFtdcInvestorIDType),
           ('InstrumentID', TThostFtdcInstrumentIDType),
           ('Direction', TThostFtdcDirectionType),
           ('OffsetFlag', TThostFtdcOffsetFlagType),
           ('HedgeFlag', TThostFtdcHedgeFlagType),
           ('MaxVolume', TThostFtdcVolumeType),
           ('Price', TThostFtdcPriceType),
           ]
class CThostFtdcQryBrokerTradingParamsField(Structure):
    _fields_ = [
           ('BrokerID', TThostFtdcBrokerIDType),
           ('InvestorID', TThostFtdcInvestorIDType),
           ('CurrencyID', TThostFtdcCurrencyIDType),
           ]
class CThostFtdcBrokerTradingParamsField(Structure):
    _fields_ = [
           ('BrokerID', TThostFtdcBrokerIDType),
           ('InvestorID', TThostFtdcInvestorIDType),
           ('MarginPriceType', TThostFtdcMarginPriceTypeType),
           ('Algorithm', TThostFtdcAlgorithmType),
           ('AvailIncludeCloseProfit', TThostFtdcIncludeCloseProfitType),
           ('CurrencyID', TThostFtdcCurrencyIDType),
           ('OptionRoyaltyPriceType', TThostFtdcOptionRoyaltyPriceTypeType),
           ]
class CThostFtdcQryBrokerTradingAlgosField(Structure):
    _fields_ = [
           ('BrokerID', TThostFtdcBrokerIDType),
           ('ExchangeID', TThostFtdcExchangeIDType),
           ('InstrumentID', TThostFtdcInstrumentIDType),
           ]
class CThostFtdcBrokerTradingAlgosField(Structure):
    _fields_ = [
           ('BrokerID', TThostFtdcBrokerIDType),
           ('ExchangeID', TThostFtdcExchangeIDType),
           ('InstrumentID', TThostFtdcInstrumentIDType),
           ('HandlePositionAlgoID', TThostFtdcHandlePositionAlgoIDType),
           ('FindMarginRateAlgoID', TThostFtdcFindMarginRateAlgoIDType),
           ('HandleTradingAccountAlgoID', TThostFtdcHandleTradingAccountAlgoIDType),
           ]
class CThostFtdcQueryBrokerDepositField(Structure):
    _fields_ = [
           ('BrokerID', TThostFtdcBrokerIDType),
           ('ExchangeID', TThostFtdcExchangeIDType),
           ]
class CThostFtdcBrokerDepositField(Structure):
    _fields_ = [
           ('TradingDay', TThostFtdcTradeDateType),
           ('BrokerID', TThostFtdcBrokerIDType),
           ('ParticipantID', TThostFtdcParticipantIDType),
           ('ExchangeID', TThostFtdcExchangeIDType),
           ('PreBalance', TThostFtdcMoneyType),
           ('CurrMargin', TThostFtdcMoneyType),
           ('CloseProfit', TThostFtdcMoneyType),
           ('Balance', TThostFtdcMoneyType),
           ('Deposit', TThostFtdcMoneyType),
           ('Withdraw', TThostFtdcMoneyType),
           ('Available', TThostFtdcMoneyType),
           ('Reserve', TThostFtdcMoneyType),
           ('FrozenMargin', TThostFtdcMoneyType),
           ]
class CThostFtdcQryCFMMCBrokerKeyField(Structure):
    _fields_ = [
           ('BrokerID', TThostFtdcBrokerIDType),
           ]
class CThostFtdcCFMMCBrokerKeyField(Structure):
    _fields_ = [
           ('BrokerID', TThostFtdcBrokerIDType),
           ('ParticipantID', TThostFtdcParticipantIDType),
           ('CreateDate', TThostFtdcDateType),
           ('CreateTime', TThostFtdcTimeType),
           ('KeyID', TThostFtdcSequenceNoType),
           ('CurrentKey', TThostFtdcCFMMCKeyType),
           ('KeyKind', TThostFtdcCFMMCKeyKindType),
           ]
class CThostFtdcCFMMCTradingAccountKeyField(Structure):
    _fields_ = [
           ('BrokerID', TThostFtdcBrokerIDType),
           ('ParticipantID', TThostFtdcParticipantIDType),
           ('AccountID', TThostFtdcAccountIDType),
           ('KeyID', TThostFtdcSequenceNoType),
           ('CurrentKey', TThostFtdcCFMMCKeyType),
           ]
class CThostFtdcQryCFMMCTradingAccountKeyField(Structure):
    _fields_ = [
           ('BrokerID', TThostFtdcBrokerIDType),
           ('InvestorID', TThostFtdcInvestorIDType),
           ]
class CThostFtdcBrokerUserOTPParamField(Structure):
    _fields_ = [
           ('BrokerID', TThostFtdcBrokerIDType),
           ('UserID', TThostFtdcUserIDType),
           ('OTPVendorsID', TThostFtdcOTPVendorsIDType),
           ('SerialNumber', TThostFtdcSerialNumberType),
           ('AuthKey', TThostFtdcAuthKeyType),
           ('LastDrift', TThostFtdcLastDriftType),
           ('LastSuccess', TThostFtdcLastSuccessType),
           ('OTPType', TThostFtdcOTPTypeType),
           ]
class CThostFtdcManualSyncBrokerUserOTPField(Structure):
    _fields_ = [
           ('BrokerID', TThostFtdcBrokerIDType),
           ('UserID', TThostFtdcUserIDType),
           ('OTPType', TThostFtdcOTPTypeType),
           ('FirstOTP', TThostFtdcPasswordType),
           ('SecondOTP', TThostFtdcPasswordType),
           ]
class CThostFtdcCommRateModelField(Structure):
    _fields_ = [
           ('BrokerID', TThostFtdcBrokerIDType),
           ('CommModelID', TThostFtdcInvestorIDType),
           ('CommModelName', TThostFtdcCommModelNameType),
           ]
class CThostFtdcQryCommRateModelField(Structure):
    _fields_ = [
           ('BrokerID', TThostFtdcBrokerIDType),
           ('CommModelID', TThostFtdcInvestorIDType),
           ]
class CThostFtdcMarginModelField(Structure):
    _fields_ = [
           ('BrokerID', TThostFtdcBrokerIDType),
           ('MarginModelID', TThostFtdcInvestorIDType),
           ('MarginModelName', TThostFtdcCommModelNameType),
           ]
class CThostFtdcQryMarginModelField(Structure):
    _fields_ = [
           ('BrokerID', TThostFtdcBrokerIDType),
           ('MarginModelID', TThostFtdcInvestorIDType),
           ]
class CThostFtdcEWarrantOffsetField(Structure):
    _fields_ = [
           ('TradingDay', TThostFtdcTradeDateType),
           ('BrokerID', TThostFtdcBrokerIDType),
           ('InvestorID', TThostFtdcInvestorIDType),
           ('ExchangeID', TThostFtdcExchangeIDType),
           ('InstrumentID', TThostFtdcInstrumentIDType),
           ('Direction', TThostFtdcDirectionType),
           ('HedgeFlag', TThostFtdcHedgeFlagType),
           ('Volume', TThostFtdcVolumeType),
           ]
class CThostFtdcQryEWarrantOffsetField(Structure):
    _fields_ = [
           ('BrokerID', TThostFtdcBrokerIDType),
           ('InvestorID', TThostFtdcInvestorIDType),
           ('ExchangeID', TThostFtdcExchangeIDType),
           ('InstrumentID', TThostFtdcInstrumentIDType),
           ]
class CThostFtdcQryInvestorProductGroupMarginField(Structure):
    _fields_ = [
           ('BrokerID', TThostFtdcBrokerIDType),
           ('InvestorID', TThostFtdcInvestorIDType),
           ('ProductGroupID', TThostFtdcInstrumentIDType),
           ('HedgeFlag', TThostFtdcHedgeFlagType),
           ]
class CThostFtdcInvestorProductGroupMarginField(Structure):
    _fields_ = [
           ('ProductGroupID', TThostFtdcInstrumentIDType),
           ('BrokerID', TThostFtdcBrokerIDType),
           ('InvestorID', TThostFtdcInvestorIDType),
           ('TradingDay', TThostFtdcDateType),
           ('SettlementID', TThostFtdcSettlementIDType),
           ('FrozenMargin', TThostFtdcMoneyType),
           ('LongFrozenMargin', TThostFtdcMoneyType),
           ('ShortFrozenMargin', TThostFtdcMoneyType),
           ('UseMargin', TThostFtdcMoneyType),
           ('LongUseMargin', TThostFtdcMoneyType),
           ('ShortUseMargin', TThostFtdcMoneyType),
           ('ExchMargin', TThostFtdcMoneyType),
           ('LongExchMargin', TThostFtdcMoneyType),
           ('ShortExchMargin', TThostFtdcMoneyType),
           ('CloseProfit', TThostFtdcMoneyType),
           ('FrozenCommission', TThostFtdcMoneyType),
           ('Commission', TThostFtdcMoneyType),
           ('FrozenCash', TThostFtdcMoneyType),
           ('CashIn', TThostFtdcMoneyType),
           ('PositionProfit', TThostFtdcMoneyType),
           ('OffsetAmount', TThostFtdcMoneyType),
           ('LongOffsetAmount', TThostFtdcMoneyType),
           ('ShortOffsetAmount', TThostFtdcMoneyType),
           ('ExchOffsetAmount', TThostFtdcMoneyType),
           ('LongExchOffsetAmount', TThostFtdcMoneyType),
           ('ShortExchOffsetAmount', TThostFtdcMoneyType),
           ('HedgeFlag', TThostFtdcHedgeFlagType),
           ]
class CThostFtdcQueryCFMMCTradingAccountTokenField(Structure):
    _fields_ = [
           ('BrokerID', TThostFtdcBrokerIDType),
           ('InvestorID', TThostFtdcInvestorIDType),
           ]
class CThostFtdcCFMMCTradingAccountTokenField(Structure):
    _fields_ = [
           ('BrokerID', TThostFtdcBrokerIDType),
           ('ParticipantID', TThostFtdcParticipantIDType),
           ('AccountID', TThostFtdcAccountIDType),
           ('KeyID', TThostFtdcSequenceNoType),
           ('Token', TThostFtdcCFMMCTokenType),
           ]
class CThostFtdcReqOpenAccountField(Structure):
    _fields_ = [
           ('TradeCode', TThostFtdcTradeCodeType),
           ('BankID', TThostFtdcBankIDType),
           ('BankBranchID', TThostFtdcBankBrchIDType),
           ('BrokerID', TThostFtdcBrokerIDType),
           ('BrokerBranchID', TThostFtdcFutureBranchIDType),
           ('TradeDate', TThostFtdcTradeDateType),
           ('TradeTime', TThostFtdcTradeTimeType),
           ('BankSerial', TThostFtdcBankSerialType),
           ('TradingDay', TThostFtdcTradeDateType),
           ('PlateSerial', TThostFtdcSerialType),
           ('LastFragment', TThostFtdcLastFragmentType),
           ('SessionID', TThostFtdcSessionIDType),
           ('CustomerName', TThostFtdcIndividualNameType),
           ('IdCardType', TThostFtdcIdCardTypeType),
           ('IdentifiedCardNo', TThostFtdcIdentifiedCardNoType),
           ('Gender', TThostFtdcGenderType),
           ('CountryCode', TThostFtdcCountryCodeType),
           ('CustType', TThostFtdcCustTypeType),
           ('Address', TThostFtdcAddressType),
           ('ZipCode', TThostFtdcZipCodeType),
           ('Telephone', TThostFtdcTelephoneType),
           ('MobilePhone', TThostFtdcMobilePhoneType),
           ('Fax', TThostFtdcFaxType),
           ('EMail', TThostFtdcEMailType),
           ('MoneyAccountStatus', TThostFtdcMoneyAccountStatusType),
           ('BankAccount', TThostFtdcBankAccountType),
           ('BankPassWord', TThostFtdcPasswordType),
           ('AccountID', TThostFtdcAccountIDType),
           ('Password', TThostFtdcPasswordType),
           ('InstallID', TThostFtdcInstallIDType),
           ('VerifyCertNoFlag', TThostFtdcYesNoIndicatorType),
           ('CurrencyID', TThostFtdcCurrencyIDType),
           ('CashExchangeCode', TThostFtdcCashExchangeCodeType),
           ('Digest', TThostFtdcDigestType),
           ('BankAccType', TThostFtdcBankAccTypeType),
           ('DeviceID', TThostFtdcDeviceIDType),
           ('BankSecuAccType', TThostFtdcBankAccTypeType),
           ('BrokerIDByBank', TThostFtdcBankCodingForFutureType),
           ('BankSecuAcc', TThostFtdcBankAccountType),
           ('BankPwdFlag', TThostFtdcPwdFlagType),
           ('SecuPwdFlag', TThostFtdcPwdFlagType),
           ('OperNo', TThostFtdcOperNoType),
           ('TID', TThostFtdcTIDType),
           ('UserID', TThostFtdcUserIDType),
           ]
class CThostFtdcReqCancelAccountField(Structure):
    _fields_ = [
           ('TradeCode', TThostFtdcTradeCodeType),
           ('BankID', TThostFtdcBankIDType),
           ('BankBranchID', TThostFtdcBankBrchIDType),
           ('BrokerID', TThostFtdcBrokerIDType),
           ('BrokerBranchID', TThostFtdcFutureBranchIDType),
           ('TradeDate', TThostFtdcTradeDateType),
           ('TradeTime', TThostFtdcTradeTimeType),
           ('BankSerial', TThostFtdcBankSerialType),
           ('TradingDay', TThostFtdcTradeDateType),
           ('PlateSerial', TThostFtdcSerialType),
           ('LastFragment', TThostFtdcLastFragmentType),
           ('SessionID', TThostFtdcSessionIDType),
           ('CustomerName', TThostFtdcIndividualNameType),
           ('IdCardType', TThostFtdcIdCardTypeType),
           ('IdentifiedCardNo', TThostFtdcIdentifiedCardNoType),
           ('Gender', TThostFtdcGenderType),
           ('CountryCode', TThostFtdcCountryCodeType),
           ('CustType', TThostFtdcCustTypeType),
           ('Address', TThostFtdcAddressType),
           ('ZipCode', TThostFtdcZipCodeType),
           ('Telephone', TThostFtdcTelephoneType),
           ('MobilePhone', TThostFtdcMobilePhoneType),
           ('Fax', TThostFtdcFaxType),
           ('EMail', TThostFtdcEMailType),
           ('MoneyAccountStatus', TThostFtdcMoneyAccountStatusType),
           ('BankAccount', TThostFtdcBankAccountType),
           ('BankPassWord', TThostFtdcPasswordType),
           ('AccountID', TThostFtdcAccountIDType),
           ('Password', TThostFtdcPasswordType),
           ('InstallID', TThostFtdcInstallIDType),
           ('VerifyCertNoFlag', TThostFtdcYesNoIndicatorType),
           ('CurrencyID', TThostFtdcCurrencyIDType),
           ('CashExchangeCode', TThostFtdcCashExchangeCodeType),
           ('Digest', TThostFtdcDigestType),
           ('BankAccType', TThostFtdcBankAccTypeType),
           ('DeviceID', TThostFtdcDeviceIDType),
           ('BankSecuAccType', TThostFtdcBankAccTypeType),
           ('BrokerIDByBank', TThostFtdcBankCodingForFutureType),
           ('BankSecuAcc', TThostFtdcBankAccountType),
           ('BankPwdFlag', TThostFtdcPwdFlagType),
           ('SecuPwdFlag', TThostFtdcPwdFlagType),
           ('OperNo', TThostFtdcOperNoType),
           ('TID', TThostFtdcTIDType),
           ('UserID', TThostFtdcUserIDType),
           ]
class CThostFtdcReqChangeAccountField(Structure):
    _fields_ = [
           ('TradeCode', TThostFtdcTradeCodeType),
           ('BankID', TThostFtdcBankIDType),
           ('BankBranchID', TThostFtdcBankBrchIDType),
           ('BrokerID', TThostFtdcBrokerIDType),
           ('BrokerBranchID', TThostFtdcFutureBranchIDType),
           ('TradeDate', TThostFtdcTradeDateType),
           ('TradeTime', TThostFtdcTradeTimeType),
           ('BankSerial', TThostFtdcBankSerialType),
           ('TradingDay', TThostFtdcTradeDateType),
           ('PlateSerial', TThostFtdcSerialType),
           ('LastFragment', TThostFtdcLastFragmentType),
           ('SessionID', TThostFtdcSessionIDType),
           ('CustomerName', TThostFtdcIndividualNameType),
           ('IdCardType', TThostFtdcIdCardTypeType),
           ('IdentifiedCardNo', TThostFtdcIdentifiedCardNoType),
           ('Gender', TThostFtdcGenderType),
           ('CountryCode', TThostFtdcCountryCodeType),
           ('CustType', TThostFtdcCustTypeType),
           ('Address', TThostFtdcAddressType),
           ('ZipCode', TThostFtdcZipCodeType),
           ('Telephone', TThostFtdcTelephoneType),
           ('MobilePhone', TThostFtdcMobilePhoneType),
           ('Fax', TThostFtdcFaxType),
           ('EMail', TThostFtdcEMailType),
           ('MoneyAccountStatus', TThostFtdcMoneyAccountStatusType),
           ('BankAccount', TThostFtdcBankAccountType),
           ('BankPassWord', TThostFtdcPasswordType),
           ('NewBankAccount', TThostFtdcBankAccountType),
           ('NewBankPassWord', TThostFtdcPasswordType),
           ('AccountID', TThostFtdcAccountIDType),
           ('Password', TThostFtdcPasswordType),
           ('BankAccType', TThostFtdcBankAccTypeType),
           ('InstallID', TThostFtdcInstallIDType),
           ('VerifyCertNoFlag', TThostFtdcYesNoIndicatorType),
           ('CurrencyID', TThostFtdcCurrencyIDType),
           ('BrokerIDByBank', TThostFtdcBankCodingForFutureType),
           ('BankPwdFlag', TThostFtdcPwdFlagType),
           ('SecuPwdFlag', TThostFtdcPwdFlagType),
           ('TID', TThostFtdcTIDType),
           ('Digest', TThostFtdcDigestType),
           ]
class CThostFtdcReqTransferField(Structure):
    _fields_ = [
           ('TradeCode', TThostFtdcTradeCodeType),
           ('BankID', TThostFtdcBankIDType),
           ('BankBranchID', TThostFtdcBankBrchIDType),
           ('BrokerID', TThostFtdcBrokerIDType),
           ('BrokerBranchID', TThostFtdcFutureBranchIDType),
           ('TradeDate', TThostFtdcTradeDateType),
           ('TradeTime', TThostFtdcTradeTimeType),
           ('BankSerial', TThostFtdcBankSerialType),
           ('TradingDay', TThostFtdcTradeDateType),
           ('PlateSerial', TThostFtdcSerialType),
           ('LastFragment', TThostFtdcLastFragmentType),
           ('SessionID', TThostFtdcSessionIDType),
           ('CustomerName', TThostFtdcIndividualNameType),
           ('IdCardType', TThostFtdcIdCardTypeType),
           ('IdentifiedCardNo', TThostFtdcIdentifiedCardNoType),
           ('CustType', TThostFtdcCustTypeType),
           ('BankAccount', TThostFtdcBankAccountType),
           ('BankPassWord', TThostFtdcPasswordType),
           ('AccountID', TThostFtdcAccountIDType),
           ('Password', TThostFtdcPasswordType),
           ('InstallID', TThostFtdcInstallIDType),
           ('FutureSerial', TThostFtdcFutureSerialType),
           ('UserID', TThostFtdcUserIDType),
           ('VerifyCertNoFlag', TThostFtdcYesNoIndicatorType),
           ('CurrencyID', TThostFtdcCurrencyIDType),
           ('TradeAmount', TThostFtdcTradeAmountType),
           ('FutureFetchAmount', TThostFtdcTradeAmountType),
           ('FeePayFlag', TThostFtdcFeePayFlagType),
           ('CustFee', TThostFtdcCustFeeType),
           ('BrokerFee', TThostFtdcFutureFeeType),
           ('Message', TThostFtdcAddInfoType),
           ('Digest', TThostFtdcDigestType),
           ('BankAccType', TThostFtdcBankAccTypeType),
           ('DeviceID', TThostFtdcDeviceIDType),
           ('BankSecuAccType', TThostFtdcBankAccTypeType),
           ('BrokerIDByBank', TThostFtdcBankCodingForFutureType),
           ('BankSecuAcc', TThostFtdcBankAccountType),
           ('BankPwdFlag', TThostFtdcPwdFlagType),
           ('SecuPwdFlag', TThostFtdcPwdFlagType),
           ('OperNo', TThostFtdcOperNoType),
           ('RequestID', TThostFtdcRequestIDType),
           ('TID', TThostFtdcTIDType),
           ('TransferStatus', TThostFtdcTransferStatusType),
           ]
class CThostFtdcRspTransferField(Structure):
    _fields_ = [
           ('TradeCode', TThostFtdcTradeCodeType),
           ('BankID', TThostFtdcBankIDType),
           ('BankBranchID', TThostFtdcBankBrchIDType),
           ('BrokerID', TThostFtdcBrokerIDType),
           ('BrokerBranchID', TThostFtdcFutureBranchIDType),
           ('TradeDate', TThostFtdcTradeDateType),
           ('TradeTime', TThostFtdcTradeTimeType),
           ('BankSerial', TThostFtdcBankSerialType),
           ('TradingDay', TThostFtdcTradeDateType),
           ('PlateSerial', TThostFtdcSerialType),
           ('LastFragment', TThostFtdcLastFragmentType),
           ('SessionID', TThostFtdcSessionIDType),
           ('CustomerName', TThostFtdcIndividualNameType),
           ('IdCardType', TThostFtdcIdCardTypeType),
           ('IdentifiedCardNo', TThostFtdcIdentifiedCardNoType),
           ('CustType', TThostFtdcCustTypeType),
           ('BankAccount', TThostFtdcBankAccountType),
           ('BankPassWord', TThostFtdcPasswordType),
           ('AccountID', TThostFtdcAccountIDType),
           ('Password', TThostFtdcPasswordType),
           ('InstallID', TThostFtdcInstallIDType),
           ('FutureSerial', TThostFtdcFutureSerialType),
           ('UserID', TThostFtdcUserIDType),
           ('VerifyCertNoFlag', TThostFtdcYesNoIndicatorType),
           ('CurrencyID', TThostFtdcCurrencyIDType),
           ('TradeAmount', TThostFtdcTradeAmountType),
           ('FutureFetchAmount', TThostFtdcTradeAmountType),
           ('FeePayFlag', TThostFtdcFeePayFlagType),
           ('CustFee', TThostFtdcCustFeeType),
           ('BrokerFee', TThostFtdcFutureFeeType),
           ('Message', TThostFtdcAddInfoType),
           ('Digest', TThostFtdcDigestType),
           ('BankAccType', TThostFtdcBankAccTypeType),
           ('DeviceID', TThostFtdcDeviceIDType),
           ('BankSecuAccType', TThostFtdcBankAccTypeType),
           ('BrokerIDByBank', TThostFtdcBankCodingForFutureType),
           ('BankSecuAcc', TThostFtdcBankAccountType),
           ('BankPwdFlag', TThostFtdcPwdFlagType),
           ('SecuPwdFlag', TThostFtdcPwdFlagType),
           ('OperNo', TThostFtdcOperNoType),
           ('RequestID', TThostFtdcRequestIDType),
           ('TID', TThostFtdcTIDType),
           ('TransferStatus', TThostFtdcTransferStatusType),
           ('ErrorID', TThostFtdcErrorIDType),
           ('ErrorMsg', TThostFtdcErrorMsgType),
           ]
class CThostFtdcReqRepealField(Structure):
    _fields_ = [
           ('RepealTimeInterval', TThostFtdcRepealTimeIntervalType),
           ('RepealedTimes', TThostFtdcRepealedTimesType),
           ('BankRepealFlag', TThostFtdcBankRepealFlagType),
           ('BrokerRepealFlag', TThostFtdcBrokerRepealFlagType),
           ('PlateRepealSerial', TThostFtdcPlateSerialType),
           ('BankRepealSerial', TThostFtdcBankSerialType),
           ('FutureRepealSerial', TThostFtdcFutureSerialType),
           ('TradeCode', TThostFtdcTradeCodeType),
           ('BankID', TThostFtdcBankIDType),
           ('BankBranchID', TThostFtdcBankBrchIDType),
           ('BrokerID', TThostFtdcBrokerIDType),
           ('BrokerBranchID', TThostFtdcFutureBranchIDType),
           ('TradeDate', TThostFtdcTradeDateType),
           ('TradeTime', TThostFtdcTradeTimeType),
           ('BankSerial', TThostFtdcBankSerialType),
           ('TradingDay', TThostFtdcTradeDateType),
           ('PlateSerial', TThostFtdcSerialType),
           ('LastFragment', TThostFtdcLastFragmentType),
           ('SessionID', TThostFtdcSessionIDType),
           ('CustomerName', TThostFtdcIndividualNameType),
           ('IdCardType', TThostFtdcIdCardTypeType),
           ('IdentifiedCardNo', TThostFtdcIdentifiedCardNoType),
           ('CustType', TThostFtdcCustTypeType),
           ('BankAccount', TThostFtdcBankAccountType),
           ('BankPassWord', TThostFtdcPasswordType),
           ('AccountID', TThostFtdcAccountIDType),
           ('Password', TThostFtdcPasswordType),
           ('InstallID', TThostFtdcInstallIDType),
           ('FutureSerial', TThostFtdcFutureSerialType),
           ('UserID', TThostFtdcUserIDType),
           ('VerifyCertNoFlag', TThostFtdcYesNoIndicatorType),
           ('CurrencyID', TThostFtdcCurrencyIDType),
           ('TradeAmount', TThostFtdcTradeAmountType),
           ('FutureFetchAmount', TThostFtdcTradeAmountType),
           ('FeePayFlag', TThostFtdcFeePayFlagType),
           ('CustFee', TThostFtdcCustFeeType),
           ('BrokerFee', TThostFtdcFutureFeeType),
           ('Message', TThostFtdcAddInfoType),
           ('Digest', TThostFtdcDigestType),
           ('BankAccType', TThostFtdcBankAccTypeType),
           ('DeviceID', TThostFtdcDeviceIDType),
           ('BankSecuAccType', TThostFtdcBankAccTypeType),
           ('BrokerIDByBank', TThostFtdcBankCodingForFutureType),
           ('BankSecuAcc', TThostFtdcBankAccountType),
           ('BankPwdFlag', TThostFtdcPwdFlagType),
           ('SecuPwdFlag', TThostFtdcPwdFlagType),
           ('OperNo', TThostFtdcOperNoType),
           ('RequestID', TThostFtdcRequestIDType),
           ('TID', TThostFtdcTIDType),
           ('TransferStatus', TThostFtdcTransferStatusType),
           ]
class CThostFtdcRspRepealField(Structure):
    _fields_ = [
           ('RepealTimeInterval', TThostFtdcRepealTimeIntervalType),
           ('RepealedTimes', TThostFtdcRepealedTimesType),
           ('BankRepealFlag', TThostFtdcBankRepealFlagType),
           ('BrokerRepealFlag', TThostFtdcBrokerRepealFlagType),
           ('PlateRepealSerial', TThostFtdcPlateSerialType),
           ('BankRepealSerial', TThostFtdcBankSerialType),
           ('FutureRepealSerial', TThostFtdcFutureSerialType),
           ('TradeCode', TThostFtdcTradeCodeType),
           ('BankID', TThostFtdcBankIDType),
           ('BankBranchID', TThostFtdcBankBrchIDType),
           ('BrokerID', TThostFtdcBrokerIDType),
           ('BrokerBranchID', TThostFtdcFutureBranchIDType),
           ('TradeDate', TThostFtdcTradeDateType),
           ('TradeTime', TThostFtdcTradeTimeType),
           ('BankSerial', TThostFtdcBankSerialType),
           ('TradingDay', TThostFtdcTradeDateType),
           ('PlateSerial', TThostFtdcSerialType),
           ('LastFragment', TThostFtdcLastFragmentType),
           ('SessionID', TThostFtdcSessionIDType),
           ('CustomerName', TThostFtdcIndividualNameType),
           ('IdCardType', TThostFtdcIdCardTypeType),
           ('IdentifiedCardNo', TThostFtdcIdentifiedCardNoType),
           ('CustType', TThostFtdcCustTypeType),
           ('BankAccount', TThostFtdcBankAccountType),
           ('BankPassWord', TThostFtdcPasswordType),
           ('AccountID', TThostFtdcAccountIDType),
           ('Password', TThostFtdcPasswordType),
           ('InstallID', TThostFtdcInstallIDType),
           ('FutureSerial', TThostFtdcFutureSerialType),
           ('UserID', TThostFtdcUserIDType),
           ('VerifyCertNoFlag', TThostFtdcYesNoIndicatorType),
           ('CurrencyID', TThostFtdcCurrencyIDType),
           ('TradeAmount', TThostFtdcTradeAmountType),
           ('FutureFetchAmount', TThostFtdcTradeAmountType),
           ('FeePayFlag', TThostFtdcFeePayFlagType),
           ('CustFee', TThostFtdcCustFeeType),
           ('BrokerFee', TThostFtdcFutureFeeType),
           ('Message', TThostFtdcAddInfoType),
           ('Digest', TThostFtdcDigestType),
           ('BankAccType', TThostFtdcBankAccTypeType),
           ('DeviceID', TThostFtdcDeviceIDType),
           ('BankSecuAccType', TThostFtdcBankAccTypeType),
           ('BrokerIDByBank', TThostFtdcBankCodingForFutureType),
           ('BankSecuAcc', TThostFtdcBankAccountType),
           ('BankPwdFlag', TThostFtdcPwdFlagType),
           ('SecuPwdFlag', TThostFtdcPwdFlagType),
           ('OperNo', TThostFtdcOperNoType),
           ('RequestID', TThostFtdcRequestIDType),
           ('TID', TThostFtdcTIDType),
           ('TransferStatus', TThostFtdcTransferStatusType),
           ('ErrorID', TThostFtdcErrorIDType),
           ('ErrorMsg', TThostFtdcErrorMsgType),
           ]
class CThostFtdcReqQueryAccountField(Structure):
    _fields_ = [
           ('TradeCode', TThostFtdcTradeCodeType),
           ('BankID', TThostFtdcBankIDType),
           ('BankBranchID', TThostFtdcBankBrchIDType),
           ('BrokerID', TThostFtdcBrokerIDType),
           ('BrokerBranchID', TThostFtdcFutureBranchIDType),
           ('TradeDate', TThostFtdcTradeDateType),
           ('TradeTime', TThostFtdcTradeTimeType),
           ('BankSerial', TThostFtdcBankSerialType),
           ('TradingDay', TThostFtdcTradeDateType),
           ('PlateSerial', TThostFtdcSerialType),
           ('LastFragment', TThostFtdcLastFragmentType),
           ('SessionID', TThostFtdcSessionIDType),
           ('CustomerName', TThostFtdcIndividualNameType),
           ('IdCardType', TThostFtdcIdCardTypeType),
           ('IdentifiedCardNo', TThostFtdcIdentifiedCardNoType),
           ('CustType', TThostFtdcCustTypeType),
           ('BankAccount', TThostFtdcBankAccountType),
           ('BankPassWord', TThostFtdcPasswordType),
           ('AccountID', TThostFtdcAccountIDType),
           ('Password', TThostFtdcPasswordType),
           ('FutureSerial', TThostFtdcFutureSerialType),
           ('InstallID', TThostFtdcInstallIDType),
           ('UserID', TThostFtdcUserIDType),
           ('VerifyCertNoFlag', TThostFtdcYesNoIndicatorType),
           ('CurrencyID', TThostFtdcCurrencyIDType),
           ('Digest', TThostFtdcDigestType),
           ('BankAccType', TThostFtdcBankAccTypeType),
           ('DeviceID', TThostFtdcDeviceIDType),
           ('BankSecuAccType', TThostFtdcBankAccTypeType),
           ('BrokerIDByBank', TThostFtdcBankCodingForFutureType),
           ('BankSecuAcc', TThostFtdcBankAccountType),
           ('BankPwdFlag', TThostFtdcPwdFlagType),
           ('SecuPwdFlag', TThostFtdcPwdFlagType),
           ('OperNo', TThostFtdcOperNoType),
           ('RequestID', TThostFtdcRequestIDType),
           ('TID', TThostFtdcTIDType),
           ]
class CThostFtdcRspQueryAccountField(Structure):
    _fields_ = [
           ('TradeCode', TThostFtdcTradeCodeType),
           ('BankID', TThostFtdcBankIDType),
           ('BankBranchID', TThostFtdcBankBrchIDType),
           ('BrokerID', TThostFtdcBrokerIDType),
           ('BrokerBranchID', TThostFtdcFutureBranchIDType),
           ('TradeDate', TThostFtdcTradeDateType),
           ('TradeTime', TThostFtdcTradeTimeType),
           ('BankSerial', TThostFtdcBankSerialType),
           ('TradingDay', TThostFtdcTradeDateType),
           ('PlateSerial', TThostFtdcSerialType),
           ('LastFragment', TThostFtdcLastFragmentType),
           ('SessionID', TThostFtdcSessionIDType),
           ('CustomerName', TThostFtdcIndividualNameType),
           ('IdCardType', TThostFtdcIdCardTypeType),
           ('IdentifiedCardNo', TThostFtdcIdentifiedCardNoType),
           ('CustType', TThostFtdcCustTypeType),
           ('BankAccount', TThostFtdcBankAccountType),
           ('BankPassWord', TThostFtdcPasswordType),
           ('AccountID', TThostFtdcAccountIDType),
           ('Password', TThostFtdcPasswordType),
           ('FutureSerial', TThostFtdcFutureSerialType),
           ('InstallID', TThostFtdcInstallIDType),
           ('UserID', TThostFtdcUserIDType),
           ('VerifyCertNoFlag', TThostFtdcYesNoIndicatorType),
           ('CurrencyID', TThostFtdcCurrencyIDType),
           ('Digest', TThostFtdcDigestType),
           ('BankAccType', TThostFtdcBankAccTypeType),
           ('DeviceID', TThostFtdcDeviceIDType),
           ('BankSecuAccType', TThostFtdcBankAccTypeType),
           ('BrokerIDByBank', TThostFtdcBankCodingForFutureType),
           ('BankSecuAcc', TThostFtdcBankAccountType),
           ('BankPwdFlag', TThostFtdcPwdFlagType),
           ('SecuPwdFlag', TThostFtdcPwdFlagType),
           ('OperNo', TThostFtdcOperNoType),
           ('RequestID', TThostFtdcRequestIDType),
           ('TID', TThostFtdcTIDType),
           ('BankUseAmount', TThostFtdcTradeAmountType),
           ('BankFetchAmount', TThostFtdcTradeAmountType),
           ]
class CThostFtdcFutureSignIOField(Structure):
    _fields_ = [
           ('TradeCode', TThostFtdcTradeCodeType),
           ('BankID', TThostFtdcBankIDType),
           ('BankBranchID', TThostFtdcBankBrchIDType),
           ('BrokerID', TThostFtdcBrokerIDType),
           ('BrokerBranchID', TThostFtdcFutureBranchIDType),
           ('TradeDate', TThostFtdcTradeDateType),
           ('TradeTime', TThostFtdcTradeTimeType),
           ('BankSerial', TThostFtdcBankSerialType),
           ('TradingDay', TThostFtdcTradeDateType),
           ('PlateSerial', TThostFtdcSerialType),
           ('LastFragment', TThostFtdcLastFragmentType),
           ('SessionID', TThostFtdcSessionIDType),
           ('InstallID', TThostFtdcInstallIDType),
           ('UserID', TThostFtdcUserIDType),
           ('Digest', TThostFtdcDigestType),
           ('CurrencyID', TThostFtdcCurrencyIDType),
           ('DeviceID', TThostFtdcDeviceIDType),
           ('BrokerIDByBank', TThostFtdcBankCodingForFutureType),
           ('OperNo', TThostFtdcOperNoType),
           ('RequestID', TThostFtdcRequestIDType),
           ('TID', TThostFtdcTIDType),
           ]
class CThostFtdcRspFutureSignInField(Structure):
    _fields_ = [
           ('TradeCode', TThostFtdcTradeCodeType),
           ('BankID', TThostFtdcBankIDType),
           ('BankBranchID', TThostFtdcBankBrchIDType),
           ('BrokerID', TThostFtdcBrokerIDType),
           ('BrokerBranchID', TThostFtdcFutureBranchIDType),
           ('TradeDate', TThostFtdcTradeDateType),
           ('TradeTime', TThostFtdcTradeTimeType),
           ('BankSerial', TThostFtdcBankSerialType),
           ('TradingDay', TThostFtdcTradeDateType),
           ('PlateSerial', TThostFtdcSerialType),
           ('LastFragment', TThostFtdcLastFragmentType),
           ('SessionID', TThostFtdcSessionIDType),
           ('InstallID', TThostFtdcInstallIDType),
           ('UserID', TThostFtdcUserIDType),
           ('Digest', TThostFtdcDigestType),
           ('CurrencyID', TThostFtdcCurrencyIDType),
           ('DeviceID', TThostFtdcDeviceIDType),
           ('BrokerIDByBank', TThostFtdcBankCodingForFutureType),
           ('OperNo', TThostFtdcOperNoType),
           ('RequestID', TThostFtdcRequestIDType),
           ('TID', TThostFtdcTIDType),
           ('ErrorID', TThostFtdcErrorIDType),
           ('ErrorMsg', TThostFtdcErrorMsgType),
           ('PinKey', TThostFtdcPasswordKeyType),
           ('MacKey', TThostFtdcPasswordKeyType),
           ]
class CThostFtdcReqFutureSignOutField(Structure):
    _fields_ = [
           ('TradeCode', TThostFtdcTradeCodeType),
           ('BankID', TThostFtdcBankIDType),
           ('BankBranchID', TThostFtdcBankBrchIDType),
           ('BrokerID', TThostFtdcBrokerIDType),
           ('BrokerBranchID', TThostFtdcFutureBranchIDType),
           ('TradeDate', TThostFtdcTradeDateType),
           ('TradeTime', TThostFtdcTradeTimeType),
           ('BankSerial', TThostFtdcBankSerialType),
           ('TradingDay', TThostFtdcTradeDateType),
           ('PlateSerial', TThostFtdcSerialType),
           ('LastFragment', TThostFtdcLastFragmentType),
           ('SessionID', TThostFtdcSessionIDType),
           ('InstallID', TThostFtdcInstallIDType),
           ('UserID', TThostFtdcUserIDType),
           ('Digest', TThostFtdcDigestType),
           ('CurrencyID', TThostFtdcCurrencyIDType),
           ('DeviceID', TThostFtdcDeviceIDType),
           ('BrokerIDByBank', TThostFtdcBankCodingForFutureType),
           ('OperNo', TThostFtdcOperNoType),
           ('RequestID', TThostFtdcRequestIDType),
           ('TID', TThostFtdcTIDType),
           ]
class CThostFtdcRspFutureSignOutField(Structure):
    _fields_ = [
           ('TradeCode', TThostFtdcTradeCodeType),
           ('BankID', TThostFtdcBankIDType),
           ('BankBranchID', TThostFtdcBankBrchIDType),
           ('BrokerID', TThostFtdcBrokerIDType),
           ('BrokerBranchID', TThostFtdcFutureBranchIDType),
           ('TradeDate', TThostFtdcTradeDateType),
           ('TradeTime', TThostFtdcTradeTimeType),
           ('BankSerial', TThostFtdcBankSerialType),
           ('TradingDay', TThostFtdcTradeDateType),
           ('PlateSerial', TThostFtdcSerialType),
           ('LastFragment', TThostFtdcLastFragmentType),
           ('SessionID', TThostFtdcSessionIDType),
           ('InstallID', TThostFtdcInstallIDType),
           ('UserID', TThostFtdcUserIDType),
           ('Digest', TThostFtdcDigestType),
           ('CurrencyID', TThostFtdcCurrencyIDType),
           ('DeviceID', TThostFtdcDeviceIDType),
           ('BrokerIDByBank', TThostFtdcBankCodingForFutureType),
           ('OperNo', TThostFtdcOperNoType),
           ('RequestID', TThostFtdcRequestIDType),
           ('TID', TThostFtdcTIDType),
           ('ErrorID', TThostFtdcErrorIDType),
           ('ErrorMsg', TThostFtdcErrorMsgType),
           ]
class CThostFtdcReqQueryTradeResultBySerialField(Structure):
    _fields_ = [
           ('TradeCode', TThostFtdcTradeCodeType),
           ('BankID', TThostFtdcBankIDType),
           ('BankBranchID', TThostFtdcBankBrchIDType),
           ('BrokerID', TThostFtdcBrokerIDType),
           ('BrokerBranchID', TThostFtdcFutureBranchIDType),
           ('TradeDate', TThostFtdcTradeDateType),
           ('TradeTime', TThostFtdcTradeTimeType),
           ('BankSerial', TThostFtdcBankSerialType),
           ('TradingDay', TThostFtdcTradeDateType),
           ('PlateSerial', TThostFtdcSerialType),
           ('LastFragment', TThostFtdcLastFragmentType),
           ('SessionID', TThostFtdcSessionIDType),
           ('Reference', TThostFtdcSerialType),
           ('RefrenceIssureType', TThostFtdcInstitutionTypeType),
           ('RefrenceIssure', TThostFtdcOrganCodeType),
           ('CustomerName', TThostFtdcIndividualNameType),
           ('IdCardType', TThostFtdcIdCardTypeType),
           ('IdentifiedCardNo', TThostFtdcIdentifiedCardNoType),
           ('CustType', TThostFtdcCustTypeType),
           ('BankAccount', TThostFtdcBankAccountType),
           ('BankPassWord', TThostFtdcPasswordType),
           ('AccountID', TThostFtdcAccountIDType),
           ('Password', TThostFtdcPasswordType),
           ('CurrencyID', TThostFtdcCurrencyIDType),
           ('TradeAmount', TThostFtdcTradeAmountType),
           ('Digest', TThostFtdcDigestType),
           ]
class CThostFtdcRspQueryTradeResultBySerialField(Structure):
    _fields_ = [
           ('TradeCode', TThostFtdcTradeCodeType),
           ('BankID', TThostFtdcBankIDType),
           ('BankBranchID', TThostFtdcBankBrchIDType),
           ('BrokerID', TThostFtdcBrokerIDType),
           ('BrokerBranchID', TThostFtdcFutureBranchIDType),
           ('TradeDate', TThostFtdcTradeDateType),
           ('TradeTime', TThostFtdcTradeTimeType),
           ('BankSerial', TThostFtdcBankSerialType),
           ('TradingDay', TThostFtdcTradeDateType),
           ('PlateSerial', TThostFtdcSerialType),
           ('LastFragment', TThostFtdcLastFragmentType),
           ('SessionID', TThostFtdcSessionIDType),
           ('ErrorID', TThostFtdcErrorIDType),
           ('ErrorMsg', TThostFtdcErrorMsgType),
           ('Reference', TThostFtdcSerialType),
           ('RefrenceIssureType', TThostFtdcInstitutionTypeType),
           ('RefrenceIssure', TThostFtdcOrganCodeType),
           ('OriginReturnCode', TThostFtdcReturnCodeType),
           ('OriginDescrInfoForReturnCode', TThostFtdcDescrInfoForReturnCodeType),
           ('BankAccount', TThostFtdcBankAccountType),
           ('BankPassWord', TThostFtdcPasswordType),
           ('AccountID', TThostFtdcAccountIDType),
           ('Password', TThostFtdcPasswordType),
           ('CurrencyID', TThostFtdcCurrencyIDType),
           ('TradeAmount', TThostFtdcTradeAmountType),
           ('Digest', TThostFtdcDigestType),
           ]
class CThostFtdcReqDayEndFileReadyField(Structure):
    _fields_ = [
           ('TradeCode', TThostFtdcTradeCodeType),
           ('BankID', TThostFtdcBankIDType),
           ('BankBranchID', TThostFtdcBankBrchIDType),
           ('BrokerID', TThostFtdcBrokerIDType),
           ('BrokerBranchID', TThostFtdcFutureBranchIDType),
           ('TradeDate', TThostFtdcTradeDateType),
           ('TradeTime', TThostFtdcTradeTimeType),
           ('BankSerial', TThostFtdcBankSerialType),
           ('TradingDay', TThostFtdcTradeDateType),
           ('PlateSerial', TThostFtdcSerialType),
           ('LastFragment', TThostFtdcLastFragmentType),
           ('SessionID', TThostFtdcSessionIDType),
           ('FileBusinessCode', TThostFtdcFileBusinessCodeType),
           ('Digest', TThostFtdcDigestType),
           ]
class CThostFtdcReturnResultField(Structure):
    _fields_ = [
           ('ReturnCode', TThostFtdcReturnCodeType),
           ('DescrInfoForReturnCode', TThostFtdcDescrInfoForReturnCodeType),
           ]
class CThostFtdcVerifyFuturePasswordField(Structure):
    _fields_ = [
           ('TradeCode', TThostFtdcTradeCodeType),
           ('BankID', TThostFtdcBankIDType),
           ('BankBranchID', TThostFtdcBankBrchIDType),
           ('BrokerID', TThostFtdcBrokerIDType),
           ('BrokerBranchID', TThostFtdcFutureBranchIDType),
           ('TradeDate', TThostFtdcTradeDateType),
           ('TradeTime', TThostFtdcTradeTimeType),
           ('BankSerial', TThostFtdcBankSerialType),
           ('TradingDay', TThostFtdcTradeDateType),
           ('PlateSerial', TThostFtdcSerialType),
           ('LastFragment', TThostFtdcLastFragmentType),
           ('SessionID', TThostFtdcSessionIDType),
           ('AccountID', TThostFtdcAccountIDType),
           ('Password', TThostFtdcPasswordType),
           ('BankAccount', TThostFtdcBankAccountType),
           ('BankPassWord', TThostFtdcPasswordType),
           ('InstallID', TThostFtdcInstallIDType),
           ('TID', TThostFtdcTIDType),
           ('CurrencyID', TThostFtdcCurrencyIDType),
           ]
class CThostFtdcVerifyCustInfoField(Structure):
    _fields_ = [
           ('CustomerName', TThostFtdcIndividualNameType),
           ('IdCardType', TThostFtdcIdCardTypeType),
           ('IdentifiedCardNo', TThostFtdcIdentifiedCardNoType),
           ('CustType', TThostFtdcCustTypeType),
           ]
class CThostFtdcVerifyFuturePasswordAndCustInfoField(Structure):
    _fields_ = [
           ('CustomerName', TThostFtdcIndividualNameType),
           ('IdCardType', TThostFtdcIdCardTypeType),
           ('IdentifiedCardNo', TThostFtdcIdentifiedCardNoType),
           ('CustType', TThostFtdcCustTypeType),
           ('AccountID', TThostFtdcAccountIDType),
           ('Password', TThostFtdcPasswordType),
           ('CurrencyID', TThostFtdcCurrencyIDType),
           ]
class CThostFtdcDepositResultInformField(Structure):
    _fields_ = [
           ('DepositSeqNo', TThostFtdcDepositSeqNoType),
           ('BrokerID', TThostFtdcBrokerIDType),
           ('InvestorID', TThostFtdcInvestorIDType),
           ('Deposit', TThostFtdcMoneyType),
           ('RequestID', TThostFtdcRequestIDType),
           ('ReturnCode', TThostFtdcReturnCodeType),
           ('DescrInfoForReturnCode', TThostFtdcDescrInfoForReturnCodeType),
           ]
class CThostFtdcReqSyncKeyField(Structure):
    _fields_ = [
           ('TradeCode', TThostFtdcTradeCodeType),
           ('BankID', TThostFtdcBankIDType),
           ('BankBranchID', TThostFtdcBankBrchIDType),
           ('BrokerID', TThostFtdcBrokerIDType),
           ('BrokerBranchID', TThostFtdcFutureBranchIDType),
           ('TradeDate', TThostFtdcTradeDateType),
           ('TradeTime', TThostFtdcTradeTimeType),
           ('BankSerial', TThostFtdcBankSerialType),
           ('TradingDay', TThostFtdcTradeDateType),
           ('PlateSerial', TThostFtdcSerialType),
           ('LastFragment', TThostFtdcLastFragmentType),
           ('SessionID', TThostFtdcSessionIDType),
           ('InstallID', TThostFtdcInstallIDType),
           ('UserID', TThostFtdcUserIDType),
           ('Message', TThostFtdcAddInfoType),
           ('DeviceID', TThostFtdcDeviceIDType),
           ('BrokerIDByBank', TThostFtdcBankCodingForFutureType),
           ('OperNo', TThostFtdcOperNoType),
           ('RequestID', TThostFtdcRequestIDType),
           ('TID', TThostFtdcTIDType),
           ]
class CThostFtdcRspSyncKeyField(Structure):
    _fields_ = [
           ('TradeCode', TThostFtdcTradeCodeType),
           ('BankID', TThostFtdcBankIDType),
           ('BankBranchID', TThostFtdcBankBrchIDType),
           ('BrokerID', TThostFtdcBrokerIDType),
           ('BrokerBranchID', TThostFtdcFutureBranchIDType),
           ('TradeDate', TThostFtdcTradeDateType),
           ('TradeTime', TThostFtdcTradeTimeType),
           ('BankSerial', TThostFtdcBankSerialType),
           ('TradingDay', TThostFtdcTradeDateType),
           ('PlateSerial', TThostFtdcSerialType),
           ('LastFragment', TThostFtdcLastFragmentType),
           ('SessionID', TThostFtdcSessionIDType),
           ('InstallID', TThostFtdcInstallIDType),
           ('UserID', TThostFtdcUserIDType),
           ('Message', TThostFtdcAddInfoType),
           ('DeviceID', TThostFtdcDeviceIDType),
           ('BrokerIDByBank', TThostFtdcBankCodingForFutureType),
           ('OperNo', TThostFtdcOperNoType),
           ('RequestID', TThostFtdcRequestIDType),
           ('TID', TThostFtdcTIDType),
           ('ErrorID', TThostFtdcErrorIDType),
           ('ErrorMsg', TThostFtdcErrorMsgType),
           ]
class CThostFtdcNotifyQueryAccountField(Structure):
    _fields_ = [
           ('TradeCode', TThostFtdcTradeCodeType),
           ('BankID', TThostFtdcBankIDType),
           ('BankBranchID', TThostFtdcBankBrchIDType),
           ('BrokerID', TThostFtdcBrokerIDType),
           ('BrokerBranchID', TThostFtdcFutureBranchIDType),
           ('TradeDate', TThostFtdcTradeDateType),
           ('TradeTime', TThostFtdcTradeTimeType),
           ('BankSerial', TThostFtdcBankSerialType),
           ('TradingDay', TThostFtdcTradeDateType),
           ('PlateSerial', TThostFtdcSerialType),
           ('LastFragment', TThostFtdcLastFragmentType),
           ('SessionID', TThostFtdcSessionIDType),
           ('CustomerName', TThostFtdcIndividualNameType),
           ('IdCardType', TThostFtdcIdCardTypeType),
           ('IdentifiedCardNo', TThostFtdcIdentifiedCardNoType),
           ('CustType', TThostFtdcCustTypeType),
           ('BankAccount', TThostFtdcBankAccountType),
           ('BankPassWord', TThostFtdcPasswordType),
           ('AccountID', TThostFtdcAccountIDType),
           ('Password', TThostFtdcPasswordType),
           ('FutureSerial', TThostFtdcFutureSerialType),
           ('InstallID', TThostFtdcInstallIDType),
           ('UserID', TThostFtdcUserIDType),
           ('VerifyCertNoFlag', TThostFtdcYesNoIndicatorType),
           ('CurrencyID', TThostFtdcCurrencyIDType),
           ('Digest', TThostFtdcDigestType),
           ('BankAccType', TThostFtdcBankAccTypeType),
           ('DeviceID', TThostFtdcDeviceIDType),
           ('BankSecuAccType', TThostFtdcBankAccTypeType),
           ('BrokerIDByBank', TThostFtdcBankCodingForFutureType),
           ('BankSecuAcc', TThostFtdcBankAccountType),
           ('BankPwdFlag', TThostFtdcPwdFlagType),
           ('SecuPwdFlag', TThostFtdcPwdFlagType),
           ('OperNo', TThostFtdcOperNoType),
           ('RequestID', TThostFtdcRequestIDType),
           ('TID', TThostFtdcTIDType),
           ('BankUseAmount', TThostFtdcTradeAmountType),
           ('BankFetchAmount', TThostFtdcTradeAmountType),
           ('ErrorID', TThostFtdcErrorIDType),
           ('ErrorMsg', TThostFtdcErrorMsgType),
           ]
class CThostFtdcTransferSerialField(Structure):
    _fields_ = [
           ('PlateSerial', TThostFtdcPlateSerialType),
           ('TradeDate', TThostFtdcTradeDateType),
           ('TradingDay', TThostFtdcDateType),
           ('TradeTime', TThostFtdcTradeTimeType),
           ('TradeCode', TThostFtdcTradeCodeType),
           ('SessionID', TThostFtdcSessionIDType),
           ('BankID', TThostFtdcBankIDType),
           ('BankBranchID', TThostFtdcBankBrchIDType),
           ('BankAccType', TThostFtdcBankAccTypeType),
           ('BankAccount', TThostFtdcBankAccountType),
           ('BankSerial', TThostFtdcBankSerialType),
           ('BrokerID', TThostFtdcBrokerIDType),
           ('BrokerBranchID', TThostFtdcFutureBranchIDType),
           ('FutureAccType', TThostFtdcFutureAccTypeType),
           ('AccountID', TThostFtdcAccountIDType),
           ('InvestorID', TThostFtdcInvestorIDType),
           ('FutureSerial', TThostFtdcFutureSerialType),
           ('IdCardType', TThostFtdcIdCardTypeType),
           ('IdentifiedCardNo', TThostFtdcIdentifiedCardNoType),
           ('CurrencyID', TThostFtdcCurrencyIDType),
           ('TradeAmount', TThostFtdcTradeAmountType),
           ('CustFee', TThostFtdcCustFeeType),
           ('BrokerFee', TThostFtdcFutureFeeType),
           ('AvailabilityFlag', TThostFtdcAvailabilityFlagType),
           ('OperatorCode', TThostFtdcOperatorCodeType),
           ('BankNewAccount', TThostFtdcBankAccountType),
           ('ErrorID', TThostFtdcErrorIDType),
           ('ErrorMsg', TThostFtdcErrorMsgType),
           ]
class CThostFtdcQryTransferSerialField(Structure):
    _fields_ = [
           ('BrokerID', TThostFtdcBrokerIDType),
           ('AccountID', TThostFtdcAccountIDType),
           ('BankID', TThostFtdcBankIDType),
           ('CurrencyID', TThostFtdcCurrencyIDType),
           ]
class CThostFtdcNotifyFutureSignInField(Structure):
    _fields_ = [
           ('TradeCode', TThostFtdcTradeCodeType),
           ('BankID', TThostFtdcBankIDType),
           ('BankBranchID', TThostFtdcBankBrchIDType),
           ('BrokerID', TThostFtdcBrokerIDType),
           ('BrokerBranchID', TThostFtdcFutureBranchIDType),
           ('TradeDate', TThostFtdcTradeDateType),
           ('TradeTime', TThostFtdcTradeTimeType),
           ('BankSerial', TThostFtdcBankSerialType),
           ('TradingDay', TThostFtdcTradeDateType),
           ('PlateSerial', TThostFtdcSerialType),
           ('LastFragment', TThostFtdcLastFragmentType),
           ('SessionID', TThostFtdcSessionIDType),
           ('InstallID', TThostFtdcInstallIDType),
           ('UserID', TThostFtdcUserIDType),
           ('Digest', TThostFtdcDigestType),
           ('CurrencyID', TThostFtdcCurrencyIDType),
           ('DeviceID', TThostFtdcDeviceIDType),
           ('BrokerIDByBank', TThostFtdcBankCodingForFutureType),
           ('OperNo', TThostFtdcOperNoType),
           ('RequestID', TThostFtdcRequestIDType),
           ('TID', TThostFtdcTIDType),
           ('ErrorID', TThostFtdcErrorIDType),
           ('ErrorMsg', TThostFtdcErrorMsgType),
           ('PinKey', TThostFtdcPasswordKeyType),
           ('MacKey', TThostFtdcPasswordKeyType),
           ]
class CThostFtdcNotifyFutureSignOutField(Structure):
    _fields_ = [
           ('TradeCode', TThostFtdcTradeCodeType),
           ('BankID', TThostFtdcBankIDType),
           ('BankBranchID', TThostFtdcBankBrchIDType),
           ('BrokerID', TThostFtdcBrokerIDType),
           ('BrokerBranchID', TThostFtdcFutureBranchIDType),
           ('TradeDate', TThostFtdcTradeDateType),
           ('TradeTime', TThostFtdcTradeTimeType),
           ('BankSerial', TThostFtdcBankSerialType),
           ('TradingDay', TThostFtdcTradeDateType),
           ('PlateSerial', TThostFtdcSerialType),
           ('LastFragment', TThostFtdcLastFragmentType),
           ('SessionID', TThostFtdcSessionIDType),
           ('InstallID', TThostFtdcInstallIDType),
           ('UserID', TThostFtdcUserIDType),
           ('Digest', TThostFtdcDigestType),
           ('CurrencyID', TThostFtdcCurrencyIDType),
           ('DeviceID', TThostFtdcDeviceIDType),
           ('BrokerIDByBank', TThostFtdcBankCodingForFutureType),
           ('OperNo', TThostFtdcOperNoType),
           ('RequestID', TThostFtdcRequestIDType),
           ('TID', TThostFtdcTIDType),
           ('ErrorID', TThostFtdcErrorIDType),
           ('ErrorMsg', TThostFtdcErrorMsgType),
           ]
class CThostFtdcNotifySyncKeyField(Structure):
    _fields_ = [
           ('TradeCode', TThostFtdcTradeCodeType),
           ('BankID', TThostFtdcBankIDType),
           ('BankBranchID', TThostFtdcBankBrchIDType),
           ('BrokerID', TThostFtdcBrokerIDType),
           ('BrokerBranchID', TThostFtdcFutureBranchIDType),
           ('TradeDate', TThostFtdcTradeDateType),
           ('TradeTime', TThostFtdcTradeTimeType),
           ('BankSerial', TThostFtdcBankSerialType),
           ('TradingDay', TThostFtdcTradeDateType),
           ('PlateSerial', TThostFtdcSerialType),
           ('LastFragment', TThostFtdcLastFragmentType),
           ('SessionID', TThostFtdcSessionIDType),
           ('InstallID', TThostFtdcInstallIDType),
           ('UserID', TThostFtdcUserIDType),
           ('Message', TThostFtdcAddInfoType),
           ('DeviceID', TThostFtdcDeviceIDType),
           ('BrokerIDByBank', TThostFtdcBankCodingForFutureType),
           ('OperNo', TThostFtdcOperNoType),
           ('RequestID', TThostFtdcRequestIDType),
           ('TID', TThostFtdcTIDType),
           ('ErrorID', TThostFtdcErrorIDType),
           ('ErrorMsg', TThostFtdcErrorMsgType),
           ]
class CThostFtdcQryAccountregisterField(Structure):
    _fields_ = [
           ('BrokerID', TThostFtdcBrokerIDType),
           ('AccountID', TThostFtdcAccountIDType),
           ('BankID', TThostFtdcBankIDType),
           ('BankBranchID', TThostFtdcBankBrchIDType),
           ('CurrencyID', TThostFtdcCurrencyIDType),
           ]
class CThostFtdcAccountregisterField(Structure):
    _fields_ = [
           ('TradeDay', TThostFtdcTradeDateType),
           ('BankID', TThostFtdcBankIDType),
           ('BankBranchID', TThostFtdcBankBrchIDType),
           ('BankAccount', TThostFtdcBankAccountType),
           ('BrokerID', TThostFtdcBrokerIDType),
           ('BrokerBranchID', TThostFtdcFutureBranchIDType),
           ('AccountID', TThostFtdcAccountIDType),
           ('IdCardType', TThostFtdcIdCardTypeType),
           ('IdentifiedCardNo', TThostFtdcIdentifiedCardNoType),
           ('CustomerName', TThostFtdcIndividualNameType),
           ('CurrencyID', TThostFtdcCurrencyIDType),
           ('OpenOrDestroy', TThostFtdcOpenOrDestroyType),
           ('RegDate', TThostFtdcTradeDateType),
           ('OutDate', TThostFtdcTradeDateType),
           ('TID', TThostFtdcTIDType),
           ('CustType', TThostFtdcCustTypeType),
           ('BankAccType', TThostFtdcBankAccTypeType),
           ]
class CThostFtdcOpenAccountField(Structure):
    _fields_ = [
           ('TradeCode', TThostFtdcTradeCodeType),
           ('BankID', TThostFtdcBankIDType),
           ('BankBranchID', TThostFtdcBankBrchIDType),
           ('BrokerID', TThostFtdcBrokerIDType),
           ('BrokerBranchID', TThostFtdcFutureBranchIDType),
           ('TradeDate', TThostFtdcTradeDateType),
           ('TradeTime', TThostFtdcTradeTimeType),
           ('BankSerial', TThostFtdcBankSerialType),
           ('TradingDay', TThostFtdcTradeDateType),
           ('PlateSerial', TThostFtdcSerialType),
           ('LastFragment', TThostFtdcLastFragmentType),
           ('SessionID', TThostFtdcSessionIDType),
           ('CustomerName', TThostFtdcIndividualNameType),
           ('IdCardType', TThostFtdcIdCardTypeType),
           ('IdentifiedCardNo', TThostFtdcIdentifiedCardNoType),
           ('Gender', TThostFtdcGenderType),
           ('CountryCode', TThostFtdcCountryCodeType),
           ('CustType', TThostFtdcCustTypeType),
           ('Address', TThostFtdcAddressType),
           ('ZipCode', TThostFtdcZipCodeType),
           ('Telephone', TThostFtdcTelephoneType),
           ('MobilePhone', TThostFtdcMobilePhoneType),
           ('Fax', TThostFtdcFaxType),
           ('EMail', TThostFtdcEMailType),
           ('MoneyAccountStatus', TThostFtdcMoneyAccountStatusType),
           ('BankAccount', TThostFtdcBankAccountType),
           ('BankPassWord', TThostFtdcPasswordType),
           ('AccountID', TThostFtdcAccountIDType),
           ('Password', TThostFtdcPasswordType),
           ('InstallID', TThostFtdcInstallIDType),
           ('VerifyCertNoFlag', TThostFtdcYesNoIndicatorType),
           ('CurrencyID', TThostFtdcCurrencyIDType),
           ('CashExchangeCode', TThostFtdcCashExchangeCodeType),
           ('Digest', TThostFtdcDigestType),
           ('BankAccType', TThostFtdcBankAccTypeType),
           ('DeviceID', TThostFtdcDeviceIDType),
           ('BankSecuAccType', TThostFtdcBankAccTypeType),
           ('BrokerIDByBank', TThostFtdcBankCodingForFutureType),
           ('BankSecuAcc', TThostFtdcBankAccountType),
           ('BankPwdFlag', TThostFtdcPwdFlagType),
           ('SecuPwdFlag', TThostFtdcPwdFlagType),
           ('OperNo', TThostFtdcOperNoType),
           ('TID', TThostFtdcTIDType),
           ('UserID', TThostFtdcUserIDType),
           ('ErrorID', TThostFtdcErrorIDType),
           ('ErrorMsg', TThostFtdcErrorMsgType),
           ]
class CThostFtdcCancelAccountField(Structure):
    _fields_ = [
           ('TradeCode', TThostFtdcTradeCodeType),
           ('BankID', TThostFtdcBankIDType),
           ('BankBranchID', TThostFtdcBankBrchIDType),
           ('BrokerID', TThostFtdcBrokerIDType),
           ('BrokerBranchID', TThostFtdcFutureBranchIDType),
           ('TradeDate', TThostFtdcTradeDateType),
           ('TradeTime', TThostFtdcTradeTimeType),
           ('BankSerial', TThostFtdcBankSerialType),
           ('TradingDay', TThostFtdcTradeDateType),
           ('PlateSerial', TThostFtdcSerialType),
           ('LastFragment', TThostFtdcLastFragmentType),
           ('SessionID', TThostFtdcSessionIDType),
           ('CustomerName', TThostFtdcIndividualNameType),
           ('IdCardType', TThostFtdcIdCardTypeType),
           ('IdentifiedCardNo', TThostFtdcIdentifiedCardNoType),
           ('Gender', TThostFtdcGenderType),
           ('CountryCode', TThostFtdcCountryCodeType),
           ('CustType', TThostFtdcCustTypeType),
           ('Address', TThostFtdcAddressType),
           ('ZipCode', TThostFtdcZipCodeType),
           ('Telephone', TThostFtdcTelephoneType),
           ('MobilePhone', TThostFtdcMobilePhoneType),
           ('Fax', TThostFtdcFaxType),
           ('EMail', TThostFtdcEMailType),
           ('MoneyAccountStatus', TThostFtdcMoneyAccountStatusType),
           ('BankAccount', TThostFtdcBankAccountType),
           ('BankPassWord', TThostFtdcPasswordType),
           ('AccountID', TThostFtdcAccountIDType),
           ('Password', TThostFtdcPasswordType),
           ('InstallID', TThostFtdcInstallIDType),
           ('VerifyCertNoFlag', TThostFtdcYesNoIndicatorType),
           ('CurrencyID', TThostFtdcCurrencyIDType),
           ('CashExchangeCode', TThostFtdcCashExchangeCodeType),
           ('Digest', TThostFtdcDigestType),
           ('BankAccType', TThostFtdcBankAccTypeType),
           ('DeviceID', TThostFtdcDeviceIDType),
           ('BankSecuAccType', TThostFtdcBankAccTypeType),
           ('BrokerIDByBank', TThostFtdcBankCodingForFutureType),
           ('BankSecuAcc', TThostFtdcBankAccountType),
           ('BankPwdFlag', TThostFtdcPwdFlagType),
           ('SecuPwdFlag', TThostFtdcPwdFlagType),
           ('OperNo', TThostFtdcOperNoType),
           ('TID', TThostFtdcTIDType),
           ('UserID', TThostFtdcUserIDType),
           ('ErrorID', TThostFtdcErrorIDType),
           ('ErrorMsg', TThostFtdcErrorMsgType),
           ]
class CThostFtdcChangeAccountField(Structure):
    _fields_ = [
           ('TradeCode', TThostFtdcTradeCodeType),
           ('BankID', TThostFtdcBankIDType),
           ('BankBranchID', TThostFtdcBankBrchIDType),
           ('BrokerID', TThostFtdcBrokerIDType),
           ('BrokerBranchID', TThostFtdcFutureBranchIDType),
           ('TradeDate', TThostFtdcTradeDateType),
           ('TradeTime', TThostFtdcTradeTimeType),
           ('BankSerial', TThostFtdcBankSerialType),
           ('TradingDay', TThostFtdcTradeDateType),
           ('PlateSerial', TThostFtdcSerialType),
           ('LastFragment', TThostFtdcLastFragmentType),
           ('SessionID', TThostFtdcSessionIDType),
           ('CustomerName', TThostFtdcIndividualNameType),
           ('IdCardType', TThostFtdcIdCardTypeType),
           ('IdentifiedCardNo', TThostFtdcIdentifiedCardNoType),
           ('Gender', TThostFtdcGenderType),
           ('CountryCode', TThostFtdcCountryCodeType),
           ('CustType', TThostFtdcCustTypeType),
           ('Address', TThostFtdcAddressType),
           ('ZipCode', TThostFtdcZipCodeType),
           ('Telephone', TThostFtdcTelephoneType),
           ('MobilePhone', TThostFtdcMobilePhoneType),
           ('Fax', TThostFtdcFaxType),
           ('EMail', TThostFtdcEMailType),
           ('MoneyAccountStatus', TThostFtdcMoneyAccountStatusType),
           ('BankAccount', TThostFtdcBankAccountType),
           ('BankPassWord', TThostFtdcPasswordType),
           ('NewBankAccount', TThostFtdcBankAccountType),
           ('NewBankPassWord', TThostFtdcPasswordType),
           ('AccountID', TThostFtdcAccountIDType),
           ('Password', TThostFtdcPasswordType),
           ('BankAccType', TThostFtdcBankAccTypeType),
           ('InstallID', TThostFtdcInstallIDType),
           ('VerifyCertNoFlag', TThostFtdcYesNoIndicatorType),
           ('CurrencyID', TThostFtdcCurrencyIDType),
           ('BrokerIDByBank', TThostFtdcBankCodingForFutureType),
           ('BankPwdFlag', TThostFtdcPwdFlagType),
           ('SecuPwdFlag', TThostFtdcPwdFlagType),
           ('TID', TThostFtdcTIDType),
           ('Digest', TThostFtdcDigestType),
           ('ErrorID', TThostFtdcErrorIDType),
           ('ErrorMsg', TThostFtdcErrorMsgType),
           ]
class CThostFtdcSecAgentACIDMapField(Structure):
    _fields_ = [
           ('BrokerID', TThostFtdcBrokerIDType),
           ('UserID', TThostFtdcUserIDType),
           ('AccountID', TThostFtdcAccountIDType),
           ('CurrencyID', TThostFtdcCurrencyIDType),
           ('BrokerSecAgentID', TThostFtdcAccountIDType),
           ]
class CThostFtdcQrySecAgentACIDMapField(Structure):
    _fields_ = [
           ('BrokerID', TThostFtdcBrokerIDType),
           ('UserID', TThostFtdcUserIDType),
           ('AccountID', TThostFtdcAccountIDType),
           ('CurrencyID', TThostFtdcCurrencyIDType),
           ]
class CThostFtdcUserRightsAssignField(Structure):
    _fields_ = [
           ('BrokerID', TThostFtdcBrokerIDType),
           ('UserID', TThostFtdcUserIDType),
           ('DRIdentityID', TThostFtdcDRIdentityIDType),
           ]
class CThostFtdcBrokerUserRightAssignField(Structure):
    _fields_ = [
           ('BrokerID', TThostFtdcBrokerIDType),
           ('DRIdentityID', TThostFtdcDRIdentityIDType),
           ('Tradeable', TThostFtdcBoolType),
           ]
class CThostFtdcDRTransferField(Structure):
    _fields_ = [
           ('OrigDRIdentityID', TThostFtdcDRIdentityIDType),
           ('DestDRIdentityID', TThostFtdcDRIdentityIDType),
           ('OrigBrokerID', TThostFtdcBrokerIDType),
           ('DestBrokerID', TThostFtdcBrokerIDType),
           ]
class CThostFtdcFensUserInfoField(Structure):
    _fields_ = [
           ('BrokerID', TThostFtdcBrokerIDType),
           ('UserID', TThostFtdcUserIDType),
           ('LoginMode', TThostFtdcLoginModeType),
           ]
class CThostFtdcCurrTransferIdentityField(Structure):
    _fields_ = [
           ('IdentityID', TThostFtdcDRIdentityIDType),
           ]
class CThostFtdcLoginForbiddenUserField(Structure):
    _fields_ = [
           ('BrokerID', TThostFtdcBrokerIDType),
           ('UserID', TThostFtdcUserIDType),
           ]
class CThostFtdcQryLoginForbiddenUserField(Structure):
    _fields_ = [
           ('BrokerID', TThostFtdcBrokerIDType),
           ('UserID', TThostFtdcUserIDType),
           ]
class CThostFtdcMulticastGroupInfoField(Structure):
    _fields_ = [
           ('GroupIP', TThostFtdcIPAddressType),
           ('GroupPort', TThostFtdcIPPortType),
           ('SourceIP', TThostFtdcIPAddressType),
           ]
class CThostFtdcTradingAccountReserveField(Structure):
    _fields_ = [
           ('BrokerID', TThostFtdcBrokerIDType),
           ('AccountID', TThostFtdcAccountIDType),
           ('Reserve', TThostFtdcMoneyType),
           ('CurrencyID', TThostFtdcCurrencyIDType),
           ]
