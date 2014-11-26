#ifndef DATASERVER_H
#define DATASERVER_H
#pragma warning (disable: 4251)
#pragma warning (disable: 4275)
//先包含mongo库再包含windows.h避免编译问题，否则定义以下宏，主要原因是winsock2.h必须在windows.h前面
//#define _WINSOCKAPI_  
//#define NOMINMAX

#include <mongo\client\dbclient.h>
#include <mongo\bson\bson.h>
#include "QuantBox.C2CTP.h"
#include "DBLog.h"
#include "toolkit.h"

#include <iostream>
#include <string>
#include <map>
#include <vector>
#include <set>
#include <mutex>
#include <atomic>

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
    bool ConnectMongodb();
    //销毁所有指针对象
    void Release();
    //获取端口信息
    static string GetPortMsg(void *port);
    //查询交易合约
    void QryInstrument(const char* szInstrumentId);
    //订阅行情
    void Subscribe(const char* instruments);
    //退订行情
    void Unsubscribe(const char* instruments);
    //订阅全部行情
    void SubscribeAll();
    //查询保证金比例
    void QryInstrumentMarginRate(TThostFtdcHedgeFlagType HedgeFlag);
    //运行心跳线程
    mongo::HANDLE StartHeartBeat();

private:
    //读取配置文件
    void ReadInifile(const char *file, const char *servername);
    //注册所有回调
    void CTP_RegAllCallback(void *tmsgQueue);
    //更新1min数据
    static void UpdateBar(CThostFtdcDepthMarketDataField *pDepthMarketData);
    //心跳线程
    friend DWORD WINAPI HeartBeatThread(LPVOID pM);
    //开辟指针空间
    bool AllocMemory();
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
    static void __stdcall OnRspQryInstrumentMarginRate(void* pTraderApi, CThostFtdcInstrumentMarginRateField *pInstrumentMarginRate, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);

private:
    //隐藏默认构造
    DataServer(){
        //默认参数设置
        path = "testStream";
        logpath = "testDblog";
        database = "testMarketData";
        mongoip = "localhost";
    };
    ~DataServer(){};
    DataServer& operator=(DataServer const&);

    static mongo::DBClientConnection *pCon;//数据库连接口
    static void *md;                                      //行情端口
    static void *td;                                        //用于获取交易合约的交易端口（非交易用）
    static void *md_msgQueue;                    //专门用于行情队列
    static DBLog *dblog;                              //日志对象
    static string path;                                   //con数据路径
    static string brokerid;                              //期商代码
    static string investor;                               //投资者代码
    static string password;                             //密码
    static string mdServer;                             //行情服务器地址
    static string tdServer;                              //交易服务器地址
    static string logpath;                                //日志路径
    static string database;                             //数据库名
    static string mongoip;                             //数据库ip地址
    static set<string> insts;                           // 查询到的合约
    static set<string> hasData;
    static std::mutex cs_instrument;               
    static mongo::HANDLE h_instrumentGeted;
};

#endif