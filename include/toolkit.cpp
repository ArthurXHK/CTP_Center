

#include "toolkit.h"

// 获取unix epoch时间
time_t GetEpochTime(SYSTEMTIME st, string UpdateTime, int milisecond)
{
    struct tm t;
    time_t res;
    t.tm_year = st.wYear - 1900;
    t.tm_mon = st.wMonth - 1;
    t.tm_mday = st.wDay;

    sscanf(UpdateTime.c_str(), "%d:%d:%d", &t.tm_hour, &t.tm_min, &t.tm_sec);
    t.tm_isdst = -1;
    res = mktime(&t);
    //如果是半夜则加一天时间
    if (t.tm_hour >= 0 && t.tm_hour <= 3)
    {
        res += 24 * 60 * 60;
    }
    return res * 1000 + milisecond;
}

time_t GetBarTime(SYSTEMTIME st, string UpdateTime)
{
    struct tm t;
    time_t res;
    t.tm_year = st.wYear - 1900;
    t.tm_mon = st.wMonth - 1;
    t.tm_mday = st.wDay;
    t.tm_sec = 0;
    sscanf(UpdateTime.c_str(), "%d:%d", &t.tm_hour, &t.tm_min);
    t.tm_isdst = -1;
    res = mktime(&t);
    //如果是半夜则加一天时间
    if (t.tm_hour >= 0 && t.tm_hour <= 3)
    {
        res += 24 * 60 * 60;
    }
    return res * 1000;
}

//转换GBK中文到UTF8格式
string GBKToUTF8(const char* strGBK)
{
    int len = MultiByteToWideChar(CP_ACP, 0, strGBK, -1, NULL, 0);
    wchar_t* wstr = new wchar_t[len + 1];
    memset(wstr, 0, len + 1);
    MultiByteToWideChar(CP_ACP, 0, strGBK, -1, wstr, len);
    len = WideCharToMultiByte(CP_UTF8, 0, wstr, -1, NULL, 0, NULL, NULL);
    char* str = new char[len + 1];
    memset(str, 0, len + 1);
    WideCharToMultiByte(CP_UTF8, 0, wstr, -1, str, len, NULL, NULL);
    string strTemp = str;
    if (wstr) delete[] wstr;
    if (str) delete[] str;
    return strTemp;
}

//转换连接信息
string ConnectionStatusMsg(const ConnectionStatus &status)
{
    string res;
    switch (status)
    {

    case E_inited:
        res = "已初始化";
        break;
    case E_connecting:
        res = "连接中";
        break;
    case E_connected:
        res = "连接成功";
        break;
    case E_authing:
        res = "授权中";
        break;
    case E_authed:
        res = "授权成功";
        break;
    case E_logining:
        res = "登录中";
        break;
    case E_logined:
        res = "登陆成功";
        break;
    case E_confirming:
        res = "结算单确认中";
        break;
    case E_confirmed:
        res = "结算单已经确认";
        break;
    case E_conn_max:
        res = "连接达到最大值";
        break;
    case E_unconnected:
        res = "已断开连接";
        break;
        
    }
    return res;
}
