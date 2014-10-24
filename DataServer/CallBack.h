#ifndef CALLBACK_H
#define CALLBACK_H

#include "QuantBox.C2CTP.h"

#include <iostream>
#include <Windows.h>
using namespace std;

//连接回报信息
static void __stdcall OnConnect(void* pApi, CThostFtdcRspUserLoginField *pRspUserLogin, ConnectionStatus result)
{
    

}

//断开连接回报信息
static void __stdcall OnDisconnect(void* pApi, CThostFtdcRspInfoField *pRspInfo, ConnectionStatus step)
{
    cout << pRspInfo->ErrorMsg << endl;
}

//撤单错误信息
static void __stdcall OnErrRtnOrderAction(void* pTraderApi, CThostFtdcOrderActionField *pOrderAction, CThostFtdcRspInfoField *pRspInfo)
{
    cout << pRspInfo->ErrorMsg << endl;
}

 //下单错误信息
static void __stdcall OnErrRtnOrderInsert(void* pTraderApi, CThostFtdcInputOrderField *pInputOrder, CThostFtdcRspInfoField *pRspInfo)
{
    cout << pRspInfo->ErrorMsg << endl;
}

 
static void __stdcall OnErrRtnQuoteAction(void* pTraderApi, CThostFtdcQuoteActionField *pQuoteAction, CThostFtdcRspInfoField *pRspInfo)
{
}

static void __stdcall OnErrRtnQuoteInsert(void* pTraderApi, CThostFtdcInputQuoteField *pInputQuote, CThostFtdcRspInfoField *pRspInfo)
{
}

 //错误信息
static void __stdcall OnRspError(void* pApi, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
{
    cout << pRspInfo->ErrorMsg << endl;
}

 //撤单回报
static void __stdcall OnRspOrderAction(void* pTraderApi, CThostFtdcInputOrderActionField *pInputOrderAction, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
{
    cout << pRspInfo->ErrorMsg << endl;
}

//下单回报
static void __stdcall OnRspOrderInsert(void* pTraderApi, CThostFtdcInputOrderField *pInputOrder, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
{
    cout << pRspInfo->ErrorMsg << endl;
}

 //查询深度行情回报
static void __stdcall OnRspQryDepthMarketData(void* pTraderApi, CThostFtdcDepthMarketDataField *pDepthMarketData, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
{
}

 //查询合约回报
static void __stdcall OnRspQryInstrument(void* pTraderApi, CThostFtdcInstrumentField *pInstrument, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
{
    cout << pInstrument->InstrumentID << endl;
}

 //查询合约手续费率回报
static void __stdcall OnRspQryInstrumentCommissionRate(void* pTraderApi, CThostFtdcInstrumentCommissionRateField *pInstrumentCommissionRate, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
{
}

 //查询合约保证金率回报
static void __stdcall OnRspQryInstrumentMarginRate(void* pTraderApi, CThostFtdcInstrumentMarginRateField *pInstrumentMarginRate, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
{
    cout << pInstrumentMarginRate->LongMarginRatioByMoney << endl;
}

 //查询投资者持仓回报
static void __stdcall OnRspQryInvestorPosition(void* pTraderApi, CThostFtdcInvestorPositionField *pInvestorPosition, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
{
    cout << pInvestorPosition->CloseProfit << endl;
}

 //查询持仓详细回报
static void __stdcall OnRspQryInvestorPositionDetail(void* pTraderApi, CThostFtdcInvestorPositionDetailField *pInvestorPositionDetail, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
{
}

 //查询订单回报
static void __stdcall OnRspQryOrder(void* pTraderApi, CThostFtdcOrderField *pOrder, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
{
}

 //查询成交回报
static void __stdcall OnRspQryTrade(void* pTraderApi, CThostFtdcTradeField *pTrade, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
{
}

 //查询投资者结算回报
static void __stdcall OnRspQrySettlementInfo(void* pTraderApi, CThostFtdcSettlementInfoField *pSettlementInfo, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
{
}

 //查询资金账户回报
static void __stdcall OnRspQryTradingAccount(void* pTraderApi, CThostFtdcTradingAccountField *pTradingAccount, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
{
    cout << pTradingAccount->AccountID << endl;
    cout << pTradingAccount->Available << endl;
    cout << pTradingAccount->Deposit << endl;
    cout << pRspInfo->ErrorMsg << endl;
}

 //深度行情回报
static void __stdcall OnRtnDepthMarketData(void* pMdUserApi, CThostFtdcDepthMarketDataField *pDepthMarketData)
{
    cout << pDepthMarketData->InstrumentID << endl;
    cout << pDepthMarketData->LastPrice << endl;
}

 //合约状态回报
static void __stdcall OnRtnInstrumentStatus(void* pTraderApi, CThostFtdcInstrumentStatusField *pInstrumentStatus)
{
     
}

 //报单回报
static void __stdcall OnRtnOrder(void* pTraderApi, CThostFtdcOrderField *pOrder)
{
    cout << pOrder->StatusMsg << endl;
}

//成交回报
static void __stdcall OnRtnTrade(void* pTraderApi, CThostFtdcTradeField *pTrade)
{
}


 //其他回调
static void __stdcall OnRspQuoteAction(void* pTraderApi, CThostFtdcInputQuoteActionField *pInputQuoteAction, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
 {
 }
static void __stdcall OnRspQuoteInsert(void* pTraderApi, CThostFtdcInputQuoteField *pInputQuote, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
 {
 }
static void __stdcall OnRtnForQuoteRsp(void* pMdUserApi, CThostFtdcForQuoteRspField *pForQuoteRsp)
 {
 }
static void __stdcall OnRtnQuote(void* pTraderApi, CThostFtdcQuoteField *pQuote)
 {
 }
#endif