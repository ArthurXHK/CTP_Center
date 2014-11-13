

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
    collection = "tick";
    mxArray *result;
    const char *field_names[] = {"tradingday", "time", "instrument", "o", "h", "l", "c", "v", "i", "a1", "b1", "av1", "bv1"};
    string instrument = mxArrayToString(inst);
    double st = mxGetScalar(start);
    double et = mxGetScalar(end);
    
    auto_ptr<DBClientCursor> cursor;
    BSONObjBuilder b;
    BSONObjBuilder timePeriod;
    
    b.append("InstrumentID", instrument);
    timePeriod.appendDate("$gte",( (st - 719529) * 24LL)* 60LL * 60LL * 1000LL);
    timePeriod.appendDate("$lte", ( (et - 719529) * 24LL) * 60LL * 60LL * 1000LL);
    b.append("UpdateTime", timePeriod.done());
    BSONObj qry = b.done();
    
    cursor = pCon->query(string("MarketData.") + collection, qry);
    int size = cursor->itcount();
    mwSize dims[2] = {1, size};
    result = mxCreateStructArray(2, dims, sizeof(field_names)/sizeof(*field_names), field_names);
    cursor = pCon->query(string("MarketData.") + collection, qry);
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

// void RemoveTick(mxArray *inst ,mxArray *start, mxArray *end)
// {
//     if(!CheckConnection())
//     {
//         PrintLog("[GetTick]δ�������ݿ�", "error");
//         return NULL;
//     }
//     collection = "tick";
// }