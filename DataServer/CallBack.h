#ifndef CALLBACK_H
#define CALLBACK_H

#include "QuantBox.C2CTP.h"

#include <iostream>
#include <Windows.h>
using namespace std;

//���ӻر���Ϣ
static void __stdcall OnConnect(void* pApi, CThostFtdcRspUserLoginField *pRspUserLogin, ConnectionStatus result)
{
    

}

//�Ͽ����ӻر���Ϣ
static void __stdcall OnDisconnect(void* pApi, CThostFtdcRspInfoField *pRspInfo, ConnectionStatus step)
{
    cout << pRspInfo->ErrorMsg << endl;
}

//����������Ϣ
static void __stdcall OnErrRtnOrderAction(void* pTraderApi, CThostFtdcOrderActionField *pOrderAction, CThostFtdcRspInfoField *pRspInfo)
{
    cout << pRspInfo->ErrorMsg << endl;
}

 //�µ�������Ϣ
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

 //������Ϣ
static void __stdcall OnRspError(void* pApi, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
{
    cout << pRspInfo->ErrorMsg << endl;
}

 //�����ر�
static void __stdcall OnRspOrderAction(void* pTraderApi, CThostFtdcInputOrderActionField *pInputOrderAction, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
{
    cout << pRspInfo->ErrorMsg << endl;
}

//�µ��ر�
static void __stdcall OnRspOrderInsert(void* pTraderApi, CThostFtdcInputOrderField *pInputOrder, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
{
    cout << pRspInfo->ErrorMsg << endl;
}

 //��ѯ�������ر�
static void __stdcall OnRspQryDepthMarketData(void* pTraderApi, CThostFtdcDepthMarketDataField *pDepthMarketData, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
{
}

 //��ѯ��Լ�ر�
static void __stdcall OnRspQryInstrument(void* pTraderApi, CThostFtdcInstrumentField *pInstrument, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
{
    cout << pInstrument->InstrumentID << endl;
}

 //��ѯ��Լ�������ʻر�
static void __stdcall OnRspQryInstrumentCommissionRate(void* pTraderApi, CThostFtdcInstrumentCommissionRateField *pInstrumentCommissionRate, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
{
}

 //��ѯ��Լ��֤���ʻر�
static void __stdcall OnRspQryInstrumentMarginRate(void* pTraderApi, CThostFtdcInstrumentMarginRateField *pInstrumentMarginRate, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
{
    cout << pInstrumentMarginRate->LongMarginRatioByMoney << endl;
}

 //��ѯͶ���ֲֻ߳ر�
static void __stdcall OnRspQryInvestorPosition(void* pTraderApi, CThostFtdcInvestorPositionField *pInvestorPosition, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
{
    cout << pInvestorPosition->CloseProfit << endl;
}

 //��ѯ�ֲ���ϸ�ر�
static void __stdcall OnRspQryInvestorPositionDetail(void* pTraderApi, CThostFtdcInvestorPositionDetailField *pInvestorPositionDetail, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
{
}

 //��ѯ�����ر�
static void __stdcall OnRspQryOrder(void* pTraderApi, CThostFtdcOrderField *pOrder, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
{
}

 //��ѯ�ɽ��ر�
static void __stdcall OnRspQryTrade(void* pTraderApi, CThostFtdcTradeField *pTrade, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
{
}

 //��ѯͶ���߽���ر�
static void __stdcall OnRspQrySettlementInfo(void* pTraderApi, CThostFtdcSettlementInfoField *pSettlementInfo, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
{
}

 //��ѯ�ʽ��˻��ر�
static void __stdcall OnRspQryTradingAccount(void* pTraderApi, CThostFtdcTradingAccountField *pTradingAccount, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
{
    cout << pTradingAccount->AccountID << endl;
    cout << pTradingAccount->Available << endl;
    cout << pTradingAccount->Deposit << endl;
    cout << pRspInfo->ErrorMsg << endl;
}

 //�������ر�
static void __stdcall OnRtnDepthMarketData(void* pMdUserApi, CThostFtdcDepthMarketDataField *pDepthMarketData)
{
    cout << pDepthMarketData->InstrumentID << endl;
    cout << pDepthMarketData->LastPrice << endl;
}

 //��Լ״̬�ر�
static void __stdcall OnRtnInstrumentStatus(void* pTraderApi, CThostFtdcInstrumentStatusField *pInstrumentStatus)
{
     
}

 //�����ر�
static void __stdcall OnRtnOrder(void* pTraderApi, CThostFtdcOrderField *pOrder)
{
    cout << pOrder->StatusMsg << endl;
}

//�ɽ��ر�
static void __stdcall OnRtnTrade(void* pTraderApi, CThostFtdcTradeField *pTrade)
{
}


 //�����ص�
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