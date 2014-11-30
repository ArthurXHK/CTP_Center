

#include "DataCenter.h"

mongo::DBClientConnection *DataCenter::pCon;
DBLog DataCenter::dblog;
string DataCenter::serverIP;
string DataCenter::database;
string DataCenter::collection;

bool DataCenter::CheckConnection()
{
    if (NULL == pCon)
        return false;
    return true;
}
bool DataCenter::connect(const string ip, const string db)
{
    if(pCon == NULL)
        pCon = new mongo::DBClientConnection();
    else
    {
        PrintLog("[connect]�Ѿ����ӵ�������", "error");
        serverIP = ip;
        database = db;
        return false;
    }
    try
    {
        pCon->connect(ip);
    }
    catch (const mongo::DBException &e)
    {
        PrintLog(e.what(), "error");
        delete pCon;
        pCon = NULL;
        return false;
    }
    database = db;
    PrintLog("���ݿ����ӳɹ�");
    
    return true;
}
void DataCenter::disconnect()
{
    if(pCon == NULL)
        PrintLog("[disconnect]δ���ӵ����ݿ�", "error");
    else
    {
        delete pCon;
        pCon = NULL;
        PrintLog("���ݿ�Ͽ��ɹ�");
    }
}

void DataCenter::PrintLog(string msg, string type)
{
    if (type == string("error"))
    {
        mexWarnMsgTxt(msg.c_str());
        dblog.PrintLog(msg, type);
        return ;
    }
    mexPrintf((msg + '\n').c_str());
    dblog.PrintLog(msg, type);
}

mxArray *DataCenter::GetTick(mxArray *inst, mxArray *start, mxArray *end)
{
    if(!CheckConnection())
    {
        PrintLog("[GetTick]δ�������ݿ�", "error");
        return NULL;
    }
    mxArray *result;
    const char *field_names[] = {"tradingday", "time", "instrument", "o", "h", "l", "c", "v", "i", "a1", "b1", "av1", "bv1"};
    string instrument = mxArrayToString(inst);
    double st = mxGetScalar(start);
    double et = mxGetScalar(end);
    if (et - st > 3)
    {
        PrintLog("��ѯ��Χ̫��: �벻Ҫ������ѯ�������죬��С��Χ��ѯƴ��", "error");
        return NULL;
    }
    auto_ptr<DBClientCursor> cursor;
    BSONObjBuilder b;
    BSONObjBuilder timePeriod;
    
    b.append("InstrumentID", instrument);
    timePeriod.appendDate("$gte",( (st - 719529) * 24LL - 8)* 60LL * 60LL * 1000LL);
    timePeriod.appendDate("$lte", ( (et - 719529) * 24LL - 8) * 60LL * 60LL * 1000LL);
    b.append("UpdateTime", timePeriod.done());
    BSONObj qry = b.done();
    
    cursor = pCon->query(database + ".tick", qry);
    int size = cursor->itcount();
    mwSize dims[2] = {1, size};
    result = mxCreateStructArray(2, dims, sizeof(field_names)/sizeof(*field_names), field_names);
    cursor = pCon->query(database + ".tick", qry);
    BSONObj p;
    
    
    
    int i = 0;
    while(cursor->more())
    {
        if(i >= size)
        {
            PrintLog("��ѯ��Χ��д�뷶Χ��", "error");
            break;
        }
        p = cursor->next();
        tm buf;
        //turn into peking time;
        Date_t pkTime = Date_t(p["UpdateTime"].Date().millis + 8 * 3600000LL);
        double time = pkTime.millis%1000 / 100 / 100000.0;
        pkTime.toTm(&buf);
        int day = (buf.tm_year + 1900) * 10000 + (buf.tm_mon + 1) * 100 + buf.tm_mday;
        time = time + buf.tm_hour + buf.tm_min / 100.0 + buf.tm_sec / 10000.0;
        
        mxSetField(result, i, "tradingday", mxCreateDoubleScalar(day));
        mxSetField(result, i, "time", mxCreateDoubleScalar(time));
        mxSetField(result, i, "instrument", mxCreateString(instrument.c_str()));
        mxSetField(result, i, "o", mxCreateDoubleScalar( p["OpenPrice"].Double() ));
        mxSetField(result, i, "h", mxCreateDoubleScalar(p["HighestPrice"].Double()));
        mxSetField(result, i, "l", mxCreateDoubleScalar(p["LowestPrice"].Double()));
        mxSetField(result, i, "c", mxCreateDoubleScalar(p["LastPrice"].Double()));
        mxSetField(result, i, "v", mxCreateDoubleScalar(p["Volume"].Int()));
        mxSetField(result, i, "i", mxCreateDoubleScalar(p["OpenInterest"].Double()));
        mxSetField(result, i, "a1", mxCreateDoubleScalar(p["AskPrice1"].Double()));
        mxSetField(result, i, "b1", mxCreateDoubleScalar(p["BidPrice1"].Double()));
        mxSetField(result, i, "av1", mxCreateDoubleScalar(p["AskVolume1"].Int()));
        mxSetField(result, i, "bv1", mxCreateDoubleScalar(p["BidVolume1"].Int()));
        ++i;
    }
    return result;
}

