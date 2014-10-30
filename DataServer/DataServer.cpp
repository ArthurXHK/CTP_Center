#include "DataServer.h"

mongo::DBClientConnection *DataServer::pCon;
void *DataServer::md;//行情端口
void *DataServer::td; //用于获取交易合约的交易端口（非交易用）
void *DataServer::md_msgQueue; //专门用于行情队列
DBLog *DataServer::dblog; //日志对象
string DataServer::path; //con文件数据流路径
string DataServer::brokerid; //期商代码
string DataServer::investor; //投资者代码
string DataServer::password; //密码
string DataServer::mdServer; //行情服务器地址
string DataServer::tdServer; //交易服务器地址
string DataServer::logpath; //日志路径
string DataServer::database;
string DataServer::mongoip;
set<string> DataServer::insts;// 查询到的合约
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
    
    //注册回调 & 注册队列
    CTP_RegAllCallback(md_msgQueue);
    MD_RegMsgQueue2MdApi(md, md_msgQueue);
    TD_RegMsgQueue2TdApi(td, md_msgQueue);
    CTP_StartMsgQueue(md_msgQueue);

    
    return true;
}
bool DataServer::ConnectMdServer(const char *file, const char *servername)
{
    //获取空间，绑定队列，注册回调
    if (!AllocMemory())
        return false;
    //读取信息
    ReadInifile(file, servername);
    dblog->RegisterPath(logpath);
    if (!ConnectMongodb())
        return false;
    //处理连接
    MD_Connect(md, path.c_str(), mdServer.c_str(), brokerid.c_str(), investor.c_str(), password.c_str());
    TD_Connect(td, path.c_str(), tdServer.c_str(), brokerid.c_str(), investor.c_str(), password.c_str(), THOST_TERT_RESTART, "", "");
    
    if (TD_WaitForConnected(td))
    {
        dblog->PrintLog("交易端已经登录(行情端账户)");
    }
    else return false;
    if (MD_WaitForConnected(md))
    {
        dblog->PrintLog("行情端已经登录(行情端账户)");
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
        dblog->PrintLog("数据库已经连接");
    return true;
    
}
DWORD WINAPI HeartBeatThread(LPVOID pM)
{
    DataServer::dblog->PrintLog("心跳线程已经启动");
    while (1)
    {
        Sleep(1000 * 300 - 3);
        DataServer::dblog->PrintLog("发送程序心跳");
        SYSTEMTIME hbt;
        GetLocalTime(&hbt);
        if (hbt.wHour == 15 && hbt.wMinute > 20)
        {
            DataServer::dblog->PrintLog("日盘行情已经结束");
            break;
        }
        else if (hbt.wHour == 2 && hbt.wMinute > 35)
        {
            DataServer::dblog->PrintLog("夜盘行情已经结束");
            break;
        }

    }
    DataServer::dblog->PrintLog("程序退出成功");
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
        res = "行情端口(行情账户)";
    else if (port == td)
        res = "交易端口(行情账户)";
    
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
    dblog->PrintLog("退订合约成功");
}

void DataServer::SubscribeAll()
{
    if (TD_WaitForInstrumentGeted(td))
    {
        dblog->PrintLog("获取今日交易合约成功");
    }
    set<string>::iterator iter;
    
    for (iter = insts.begin(); iter != insts.end(); ++iter)
    {
        Subscribe(iter->c_str());
    }
    dblog->PrintLog("订阅所有合约成功");
}

void DataServer::QryInstrument(const char* szInstrumentId)
{
    TD_ReqQryInstrument(td, szInstrumentId);
    dblog->PrintLog("查询合约已发送");
}

