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

// ��ȡunix epochʱ��
time_t GetEpochTime(SYSTEMTIME st, string UpdateTime, int milisecond);

//ת��GBK���ĵ�UTF8��ʽ
string GBKToUTF8(const char* strGBK);

//ת��������Ϣ
string ConnectionStatusMsg(const ConnectionStatus &status);
#endif 
