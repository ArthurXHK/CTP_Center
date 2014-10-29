
#include "Account.h"
using namespace std;


int main(int argc, char *argv[])
{
    
    Account& acc = Account::GetAccountInstance();
    if (acc.ConnectMdServer("E:\\workplace\\CTP_Center\\server.ini", "simServer"))
        cout << "已经连接" << endl;
    acc.Subscribe("IF1411");
    int accind = acc.CreateTdAccount("E:\\workplace\\CTP_Center\\server.ini", "simServer2");
    cout << accind << endl;
    accind = acc.CreateTdAccount("E:\\workplace\\CTP_Center\\server.ini", "simServer2");
    cout << accind << endl;
    int a;
    cin >> a;
    return 0;
}
