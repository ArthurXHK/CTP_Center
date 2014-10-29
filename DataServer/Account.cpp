#include "Account.h"

void *Account::md;//行情端口
void *Account::td; //用于获取交易合约的交易端口（非交易用）
void *Account::md_msgQueue; //专门用于行情队列
void *Account::td_msgQueue; //交易队列，交易账户集合用
map<void *, int> Account::m_tdposition; //交易账户映射
vector<void *> Account::v_tds; //交易账户集合
DBLog *Account::dblog; //日志对象
string Account::path; //con数据路径
string Account::brokerid; //期商代码
string Account::investor; //投资者代码
string Account::password; //密码
string Account::mdServer; //行情服务器地址
string Account::tdServer; //交易服务器地址
string Account::dbpath; //日志路径

bool Account::ConnectMdServer(const char *file, const char *servername)
{
    bool isconnected = true;
    //获取空间，绑定队列，注册回调
    
    md = MD_CreateMdApi();
    td = TD_CreateTdApi();
    md_msgQueue = CTP_CreateMsgQueue();
    td_msgQueue = CTP_CreateMsgQueue();
    CTP_RegAllCallback(md_msgQueue);
    CTP_RegAllCallback(td_msgQueue);
    MD_RegMsgQueue2MdApi(md, md_msgQueue);
    TD_RegMsgQueue2TdApi(td, md_msgQueue);
    CTP_StartMsgQueue(md_msgQueue);
    CTP_StartMsgQueue(td_msgQueue);
    dblog = NULL;

    //读取信息，处理连接
    ReadInifile(file, servername);
    AddLogPath(dbpath);
    MD_Connect(md, path.c_str(), mdServer.c_str(), brokerid.c_str(), investor.c_str(), password.c_str());
    TD_Connect(td, path.c_str(), tdServer.c_str(), brokerid.c_str(), investor.c_str(), password.c_str(), THOST_TERT_RESTART, "", "");
    if (TD_WaitForConnected(td))
    {
        dblog->PrintLog("交易端已经登录(行情端账户)");
    }
    if (MD_WaitForConnected(md))
    {
        dblog->PrintLog("行情端已经登录(行情端账户)");
    }
    v_tds.push_back(td);
    return isconnected;
}
int Account::CreateTdAccount(const char *file, const char *servername)
{
    int ind;
    if (0 == (ind = v_tds.size()))
        dblog->PrintLog("行情端未登陆", "error");
    else
    {
        ReadInifile(file, servername);
        void *ttd = TD_CreateTdApi();
        TD_RegMsgQueue2TdApi(ttd, td_msgQueue);
        m_tdposition[ttd] = ind;
        v_tds.push_back(ttd);

        TD_Connect(ttd, path.c_str(), tdServer.c_str(), brokerid.c_str(), investor.c_str(), password.c_str(), THOST_TERT_RESTART, "", "");
        bool ok = TD_WaitForConnected(ttd);
        if (ok) dblog->PrintLog(string("交易账户") + char(ind + '0') + string("连接成功"));
        else dblog->PrintLog(string("交易账户") + char(ind + '0') + string("连接失败"), "error");
        
    }
    return ind;
    
}
void Account::ReleaseAccount()
{
    TD_ReleaseTdApi(td);
    MD_ReleaseMdApi(md);
    int len = v_tds.size();
    for (int i = 1; i < len; ++i)
        TD_ReleaseTdApi(v_tds[i]);
    CTP_ReleaseMsgQueue(td_msgQueue);
    CTP_ReleaseMsgQueue(md_msgQueue);
    delete dblog;
    dblog = NULL;

}

string Account::GetPortMsg(void *port)
{
    string res;
    if (port == md)
        res = "行情端口(行情账户)";
    else if (port == td)
        res = "交易端口(行情账户)";
    else
    {
        int ind;
        if (ind = m_tdposition[port])
        {
            res = (string("交易账户[") + char(ind + '0')) + ']';
        }
        else
        {
            res = "没有这个交易账户";
        }
    }
    return res;
}
void Account::CTP_RegAllCallback(void *tmsgQueue)
{
    CTP_RegOnConnect(tmsgQueue, OnConnect);
    CTP_RegOnDisconnect(tmsgQueue, OnDisconnect);
    CTP_RegOnErrRtnOrderAction(tmsgQueue, OnErrRtnOrderAction);
    CTP_RegOnErrRtnOrderInsert(tmsgQueue, OnErrRtnOrderInsert);
    CTP_RegOnErrRtnQuoteAction(tmsgQueue, OnErrRtnQuoteAction);
    CTP_RegOnErrRtnQuoteInsert(tmsgQueue, OnErrRtnQuoteInsert);
    CTP_RegOnRspError(tmsgQueue, OnRspError);
    CTP_RegOnRspOrderAction(tmsgQueue, OnRspOrderAction);
    CTP_RegOnRspOrderInsert(tmsgQueue, OnRspOrderInsert);
    CTP_RegOnRspQryDepthMarketData(tmsgQueue, OnRspQryDepthMarketData);
    CTP_RegOnRspQryInstrument(tmsgQueue, OnRspQryInstrument);
    CTP_RegOnRspQryInstrumentCommissionRate(tmsgQueue, OnRspQryInstrumentCommissionRate);
    CTP_RegOnRspQryInstrumentMarginRate(tmsgQueue, OnRspQryInstrumentMarginRate);
    CTP_RegOnRspQryInvestorPosition(tmsgQueue, OnRspQryInvestorPosition);
    CTP_RegOnRspQryInvestorPositionDetail(tmsgQueue, OnRspQryInvestorPositionDetail);
    CTP_RegOnRspQryOrder(tmsgQueue, OnRspQryOrder);
    CTP_RegOnRspQryTrade(tmsgQueue, OnRspQryTrade);
    CTP_RegOnRspQrySettlementInfo(tmsgQueue, OnRspQrySettlementInfo);
    CTP_RegOnRspQryTradingAccount(tmsgQueue, OnRspQryTradingAccount);
    CTP_RegOnRtnDepthMarketData(tmsgQueue, OnRtnDepthMarketData);
    CTP_RegOnRtnForQuoteRsp(tmsgQueue, OnRtnForQuoteRsp);
    CTP_RegOnRtnInstrumentStatus(tmsgQueue, OnRtnInstrumentStatus);
    CTP_RegOnRtnOrder(tmsgQueue, OnRtnOrder);
    CTP_RegOnRtnQuote(tmsgQueue, OnRtnQuote);
    CTP_RegOnRtnTrade(tmsgQueue, OnRtnTrade);


}


void Account::ReadInifile(const char *file, const char *servername)
{
    char tmp[105];
    GetPrivateProfileStringA(servername, "streampath", "", tmp, sizeof(tmp), file);
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
    GetPrivateProfileStringA(servername, "dbpath", "", tmp, sizeof(tmp), file);
    dbpath = tmp;
}

void Account::AddLogPath(const string &dbpath)
{
    if (NULL == dblog)
        dblog = new DBLog(dbpath);
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


