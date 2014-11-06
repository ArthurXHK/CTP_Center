#include "Trader.h"

//----------------CallBack--------------------

//�������ر�
void __stdcall Trader::OnRtnDepthMarketData(void* pMdUserApi, CThostFtdcDepthMarketDataField *pDepthMarketData)
{

}

//���ӻر���Ϣ
void __stdcall Trader::OnConnect(void* pApi, CThostFtdcRspUserLoginField *pRspUserLogin, ConnectionStatus result)
{
     PrintLog(GetPortMsg(pApi) +string("-->") + ConnectionStatusMsg(result));
}

//�Ͽ����ӻر���Ϣ
void __stdcall Trader::OnDisconnect(void* pApi, CThostFtdcRspInfoField *pRspInfo, ConnectionStatus step)
{
    PrintLog(GetPortMsg(pApi) + string("-->") + ConnectionStatusMsg(step));
}

//����������Ϣ
void __stdcall Trader::OnErrRtnOrderAction(void* pTraderApi, CThostFtdcOrderActionField *pOrderAction, CThostFtdcRspInfoField *pRspInfo)
{
    PrintLog(GetPortMsg(pTraderApi) + ": " + pRspInfo->ErrorMsg, "error");
}

//�µ�������Ϣ
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

//������Ϣ
void __stdcall Trader::OnRspError(void* pApi, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
{
    PrintLog(GetPortMsg(pApi) + ": " + pRspInfo->ErrorMsg, "error");
}

//�����ر�
void __stdcall Trader::OnRspOrderAction(void* pTraderApi, CThostFtdcInputOrderActionField *pInputOrderAction, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
{
    if (pRspInfo->ErrorID)
        PrintLog(GetPortMsg(pTraderApi) + ": " + pRspInfo->ErrorMsg, "error");
}

//�µ��ر�
void __stdcall Trader::OnRspOrderInsert(void* pTraderApi, CThostFtdcInputOrderField *pInputOrder, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
{
    if (pRspInfo->ErrorID)
        PrintLog(GetPortMsg(pTraderApi) + ": " + pRspInfo->ErrorMsg, "error");
}

//��ѯ�������ر�
void __stdcall Trader::OnRspQryDepthMarketData(void* pTraderApi, CThostFtdcDepthMarketDataField *pDepthMarketData, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
{
    if (pRspInfo->ErrorID)
        PrintLog(GetPortMsg(pTraderApi) + ": " + pRspInfo->ErrorMsg, "error");
}

//��ѯ��Լ�ر�
void __stdcall Trader::OnRspQryInstrument(void* pTraderApi, CThostFtdcInstrumentField *pInstrument, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
{
    if (pRspInfo->ErrorID)
        PrintLog(GetPortMsg(pTraderApi) + ": " + pRspInfo->ErrorMsg, "error");
}

//��ѯ��Լ�������ʻر�
void __stdcall Trader::OnRspQryInstrumentCommissionRate(void* pTraderApi, CThostFtdcInstrumentCommissionRateField *pInstrumentCommissionRate, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
{
    if (pRspInfo->ErrorID)
        PrintLog(GetPortMsg(pTraderApi) + ": " + pRspInfo->ErrorMsg, "error");
}

//��ѯ��Լ��֤���ʻر�
void __stdcall Trader::OnRspQryInstrumentMarginRate(void* pTraderApi, CThostFtdcInstrumentMarginRateField *pInstrumentMarginRate, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
{
    if (pRspInfo->ErrorID)
        PrintLog(GetPortMsg(pTraderApi) + ": " + pRspInfo->ErrorMsg, "error");
}

//��ѯͶ���ֲֻ߳ر�
void __stdcall Trader::OnRspQryInvestorPosition(void* pTraderApi, CThostFtdcInvestorPositionField *pInvestorPosition, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
{
    if (pRspInfo->ErrorID)
        PrintLog(GetPortMsg(pTraderApi) + ": " + pRspInfo->ErrorMsg, "error");
}

//��ѯ�ֲ���ϸ�ر�
void __stdcall Trader::OnRspQryInvestorPositionDetail(void* pTraderApi, CThostFtdcInvestorPositionDetailField *pInvestorPositionDetail, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
{
    if (pRspInfo->ErrorID)
        PrintLog(GetPortMsg(pTraderApi) + ": " + pRspInfo->ErrorMsg, "error");
}

//��ѯ�����ر�
void __stdcall Trader::OnRspQryOrder(void* pTraderApi, CThostFtdcOrderField *pOrder, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
{
    if (pRspInfo->ErrorID)
        PrintLog(GetPortMsg(pTraderApi) + ": " + pRspInfo->ErrorMsg, "error");
}

//��ѯ�ɽ��ر�
void __stdcall Trader::OnRspQryTrade(void* pTraderApi, CThostFtdcTradeField *pTrade, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
{
    if (pRspInfo->ErrorID)
        PrintLog(GetPortMsg(pTraderApi) + ": " + pRspInfo->ErrorMsg, "error");
}

//��ѯͶ���߽���ر�
void __stdcall Trader::OnRspQrySettlementInfo(void* pTraderApi, CThostFtdcSettlementInfoField *pSettlementInfo, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
{
    if (pRspInfo->ErrorID)
        PrintLog(GetPortMsg(pTraderApi) + ": " + pRspInfo->ErrorMsg, "error");
}

//��ѯ�ʽ��˻��ر�
void __stdcall Trader::OnRspQryTradingAccount(void* pTraderApi, CThostFtdcTradingAccountField *pTradingAccount, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
{
    if (pRspInfo->ErrorID)
        PrintLog(GetPortMsg(pTraderApi) + ": " + pRspInfo->ErrorMsg, "error");
}

//��Լ״̬�ر�
void __stdcall Trader::OnRtnInstrumentStatus(void* pTraderApi, CThostFtdcInstrumentStatusField *pInstrumentStatus)
{

}

//�����ر�
void __stdcall Trader::OnRtnOrder(void* pTraderApi, CThostFtdcOrderField *pOrder)
{

}

//�ɽ��ر�
void __stdcall Trader::OnRtnTrade(void* pTraderApi, CThostFtdcTradeField *pTrade)
{
}


//�����ص�
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
