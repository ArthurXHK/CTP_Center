#ifndef TRADER_H
#define TRADER_H

#include "QuantBox.C2CTP.h"
#include "DBLog.h"
#include "toolkit.h"
#include "mex.h"
#include "matrix.h"

#include <iostream>
#include <string>
#include <Windows.h>
#include <map>
#include <vector>
#include <mutex>
#include <atomic>
using namespace std;


// ���׹�������
class Trader
{
public:
    //��ȡΨһʵ��
    static Trader& GetInstance()
    {
        static Trader trader;
        return trader;
    }
    static void PrintLog(string msg, string type = "normal");
    //�������������
    bool ConnectMdServer(const char *file, const char *servername);
    //�����½����˻��������˻��±꣬-1Ϊ����ʧ��
    int CreateTdAccount(const char *file, const char *servername);
    //���������˻�
    void ReleaseTrader();
    //����ָ���˻�
    void ReleaseTrader(int ind);
    //��ȡ�˿���Ϣ
    static string GetPortMsg(void *port);
    //��������
    void Subscribe(const char* instruments);
    //�˶�����
    void Unsubscribe(const char* instruments);
    
    //�µ�
    int Trader::SendOrder(int ind,
            const char* szInstrument,
            TThostFtdcDirectionType Direction,
            const char* szCombOffsetFlag,
            TThostFtdcVolumeType VolumeTotalOriginal,
            double LimitPrice);
    
