
#include "DataCenter.h"

//mex���������
void mexFunction(int nlhs, mxArray *plhs[], int nrhs, mxArray *prhs[])
{
    DataCenter &DCenter = DataCenter::GetInstance();
    int choise = (int)mxGetScalar(prhs[0]);
    switch(choise)
    {
        //�������ݿ�
        case 1:
        {
            DCenter.connect("198.16.100.88", "MarketData");
            break;
        }
        case 2:
        {
            DCenter.disconnect();
            break;
        }
        case 3:
        {
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
            mexPrintf("δ�ҵ�����\n");
            break;
    }
}