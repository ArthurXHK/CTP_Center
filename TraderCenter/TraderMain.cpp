#include "Trader.h"

void mexFunction(int nlhs, mxArray *plhs[], int nrhs, mxArray *prhs[])
{
    Trader &trader = Trader::GetInstance();
    int choise = (int)mxGetScalar(prhs[0]);
    
    
    switch(choise)
    {
        case 1:
        {
            trader.ConnectMdServer(mxArrayToString(prhs[1]), mxArrayToString(prhs[2]));
            break;
        }
        case 2:
        {
            plhs[0] = mxCreateDoubleScalar(trader.CreateTdAccount(mxArrayToString(prhs[1]), mxArrayToString(prhs[2])));
            break;
        }
        case 3:
        {
            if(nrhs == 1)
                trader.ReleaseTrader();
            else if(nrhs == 2)
            {
                trader.ReleaseTrader(mxGetScalar(prhs[1]));
            }
            break;
        }
        case 4:
        {
            
            break;
        }
        default:
        {
            break;
        }
    }
}