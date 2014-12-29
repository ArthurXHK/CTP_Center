import threading
import Trader, MarketDataCenter



listOfEvent = {}
listOfEventLock = threading.Lock()
listOfThread = {}
def RegisterStrategy(instrument, strategyevent):
    with MarketDataCenter.MarketEventLock:
        MarketDataCenter.MarketEvent[instrument].append(strategyevent)
        
def HangupStrategy(strategyname):
    with listOfEventLock:
        if strategyname in listOfEvent:
            instrument, strategyevent = listOfEvent[strategyname]
            with MarketDataCenter.MarketEventLock:
                MarketDataCenter.MarketEvent[instrument].remove(strategyevent)
        else:
            print strategyname, ' not exist'
"""
#no terminate method
def StopStrategy(strategyname):
    if strategyname in listOfThread:
        listOfThread[strategyname].terminate() #no terminate method
        del listOfThread[strategyname]
    else:
        print strategyname, ' not in listOfThread'
"""     
class ListExistEleError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr('listOfEvent has this element: ' + self.value)
    
def testStrategy():
    func_name = 'testStrategy'
    with listOfEventLock:
        instrument, strategyevent = listOfEvent[func_name]
    while True:
        strategyevent.wait()
        strategyevent.clear()
        with MarketDataCenter.MarketEventLock:
            
            print MarketDataCenter.MarketData[instrument].InstrumentID
            
def testStrategy2():
    func_name = 'testStrategy2'
    with listOfEventLock:
        instrument, strategyevent = listOfEvent[func_name]
    while True:
        strategyevent.wait()
        strategyevent.clear()
        with MarketDataCenter.MarketEventLock:
            
            print MarketDataCenter.MarketData[instrument].InstrumentID
            
