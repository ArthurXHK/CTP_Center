#include "Trader.h"

void mexFunction(int nlhs, mxArray *plhs[], int nrhs, mxArray *prhs[])
{
    Trader &trader = Trader::GetInstance();
    int choise = (int)mxGetScalar(prhs[0]);
    
    
    switch(choise)
    {
        //连接数据服务器
        case 1:
        {
            trader.ConnectMdServer(mxArrayToString(prhs[1]), mxArrayToString(prhs[2]));
            break;
        }
        //创建交易账户
        case 2:
        {
            plhs[0] = mxCreateDoubleScalar(trader.CreateTdAccount(mxArrayToString(prhs[1]), mxArrayToString(prhs[2])));
            break;
        }
        //释放交易账户
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
        //下单
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
        //获取订单
        case 5:
        {
            int ind = mxGetScalar(prhs[1]);
            string ref = mxArrayToString(prhs[2]);
            plhs[0] = trader.GetOrder(ind, ref);
            break;
        }
        //撤单
        case 6:
        {
            int ind = mxGetScalar(prhs[1]);
            string ref = mxArrayToString(prhs[2]);
            plhs[0] = mxCreateLogicalScalar(trader.CancelOrder(ind, ref));
            break;
        }
        default:
        {
            break;
        }
    }
}