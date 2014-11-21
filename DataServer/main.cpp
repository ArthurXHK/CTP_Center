
#include "DataServer.h"

int main(int argc, char *argv[])
{
    string inifile = "..\\server.ini";
    string field = "DataServer";
    // Èë¿ÚÅäÖÃ
    if (argc > 1)
    {
        for (int i = 1; i < argc;)
        {
            if (strcmp(argv[i], "--inifile") == 0)
            {
                assert(argc >= i + 2);
                inifile = argv[i + 1];
                i += 2;
            }
            else if (strcmp(argv[i], "--field") == 0)
            {
                assert(argc >= i + 2);
                field = argv[i + 1];
                i += 2;
            }
        }
    }

    // Ö÷Âß¼­
    DataServer& server = DataServer::GetAccountInstance();
    while (!server.ConnectMdServer(inifile.c_str(), field.c_str()))
        server.Release();
    mongo::HANDLE h_heartbeat = server.StartHeartBeat();

    server.QryInstrument("");
    server.SubscribeAll();
    WaitForSingleObject(h_heartbeat, INFINITE);
    server.Release();
    return 0;
}
