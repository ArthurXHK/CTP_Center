#include <iostream>
#include<Windows.h>
#include "Account.h"
using namespace std;


int main()
{
    
    Account test;
    test.ReadInifile("E:\\workplace\\CTP_Center\\server.ini", "realServer");
    test.Connect();
    if (test.WaitForConnected())
    {
        cout << "全部链接" << endl;
        test.QryInstrument("");
        test.Subscribe("IF1411");
        test.QryTradingAccount();
    }
    else
    {
        cout << "连接超时" << endl;
    }
    
    //test.Subscribe("IF1410");

    int a;
    cin >> a;
    return 0;
}