void DataCenter::RemoveTick(mxArray *inst ,mxArray *start, mxArray *end)
{
    
    if(!CheckConnection())
    {
        PrintLog("[RemoveTick]δ�������ݿ�", "error");
        return ;
    }
    string instrument = mxArrayToString(inst);
    double st = mxGetScalar(start);
    double et = mxGetScalar(end);
    BSONObjBuilder b;
    BSONObjBuilder timePeriod;
    if (instrument.size() > 0)
    {
        b.append("InstrumentID", instrument);
    }
    timePeriod.appendDate("$gte",( (st - 719529) * 24LL - 8)* 60LL * 60LL * 1000LL);
    timePeriod.appendDate("$lte", ( (et - 719529) * 24LL - 8) * 60LL * 60LL * 1000LL);
    b.append("UpdateTime", timePeriod.done());
    pCon->remove(database + ".tick", b.done());
}


time_t DataCenter::GetEpochTime(char *st, string UpdateTime, int milisecond)
{
    if(NULL == st)
        return 0;
    struct tm t;
    time_t res;
    sscanf(st, "%4d%2d%2d", &t.tm_year, &t.tm_mon, &t.tm_mday);
    t.tm_year = t.tm_year - 1900;
    t.tm_mon = t.tm_mon - 1;
    t.tm_mday = t.tm_mday;

    sscanf(UpdateTime.c_str(), "%d:%d:%d", &t.tm_hour, &t.tm_min, &t.tm_sec);
    t.tm_isdst = -1;
    res = mktime(&t);
    //��������ϰ�ҹǰ���һ��ʱ��
    if (t.tm_hour >= 18 && t.tm_hour <= 24)
    {
        res -= 24 * 60 * 60;
    }
    return res * 1000 + milisecond;
}

time_t DataCenter::GetBarTime(char *st, string UpdateTime)
{
    if(NULL == st)
        return 0;
    struct tm t;
    time_t res;
    sscanf(st, "%4d%2d%2d", &t.tm_year, &t.tm_mon, &t.tm_mday);
    t.tm_year = t.tm_year - 1900;
    t.tm_mon = t.tm_mon - 1;
    t.tm_mday = t.tm_mday;
    t.tm_sec = 0;
    sscanf(UpdateTime.c_str(), "%d:%d", &t.tm_hour, &t.tm_min);
    t.tm_isdst = -1;
    res = mktime(&t);
    //����ǰ�ҹǰ���һ��ʱ��
    if (t.tm_hour >= 18 && t.tm_hour <= 24)
    {
        res -= 24 * 60 * 60;
    }
    return res * 1000;
}

