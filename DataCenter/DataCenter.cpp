

#include "DataCenter.h"

mongo::DBClientConnection *DataCenter::pCon; //���ݿ����ӿ�
DBLog DataCenter::dblog;
string DataCenter::serverIP;                          //��������ַ
string DataCenter::database;                        //��ǰ�������ݿ�
string DataCenter::collection;                       //��ǰ��������

bool DataCenter::connect(const string ip, const string db)
{
    if(pCon == NULL)
        pCon = new mongo::DBClientConnection();
    else
    {
        PrintLog("�Ѿ����ӵ�������", "error");
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
        PrintLog("�ѶϿ�����, δ���ӵ����ݿ�", "error");
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