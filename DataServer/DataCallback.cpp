#include "DataServer.h"

//----------------CallBack--------------------

//�������ر�
void __stdcall DataServer::OnRtnDepthMarketData(void* pMdUserApi, CThostFtdcDepthMarketDataField *pDepthMarketData)
{

}

//���ӻر���Ϣ
void __stdcall DataServer::OnConnect(void* pApi, CThostFtdcRspUserLoginField *pRspUserLogin, ConnectionStatus result)
{
     dblog->PrintLog(GetPortMsg(pApi) +string("-->") + ConnectionStatusMsg(result));
}

//�Ͽ����ӻر���Ϣ
void __stdcall DataServer::OnDisconnect(void* pApi, CThostFtdcRspInfoField *pRspInfo, ConnectionStatus step)
{
    dblog->PrintLog(GetPortMsg(pApi) + string("-->") + ConnectionStatusMsg(step));
}


//������Ϣ
void __stdcall DataServer::OnRspError(void* pApi, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
{
    dblog->PrintLog(GetPortMsg(pApi) + ": " + pRspInfo->ErrorMsg, "error");
}

//��Լ״̬�ر�
void __stdcall DataServer::OnRtnInstrumentStatus(void* pTraderApi, CThostFtdcInstrumentStatusField *pInstrumentStatus)
{

}
