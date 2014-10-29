#ifndef ACCOUNT_H
#define ACCOUNT_H

#include "QuantBox.C2CTP.h"
#include "DBLog.h"
#include "toolkit.h"
#include <mongo\client\dbclient.h>
#include <mongo\bson\bson.h>
#include <iostream>
#include <string>
#include <Windows.h>
#include <map>
#include <vector>
using namespace std;
using namespace mongo;
using namespace bson;

// 数据服务器
class DataServer
{
public:
    //获取唯一实例
    static DataServer& GetAccountInstance()
    {
        static DataServer account;
        return account;
    }
    //连接行情服务器
    bool ConnectMdServer(const char *file, const char *servername);
    //销毁所有指针对象
    void Release();
    //添加log路径
    void AddLogPath(const string &dbpath);
    //获取端口信息
    static string GetPortMsg(void *port);
    //查询交易合约
    void QryInstrument(const char* szInstrumentId);
    //订阅行情
    void Subscribe(const char* instruments);
    //退订行情
    void Unsubscribe(const char* instruments);
    //运行心跳线程
    void StartHeartBeat();

private:
    //读取配置文件
    void ReadInifile(const char *file, const char *servername);
    //注册所有回调
    void CTP_RegAllCallback(void *tmsgQueue);
    //心跳线程
    friend DWORD WINAPI HeartBeatThread(LPVOID pM);
    //连接回报信息
    static void __stdcall OnConnect(void* pApi, CThostFtdcRspUserLoginField *pRspUserLogin, ConnectionStatus result);
    //断开连接回报信息
    static void __stdcall OnDisconnect(void* pApi, CThostFtdcRspInfoField *pRspInfo, ConnectionStatus step);
    //错误信息
    static void __stdcall OnRspError(void* pApi, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
    //查询合约回报
    static void __stdcall OnRspQryInstrument(void* pTraderApi, CThostFtdcInstrumentField *pInstrument, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
    //深度行情回报
    static void __stdcall OnRtnDepthMarketData(void* pMdUserApi, CThostFtdcDepthMarketDataField *pDepthMarketData);
    //合约状态回报
    static void __stdcall OnRtnInstrumentStatus(void* pTraderApi, CThostFtdcInstrumentStatusField *pInstrumentStatus);
    

private:
    //隐藏默认构造
    DataServer(){};
    ~DataServer(){};
    DataServer& operator=(DataServer const&);

    static mongo::DBClientConnection *con;
    static void *md;//行情端口
    static void *td; //用于获取交易合约的交易端口（非交易用）
    static void *md_msgQueue; //专门用于行情队列
    static DBLog *dblog; //日志对象
    static string path; //con数据路径
    static string brokerid; //期商代码
    static string investor; //投资者代码
    static string password; //密码
    static string mdServer; //行情服务器地址
    static string tdServer; //交易服务器地址
    static string dbpath; //日志路径
};

#endif