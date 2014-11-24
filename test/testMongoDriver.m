MongoStart;
m = Mongo('198.16.100.88');
inst2 = m.distinct('MarketData.instrument', 'InstrumentID');

