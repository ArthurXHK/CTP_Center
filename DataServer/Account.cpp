#include "Account.h"

Account::Account()
{
    md = MD_CreateMdApi();
    td = TD_CreateTdApi();
    msgQueue = CTP_CreateMsgQueue();
    
    CTP_RegAllCallback();

    MD_RegMsgQueue2MdApi(md, msgQueue);
    TD_RegMsgQueue2TdApi(td, msgQueue);
    CTP_StartMsgQueue(msgQueue);
}
Account::~Account()
{
    MD_ReleaseMdApi(md);
    TD_ReleaseTdApi(td);
    CTP_ReleaseMsgQueue(msgQueue);
}

bool Account::WaitForConnected()
{
    bool res = true;
    if (TD_WaitForConnected(td))
    {
        cout << "td connected" << endl; 
    }
    else res = false;
    if (MD_WaitForConnected(md))
    {
        cout << "md connected" << endl;
    }
    else res = false;

    return res;
}
void Account::CTP_RegAllCallback()
{
    CTP_RegOnConnect(msgQueue, OnConnect);
    CTP_RegOnDisconnect(msgQueue, OnDisconnect);
    CTP_RegOnErrRtnOrderAction(msgQueue, OnErrRtnOrderAction);
    CTP_RegOnErrRtnOrderInsert(msgQueue, OnErrRtnOrderInsert);
    CTP_RegOnErrRtnQuoteAction(msgQueue, OnErrRtnQuoteAction);
    CTP_RegOnErrRtnQuoteInsert(msgQueue, OnErrRtnQuoteInsert);
    CTP_RegOnRspError(msgQueue, OnRspError);
    CTP_RegOnRspOrderAction(msgQueue, OnRspOrderAction);
    CTP_RegOnRspOrderInsert(msgQueue, OnRspOrderInsert);
    CTP_RegOnRspQryDepthMarketData(msgQueue, OnRspQryDepthMarketData);
    CTP_RegOnRspQryInstrument(msgQueue, OnRspQryInstrument);
    CTP_RegOnRspQryInstrumentCommissionRate(msgQueue, OnRspQryInstrumentCommissionRate);
    CTP_RegOnRspQryInstrumentMarginRate(msgQueue, OnRspQryInstrumentMarginRate);
    CTP_RegOnRspQryInvestorPosition(msgQueue, OnRspQryInvestorPosition);
    CTP_RegOnRspQryInvestorPositionDetail(msgQueue, OnRspQryInvestorPositionDetail);
    CTP_RegOnRspQryOrder(msgQueue, OnRspQryOrder);
    CTP_RegOnRspQryTrade(msgQueue, OnRspQryTrade);
    CTP_RegOnRspQrySettlementInfo(msgQueue, OnRspQrySettlementInfo);
    CTP_RegOnRspQryTradingAccount(msgQueue, OnRspQryTradingAccount);
    CTP_RegOnRtnDepthMarketData(msgQueue, OnRtnDepthMarketData);
    CTP_RegOnRtnForQuoteRsp(msgQueue, OnRtnForQuoteRsp);
    CTP_RegOnRtnInstrumentStatus(msgQueue, OnRtnInstrumentStatus);
    CTP_RegOnRtnOrder(msgQueue, OnRtnOrder);
    CTP_RegOnRtnQuote(msgQueue, OnRtnQuote);
    CTP_RegOnRtnTrade(msgQueue, OnRtnTrade);


}


void Account::ReadInifile(const char *file, const char *servername)
{
    char tmp[105];
    GetPrivateProfileStringA(servername, "path", "", tmp, sizeof(tmp), file);
    path = tmp;
    GetPrivateProfileStringA(servername, "mdserver", "", tmp, sizeof(tmp), file);
    mdServer = tmp;
    GetPrivateProfileStringA(servername, "tdserver", "", tmp, sizeof(tmp), file);
    tdServer = tmp;
    GetPrivateProfileStringA(servername, "brokerid", "", tmp, sizeof(tmp), file);
    brokerid = tmp;
    GetPrivateProfileStringA(servername, "investorid", "", tmp, sizeof(tmp), file);
    investor = tmp;
    GetPrivateProfileStringA(servername, "password", "", tmp, sizeof(tmp), file);
    password = tmp;

}

void Account::Connect()
{
    MD_Connect(md, path.c_str(), mdServer.c_str(), brokerid.c_str(), investor.c_str(), password.c_str());
    TD_Connect(td, path.c_str(), tdServer.c_str(), brokerid.c_str(), investor.c_str(), password.c_str(), THOST_TERT_RESTART, "", "");
}

void Account::Disconnect()
{
    MD_Disconnect(md);
    TD_Disconnect(td);
}

void Account::Subscribe(const char* instruments)
{
    MD_Subscribe(md, instruments, "");
}

void Account::Unsubscribe(const char* instruments)
{
    MD_Unsubscribe(md, instruments, "");
}


int Account::SendOrder(int OrderRef,
    const char* szInstrument,
    const char* szExchange,
    TThostFtdcDirectionType Direction,
    const char* szCombOffsetFlag,
    const char* szCombHedgeFlag,
    TThostFtdcVolumeType VolumeTotalOriginal,
    double LimitPrice,
    TThostFtdcOrderPriceTypeType OrderPriceType,
    TThostFtdcTimeConditionType TimeCondition,
    TThostFtdcContingentConditionType ContingentCondition,
    double StopPrice,
    TThostFtdcVolumeConditionType VolumeCondition)
{
    return TD_SendOrder(td, OrderRef, szInstrument, szExchange, Direction, szCombOffsetFlag, szCombHedgeFlag,
        VolumeTotalOriginal, LimitPrice, OrderPriceType, TimeCondition, ContingentCondition, StopPrice, VolumeCondition);
}


void Account::CancelOrder(CThostFtdcOrderField *pOrder)
{
    TD_CancelOrder(td, pOrder);
}


//查持仓
void Account::QryInvestorPosition(const char* szInstrumentId)
{
    TD_ReqQryInvestorPosition(td, szInstrumentId);
}

//查持仓明细
void Account::QryInvestorPositionDetail(const char* szInstrumentId)
{
    TD_ReqQryInvestorPositionDetail(td, szInstrumentId);
}

//查资金账号
void Account::QryTradingAccount()
{
    TD_ReqQryTradingAccount(td);
}

//查合约
void Account::QryInstrument(const char* szInstrumentId)
{
    TD_ReqQryInstrument(td, szInstrumentId);
}

//查手续费
void Account::QryInstrumentCommissionRate(const char* szInstrumentId)
{
    TD_ReqQryInstrumentCommissionRate(td, szInstrumentId);
}

//查保证金
void Account::QryInstrumentMarginRate(const char* szInstrumentId, TThostFtdcHedgeFlagType HedgeFlag)
{
    TD_ReqQryInstrumentMarginRate(td, szInstrumentId, HedgeFlag);
}

//查深度行情
void Account::QryDepthMarketData(const char* szInstrumentId)
{
    TD_ReqQryDepthMarketData(td, szInstrumentId);
}

//请求查询投资者结算结果
void Account::QrySettlementInfo(const char* szTradingDay)
{
    TD_ReqQrySettlementInfo(td, szTradingDay);
}
