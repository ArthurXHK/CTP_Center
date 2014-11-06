#include "Trader.h"

//----------------CallBack--------------------

//深度行情回报
void __stdcall Trader::OnRtnDepthMarketData(void* pMdUserApi, CThostFtdcDepthMarketDataField *pDepthMarketData)
{

}

//连接回报信息
void __stdcall Trader::OnConnect(void* pApi, CThostFtdcRspUserLoginField *pRspUserLogin, ConnectionStatus result)
{
     PrintLog(GetPortMsg(pApi) +string("-->") + ConnectionStatusMsg(result));
}

//断开连接回报信息
void __stdcall Trader::OnDisconnect(void* pApi, CThostFtdcRspInfoField *pRspInfo, ConnectionStatus step)
{
    PrintLog(GetPortMsg(pApi) + string("-->") + ConnectionStatusMsg(step));
}

//撤单错误信息
void __stdcall Trader::OnErrRtnOrderAction(void* pTraderApi, CThostFtdcOrderActionField *pOrderAction, CThostFtdcRspInfoField *pRspInfo)
{
    PrintLog(GetPortMsg(pTraderApi) + ": " + pRspInfo->ErrorMsg, "error");
}

//下单错误信息
void __stdcall Trader::OnErrRtnOrderInsert(void* pTraderApi, CThostFtdcInputOrderField *pInputOrder, CThostFtdcRspInfoField *pRspInfo)
{
    PrintLog(GetPortMsg(pTraderApi) + ": " + pRspInfo->ErrorMsg, "error");
}


void __stdcall Trader::OnErrRtnQuoteAction(void* pTraderApi, CThostFtdcQuoteActionField *pQuoteAction, CThostFtdcRspInfoField *pRspInfo)
{
    PrintLog(GetPortMsg(pTraderApi) + ": " + pRspInfo->ErrorMsg, "error");
}

void __stdcall Trader::OnErrRtnQuoteInsert(void* pTraderApi, CThostFtdcInputQuoteField *pInputQuote, CThostFtdcRspInfoField *pRspInfo)
{
    PrintLog(GetPortMsg(pTraderApi) + ": " + pRspInfo->ErrorMsg, "error");
}

//错误信息
void __stdcall Trader::OnRspError(void* pApi, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
{
    PrintLog(GetPortMsg(pApi) + ": " + pRspInfo->ErrorMsg, "error");
}

//撤单回报
void __stdcall Trader::OnRspOrderAction(void* pTraderApi, CThostFtdcInputOrderActionField *pInputOrderAction, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
{
    if (pRspInfo->ErrorID)
        PrintLog(GetPortMsg(pTraderApi) + ": " + pRspInfo->ErrorMsg, "error");
}

//下单回报
void __stdcall Trader::OnRspOrderInsert(void* pTraderApi, CThostFtdcInputOrderField *pInputOrder, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
{
    if (pRspInfo->ErrorID)
        PrintLog(GetPortMsg(pTraderApi) + ": " + pRspInfo->ErrorMsg, "error");
}

//查询深度行情回报
void __stdcall Trader::OnRspQryDepthMarketData(void* pTraderApi, CThostFtdcDepthMarketDataField *pDepthMarketData, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
{
    if (pRspInfo->ErrorID)
        PrintLog(GetPortMsg(pTraderApi) + ": " + pRspInfo->ErrorMsg, "error");
}

//查询合约回报
void __stdcall Trader::OnRspQryInstrument(void* pTraderApi, CThostFtdcInstrumentField *pInstrument, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
{
    if (pRspInfo->ErrorID)
        PrintLog(GetPortMsg(pTraderApi) + ": " + pRspInfo->ErrorMsg, "error");
}

//查询合约手续费率回报
void __stdcall Trader::OnRspQryInstrumentCommissionRate(void* pTraderApi, CThostFtdcInstrumentCommissionRateField *pInstrumentCommissionRate, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
{
    if (pRspInfo->ErrorID)
        PrintLog(GetPortMsg(pTraderApi) + ": " + pRspInfo->ErrorMsg, "error");
}

//查询合约保证金率回报
void __stdcall Trader::OnRspQryInstrumentMarginRate(void* pTraderApi, CThostFtdcInstrumentMarginRateField *pInstrumentMarginRate, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
{
    if (pRspInfo->ErrorID)
        PrintLog(GetPortMsg(pTraderApi) + ": " + pRspInfo->ErrorMsg, "error");
}

//查询投资者持仓回报
void __stdcall Trader::OnRspQryInvestorPosition(void* pTraderApi, CThostFtdcInvestorPositionField *pInvestorPosition, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
{
    if (pRspInfo->ErrorID)
        PrintLog(GetPortMsg(pTraderApi) + ": " + pRspInfo->ErrorMsg, "error");
}

//查询持仓详细回报
void __stdcall Trader::OnRspQryInvestorPositionDetail(void* pTraderApi, CThostFtdcInvestorPositionDetailField *pInvestorPositionDetail, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
{
    if (pRspInfo->ErrorID)
        PrintLog(GetPortMsg(pTraderApi) + ": " + pRspInfo->ErrorMsg, "error");
}

//查询订单回报
void __stdcall Trader::OnRspQryOrder(void* pTraderApi, CThostFtdcOrderField *pOrder, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
{
    if (pRspInfo->ErrorID)
        PrintLog(GetPortMsg(pTraderApi) + ": " + pRspInfo->ErrorMsg, "error");
}

//查询成交回报
void __stdcall Trader::OnRspQryTrade(void* pTraderApi, CThostFtdcTradeField *pTrade, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
{
    if (pRspInfo->ErrorID)
        PrintLog(GetPortMsg(pTraderApi) + ": " + pRspInfo->ErrorMsg, "error");
}

//查询投资者结算回报
void __stdcall Trader::OnRspQrySettlementInfo(void* pTraderApi, CThostFtdcSettlementInfoField *pSettlementInfo, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
{
    if (pRspInfo->ErrorID)
        PrintLog(GetPortMsg(pTraderApi) + ": " + pRspInfo->ErrorMsg, "error");
}

//查询资金账户回报
void __stdcall Trader::OnRspQryTradingAccount(void* pTraderApi, CThostFtdcTradingAccountField *pTradingAccount, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
{
    if (pRspInfo->ErrorID)
        PrintLog(GetPortMsg(pTraderApi) + ": " + pRspInfo->ErrorMsg, "error");
}

//合约状态回报
void __stdcall Trader::OnRtnInstrumentStatus(void* pTraderApi, CThostFtdcInstrumentStatusField *pInstrumentStatus)
{

}

//报单回报
void __stdcall Trader::OnRtnOrder(void* pTraderApi, CThostFtdcOrderField *pOrder)
{

}

//成交回报
void __stdcall Trader::OnRtnTrade(void* pTraderApi, CThostFtdcTradeField *pTrade)
{
}


//其他回调
void __stdcall Trader::OnRspQuoteAction(void* pTraderApi, CThostFtdcInputQuoteActionField *pInputQuoteAction, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
{
}
void __stdcall Trader::OnRspQuoteInsert(void* pTraderApi, CThostFtdcInputQuoteField *pInputQuote, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
{
}
void __stdcall Trader::OnRtnForQuoteRsp(void* pMdUserApi, CThostFtdcForQuoteRspField *pForQuoteRsp)
{
}
void __stdcall Trader::OnRtnQuote(void* pTraderApi, CThostFtdcQuoteField *pQuote)
{
}
