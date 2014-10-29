#include "DBLog.h"


void DBLog::printpath()
{
    cout << filepath << endl;
}

void DBLog::PrintLog(string msg, string type)
{
    lock_guard<mutex> cl(cs_writing);
    GetLocalTime(&ST);
    string time = "[";
    string tmp;
    time += to_string(ST.wYear) + '-';
    time += (tmp = to_string(ST.wMonth), tmp.size() == 1 ? string("0") + tmp : tmp) + '-';
    time += (tmp = to_string(ST.wDay), tmp.size() == 1 ? string("0") + tmp : tmp) + 'T';
    time += (tmp = to_string(ST.wHour), tmp.size() == 1 ? string("0") + tmp : tmp) + ':';
    time += (tmp = to_string(ST.wMinute), tmp.size() == 1 ? string("0") + tmp : tmp) + ':';
    time += (tmp = to_string(ST.wSecond), tmp.size() == 1 ? string("0") + tmp : tmp) + '.';
    tmp = to_string(ST.wMilliseconds);
    if (tmp.size() == 2)
        tmp = string("0") + tmp;
    else if (tmp.size() == 1)
        tmp = string("00") + tmp;
    time += tmp + string("Z] [") + string(type) + string("]: ");
    filestream << time << msg << endl;
    //you can replace this for other lang's print function
    cout << time << msg << endl;
}

