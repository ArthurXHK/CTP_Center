#include "Account.h"

void *Account::md;//����˿�
void *Account::td; //���ڻ�ȡ���׺�Լ�Ľ��׶˿ڣ��ǽ����ã�
void *Account::md_msgQueue; //ר�������������
void *Account::td_msgQueue; //���׶��У������˻�������
map<void *, int> Account::m_tdposition; //�����˻�ӳ��
vector<void *> Account::v_tds; //�����˻�����
DBLog *Account::dblog; //��־����
string Account::path; //con����·��
string Account::brokerid; //���̴���
string Account::investor; //Ͷ���ߴ���
string Account::password; //����
string Account::mdServer; //�����������ַ
string Account::tdServer; //���׷�������ַ
string Account::dbpath; //��־·��

bool Account::ConnectMdServer(const char *file, const char *servername)
{
    bool isconnected = true;
    //��ȡ�ռ䣬�󶨶��У�ע��ص�
    
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

    //��ȡ��Ϣ����������
    ReadInifile(file, servername);
    AddLogPath(dbpath);
    MD_Connect(md, path.c_str(), mdServer.c_str(), brokerid.c_str(), investor.c_str(), password.c_str());
    TD_Connect(td, path.c_str(), tdServer.c_str(), brokerid.c_str(), investor.c_str(), password.c_str(), THOST_TERT_RESTART, "", "");
    if (TD_WaitForConnected(td))
    {
        dblog->PrintLog("���׶��Ѿ���¼(������˻�)");
    }
    if (MD_WaitForConnected(md))
    {
        dblog->PrintLog("������Ѿ���¼(������˻�)");
    }
    v_tds.push_back(td);
    return isconnected;
}
int Account::CreateTdAccount(const char *file, const char *servername)
{
    int ind;
    if (0 == (ind = v_tds.size()))
        dblog->PrintLog("�����δ��½", "error");
    else
    {
        ReadInifile(file, servername);
        void *ttd = TD_CreateTdApi();
        TD_RegMsgQueue2TdApi(ttd, td_msgQueue);
        m_tdposition[ttd] = ind;
        v_tds.push_back(ttd);

        TD_Connect(ttd, path.c_str(), tdServer.c_str(), brokerid.c_str(), investor.c_str(), password.c_str(), THOST_TERT_RESTART, "", "");
        bool ok = TD_WaitForConnected(ttd);
        if (ok) dblog->PrintLog(string("�����˻�") + char(ind + '0') + string("���ӳɹ�"));
        else dblog->PrintLog(string("�����˻�") + char(ind + '0') + string("����ʧ��"), "error");
        
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
        res = "����˿�(�����˻�)";
    else if (port == td)
        res = "���׶˿�(�����˻�)";
    else
    {
        int ind;
        if (ind = m_tdposition[port])
        {
            res = (string("�����˻�[") + char(ind + '0')) + ']';
        }
        else
        {
            res = "û����������˻�";
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


//��ֲ�
void Account::QryInvestorPosition(const char* szInstrumentId)
{
    TD_ReqQryInvestorPosition(td, szInstrumentId);
}

//��ֲ���ϸ
void Account::QryInvestorPositionDetail(const char* szInstrumentId)
{
    TD_ReqQryInvestorPositionDetail(td, szInstrumentId);
}

//���ʽ��˺�
void Account::QryTradingAccount()
{
    TD_ReqQryTradingAccount(td);
}

//���Լ
void Account::QryInstrument(const char* szInstrumentId)
{
    TD_ReqQryInstrument(td, szInstrumentId);
}

//��������
void Account::QryInstrumentCommissionRate(const char* szInstrumentId)
{
    TD_ReqQryInstrumentCommissionRate(td, szInstrumentId);
}

//�鱣֤��
void Account::QryInstrumentMarginRate(const char* szInstrumentId, TThostFtdcHedgeFlagType HedgeFlag)
{
    TD_ReqQryInstrumentMarginRate(td, szInstrumentId, HedgeFlag);
}

//���������
void Account::QryDepthMarketData(const char* szInstrumentId)
{
    TD_ReqQryDepthMarketData(td, szInstrumentId);
}

//�����ѯͶ���߽�����
void Account::QrySettlementInfo(const char* szTradingDay)
{
    TD_ReqQrySettlementInfo(td, szTradingDay);
}


