#此项目为基于CTP的一系列项目
在vs2013，32位matlab运行
编译前请添加CTP_Center环境变量为当前项目位置如：CTP_Center: E:\workplace\CTP_Center

## FrameDll
将原始CTP接口封装为DLL，源码为QuantBox的C接口，修改增加了一些其他机制。

## C_API
调用FrameDll产生的dll

## DataServer
基于mongodb和CTP的自动收集处理数据服务器

## DataCenter
基于matlab和mongodb的数据处理终端（客户端）

## TraderCenter
基于matlab和CTP的交易终端

## test
测试中心