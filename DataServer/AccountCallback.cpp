#include "Account.h"

//----------------CallBack--------------------

//连接回报信息
void __stdcall Account::OnConnect(void* pApi, CThostFtdcRspUserLoginField *pRspUserLogin, ConnectionStatus result)
{
     dblog->PrintLog(GetPortMsg(pApi) +string("-->") + ConnectionStatusMsg(result));
}

//断开连接回报信息
void __stdcall Account::OnDisconnect(void* pApi, CThostFtdcRspInfoField *pRspInfo, ConnectionStatus step)
{
    cout << pRspInfo->ErrorMsg << endl;
}

//撤单错误信息
void __stdcall Account::OnErrRtnOrderAction(void* pTraderApi, CThostFtdcOrderActionField *pOrderAction, CThostFtdcRspInfoField *pRspInfo)
{
    cout << pRspInfo->ErrorMsg << endl;
}

//下单错误信息
void __stdcall Account::OnErrRtnOrderInsert(void* pTraderApi, CThostFtdcInputOrderField *pInputOrder, CThostFtdcRspInfoField *pRspInfo)
{
    cout << pRspInfo->ErrorMsg << endl;
}


void __stdcall Account::OnErrRtnQuoteAction(void* pTraderApi, CThostFtdcQuoteActionField *pQuoteAction, CThostFtdcRspInfoField *pRspInfo)
{
}

void __stdcall Account::OnErrRtnQuoteInsert(void* pTraderApi, CThostFtdcInputQuoteField *pInputQuote, CThostFtdcRspInfoField *pRspInfo)
{
}

//错误信息
void __stdcall Account::OnRspError(void* pApi, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
{
    cout << pRspInfo->ErrorMsg << endl;
}

//撤单回报
void __stdcall Account::OnRspOrderAction(void* pTraderApi, CThostFtdcInputOrderActionField *pInputOrderAction, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
{
    cout << pRspInfo->ErrorMsg << endl;
}

//下单回报
void __stdcall Account::OnRspOrderInsert(void* pTraderApi, CThostFtdcInputOrderField *pInputOrder, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
{
    cout << pRspInfo->ErrorMsg << endl;
}

//查询深度行情回报
void __stdcall Account::OnRspQryDepthMarketData(void* pTraderApi, CThostFtdcDepthMarketDataField *pDepthMarketData, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
{
}

//查询合约回报
void __stdcall Account::OnRspQryInstrument(void* pTraderApi, CThostFtdcInstrumentField *pInstrument, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
{
    cout << pInstrument->InstrumentID << endl;
}

//查询合约手续费率回报
void __stdcall Account::OnRspQryInstrumentCommissionRate(void* pTraderApi, CThostFtdcInstrumentCommissionRateField *pInstrumentCommissionRate, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
{
}

//查询合约保证金率回报
void __stdcall Account::OnRspQryInstrumentMarginRate(void* pTraderApi, CThostFtdcInstrumentMarginRateField *pInstrumentMarginRate, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
{
    cout << pInstrumentMarginRate->LongMarginRatioByMoney << endl;
}

//查询投资者持仓回报
void __stdcall Account::OnRspQryInvestorPosition(void* pTraderApi, CThostFtdcInvestorPositionField *pInvestorPosition, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
{
    cout << pInvestorPosition->CloseProfit << endl;
}

//查询持仓详细回报
void __stdcall Account::OnRspQryInvestorPositionDetail(void* pTraderApi, CThostFtdcInvestorPositionDetailField *pInvestorPositionDetail, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
{
}

//查询订单回报
void __stdcall Account::OnRspQryOrder(void* pTraderApi, CThostFtdcOrderField *pOrder, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
{
}

//查询成交回报
void __stdcall Account::OnRspQryTrade(void* pTraderApi, CThostFtdcTradeField *pTrade, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
{
}

//查询投资者结算回报
void __stdcall Account::OnRspQrySettlementInfo(void* pTraderApi, CThostFtdcSettlementInfoField *pSettlementInfo, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
{
}

//查询资金账户回报
void __stdcall Account::OnRspQryTradingAccount(void* pTraderApi, CThostFtdcTradingAccountField *pTradingAccount, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
{
    cout << pTradingAccount->AccountID << endl;
    cout << pTradingAccount->Available << endl;
    cout << pTradingAccount->Deposit << endl;
    cout << pRspInfo->ErrorMsg << endl;
}

//深度行情回报
void __stdcall Account::OnRtnDepthMarketData(void* pMdUserApi, CThostFtdcDepthMarketDataField *pDepthMarketData)
{
    cout << pDepthMarketData->InstrumentID << endl;
    cout << pDepthMarketData->LastPrice << endl;
}

//合约状态回报
void __stdcall Account::OnRtnInstrumentStatus(void* pTraderApi, CThostFtdcInstrumentStatusField *pInstrumentStatus)
{

}

//报单回报
void __stdcall Account::OnRtnOrder(void* pTraderApi, CThostFtdcOrderField *pOrder)
{
    cout << pOrder->StatusMsg << endl;
}

//成交回报
void __stdcall Account::OnRtnTrade(void* pTraderApi, CThostFtdcTradeField *pTrade)
{
}


//其他回调
void __stdcall Account::OnRspQuoteAction(void* pTraderApi, CThostFtdcInputQuoteActionField *pInputQuoteAction, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
{
}
void __stdcall Account::OnRspQuoteInsert(void* pTraderApi, CThostFtdcInputQuoteField *pInputQuote, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
{
}
void __stdcall Account::OnRtnForQuoteRsp(void* pMdUserApi, CThostFtdcForQuoteRspField *pForQuoteRsp)
{
}
void __stdcall Account::OnRtnQuote(void* pTraderApi, CThostFtdcQuoteField *pQuote)
{
}