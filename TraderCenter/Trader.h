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


// 交易管理中心
class Trader
{
public:
    //获取唯一实例
    static Trader& GetInstance()
    {
        static Trader trader;
        return trader;
    }
    static void PrintLog(string msg, string type = "normal");
    //连接行情服务器
    bool ConnectMdServer(const char *file, const char *servername);
    //创建新交易账户，返回账户下标，-1为连接失败
    int CreateTdAccount(const char *file, const char *servername);
    //销毁所有账户
    void ReleaseTrader();
    //销毁指定账户
    void ReleaseTrader(int ind);
    //获取端口信息
    static string GetPortMsg(void *port);
    //订阅行情
    void Subscribe(const char* instruments);
    //退订行情
    void Unsubscribe(const char* instruments);
    
    //下单
    int Trader::SendOrder(int ind,
            const char* szInstrument,
            TThostFtdcDirectionType Direction,
            const char* szCombOffsetFlag,
            TThostFtdcVolumeType VolumeTotalOriginal,
            double LimitPrice);
    
    // 撤单
    bool CancelOrder(int ind, CThostFtdcOrderField *pOrder);
    // 获取订单信息
    mxArray *GetOrder(int ind, string OrderRef);
    //查持仓
    bool QryInvestorPosition(int ind, const char* szInstrumentId);
    //查持仓明细
    bool QryInvestorPositionDetail(int ind, const char* szInstrumentId);
    //查资金账号
    bool QryTradingAccount(int ind);
    //查合约
    void QryInstrument(const char* szInstrumentId);
    //查手续费
    void QryInstrumentCommissionRate(const char* szInstrumentId);
    //查保证金
    void QryInstrumentMarginRate(const char* szInstrumentId, TThostFtdcHedgeFlagType HedgeFlag);
    //查深度行情
    void QryDepthMarketData(const char* szInstrumentId);
    //请求查询投资者结算结果
    bool QrySettlementInfo(int ind, const char* szTradingDay);
    
private:
    //读取配置文件
    void ReadInifile(const char *file, const char *servername);
    //注册所有回调
    void CTP_RegAllCallback(void *tmsgQueue);
    //连接回报信息
    static void __stdcall OnConnect(void* pApi, CThostFtdcRspUserLoginField *pRspUserLogin, ConnectionStatus result);
    //断开连接回报信息
    static void __stdcall OnDisconnect(void* pApi, CThostFtdcRspInfoField *pRspInfo, ConnectionStatus step);
    //撤单错误信息
    static void __stdcall OnErrRtnOrderAction(void* pTraderApi, CThostFtdcOrderActionField *pOrderAction, CThostFtdcRspInfoField *pRspInfo);
    //下单错误信息
    static void __stdcall OnErrRtnOrderInsert(void* pTraderApi, CThostFtdcInputOrderField *pInputOrder, CThostFtdcRspInfoField *pRspInfo);
    static void __stdcall OnErrRtnQuoteAction(void* pTraderApi, CThostFtdcQuoteActionField *pQuoteAction, CThostFtdcRspInfoField *pRspInfo);
    static void __stdcall OnErrRtnQuoteInsert(void* pTraderApi, CThostFtdcInputQuoteField *pInputQuote, CThostFtdcRspInfoField *pRspInfo);
    //错误信息
    static void __stdcall OnRspError(void* pApi, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
    //撤单回报
    static void __stdcall OnRspOrderAction(void* pTraderApi, CThostFtdcInputOrderActionField *pInputOrderAction, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
    //下单回报
    static void __stdcall OnRspOrderInsert(void* pTraderApi, CThostFtdcInputOrderField *pInputOrder, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
    //查询深度行情回报
    static void __stdcall OnRspQryDepthMarketData(void* pTraderApi, CThostFtdcDepthMarketDataField *pDepthMarketData, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
    //查询合约回报
    static void __stdcall OnRspQryInstrument(void* pTraderApi, CThostFtdcInstrumentField *pInstrument, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
    //查询合约手续费率回报
    static void __stdcall OnRspQryInstrumentCommissionRate(void* pTraderApi, CThostFtdcInstrumentCommissionRateField *pInstrumentCommissionRate, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
    //查询合约保证金率回报
    static void __stdcall OnRspQryInstrumentMarginRate(void* pTraderApi, CThostFtdcInstrumentMarginRateField *pInstrumentMarginRate, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
    //查询投资者持仓回报
    static void __stdcall OnRspQryInvestorPosition(void* pTraderApi, CThostFtdcInvestorPositionField *pInvestorPosition, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
    
    //查询持仓详细回报
    static void __stdcall OnRspQryInvestorPositionDetail(void* pTraderApi, CThostFtdcInvestorPositionDetailField *pInvestorPositionDetail, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
    //查询订单回报
    static void __stdcall OnRspQryOrder(void* pTraderApi, CThostFtdcOrderField *pOrder, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
    //查询成交回报
    static void __stdcall OnRspQryTrade(void* pTraderApi, CThostFtdcTradeField *pTrade, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
    //查询投资者结算回报
    static void __stdcall OnRspQrySettlementInfo(void* pTraderApi, CThostFtdcSettlementInfoField *pSettlementInfo, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
    //查询资金账户回报
    static void __stdcall OnRspQryTradingAccount(void* pTraderApi, CThostFtdcTradingAccountField *pTradingAccount, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
    //深度行情回报
    static void __stdcall OnRtnDepthMarketData(void* pMdUserApi, CThostFtdcDepthMarketDataField *pDepthMarketData);
    //合约状态回报
    static void __stdcall OnRtnInstrumentStatus(void* pTraderApi, CThostFtdcInstrumentStatusField *pInstrumentStatus);
    //报单回报
    static void __stdcall OnRtnOrder(void* pTraderApi, CThostFtdcOrderField *pOrder);
    //成交回报
    static void __stdcall OnRtnTrade(void* pTraderApi, CThostFtdcTradeField *pTrade);
    //其他回调
    static void __stdcall OnRspQuoteAction(void* pTraderApi, CThostFtdcInputQuoteActionField *pInputQuoteAction, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
    static void __stdcall OnRspQuoteInsert(void* pTraderApi, CThostFtdcInputQuoteField *pInputQuote, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
    static void __stdcall OnRtnForQuoteRsp(void* pMdUserApi, CThostFtdcForQuoteRspField *pForQuoteRsp);
    static void __stdcall OnRtnQuote(void* pTraderApi, CThostFtdcQuoteField *pQuote);
    
private:
    //隐藏默认构造
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
    
    static void *md;//行情端口
    static void *td; //用于获取交易合约的交易端口（非交易用）
    static void *pmd, *ptd; //暂存行情端口地址
    static void *md_msgQueue; //专门用于行情队列
    static void *td_msgQueue; //交易队列，交易账户集合用
    static map<void *, int> m_tdposition; //交易账户映射
    static vector<void *> v_tds; //交易账户集合
    static DBLog dblog; //日志对象
    static string path; //con数据路径
    static string brokerid; //期商代码
    static string investor; //投资者代码
    static string password; //密码
    static string mdServer; //行情服务器地址
    static string tdServer; //交易服务器地址
    static string logpath; //日志路径
    static mutex csLog;
};

#endif