bool DataCenter::InsertTickByRawfile(mxArray *file)
{
    static double INF = 1e+100;
    if(!CheckConnection())
    {
        PrintLog("[InsertTickByRawfile]δ�������ݿ�", "error");
        return false;
    }
    string sFile = mxArrayToString(file);
    mongo::HANDLE hFile = ::CreateFileA(sFile.c_str(), GENERIC_READ, 0, NULL, OPEN_EXISTING, FILE_ATTRIBUTE_NORMAL, NULL);

    //mongo��HANDLE��windows��ͻ����ʱ�Դ˴���
    if (hFile != ((mongo::HANDLE)(LONG_PTR)-1))//hFile != INVALID_HANDLE_VALUE
    {
        CThostFtdcDepthMarketDataFieldOld *pDepthMarketData = new CThostFtdcDepthMarketDataFieldOld;
        DWORD readsize = 0;
        int len = GetFileSize(hFile, NULL);
        len = len / sizeof(CThostFtdcDepthMarketDataFieldOld);
        
        for (int i = 0; i < len; ++i)
        {
            bool ok = ReadFile(hFile, pDepthMarketData, sizeof(CThostFtdcDepthMarketDataFieldOld), &readsize, NULL);
            BSONObjBuilder b;
            b.appendDate("UpdateTime", Date_t(GetEpochTime(pDepthMarketData->TradingDay, pDepthMarketData->UpdateTime, pDepthMarketData->UpdateMillisec)));
            b.append("InstrumentID", pDepthMarketData->InstrumentID);
            b.append("OpenPrice", pDepthMarketData->OpenPrice > INF ? -1 : pDepthMarketData->OpenPrice);
            b.append("HighestPrice", pDepthMarketData->HighestPrice > INF ? -1 : pDepthMarketData->HighestPrice);
            b.append("LowestPrice", pDepthMarketData->LowestPrice > INF ? -1 : pDepthMarketData->LowestPrice);
            b.append("ClosePrice", pDepthMarketData->ClosePrice > INF ? -1 : pDepthMarketData->ClosePrice);
            b.append("LastPrice", pDepthMarketData->LastPrice > INF ? -1 : pDepthMarketData->LastPrice);
            b.append("Volume", pDepthMarketData->Volume);
            b.append("AskPrice1", pDepthMarketData->AskPrice1 > INF ? -1 : pDepthMarketData->AskPrice1);
            b.append("BidPrice1", pDepthMarketData->BidPrice1 > INF ? -1 : pDepthMarketData->BidPrice1);
            b.append("AskVolume1", pDepthMarketData->AskVolume1);
            b.append("BidVolume1", pDepthMarketData->BidVolume1);
            b.append("Turnover", pDepthMarketData->Turnover > INF ? -1 : pDepthMarketData->Turnover);
            b.append("UpperLimitPrice", pDepthMarketData->UpperLimitPrice > INF ? -1 : pDepthMarketData->UpperLimitPrice);
            b.append("LowerLimitPrice", pDepthMarketData->LowerLimitPrice > INF ? -1 : pDepthMarketData->LowerLimitPrice);
            b.append("AveragePrice", pDepthMarketData->AveragePrice > INF ? -1 : pDepthMarketData->AveragePrice);
            b.append("PreSettlementPrice", pDepthMarketData->PreSettlementPrice > INF ? -1 : pDepthMarketData->PreSettlementPrice);
            b.append("PreClosePrice", pDepthMarketData->PreClosePrice > INF ? -1 : pDepthMarketData->PreClosePrice);
            b.append("PreOpenInterest", pDepthMarketData->PreOpenInterest > INF ? -1 : pDepthMarketData->PreOpenInterest);
            b.append("OpenInterest", pDepthMarketData->OpenInterest > INF ? -1 : pDepthMarketData->OpenInterest);
            b.append("SettlementPrice", pDepthMarketData->SettlementPrice > INF ? -1 : pDepthMarketData->SettlementPrice);
            pCon->insert(database + ".tick", b.done());
            UpdateBar(pDepthMarketData);
        }
        CloseHandle(hFile);
        return true;
    }
    else
    {
        CloseHandle(hFile);
        return false;
    }
    CloseHandle(hFile);
    return true;
}

