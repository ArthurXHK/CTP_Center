// 输出日志信息
#ifndef DBLOG_H
#define DBLOG_H

#include "toolkit.h"

#include <iostream>
#include <string>
#include <mutex>
#include <atomic>
#include <Windows.h>
#include <fstream>

using namespace std;

class DBLog
{
public:
    DBLog()
    {
    }
    ~DBLog()
    {
        filestream.close();
    }
    void PrintLog(string msg, string type = "normal");
    void RegisterPath(const string &path);//注册路径
    void printpath();
private:
    fstream filestream;
    std::mutex cs_writing;
    string filepath;
    SYSTEMTIME ST;
};


#endif