#include "DataServer.h"

mongo::DBClientConnection *DataServer::pCon;
void *DataServer::md;//����˿�
void *DataServer::td; //���ڻ�ȡ���׺�Լ�Ľ��׶˿ڣ��ǽ����ã�
void *DataServer::md_msgQueue; //ר�������������
DBLog *DataServer::dblog; //��־����
string DataServer::path; //con�ļ�������·��
string DataServer::brokerid; //���̴���
string DataServer::investor; //Ͷ���ߴ���
string DataServer::password; //����
string DataServer::mdServer; //�����������ַ
string DataServer::tdServer; //���׷�������ַ
string DataServer::logpath; //��־·��
string DataServer::database;
string DataServer::mongoip;
set<string> DataServer::insts;// ��ѯ���ĺ�Լ
std::mutex DataServer::cs_instrument;
SYSTEMTIME DataServer::st;

bool DataServer::AllocMemory()
{
    md = td = md_msgQueue = pCon = NULL;
    md = MD_CreateMdApi();
    td = TD_CreateTdApi();
    md_msgQueue = CTP_CreateMsgQueue();
    pCon = new mongo::DBClientConnection();
    dblog = new DBLog();
    if (NULL == md || NULL == td || NULL == md_msgQueue || NULL == pCon || NULL == dblog)
        return false;
    
    //ע��ص� & ע�����
    CTP_RegAllCallback(md_msgQueue);
    MD_RegMsgQueue2MdApi(md, md_msgQueue);
    TD_RegMsgQueue2TdApi(td, md_msgQueue);
    CTP_StartMsgQueue(md_msgQueue);

    
    return true;
}
bool DataServer::ConnectMdServer(const char *file, const char *servername)
{
    //��ȡ�ռ䣬�󶨶��У�ע��ص�
    if (!AllocMemory())
        return false;
    //��ȡ��Ϣ
    ReadInifile(file, servername);
    dblog->RegisterPath(logpath);
    if (!ConnectMongodb())
        return false;
    //��������
    MD_Connect(md, path.c_str(), mdServer.c_str(), brokerid.c_str(), investor.c_str(), password.c_str());
    TD_Connect(td, path.c_str(), tdServer.c_str(), brokerid.c_str(), investor.c_str(), password.c_str(), THOST_TERT_RESTART, "", "");
    
    if (TD_WaitForConnected(td))
    {
        dblog->PrintLog("���׶��Ѿ���¼(������˻�)");
    }
    else return false;
    if (MD_WaitForConnected(md))
    {
        dblog->PrintLog("������Ѿ���¼(������˻�)");
    }
    else return false;

    return true;
}

bool DataServer::ConnectMongodb()
{
    try
    {
        pCon->connect(mongoip);
    }
    catch (const mongo::DBException &e)
    {
        if (dblog)
            dblog->PrintLog(e.what(), "error");
        return false;
    }
    if (dblog)
        dblog->PrintLog("���ݿ��Ѿ�����");
    return true;
    
}
DWORD WINAPI HeartBeatThread(LPVOID pM)
{
    DataServer::dblog->PrintLog("�����߳��Ѿ�����");
    while (1)
    {
        Sleep(1000 * 300 - 3);
        DataServer::dblog->PrintLog("���ͳ�������");
        SYSTEMTIME hbt;
        GetLocalTime(&hbt);
        if (hbt.wHour == 15 && hbt.wMinute > 20)
        {
            DataServer::dblog->PrintLog("���������Ѿ�����");
            break;
        }
        else if (hbt.wHour == 2 && hbt.wMinute > 35)
        {
            DataServer::dblog->PrintLog("ҹ�������Ѿ�����");
            break;
        }

    }
    DataServer::dblog->PrintLog("�����˳��ɹ�");
    return 0;
}

mongo::HANDLE DataServer::StartHeartBeat()
{
    GetLocalTime(&st);
    return CreateThread(NULL, 0, HeartBeatThread, NULL, 0, NULL);
}
void DataServer::Release()
{
    TD_ReleaseTdApi(td);
    MD_ReleaseMdApi(md);
    CTP_ReleaseMsgQueue(md_msgQueue);
    if (dblog)
    {
        delete dblog;
        dblog = NULL;
    }

}

string DataServer::GetPortMsg(void *port)
{
    string res;
    if (port == md)
        res = "����˿�(�����˻�)";
    else if (port == td)
        res = "���׶˿�(�����˻�)";
    
    return res;
}
void DataServer::CTP_RegAllCallback(void *tmsgQueue)
{
    CTP_RegOnConnect(tmsgQueue, OnConnect);
    CTP_RegOnDisconnect(tmsgQueue, OnDisconnect);
    CTP_RegOnRspError(tmsgQueue, OnRspError);
    CTP_RegOnRspQryInstrument(tmsgQueue, OnRspQryInstrument);
    CTP_RegOnRtnDepthMarketData(tmsgQueue, OnRtnDepthMarketData);
    CTP_RegOnRtnInstrumentStatus(tmsgQueue, OnRtnInstrumentStatus);
}


void DataServer::ReadInifile(const char *file, const char *servername)
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
    GetPrivateProfileStringA(servername, "mongoip", "", tmp, sizeof(tmp), file);
    mongoip = tmp;
    GetPrivateProfileStringA(servername, "database", "", tmp, sizeof(tmp), file);
    database = tmp;
}



void DataServer::Subscribe(const char* instruments)
{
    MD_Subscribe(md, instruments, "");
}

void DataServer::Unsubscribe(const char* instruments)
{
    MD_Unsubscribe(md, instruments, "");
    dblog->PrintLog("�˶���Լ�ɹ�");
}

void DataServer::SubscribeAll()
{
    if (TD_WaitForInstrumentGeted(td))
    {
        dblog->PrintLog("��ȡ���ս��׺�Լ�ɹ�");
    }
    set<string>::iterator iter;
    
    for (iter = insts.begin(); iter != insts.end(); ++iter)
    {
        Subscribe(iter->c_str());
    }
    dblog->PrintLog("�������к�Լ�ɹ�");
}

void DataServer::QryInstrument(const char* szInstrumentId)
{
    TD_ReqQryInstrument(td, szInstrumentId);
    dblog->PrintLog("��ѯ��Լ�ѷ���");
}

