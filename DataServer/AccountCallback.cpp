#include "Account.h"

//----------------CallBack--------------------

//���ӻر���Ϣ
void __stdcall Account::OnConnect(void* pApi, CThostFtdcRspUserLoginField *pRspUserLogin, ConnectionStatus result)
{
     dblog->PrintLog(GetPortMsg(pApi) +string("-->") + ConnectionStatusMsg(result));
}

//�Ͽ����ӻر���Ϣ
void __stdcall Account::OnDisconnect(void* pApi, CThostFtdcRspInfoField *pRspInfo, ConnectionStatus step)
{
    cout << pRspInfo->ErrorMsg << endl;
}

//����������Ϣ
void __stdcall Account::OnErrRtnOrderAction(void* pTraderApi, CThostFtdcOrderActionField *pOrderAction, CThostFtdcRspInfoField *pRspInfo)
{
    cout << pRspInfo->ErrorMsg << endl;
}

//�µ�������Ϣ
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

//������Ϣ
void __stdcall Account::OnRspError(void* pApi, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
{
    cout << pRspInfo->ErrorMsg << endl;
}

//�����ر�
void __stdcall Account::OnRspOrderAction(void* pTraderApi, CThostFtdcInputOrderActionField *pInputOrderAction, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
{
    cout << pRspInfo->ErrorMsg << endl;
}

//�µ��ر�
void __stdcall Account::OnRspOrderInsert(void* pTraderApi, CThostFtdcInputOrderField *pInputOrder, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
{
    cout << pRspInfo->ErrorMsg << endl;
}

//��ѯ�������ر�
void __stdcall Account::OnRspQryDepthMarketData(void* pTraderApi, CThostFtdcDepthMarketDataField *pDepthMarketData, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
{
}

//��ѯ��Լ�ر�
void __stdcall Account::OnRspQryInstrument(void* pTraderApi, CThostFtdcInstrumentField *pInstrument, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
{
    cout << pInstrument->InstrumentID << endl;
}

//��ѯ��Լ�������ʻر�
void __stdcall Account::OnRspQryInstrumentCommissionRate(void* pTraderApi, CThostFtdcInstrumentCommissionRateField *pInstrumentCommissionRate, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
{
}

//��ѯ��Լ��֤���ʻر�
void __stdcall Account::OnRspQryInstrumentMarginRate(void* pTraderApi, CThostFtdcInstrumentMarginRateField *pInstrumentMarginRate, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
{
    cout << pInstrumentMarginRate->LongMarginRatioByMoney << endl;
}

//��ѯͶ���ֲֻ߳ر�
void __stdcall Account::OnRspQryInvestorPosition(void* pTraderApi, CThostFtdcInvestorPositionField *pInvestorPosition, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
{
    cout << pInvestorPosition->CloseProfit << endl;
}

//��ѯ�ֲ���ϸ�ر�
void __stdcall Account::OnRspQryInvestorPositionDetail(void* pTraderApi, CThostFtdcInvestorPositionDetailField *pInvestorPositionDetail, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
{
}

//��ѯ�����ر�
void __stdcall Account::OnRspQryOrder(void* pTraderApi, CThostFtdcOrderField *pOrder, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
{
}

//��ѯ�ɽ��ر�
void __stdcall Account::OnRspQryTrade(void* pTraderApi, CThostFtdcTradeField *pTrade, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
{
}

//��ѯͶ���߽���ر�
void __stdcall Account::OnRspQrySettlementInfo(void* pTraderApi, CThostFtdcSettlementInfoField *pSettlementInfo, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
{
}

//��ѯ�ʽ��˻��ر�
void __stdcall Account::OnRspQryTradingAccount(void* pTraderApi, CThostFtdcTradingAccountField *pTradingAccount, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
{
    cout << pTradingAccount->AccountID << endl;
    cout << pTradingAccount->Available << endl;
    cout << pTradingAccount->Deposit << endl;
    cout << pRspInfo->ErrorMsg << endl;
}

//�������ر�
void __stdcall Account::OnRtnDepthMarketData(void* pMdUserApi, CThostFtdcDepthMarketDataField *pDepthMarketData)
{
    cout << pDepthMarketData->InstrumentID << endl;
    cout << pDepthMarketData->LastPrice << endl;
}

//��Լ״̬�ر�
void __stdcall Account::OnRtnInstrumentStatus(void* pTraderApi, CThostFtdcInstrumentStatusField *pInstrumentStatus)
{

}

//�����ر�
void __stdcall Account::OnRtnOrder(void* pTraderApi, CThostFtdcOrderField *pOrder)
{
    cout << pOrder->StatusMsg << endl;
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