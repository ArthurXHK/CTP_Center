from CTPUserApiStruct import *
from MarketDataCenter import *

class StrategyCenter(MarketDataCenter):
    
    
    def __RegisterCallback(self):
        pass
    
    
if __name__ == '__main__':
    center = MarketDataCenter()
    print center
    if center.Connect():
        center.QryInstrument('')
        
        center.SubscribeAll()
        
        center.Join()
        