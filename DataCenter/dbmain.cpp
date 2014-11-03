
#include "DataCenter.h"

//mex主函数入口
void mexFunction(int nlhs, mxArray *plhs[], int nrhs, mxArray *prhs[])
{
    DataCenter &DCenter = DataCenter::GetInstance();
    int choise = (int)mxGetScalar(prhs[0]);
    switch(choise)
    {
        //连接数据库
        case 1:
        {
            if(1 == nrhs)
                DCenter.connect();
            else if(2 == nrhs)
                DCenter.connect(mxArrayToString(prhs[1]));
            else if(3 == nrhs)
                DCenter.connect(mxArrayToString(prhs[1]), mxArrayToString(prhs[2]));
            break;
        }
        case 2:
        {
            DCenter.disconnect();
            break;
        }
        case 3:
        {
            plhs[0] = DCenter.GetTick(prhs[1], prhs[2], prhs[3]);
            break;
        }
        case 4:
        {
            break;
        }
        case 5:
        {
            break;
        }
        case 6:
        {
            break;
        }
        case 7:
        {
            break;
        }
        case 8:
        {
            break;
        }
        default:
            mexPrintf("未找到操作\n");
            break;
    }
}