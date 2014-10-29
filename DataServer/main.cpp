
#include "DataServer.h"
using namespace std;


int main(int argc, char *argv[])
{
    
    DataServer& server = DataServer::GetAccountInstance();
    while (!server.ConnectMdServer("E:\\workplace\\CTP_Center\\server.ini", "simServer"));
    server.Subscribe("IF1411");
    
    
    return 0;
}
