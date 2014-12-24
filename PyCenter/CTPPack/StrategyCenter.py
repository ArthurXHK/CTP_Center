import threading
import Trader, MarketDataCenter



listOfEvent = {}
listOfThread = {}
def RegisterStrategy(instrument, strategyevent):
    with MarketDataCenter.MarketEventLock:
        MarketDataCenter.MarketEvent[instrument].append(strategyevent)

def HangupStrategy(strategyname):
        if strategyname in listOfEvent:
            instrument, strategyevent = listOfEvent[strategyname]
            with MarketDataCenter.MarketEventLock:
                MarketDataCenter.MarketEvent[instrument].remove(strategyevent)
        else:
            print strategyname, ' not in listOfEvent'
            
def StopStrategy(strategyname):
    if strategyname in listOfThread:
        listOfThread[strategyname].terminate() #no terminate method
        del listOfThread[strategyname]
    else:
        print strategyname, ' not in listOfThread'
        
class ListExistEleError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr('listOfEvent has this element: ' + self.value)
    
def testStrategy():
    instrument = 'IF1501'
    func_name = 'testStrategy'
    StrategyEvent = threading.Event()
    RegisterStrategy(instrument, StrategyEvent)
    
    if func_name in listOfEvent:
        raise ListExistEleError(func_name)
    
    listOfEvent[func_name] = (instrument, StrategyEvent)
    while True:
        StrategyEvent.wait()
        with MarketDataCenter.MarketEventLock:
            StrategyEvent.clear()
            print MarketDataCenter.MarketData[instrument].InstrumentID
            
def testStrategy2():
    instrument = 'IF1502'
    func_name = 'testStrategy2'
    StrategyEvent = threading.Event()
    RegisterStrategy(instrument, StrategyEvent)
    
    if func_name in listOfEvent:
        raise ListExistEleError(func_name)
    
    listOfEvent[func_name] = (instrument, StrategyEvent)
    while True:
        StrategyEvent.wait()
        with MarketDataCenter.MarketEventLock:
            StrategyEvent.clear()
            print MarketDataCenter.MarketData[instrument].InstrumentID
            
