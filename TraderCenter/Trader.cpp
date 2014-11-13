#include "Trader.h"

void *Trader::md;//����˿�
void *Trader::td; //���ڻ�ȡ���׺�Լ�Ľ��׶˿ڣ��ǽ����ã�
void *Trader::pmd, *Trader::ptd;
void *Trader::md_msgQueue; //ר�������������
void *Trader::td_msgQueue; //���׶��У������˻�������
map<void *, int> Trader::m_tdposition; //�����˻�ӳ��
vector<void *> Trader::v_tds; //�����˻�����
DBLog Trader::dblog; //��־����
string Trader::path; //con����·��
string Trader::brokerid; //���̴���
string Trader::investor; //Ͷ���ߴ���
string Trader::password; //����
string Trader::mdServer; //�����������ַ
string Trader::tdServer; //���׷�������ַ
string Trader::logpath; //��־·��
mutex Trader::csLog;

void Trader::PrintLog(string msg, string type)
{
    dblog.PrintLog(msg, type);
}
bool Trader::ConnectMdServer(const char *file, const char *servername)
{
    //��ȡ�ռ䣬�󶨶��У�ע��ص�
    if (md != NULL || td != NULL)
    {
        PrintLog("������Ѿ�����", "error");
        return false;
    }
    md = MD_CreateMdApi();
    pmd = md;
    td = TD_CreateTdApi();
    ptd = td;
    md_msgQueue = CTP_CreateMsgQueue();
    td_msgQueue = CTP_CreateMsgQueue();
    CTP_RegAllCallback(md_msgQueue);
    CTP_RegAllCallback(td_msgQueue);
    MD_RegMsgQueue2MdApi(md, md_msgQueue);
    TD_RegMsgQueue2TdApi(td, md_msgQueue);
    CTP_StartMsgQueue(md_msgQueue);
    CTP_StartMsgQueue(td_msgQueue);
    
    //��ȡ��Ϣ����������
    ReadInifile(file, servername);
    
    MD_Connect(md, path.c_str(), mdServer.c_str(), brokerid.c_str(), investor.c_str(), password.c_str());
    TD_Connect(td, path.c_str(), tdServer.c_str(), brokerid.c_str(), investor.c_str(), password.c_str(), THOST_TERT_RESTART, "", "");
    if (TD_WaitForConnected(td))
    {
        PrintLog("���׶��Ѿ���¼(������˻�)");
        v_tds.push_back(td);
    } else return false;
    if (MD_WaitForConnected(md))
    {
        PrintLog("������Ѿ���¼(������˻�)");
    }else return false;
    return true;
}
int Trader::CreateTdAccount(const char *file, const char *servername)
{
    int ind;
    if (td == NULL || md == NULL)
    {
        PrintLog("δ��ȡ�����", "error");
        return -1;
    }
    else
    {
        ind = v_tds.size();
        ReadInifile(file, servername);
        void *ttd = TD_CreateTdApi();
        TD_RegMsgQueue2TdApi(ttd, td_msgQueue);
        m_tdposition[ttd] = ind;
        
        TD_Connect(ttd, path.c_str(), tdServer.c_str(), brokerid.c_str(), investor.c_str(), password.c_str(), THOST_TERT_RESTART, "", "");
        bool ok = TD_WaitForConnected(ttd);
        if (ok)
        {
            v_tds.push_back(ttd);
            mexPrintf("�ɹ���ȡ��ַ%x\n", ttd);
            PrintLog(string("�����˻�[") + to_string(ind) + string("]���ӳɹ�"));
        }
        else
        {
            PrintLog(string("�����˻�[") + to_string(ind) + string("]����ʧ��"), "error");
            TD_ReleaseTdApi(ttd);
            return -2;
        }
        
    }
    return ind;
    
}
void Trader::ReleaseTrader()
{
    
    int len = v_tds.size();
    for (int i = 1; i < len; ++i)
    {
        TD_ReleaseTdApi(v_tds[i]);
        v_tds[i] = NULL;
    }
    TD_ReleaseTdApi(td);
    MD_ReleaseMdApi(md);
    
    td = NULL;
    md = NULL;
    
    v_tds.clear();
    CTP_ReleaseMsgQueue(td_msgQueue);
    CTP_ReleaseMsgQueue(md_msgQueue);
    td_msgQueue = NULL;
    md_msgQueue = NULL;
    m_tdposition.clear();
}

