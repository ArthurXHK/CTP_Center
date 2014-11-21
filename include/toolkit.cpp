

#include "toolkit.h"

// ��ȡunix epochʱ��
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
    //����ǰ�ҹ���һ��ʱ��
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
    //����ǰ�ҹ���һ��ʱ��
    if (t.tm_hour >= 0 && t.tm_hour <= 3)
    {
        res += 24 * 60 * 60;
    }
    return res * 1000;
}

//ת��GBK���ĵ�UTF8��ʽ
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

//ת��������Ϣ
string ConnectionStatusMsg(const ConnectionStatus &status)
{
    string res;
    switch (status)
    {

    case E_inited:
        res = "�ѳ�ʼ��";
        break;
    case E_connecting:
        res = "������";
        break;
    case E_connected:
        res = "���ӳɹ�";
        break;
    case E_authing:
        res = "��Ȩ��";
        break;
    case E_authed:
        res = "��Ȩ�ɹ�";
        break;
    case E_logining:
        res = "��¼��";
        break;
    case E_logined:
        res = "��½�ɹ�";
        break;
    case E_confirming:
        res = "���㵥ȷ����";
        break;
    case E_confirmed:
        res = "���㵥�Ѿ�ȷ��";
        break;
    case E_conn_max:
        res = "���Ӵﵽ���ֵ";
        break;
    case E_unconnected:
        res = "�ѶϿ�����";
        break;
        
    }
    return res;
}
