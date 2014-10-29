#include "DataServer.h"

mongo::DBClientConnection *con;
void *DataServer::md;//行情端口
void *DataServer::td; //用于获取交易合约的交易端口（非交易用）
void *DataServer::md_msgQueue; //专门用于行情队列
DBLog *DataServer::dblog; //日志对象
string DataServer::path; //con数据路径
string DataServer::brokerid; //期商代码
string DataServer::investor; //投资者代码
string DataServer::password; //密码
string DataServer::mdServer; //行情服务器地址
string DataServer::tdServer; //交易服务器地址
string DataServer::dbpath; //日志路径

bool DataServer::ConnectMdServer(const char *file, const char *servername)
{
    bool isconnected = true;
    //获取空间，绑定队列，注册回调
    
    md = MD_CreateMdApi();
    td = TD_CreateTdApi();
    md_msgQueue = CTP_CreateMsgQueue();
    CTP_RegAllCallback(md_msgQueue);
    MD_RegMsgQueue2MdApi(md, md_msgQueue);
    TD_RegMsgQueue2TdApi(td, md_msgQueue);
    CTP_StartMsgQueue(md_msgQueue);
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
    return isconnected;
}
DWORD WINAPI HeartBeatThread(LPVOID pM)
{
    DataServer::dblog->PrintLog("心跳线程已经启动");
    while (1)
    {
        Sleep(1000 * 300 - 3);
        DataServer::dblog->PrintLog("发送程序心跳，正常运行中");
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
void DataServer::Release()
{
    TD_ReleaseTdApi(td);
    MD_ReleaseMdApi(md);
    CTP_ReleaseMsgQueue(md_msgQueue);
    delete dblog;
    dblog = NULL;

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
    GetPrivateProfileStringA(servername, "dbpath", "", tmp, sizeof(tmp), file);
    dbpath = tmp;
}

void DataServer::AddLogPath(const string &dbpath)
{
    if (NULL == dblog)
        dblog = new DBLog(dbpath);
}


void DataServer::Subscribe(const char* instruments)
{
    MD_Subscribe(md, instruments, "");
    dblog->PrintLog("订阅合约成功");
}

void DataServer::Unsubscribe(const char* instruments)
{
    MD_Unsubscribe(md, instruments, "");
    dblog->PrintLog("退订合约成功");
}

void DataServer::QryInstrument(const char* szInstrumentId)
{
    TD_ReqQryInstrument(td, szInstrumentId);
    if (TD_WaitForInstrumentGeted(td))
    {
        dblog->PrintLog("获取今日交易合约成功");
    }
}

