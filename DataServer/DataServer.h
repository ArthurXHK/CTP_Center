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
    //��������ָ�����
    void Release();
    //���log·��
    void AddLogPath(const string &dbpath);
    //��ȡ�˿���Ϣ
    static string GetPortMsg(void *port);
    //��ѯ���׺�Լ
    void QryInstrument(const char* szInstrumentId);
    //��������
    void Subscribe(const char* instruments);
    //�˶�����
    void Unsubscribe(const char* instruments);
    //���������߳�
    void StartHeartBeat();

private:
    //��ȡ�����ļ�
    void ReadInifile(const char *file, const char *servername);
    //ע�����лص�
    void CTP_RegAllCallback(void *tmsgQueue);
    //�����߳�
    friend DWORD WINAPI HeartBeatThread(LPVOID pM);
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
    

private:
    //����Ĭ�Ϲ���
    DataServer(){};
    ~DataServer(){};
    DataServer& operator=(DataServer const&);

    static mongo::DBClientConnection *con;
    static void *md;//����˿�
    static void *td; //���ڻ�ȡ���׺�Լ�Ľ��׶˿ڣ��ǽ����ã�
    static void *md_msgQueue; //ר�������������
    static DBLog *dblog; //��־����
    static string path; //con����·��
    static string brokerid; //���̴���
    static string investor; //Ͷ���ߴ���
    static string password; //����
    static string mdServer; //�����������ַ
    static string tdServer; //���׷�������ַ
    static string dbpath; //��־·��
};

#endif