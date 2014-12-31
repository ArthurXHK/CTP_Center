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

listOfThread = StrategyCenter.listOfThread
listOfEvent = StrategyCenter.listOfEvent
listOfEventLock = StrategyCenter.listOfEventLock


strategyPack = StrategyCenter

trader = ''
market = ''




def MarketThread():
    '''行情线程'''
    market.run()
    MainOverEvent.wait()
    MainOverEvent.clear()
    Release()
marketthread = threading.Thread(None, target=MarketThread)

def Connect():
    '''连接端口'''
    global trader, market
    trader = Trader.Trader()
    market = MarketDataCenter.MarketDataCenter()
    res = True
    if market.Connect() == False or trader.Connect() == False:
        res = False
    if res == False:
        Release()
    return res
def Release():
    '''释放端口'''
    trader.Release()
    market.Release()




def SetStrategyPack(strategypack):
    '''设置使用策略包'''
    global strategyPack
    strategyPack = strategypack
    

def StartStrategy(instrument, strategyname):
    '''启动策略'''
    if strategyname in listOfEvent:
        print strategyname, 'is exist'
    else:
        strategyfun = getattr(strategyPack, strategyname)#get strategy function, maybe modify later
        strategyevent = threading.Event()
        RegisterStrategy(instrument, strategyevent)
        with listOfEventLock:
            listOfEvent[strategyname] = (instrument, strategyevent)
        strategythread = threading.Thread(None, target=strategyfun)
        #listOfThread[strategyname] = strategythread
        strategythread.start()
    
def ResumeStrategyEvent(strategyname):
    '''恢复运行策略'''
    if strategyname not in listOfEvent:
        print strategyname, 'not exist'
    instrument, strategyevent = listOfEvent[strategyname]
    RegisterStrategy(instrument, strategyevent)


def StartMarket():
    '''启动行情'''
    if not marketthread.is_alive():
        if Connect():
            marketthread.start()
        else:
            print 'connection error'
    else: print 'Market is alive'
    
def StopMarket():
    '''停止行情'''
    MainOverEvent.set()


def SendOrder(instrument, direction, OffsetFlag, volume, price):
    trader.SendOrder(instrument, direction, OffsetFlag, volume, price)

def CancelOrder(orderref):
    trader.CancelOrder(orderref)
    
    
def main():
    print Connect()
    '''
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
    '''



if __name__ == '__main__':
    main()