#include "Account.h"

//----------------CallBack--------------------

//�������ر�
void __stdcall Account::OnRtnDepthMarketData(void* pMdUserApi, CThostFtdcDepthMarketDataField *pDepthMarketData)
{
    cout << pDepthMarketData->InstrumentID << endl;
    cout << pDepthMarketData->LastPrice << endl;
}

//���ӻر���Ϣ
void __stdcall Account::OnConnect(void* pApi, CThostFtdcRspUserLoginField *pRspUserLogin, ConnectionStatus result)
{
     dblog->PrintLog(GetPortMsg(pApi) +string("-->") + ConnectionStatusMsg(result));
}

//�Ͽ����ӻر���Ϣ
void __stdcall Account::OnDisconnect(void* pApi, CThostFtdcRspInfoField *pRspInfo, ConnectionStatus step)
{
    dblog->PrintLog(GetPortMsg(pApi) + string("-->") + ConnectionStatusMsg(step));
}

//����������Ϣ
void __stdcall Account::OnErrRtnOrderAction(void* pTraderApi, CThostFtdcOrderActionField *pOrderAction, CThostFtdcRspInfoField *pRspInfo)
{
    dblog->PrintLog(GetPortMsg(pTraderApi) + ": " + pRspInfo->ErrorMsg, "error");
}

//�µ�������Ϣ
void __stdcall Account::OnErrRtnOrderInsert(void* pTraderApi, CThostFtdcInputOrderField *pInputOrder, CThostFtdcRspInfoField *pRspInfo)
{
    dblog->PrintLog(GetPortMsg(pTraderApi) + ": " + pRspInfo->ErrorMsg, "error");
}


void __stdcall Account::OnErrRtnQuoteAction(void* pTraderApi, CThostFtdcQuoteActionField *pQuoteAction, CThostFtdcRspInfoField *pRspInfo)
{
    dblog->PrintLog(GetPortMsg(pTraderApi) + ": " + pRspInfo->ErrorMsg, "error");
}

void __stdcall Account::OnErrRtnQuoteInsert(void* pTraderApi, CThostFtdcInputQuoteField *pInputQuote, CThostFtdcRspInfoField *pRspInfo)
{
    dblog->PrintLog(GetPortMsg(pTraderApi) + ": " + pRspInfo->ErrorMsg, "error");
}

//������Ϣ
void __stdcall Account::OnRspError(void* pApi, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
{
    dblog->PrintLog(GetPortMsg(pApi) + ": " + pRspInfo->ErrorMsg, "error");
}

//�����ر�
void __stdcall Account::OnRspOrderAction(void* pTraderApi, CThostFtdcInputOrderActionField *pInputOrderAction, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
{
    if (pRspInfo->ErrorID)
        dblog->PrintLog(GetPortMsg(pTraderApi) + ": " + pRspInfo->ErrorMsg, "error");
}

//�µ��ر�
void __stdcall Account::OnRspOrderInsert(void* pTraderApi, CThostFtdcInputOrderField *pInputOrder, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
{
    if (pRspInfo->ErrorID)
        dblog->PrintLog(GetPortMsg(pTraderApi) + ": " + pRspInfo->ErrorMsg, "error");
}

//��ѯ�������ر�
void __stdcall Account::OnRspQryDepthMarketData(void* pTraderApi, CThostFtdcDepthMarketDataField *pDepthMarketData, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
{
    if (pRspInfo->ErrorID)
        dblog->PrintLog(GetPortMsg(pTraderApi) + ": " + pRspInfo->ErrorMsg, "error");
}

//��ѯ��Լ�ر�
void __stdcall Account::OnRspQryInstrument(void* pTraderApi, CThostFtdcInstrumentField *pInstrument, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
{
    if (pRspInfo->ErrorID)
        dblog->PrintLog(GetPortMsg(pTraderApi) + ": " + pRspInfo->ErrorMsg, "error");
}

//��ѯ��Լ�������ʻر�
void __stdcall Account::OnRspQryInstrumentCommissionRate(void* pTraderApi, CThostFtdcInstrumentCommissionRateField *pInstrumentCommissionRate, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
{
    if (pRspInfo->ErrorID)
        dblog->PrintLog(GetPortMsg(pTraderApi) + ": " + pRspInfo->ErrorMsg, "error");
}

//��ѯ��Լ��֤���ʻر�
void __stdcall Account::OnRspQryInstrumentMarginRate(void* pTraderApi, CThostFtdcInstrumentMarginRateField *pInstrumentMarginRate, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
{
    if (pRspInfo->ErrorID)
        dblog->PrintLog(GetPortMsg(pTraderApi) + ": " + pRspInfo->ErrorMsg, "error");
}

//��ѯͶ���ֲֻ߳ر�
void __stdcall Account::OnRspQryInvestorPosition(void* pTraderApi, CThostFtdcInvestorPositionField *pInvestorPosition, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
{
    if (pRspInfo->ErrorID)
        dblog->PrintLog(GetPortMsg(pTraderApi) + ": " + pRspInfo->ErrorMsg, "error");
}

//��ѯ�ֲ���ϸ�ر�
void __stdcall Account::OnRspQryInvestorPositionDetail(void* pTraderApi, CThostFtdcInvestorPositionDetailField *pInvestorPositionDetail, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
{
    if (pRspInfo->ErrorID)
        dblog->PrintLog(GetPortMsg(pTraderApi) + ": " + pRspInfo->ErrorMsg, "error");
}

//��ѯ�����ر�
void __stdcall Account::OnRspQryOrder(void* pTraderApi, CThostFtdcOrderField *pOrder, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
{
    if (pRspInfo->ErrorID)
        dblog->PrintLog(GetPortMsg(pTraderApi) + ": " + pRspInfo->ErrorMsg, "error");
}

//��ѯ�ɽ��ر�
void __stdcall Account::OnRspQryTrade(void* pTraderApi, CThostFtdcTradeField *pTrade, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
{
    if (pRspInfo->ErrorID)
        dblog->PrintLog(GetPortMsg(pTraderApi) + ": " + pRspInfo->ErrorMsg, "error");
}

//��ѯͶ���߽���ر�
void __stdcall Account::OnRspQrySettlementInfo(void* pTraderApi, CThostFtdcSettlementInfoField *pSettlementInfo, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
{
    if (pRspInfo->ErrorID)
        dblog->PrintLog(GetPortMsg(pTraderApi) + ": " + pRspInfo->ErrorMsg, "error");
}

//��ѯ�ʽ��˻��ر�
void __stdcall Account::OnRspQryTradingAccount(void* pTraderApi, CThostFtdcTradingAccountField *pTradingAccount, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
{
    if (pRspInfo->ErrorID)
        dblog->PrintLog(GetPortMsg(pTraderApi) + ": " + pRspInfo->ErrorMsg, "error");
}

//��Լ״̬�ر�
void __stdcall Account::OnRtnInstrumentStatus(void* pTraderApi, CThostFtdcInstrumentStatusField *pInstrumentStatus)
{

}

//�����ر�
void __stdcall Account::OnRtnOrder(void* pTraderApi, CThostFtdcOrderField *pOrder)
{

}

//�ɽ��ر�
void __stdcall Account::OnRtnTrade(void* pTraderApi, CThostFtdcTradeField *pTrade)
{
}


//�����ص�
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
