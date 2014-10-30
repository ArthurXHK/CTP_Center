
#include "DataServer.h"



int main(int argc, char *argv[])
{
    
    DataServer& server = DataServer::GetAccountInstance();
    //server.ini���޸�δ���ini�ļ�
    while (!server.ConnectMdServer("E:\\workplace\\CTP_Center\\server.ini", "DataServer"))
        server.Release();
    mongo::HANDLE h_heartbeat = server.StartHeartBeat();

    server.QryInstrument("");
    server.SubscribeAll();
    WaitForSingleObject(h_heartbeat, INFINITE);
    return 0;
}
