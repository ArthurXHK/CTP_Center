% connectdb('198.16.100.88', 'MarketData');
connectdb('localhost', 'MarketData');

% tick = GetTick('ag1412', datenum(2014, 11, 17, 20, 0, 0) , today + 1);
bar1 = GetBar('ag1412', 1, datenum(2014, 11, 17, 20,0,0), datenum(2014, 11, 17, 22, 0, 0));
% bar = Syn1min('ag1412', tick);
% InsertBar(bar);
disconnectdb;

