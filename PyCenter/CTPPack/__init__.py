

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

def Connect():
    global trader, market
    trader = Trader.Trader()
    market = MarketDataCenter.MarketDataCenter()
    market.Connect()
    trader.Connect()

def Release():
    trader.Release()
    market.Release()

def MarketThread():
    market.run()
    MainOverEvent.wait()
    MainOverEvent.clear()
    Release()

def StartStrategy(strategyname):
    strategy = getattr(StrategyCenter, strategyname)
    strategythread = threading.Thread(None, target=strategy)
    listOfThread[strategyname] = strategythread
    strategythread.start()
    
    
def main():
    global marketthread
    Connect()
    marketthread = threading.Thread(None, target=MarketThread)
    while True:
        msg = raw_input('input: ')
        if msg == 'start':
            marketthread.start()
        elif msg == 'stop':
            MainOverEvent.set()
            break
        elif msg == 'import1':
            StartStrategy('testStrategy')
        elif msg == 'import2':
            StartStrategy('testStrategy2')
        elif msg == 'hangup':
            for i,j in StrategyCenter.listOfEvent:
                HangupStrategy(i, j)
        elif msg == 'stopstra':
            StopStrategy('testStrategy')
        else:
            if msg in MarketData:
                print MarketData[msg].LastPrice
            else:
                print 'no inst'
    



if __name__ == '__main__':
    main()