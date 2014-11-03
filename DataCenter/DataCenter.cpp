

#include "DataCenter.h"

mongo::DBClientConnection *DataCenter::pCon; //数据库连接口
DBLog DataCenter::dblog;
string DataCenter::serverIP;                          //服务器地址
string DataCenter::database;                        //当前操作数据库
string DataCenter::collection;                       //当前操作集合

bool DataCenter::connect(const string ip, const string db)
{
    if(pCon == NULL)
        pCon = new mongo::DBClientConnection();
    else
    {
        PrintLog("已经连接到服务器", "error");
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
    PrintLog("数据库连接成功");
    
    return true;
}
void DataCenter::disconnect()
{
    if(pCon == NULL)
        PrintLog("已断开连接, 未连接到数据库", "error");
    else
    {
        delete pCon;
        pCon = NULL;
        PrintLog("数据库断开成功");
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