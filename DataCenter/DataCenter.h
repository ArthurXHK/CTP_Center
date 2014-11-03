#ifndef DATACENTER_H
#define DATACENTER_H

#pragma warning (disable: 4251)
#pragma warning (disable: 4275)

#include "mongo/client/dbclient.h"
#include "mex.h"
#include "matrix.h"
#include "DBLog.h"

#include <iostream>
#include <string>
#include <set>
#include <utility>
#include <Windows.h>
using namespace std;
using namespace mongo;
using namespace bson;

class DataCenter
{
public:
    static DataCenter& GetInstance()
    {
        static DataCenter datacenter;
        return datacenter;
    }
    bool connect(const string ip = "localhost", const string db = "testMarketData");
    void disconnect();
private:
    DataCenter()
    {
        serverIP = "localhost"; database = "testMarketData"; collection = "";
        dblog.RegisterPath("..\\DataCenter\\log");
        pCon = NULL;
    }
    ~DataCenter(){}
    DataCenter& operator=(DataCenter const&){}
    void PrintLog(string msg, string type = "normal");
    static mongo::DBClientConnection *pCon; //数据库连接口
    static DBLog dblog;
    static string serverIP;                          //服务器地址
    static string database;                        //当前操作数据库
    static string collection;                       //当前操作集合
};

#endif