#ifndef DATASERVER_H
#define DATASERVER_H
#pragma warning (disable: 4251)
#pragma warning (disable: 4275)
//�Ȱ���mongo���ٰ���windows.h����������⣬���������º꣬��Ҫԭ����winsock2.h������windows.hǰ��
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

// ���ݷ�����
class DataServer
{
public:
    //��ȡΨһʵ��
    static DataServer& GetAccountInstance()
    {
        static DataServer account;
        return account;
    }
    //�������������
    bool ConnectMdServer(const char *file, const char *servername);
    bool ConnectMongodb();
    //��������ָ�����
    void Release();
    //��ȡ�˿���Ϣ
    static string GetPortMsg(void *port);
    //��ѯ���׺�Լ
    void QryInstrument(const char* szInstrumentId);
    //��������
    void Subscribe(const char* instruments);
    //�˶�����
    void Unsubscribe(const char* instruments);
    //����ȫ������
    void SubscribeAll();
    //��ѯ��֤�����
    void QryInstrumentMarginRate(TThostFtdcHedgeFlagType HedgeFlag);
    //���������߳�
    mongo::HANDLE StartHeartBeat();

private:
    //��ȡ�����ļ�
    void ReadInifile(const char *file, const char *servername);
    //ע�����лص�
    void CTP_RegAllCallback(void *tmsgQueue);
    //����1min����
    static void UpdateBar(CThostFtdcDepthMarketDataField *pDepthMarketData);
    //�����߳�
    friend DWORD WINAPI HeartBeatThread(LPVOID pM);
    //����ָ��ռ�
    bool AllocMemory();
    //���ӻر���Ϣ
    static void __stdcall OnConnect(void* pApi, CThostFtdcRspUserLoginField *pRspUserLogin, ConnectionStatus result);
    //�Ͽ����ӻر���Ϣ
    static void __stdcall OnDisconnect(void* pApi, CThostFtdcRspInfoField *pRspInfo, ConnectionStatus step);
    //������Ϣ
    static void __stdcall OnRspError(void* pApi, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
    //��ѯ��Լ�ر�
    static void __stdcall OnRspQryInstrument(void* pTraderApi, CThostFtdcInstrumentField *pInstrument, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
    //�������ر�
    static void __stdcall OnRtnDepthMarketData(void* pMdUserApi, CThostFtdcDepthMarketDataField *pDepthMarketData);
    //��Լ״̬�ر�
    static void __stdcall OnRtnInstrumentStatus(void* pTraderApi, CThostFtdcInstrumentStatusField *pInstrumentStatus);
    static void __stdcall OnRspQryInstrumentMarginRate(void* pTraderApi, CThostFtdcInstrumentMarginRateField *pInstrumentMarginRate, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);

private:
    //����Ĭ�Ϲ���
    DataServer(){
        //Ĭ�ϲ�������
        path = "testStream";
        logpath = "testDblog";
        database = "testMarketData";
        mongoip = "localhost";
    };
    ~DataServer(){};
    DataServer& operator=(DataServer const&);

    static mongo::DBClientConnection *pCon;//���ݿ����ӿ�
    static void *md;                                      //����˿�
    static void *td;                                        //���ڻ�ȡ���׺�Լ�Ľ��׶˿ڣ��ǽ����ã�
    static void *md_msgQueue;                    //ר�������������
    static DBLog *dblog;                              //��־����
    static string path;                                   //con����·��
    static string brokerid;                              //���̴���
    static string investor;                               //Ͷ���ߴ���
    static string password;                             //����
    static string mdServer;                             //�����������ַ
    static string tdServer;                              //���׷�������ַ
    static string logpath;                                //��־·��
    static string database;                             //���ݿ���
    static string mongoip;                             //���ݿ�ip��ַ
    static set<string> insts;                           // ��ѯ���ĺ�Լ
    static set<string> hasData;
    static std::mutex cs_instrument;               
    static mongo::HANDLE h_instrumentGeted;
};

#endif