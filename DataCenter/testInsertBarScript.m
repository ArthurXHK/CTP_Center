connectdb('198.16.100.88', 'MarketData');


instrument = inst3;

for date = datenum(2014, 11, 21) : datenum(2014, 11, 21)
    for i = 1:length(instrument)
        inst = instrument{i};
        disp([datestr(date), instrument]);
        tick = GetTick(inst, date - datenum(0, 0, 0, 4, 0, 0, 0), date + datenum(0, 0, 0, 16, 0, 0));
        
        bar = Syn1min(inst, tick);
        InsertBar(bar);
    end
    
end


disconnectdb;