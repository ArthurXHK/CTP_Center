connectdb('localhost', 'MarketData');


instrument = GetInstrument();

for date = datenum(2014, 1, 1) : today
    for i = 1:length(instrument)
        inst = instrument{i};
        tick = GetTick(inst, date - datenum(0, 0, 0, 4, 0, 0, 0), date + datenum(0, 0, 0, 16, 0, 0));
        
        bar = Syn1min(inst, tick);
    end
    
end


