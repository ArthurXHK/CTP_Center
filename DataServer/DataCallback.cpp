#include "DataServer.h"

//----------------CallBack--------------------

//深度行情回报
void __stdcall DataServer::OnRtnDepthMarketData(void* pMdUserApi, CThostFtdcDepthMarketDataField *pDepthMarketData)
{

}

//连接回报信息
void __stdcall DataServer::OnConnect(void* pApi, CThostFtdcRspUserLoginField *pRspUserLogin, ConnectionStatus result)
{
     dblog->PrintLog(GetPortMsg(pApi) +string("-->") + ConnectionStatusMsg(result));
}

//断开连接回报信息
void __stdcall DataServer::OnDisconnect(void* pApi, CThostFtdcRspInfoField *pRspInfo, ConnectionStatus step)
{
    dblog->PrintLog(GetPortMsg(pApi) + string("-->") + ConnectionStatusMsg(step));
}


//错误信息
void __stdcall DataServer::OnRspError(void* pApi, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
{
    dblog->PrintLog(GetPortMsg(pApi) + ": " + pRspInfo->ErrorMsg, "error");
}

//合约状态回报
void __stdcall DataServer::OnRtnInstrumentStatus(void* pTraderApi, CThostFtdcInstrumentStatusField *pInstrumentStatus)
{

}
