# -*- coding=UTF-8 -*-

import MarketDataCenter
import Trader
import StrategyCenter
import threading
MarketData = MarketDataCenter.MarketData
InstrumentList = MarketDataCenter.InstrumentList
MainOverEvent = MarketDataCenter.MainOverEvent
MarketEvent = MarketDataCenter.MarketEvent

Orders = Trader.Orders

RegisterStrategy = StrategyCenter.RegisterStrategy
HangupStrategy = StrategyCenter.HangupStrategy
StopStrategy = StrategyCenter.HangupStrategy

listOfThread = StrategyCenter.listOfThread
listOfEvent = StrategyCenter.listOfEvent
listOfEventLock = StrategyCenter.listOfEventLock



def Connect():
    global trader, market
    trader = Trader.Trader()
    market = MarketDataCenter.MarketDataCenter()
    market.Connect()
    trader.Connect()

def Release():
    trader.Release()
    market.Release()

#行情线程
def MarketThread():
    market.run()
    MainOverEvent.wait()
    MainOverEvent.clear()
    Release()
marketthread = threading.Thread(None, target=MarketThread)

#启动策略
def StartStrategy(instrument, strategyname):
    #判断策略是否已加入
    if strategyname in listOfEvent:
        print strategyname, 'is exist'
    else:
        strategyfun = getattr(StrategyCenter, strategyname)#get strategy function, maybe modify later
        strategyevent = threading.Event()
        RegisterStrategy(instrument, strategyevent)
        with listOfEventLock:
            listOfEvent[strategyname] = (instrument, strategyevent)
        strategythread = threading.Thread(None, target=strategyfun)
        #listOfThread[strategyname] = strategythread
        strategythread.start()
    
#恢复运行策略
def ResumeStrategy(strategyname):
    if strategyname not in listOfEvent:
        print strategyname, 'not exist'
    instrument, strategyevent = listOfEvent[strategyname]
    RegisterStrategy(instrument, strategyevent)
        
#启动行情
def StartMarket():
    
    if not marketthread.is_alive():
        Connect()
        
        marketthread.start()
    else: print 'Market is alive'
    
#停止行情
def StopMarket():
    MainOverEvent.set()


def SendOrder(instrument, direction, OffsetFlag, volume, price):
    trader.SendOrder(instrument, direction, OffsetFlag, volume, price)

def CancelOrder(orderref):
    trader.CancelOrder(orderref)
    
    
def main():
    
    StartMarket()
    while True:
        msg = raw_input('input: ')
        if msg == 'start':
            StartMarket()
        elif msg == 'stop':
            StopMarket()
            break
        elif msg == 'import1':
            StartStrategy('IF1501', 'testStrategy')
        elif msg == 'import2':
            StartStrategy('IF1502', 'testStrategy2')
        elif msg == 'hangup1':
            HangupStrategy('testStrategy')
        elif msg == 'hangup2':
            HangupStrategy('testStrategy2')
        elif msg == 'resume1':
            ResumeStrategy('testStrategy')
        elif msg == 'resume2':
            ResumeStrategy('testStrategy2')
        else:
            if msg in MarketData:
                print MarketData[msg].LastPrice
            else:
                print 'no inst'
    



if __name__ == '__main__':
    main()