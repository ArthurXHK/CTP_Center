#此项目为基于CTP的一系列项目
在vs2013，32位matlab运行

matlab环境请将CTP_Center\lib加入路径
请自行下载boost_1.56，将boost文件夹copy到include文件夹内，已经将用到的lib库上传

## FrameDll
将原始CTP接口封装为DLL，源码为QuantBox的C接口，修改增加了一些其他机制。

## DataServer
基于mongodb和CTP的自动收集处理数据服务器

## DataCenter
基于matlab和mongodb的数据处理终端（客户端）

## TraderCenter
基于matlab和CTP的交易终端

## PyCenter
基于python的策略处理终端

## test
测试中心