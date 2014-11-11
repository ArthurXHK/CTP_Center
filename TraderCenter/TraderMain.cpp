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
            int ind = mxGetScalar(prhs[1]);
            string inst = mxArrayToString(prhs[2]);
            string direction = mxArrayToString(prhs[3]);
            string offsetFlag = mxArrayToString(prhs[4]);
            double volume = mxGetScalar(prhs[5]);
            double price = mxGetScalar(prhs[6]);
            plhs[0] = mxCreateDoubleScalar(trader.SendOrder(ind, inst.c_str(), direction[0], offsetFlag.c_str(), volume, price));
            break;
        }
        case 5:
        {
            int ind = mxGetScalar(prhs[1]);
            string ref = mxArrayToString(prhs[2]);
            plhs[0] = trader.GetOrder(ind, ref);
            break;
        }
        default:
        {
            break;
        }
    }
}