    // ����
    bool CancelOrder(int ind, CThostFtdcOrderField *pOrder);
    // ��ȡ������Ϣ
    mxArray *GetOrder(int ind, string OrderRef);
    //��ֲ�
    bool QryInvestorPosition(int ind, const char* szInstrumentId);
    //��ֲ���ϸ
    bool QryInvestorPositionDetail(int ind, const char* szInstrumentId);
    //���ʽ��˺�
    bool QryTradingAccount(int ind);
    //���Լ
    void QryInstrument(const char* szInstrumentId);
    //��������
    void QryInstrumentCommissionRate(const char* szInstrumentId);
    //�鱣֤��
    void QryInstrumentMarginRate(const char* szInstrumentId, TThostFtdcHedgeFlagType HedgeFlag);
    //���������
    void QryDepthMarketData(const char* szInstrumentId);
    //�����ѯͶ���߽�����
    bool QrySettlementInfo(int ind, const char* szTradingDay);
    
private:
    //��ȡ�����ļ�
    void ReadInifile(const char *file, const char *servername);
    //ע�����лص�
    void CTP_RegAllCallback(void *tmsgQueue);
    //���ӻر���Ϣ
    static void __stdcall OnConnect(void* pApi, CThostFtdcRspUserLoginField *pRspUserLogin, ConnectionStatus result);
    //�Ͽ����ӻر���Ϣ
    static void __stdcall OnDisconnect(void* pApi, CThostFtdcRspInfoField *pRspInfo, ConnectionStatus step);
    //����������Ϣ
    static void __stdcall OnErrRtnOrderAction(void* pTraderApi, CThostFtdcOrderActionField *pOrderAction, CThostFtdcRspInfoField *pRspInfo);
    //�µ�������Ϣ
    static void __stdcall OnErrRtnOrderInsert(void* pTraderApi, CThostFtdcInputOrderField *pInputOrder, CThostFtdcRspInfoField *pRspInfo);
    static void __stdcall OnErrRtnQuoteAction(void* pTraderApi, CThostFtdcQuoteActionField *pQuoteAction, CThostFtdcRspInfoField *pRspInfo);
    static void __stdcall OnErrRtnQuoteInsert(void* pTraderApi, CThostFtdcInputQuoteField *pInputQuote, CThostFtdcRspInfoField *pRspInfo);
    //������Ϣ
    static void __stdcall OnRspError(void* pApi, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
    //�����ر�
    static void __stdcall OnRspOrderAction(void* pTraderApi, CThostFtdcInputOrderActionField *pInputOrderAction, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
    //�µ��ر�
    static void __stdcall OnRspOrderInsert(void* pTraderApi, CThostFtdcInputOrderField *pInputOrder, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
    //��ѯ�������ر�
    static void __stdcall OnRspQryDepthMarketData(void* pTraderApi, CThostFtdcDepthMarketDataField *pDepthMarketData, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
    //��ѯ��Լ�ر�
    static void __stdcall OnRspQryInstrument(void* pTraderApi, CThostFtdcInstrumentField *pInstrument, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
    //��ѯ��Լ�������ʻر�
    static void __stdcall OnRspQryInstrumentCommissionRate(void* pTraderApi, CThostFtdcInstrumentCommissionRateField *pInstrumentCommissionRate, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
    //��ѯ��Լ��֤���ʻر�
    static void __stdcall OnRspQryInstrumentMarginRate(void* pTraderApi, CThostFtdcInstrumentMarginRateField *pInstrumentMarginRate, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
    //��ѯͶ���ֲֻ߳ر�
    static void __stdcall OnRspQryInvestorPosition(void* pTraderApi, CThostFtdcInvestorPositionField *pInvestorPosition, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
    
    //��ѯ�ֲ���ϸ�ر�
    static void __stdcall OnRspQryInvestorPositionDetail(void* pTraderApi, CThostFtdcInvestorPositionDetailField *pInvestorPositionDetail, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
    //��ѯ�����ر�
    static void __stdcall OnRspQryOrder(void* pTraderApi, CThostFtdcOrderField *pOrder, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
    //��ѯ�ɽ��ر�
    static void __stdcall OnRspQryTrade(void* pTraderApi, CThostFtdcTradeField *pTrade, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
    //��ѯͶ���߽���ر�
    static void __stdcall OnRspQrySettlementInfo(void* pTraderApi, CThostFtdcSettlementInfoField *pSettlementInfo, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
    //��ѯ�ʽ��˻��ر�
    static void __stdcall OnRspQryTradingAccount(void* pTraderApi, CThostFtdcTradingAccountField *pTradingAccount, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
    //�������ر�
    static void __stdcall OnRtnDepthMarketData(void* pMdUserApi, CThostFtdcDepthMarketDataField *pDepthMarketData);
    //��Լ״̬�ر�
    static void __stdcall OnRtnInstrumentStatus(void* pTraderApi, CThostFtdcInstrumentStatusField *pInstrumentStatus);
    //�����ر�
    static void __stdcall OnRtnOrder(void* pTraderApi, CThostFtdcOrderField *pOrder);
    //�ɽ��ر�
    static void __stdcall OnRtnTrade(void* pTraderApi, CThostFtdcTradeField *pTrade);
    //�����ص�
    static void __stdcall OnRspQuoteAction(void* pTraderApi, CThostFtdcInputQuoteActionField *pInputQuoteAction, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
    static void __stdcall OnRspQuoteInsert(void* pTraderApi, CThostFtdcInputQuoteField *pInputQuote, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
    static void __stdcall OnRtnForQuoteRsp(void* pMdUserApi, CThostFtdcForQuoteRspField *pForQuoteRsp);
    static void __stdcall OnRtnQuote(void* pTraderApi, CThostFtdcQuoteField *pQuote);
    
private:
    //����Ĭ�Ϲ���
    Trader()
    {
        md = NULL;
        td = NULL;
        md_msgQueue = NULL;
        td_msgQueue = NULL;
        dblog.RegisterPath("..\\TraderCenter\\log");
    }
    ~Trader(){};
    Trader& operator=(Trader const&);
    
    static void *md;//����˿�
    static void *td; //���ڻ�ȡ���׺�Լ�Ľ��׶˿ڣ��ǽ����ã�
    static void *pmd, *ptd; //�ݴ�����˿ڵ�ַ
    static void *md_msgQueue; //ר�������������
    static void *td_msgQueue; //���׶��У������˻�������
    static map<void *, int> m_tdposition; //�����˻�ӳ��
    static vector<void *> v_tds; //�����˻�����
    static DBLog dblog; //��־����
    static string path; //con����·��
    static string brokerid; //���̴���
    static string investor; //Ͷ���ߴ���
    static string password; //����
    static string mdServer; //�����������ַ
    static string tdServer; //���׷�������ַ
    static string logpath; //��־·��
    static mutex csLog;
};

#endif