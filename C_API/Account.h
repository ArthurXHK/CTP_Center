#ifndef ACCOUNT_H
#define ACCOUNT_H

#include "CallBack.h"
#include "QuantBox.C2CTP.h"


#include <iostream>
#include <string>
#include <Windows.h>


using namespace std;

class Account
{
public:
    Account();
    ~Account();
    bool WaitForConnected();
    
    void ReadInifile(const char *file, const char *servername);
    void Connect();
    void Disconnect();
    void Subscribe(const char* instruments);
    void Unsubscribe(const char* instruments);

    int SendOrder(int OrderRef,
        const char* szInstrument,
        const char* szExchange,
        TThostFtdcDirectionType Direction,
        const char* szCombOffsetFlag,
        const char* szCombHedgeFlag,
        TThostFtdcVolumeType VolumeTotalOriginal,
        double LimitPrice,
        TThostFtdcOrderPriceTypeType OrderPriceType,
        TThostFtdcTimeConditionType TimeCondition,
        TThostFtdcContingentConditionType ContingentCondition,
        double StopPrice,
        TThostFtdcVolumeConditionType VolumeCondition);

    void CancelOrder(CThostFtdcOrderField *pOrder);

    //查持仓
    void QryInvestorPosition(const char* szInstrumentId);
    //查持仓明细
    void QryInvestorPositionDetail(const char* szInstrumentId);
    //查资金账号
    void QryTradingAccount();
    //查合约
    void QryInstrument(const char* szInstrumentId);
    //查手续费
    void QryInstrumentCommissionRate(const char* szInstrumentId);
    //查保证金
    void QryInstrumentMarginRate(const char* szInstrumentId, TThostFtdcHedgeFlagType HedgeFlag);
    //查深度行情
    void QryDepthMarketData(const char* szInstrumentId);
    //请求查询投资者结算结果
    void QrySettlementInfo(const char* szTradingDay);
    
private:
    void CTP_RegAllCallback();
private:
    void *md, *td, *msgQueue;
    string path;
    string brokerid;
    string investor;
    string password;
    string mdServer;
    string tdServer;
};

#endif