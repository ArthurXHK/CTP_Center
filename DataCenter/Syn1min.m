function bar = Syn1min( inst , tick )

if(~isempty(tick))
    tick = Process(tick);
    % starttime = datenum(0, 0, 0, 20, 54, 0);
    % endtime = datenum(0, 0, 1, 15, 16, 0);
    td = sscanf(num2str(tick(1).tradingday), '%4d%2d%2d');
    tbar = 0;
    ttime = [tick.time];
    for i = 20 * 60 + 54 : (24 + 15) * 60 + 16
        ttick = tick(ttime >= datenum(0, 0, 0, 0, i, 0) & ttime < datenum(0, 0, 0, 0, i + 1, 0));
        if(~isempty(ttick))
            tbar = tbar + 1;
            
            % 转换为GTD时间
            bar(tbar).time = datenum(datestr(datenum(td(1), td(2), td(3), -8, i, 0)));
            bar(tbar).time = round(8.64e7 * (bar(tbar).time - datenum('1970', 'yyyy')));
            bar(tbar).type = 1;
            bar(tbar).instrument = inst;
            bar(tbar).o = ttick(1).c;
            bar(tbar).h = max([ttick.c]);
            bar(tbar).l = min([ttick.c]);
            bar(tbar).c = ttick(end).c;
            bar(tbar).v = sum([ttick.v]);
            bar(tbar).i = ttick(end).i;
        end
    end
    if(tbar == 0)
        bar = [];
    end
else
    bar = [];
end

end

function tick = Process(tick1)

for i = length(tick1):-1:2
    tick1(i).v = tick1(i).v - tick1(i - 1).v;
end
for i = 1:length(tick1)
    hm = sscanf(num2str(tick1(i).time + 0.0000005, '%f'), '%2d.%2d%2d');
    if(hm(1) >= 18)
        tick1(i).time = datenum(0, 0, 0, hm(1), hm(2), hm(3));
    else
        tick1(i).time = datenum(0, 0, 1, hm(1), hm(2), hm(3));
    end
    
end
tick = tick1;
end