void DataCenter::UpdateBar(CThostFtdcDepthMarketDataFieldOld *pDepthMarketData)
{
    BSONObjBuilder b;
//     BSONObjBuilder timePeriod;
    Date_t time = Date_t(GetBarTime(pDepthMarketData->TradingDay, pDepthMarketData->UpdateTime));
    b.append("instrument", pDepthMarketData->InstrumentID);
    b.append("type", 1);
//     timePeriod.appendDate("$gte", time - 1);
//     timePeriod.appendDate("$lte", time + 1);
    b.append("time", time);
    BSONObj qry = b.done();

    auto_ptr<DBClientCursor> cursor;
    cursor = pCon->query(database + ".bar", qry);
    BSONObjBuilder bsonbar;
    bsonbar.append("instrument", pDepthMarketData->InstrumentID);
    bsonbar.append("time", time);
    bsonbar.append("type", 1);
    bsonbar.append("v", pDepthMarketData->Volume);
    bsonbar.append("i", pDepthMarketData->OpenInterest);
        
    if (cursor->more())
    {
        BSONObj p = cursor->next();
        bsonbar.append("o", p["o"].Double());
        bsonbar.append("h", p["h"].Double() > pDepthMarketData->LastPrice ? p["h"].Double() : pDepthMarketData->LastPrice);
        bsonbar.append("l", p["l"].Double() < pDepthMarketData->LastPrice ? p["l"].Double() : pDepthMarketData->LastPrice);
        bsonbar.append("c", pDepthMarketData->LastPrice);
        
        pCon->update(database + ".bar", qry, bsonbar.done());
    }
    else
    {
        bsonbar.append("o", pDepthMarketData->LastPrice);
        bsonbar.append("h", pDepthMarketData->LastPrice);
        bsonbar.append("l",  pDepthMarketData->LastPrice);
        bsonbar.append("c", pDepthMarketData->LastPrice);
        pCon->insert(database + ".bar", bsonbar.done());
    }
}

void DataCenter::InsertBar(mxArray *bar)
{
    if(!CheckConnection())
    {
        PrintLog("[InsertBar]δ�������ݿ�", "error");
        return ;
    }
    int len = mxGetNumberOfElements(bar);
    for(int i = 0; i < len; ++i)
    {
        BSONObjBuilder b;
        b.append("instrument", mxArrayToString(mxGetField(bar, i, "instrument")));
        b.appendDate("time", Date_t((long long)mxGetScalar(mxGetField(bar, i, "time")) ));
        b.append("type", (int)mxGetScalar(mxGetField(bar, i, "type")));
        b.append("o", mxGetScalar(mxGetField(bar, i, "o")));
        b.append("h", mxGetScalar(mxGetField(bar, i, "h")));
        b.append("l", mxGetScalar(mxGetField(bar, i, "l")));
        b.append("c", mxGetScalar(mxGetField(bar, i, "c")));
        b.append("v", mxGetScalar(mxGetField(bar, i, "v")));
        b.append("i", mxGetScalar(mxGetField(bar, i, "i")));
        pCon->insert(database + ".bar", b.done());
    }
}

mxArray *DataCenter::GetBar(mxArray *inst, mxArray *tp, mxArray *start, mxArray *end)
{
    if(!CheckConnection())
    {
        PrintLog("[GetBar]δ�������ݿ�", "error");
        return NULL;
    }
    mxArray *result;
    const char *field_names[] = {"tradingday", "time", "instrument", "type", "o", "h", "l", "c", "v", "i"};
    
    string instrument = mxArrayToString(inst);
    int type = mxGetScalar(tp);
    double st = mxGetScalar(start);
    double et = mxGetScalar(end);
    auto_ptr<DBClientCursor> cursor;
    BSONObjBuilder b;
    BSONObjBuilder timePeriod;
    
    b.append("instrument", instrument);
    b.append("type", type);
    timePeriod.appendDate("$gte",( (st - 719529) * 24LL - 8)* 60LL * 60LL * 1000LL);
    timePeriod.appendDate("$lte", ( (et - 719529) * 24LL - 8) * 60LL * 60LL * 1000LL);
    b.append("time", timePeriod.done());
    BSONObj qry = b.done();
    
    cursor = pCon->query(database + ".bar", qry);
    int size = cursor->itcount();
    mwSize dims[2] = {1, size};
    result = mxCreateStructArray(2, dims, sizeof(field_names)/sizeof(*field_names), field_names);
    cursor = pCon->query(database + ".bar", qry);
    BSONObj p;
    
    int i = 0;
    
    while(cursor->more())
    {
        if(i >= size)
        {
            mexWarnMsgTxt("��ѯ��Χ������д�뷶Χ��\n");
            break;
        }
        p = cursor->next();
        tm buf;
        
        Date_t pkTime = Date_t(p["time"].Date().millis + 8 * 3600000LL);
        double time = pkTime.millis%1000 / 100 / 100000.0;
        pkTime.toTm(&buf);
        int day = (buf.tm_year + 1900) * 10000 + (buf.tm_mon + 1) * 100 + buf.tm_mday;
        time = time + buf.tm_hour + buf.tm_min / 100.0 + buf.tm_sec / 10000.0;
        
        mxSetField(result, i, "tradingday", mxCreateDoubleScalar(day));
        mxSetField(result, i, "time", mxCreateDoubleScalar(time));
        mxSetField(result, i, "instrument", mxCreateString(instrument.c_str()));
        mxSetField(result, i, "type", mxCreateDoubleScalar(type));
        mxSetField(result, i, "o", mxCreateDoubleScalar( p["o"].Double() ));
        mxSetField(result, i, "h", mxCreateDoubleScalar(p["h"].Double()));
        mxSetField(result, i, "l", mxCreateDoubleScalar(p["l"].Double()));
        mxSetField(result, i, "c", mxCreateDoubleScalar(p["c"].Double()));
        mxSetField(result, i, "v", mxCreateDoubleScalar(p["v"].Int()));
        mxSetField(result, i, "i", mxCreateDoubleScalar(p["i"].Double()));
        ++i;
        
    }
    return result;
}

