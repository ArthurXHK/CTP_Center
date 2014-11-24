MongoStart;
m = Mongo('198.16.100.88');
inst = m.distinct('MarketData.tick', 'InstrumentID');

