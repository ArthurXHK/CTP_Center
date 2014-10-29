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
    DBLog(const string path) : filepath(path)
    {
        SYSTEMTIME st;
        GetLocalTime(&st);
        int len = filepath.size();
        if (len > 0 && filepath[len - 1] == '\\')
            cout << "ok" << endl;
        else
            filepath += '\\';
        filepath += to_string(st.wYear) + to_string(st.wMonth) + to_string(st.wDay) + string(".log");
        filestream.open(filepath, ios::app);
    };
    ~DBLog()
    {
        filestream.close();
    };
    void PrintLog(string msg, string type = "normal");
    void printpath();
private:
    fstream filestream;
    mutex cs_writing;
    string filepath;
    SYSTEMTIME ST;
};


#endif