mxArray *DataCenter::GetInstrument(mxArray *inst)
{
    mxArray *result;
    const char *field_names[] = {"InstrumentID", "ExchangeID", "InstrumentName",
    "ProductID", "DeliveryYear", "DeliveryMonth",
    "PriceTick", "CreateDate", "OpenDate", "ExpireDate",
    "StartDelivDate", "EndDelivDate", "LongMarginRatio", "ShortMarginRatio"};
    string instrument = mxArrayToString(inst);
    auto_ptr<DBClientCursor> cursor;
    BSONObjBuilder b;
    int size = 0;
    if(instrument.size() > 2)
    {
        b.append("InstrumentID", instrument);
        cursor = pCon->query(database + ".instrument", b.done());
        size = 1;
    }
    else if(instrument.size() == 0)
    {
        size = pCon->count(database + ".instrument");
        cursor = pCon->query(database + ".instrument", BSONObj());
    }
    else
    {
        b.append("ProductID", instrument);
        BSONObj qry = b.done();
        cursor = pCon->query(database + ".instrument", qry);
        size = cursor->itcount();
        cursor = pCon->query(database + ".instrument", qry);
    }
    
    mwSize dims[2] = {1, size};
    result = mxCreateStructArray(2, dims, sizeof(field_names)/sizeof(*field_names), field_names);
    int i = 0;
    BSONObj p;
    while(cursor->more())
    {
        if(i >= size)
        {
            mexWarnMsgTxt("��ѯʱ���ݿ�����д���Լ��Ϣ");
            break;
        }
        p = cursor->next();
        mxSetField(result, i, "InstrumentID", mxCreateString(p["InstrumentID"].String().c_str()));
        mxSetField(result, i, "ExchangeID", mxCreateString(p["ExchangeID"].String().c_str()));
        mxSetField(result, i, "InstrumentName", mxCreateString(p["InstrumentName"].String().c_str()));
        mxSetField(result, i, "ProductID", mxCreateString(p["ProductID"].String().c_str()));
        mxSetField(result, i, "DeliveryYear", mxCreateDoubleScalar(p["DeliveryYear"].Int()));
        mxSetField(result, i, "DeliveryMonth", mxCreateDoubleScalar(p["DeliveryMonth"].Int()));
        mxSetField(result, i, "PriceTick", mxCreateDoubleScalar(p["PriceTick"].Double()));
        mxSetField(result, i, "CreateDate", mxCreateString(p["CreateDate"].String().c_str()));
        mxSetField(result, i, "OpenDate", mxCreateString(p["OpenDate"].String().c_str()));
        mxSetField(result, i, "ExpireDate", mxCreateString(p["ExpireDate"].String().c_str()));
        mxSetField(result, i, "StartDelivDate", mxCreateString(p["StartDelivDate"].String().c_str()));
        mxSetField(result, i, "EndDelivDate", mxCreateString(p["EndDelivDate"].String().c_str()));
        mxSetField(result, i, "LongMarginRatio", mxCreateDoubleScalar(p["LongMarginRatio"].Double()));
        mxSetField(result, i, "ShortMarginRatio", mxCreateDoubleScalar(p["ShortMarginRatio"].Double()));
        
        ++i;
    }
    return result;
}