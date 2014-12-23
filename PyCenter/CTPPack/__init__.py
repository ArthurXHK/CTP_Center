

import MarketDataCenter
import Trader

MarketData = MarketDataCenter.MarketData
InstrumentList = MarketDataCenter.InstrumentList
MainOverEvent = MarketDataCenter.MainOverEvent
MarketEvent = MarketDataCenter.MarketEvent

Orders = Trader.Orders

def CreateTrader():
    return Trader.Trader()


def main():
    center = MarketDataCenter.MarketDataCenter()
    center.run()
    MainOverEvent.wait()
    center.Release()

if __name__ == '__main__':
    main()