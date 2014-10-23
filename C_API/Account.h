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

    //��ֲ�
    void QryInvestorPosition(const char* szInstrumentId);
    //��ֲ���ϸ
    void QryInvestorPositionDetail(const char* szInstrumentId);
    //���ʽ��˺�
    void QryTradingAccount();
    //���Լ
    void QryInstrument(const char* szInstrumentId);
    //��������
    void QryInstrumentCommissionRate(const char* szInstrumentId);
    //�鱣֤��
    void QryInstrumentMarginRate(const char* szInstrumentId, TThostFtdcHedgeFlagType HedgeFlag);
    //���������
    void QryDepthMarketData(const char* szInstrumentId);
    //�����ѯͶ���߽�����
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