void Trader::ReleaseTrader(int ind)
{
    if(ind == 0 || ind >= v_tds.size())
        PrintLog("û��������׶��˻�", "error");
    else
    {
        TD_ReleaseTdApi(v_tds[ind]);
        v_tds[ind] = NULL;
    }
}
string Trader::GetPortMsg(void *port)
{
    
    string res;
    if (NULL == port)
        return "�˿�Ϊ��";
    if (port == pmd)
        return  "����˿�(�����˻�)";
    else if (port == ptd)
        return  "���׶˿�(�����˻�)";
    else
    {
        int ind;
        if (ind = m_tdposition[port])
        {
            res = string("�����˻�[") + to_string(ind) + ']';
        }
        else
        {
            res = "û����������˻�";
        }
    }
    return res;
}
void Trader::CTP_RegAllCallback(void *tmsgQueue)
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


void Trader::ReadInifile(const char *file, const char *servername)
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
    GetPrivateProfileStringA(servername, "logpath", "", tmp, sizeof(tmp), file);
    logpath = tmp;
}

void Trader::Subscribe(const char* instruments)
{
    MD_Subscribe(md, instruments, "");
}

void Trader::Unsubscribe(const char* instruments)
{
    MD_Unsubscribe(md, instruments, "");
}


int Trader::SendOrder(int ind,
        const char* szInstrument,
        TThostFtdcDirectionType Direction,
        const char* szCombOffsetFlag,
        TThostFtdcVolumeType VolumeTotalOriginal,
        double LimitPrice)
{
    int res;
    if(ind < v_tds.size() && v_tds[ind] != NULL)
    {
        
        res = TD_SendOrder(v_tds[ind], -1, szInstrument, "", Direction, szCombOffsetFlag, "1",
                VolumeTotalOriginal, LimitPrice, THOST_FTDC_OPT_LimitPrice, THOST_FTDC_TC_GFD,
                THOST_FTDC_CC_Immediately, 0, THOST_FTDC_VC_AV);
        PrintLog(string(__FUNCTION__) + string("�˻�: ") + to_string(ind) + "�Ѿ��µ�");
        return res;
    }
    PrintLog(string(__FUNCTION__) + string("�������˻�: ") + to_string(ind), "error");
    return -1;
}


bool Trader::CancelOrder(int ind, string OrderRef)
{
    
    if(ind < v_tds.size() && v_tds[ind] != NULL)
    {
        CThostFtdcOrderField order;
        if(TD_GetOrder(v_tds[ind], OrderRef.c_str(), &order))
        {
            TD_CancelOrder(v_tds[ind], &order);
            return true;
        }
        
        else
        {
            PrintLog(string(__FUNCTION__) +  string("�˻�: ") + to_string(ind) + string(" �����ڶ���: ") + OrderRef, "error");
            return false;
        }
    }
    PrintLog(string(__FUNCTION__) + string("�������˻�: ") + to_string(ind), "error");
    return false;
}

