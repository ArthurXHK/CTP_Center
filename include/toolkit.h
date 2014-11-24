#ifndef _TOOLKIT_H_
#define _TOOLKIT_H_

#include "ThostFtdcUserApiStruct.h"
#include "QuantBox.C2CTP.h"

#include <vector>
#include <set>
#include <string>
#include <ctime>
#include <Windows.h>
#include <fstream>
#include <iostream>
using namespace std;

// 获取unix epoch时间
time_t GetEpochTime(char *st, string UpdateTime, int milisecond);
//获取1min时间
time_t GetBarTime(char *st, string UpdateTime);
//转换GBK中文到UTF8格式
string GBKToUTF8(const char* strGBK);

//转换连接信息
string ConnectionStatusMsg(const ConnectionStatus &status);
#endif 
