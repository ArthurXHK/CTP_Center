// 输出日志信息
#ifndef DBLOG_H
#define DBLOG_H

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
        filestream.open(filepath, ios::app);
    };
    ~DBLog()
    {
        filestream.close();
    };
    void PrintLog(string msg);
    void printpath();
private:
    fstream filestream;
    mutex cs_writing;
    string filepath;
    SYSTEMTIME ST;
    
    
};


#endif