mxArray *Trader::GetOrder(int ind, string OrderRef)
{
    if(ind < v_tds.size() && v_tds[ind] != NULL)
    {
        CThostFtdcOrderField order;
        if (TD_GetOrder(v_tds[ind], OrderRef.c_str(), &order))
        {
            mxArray *result;
            const char *field_names[] = {"BrokerID", "InvestorID", "InstrumentID", "OrderRef", "UserID", "Direction",
            "CombOffsetFlag", "LimitPrice", "ExchangeID", "OrderSysID",
            "OrderStatus", "FrontID", "SessionID"};
            mwSize dims[2] = {1, 1};
            result = mxCreateStructArray(2, dims, sizeof(field_names)/sizeof(*field_names), field_names);
            string tmp;
            mxSetField(result, 0, "BrokerID", mxCreateString(order.BrokerID));
            mxSetField(result, 0, "InvestorID", mxCreateString(order.InvestorID));
            mxSetField(result, 0, "InstrumentID", mxCreateString(order.InstrumentID));
            mxSetField(result, 0, "OrderRef", mxCreateString(order.OrderRef));
            mxSetField(result, 0, "UserID", mxCreateString(order.UserID));
            tmp = string("") + order.Direction;
            mxSetField(result, 0, "Direction", mxCreateString(tmp.c_str()));
            mxSetField(result, 0, "CombOffsetFlag", mxCreateString(order.CombOffsetFlag));
            mxSetField(result, 0, "LimitPrice", mxCreateDoubleScalar(order.LimitPrice));
            mxSetField(result, 0, "ExchangeID", mxCreateString(order.ExchangeID));
            mxSetField(result, 0, "OrderSysID", mxCreateString(order.OrderSysID));
            tmp = string("") + order.OrderStatus;
            mxSetField(result, 0, "OrderStatus", mxCreateString(tmp.c_str()));
            mxSetField(result, 0, "FrontID", mxCreateDoubleScalar(order.FrontID));
            mxSetField(result, 0, "SessionID", mxCreateDoubleScalar(order.SessionID));
            return result;
        }
        PrintLog(string(__FUNCTION__) +  string("�˻�: ") + to_string(ind) + string(" �����ڶ���: ") + OrderRef, "error");
        return mxCreateDoubleScalar(0);
    }
    PrintLog(string(__FUNCTION__) + string("�������˻�: ") + to_string(ind), "error");
    return mxCreateDoubleScalar(0);
    
    
}
//��ֲ�
bool Trader::QryInvestorPosition(int ind, const char* szInstrumentId)
{
    if(ind < v_tds.size() && v_tds[ind] != NULL)
    {
        TD_ReqQryInvestorPosition(v_tds[ind], szInstrumentId);
        return true;
    }
    PrintLog(string(__FUNCTION__) + string("�������˻�: ") + to_string(ind), "error");
    return false;
}

//��ֲ���ϸ
bool Trader::QryInvestorPositionDetail(int ind, const char* szInstrumentId)
{
    if(ind < v_tds.size() && v_tds[ind] != NULL)
    {
        TD_ReqQryInvestorPositionDetail(v_tds[ind], szInstrumentId);
        return true;
    }
    PrintLog(string(__FUNCTION__) + string("�������˻�: ") + to_string(ind), "error");
    return false;
}

//���ʽ��˺�
bool Trader::QryTradingAccount(int ind)
{
    if(ind < v_tds.size() && v_tds[ind] != NULL)
    {
        TD_ReqQryTradingAccount(v_tds[ind]);
        return true;
    }
    PrintLog(string(__FUNCTION__) + string("�������˻�: ") + to_string(ind), "error");
    return false;
}

//���Լ
void Trader::QryInstrument(const char* szInstrumentId)
{
    TD_ReqQryInstrument(td, szInstrumentId);
    if (TD_WaitForInstrumentGeted(td))
    {
        PrintLog("��ȡ���ս��׺�Լ�ɹ�");
    }
    else PrintLog("��ȡ��Լʧ��", "error");
}

//��������
void Trader::QryInstrumentCommissionRate(const char* szInstrumentId)
{
    TD_ReqQryInstrumentCommissionRate(td, szInstrumentId);
}

//�鱣֤��
void Trader::QryInstrumentMarginRate(const char* szInstrumentId, TThostFtdcHedgeFlagType HedgeFlag)
{
    TD_ReqQryInstrumentMarginRate(td, szInstrumentId, HedgeFlag);
}

//���������
void Trader::QryDepthMarketData(const char* szInstrumentId)
{
    TD_ReqQryDepthMarketData(td, szInstrumentId);
}

//�����ѯͶ���߽�����
bool Trader::QrySettlementInfo(int ind, const char* szTradingDay)
{
    if(ind < v_tds.size() && v_tds[ind] != NULL)
    {
        TD_ReqQrySettlementInfo(td, szTradingDay);
        return true;
    }
    PrintLog(string(__FUNCTION__) + string("�������˻�: ") + to_string(ind), "error");
    return false;
}


