function ind = Check( tick )
t = 1;
for i = 2:length(tick)
    if(abs(tick(i).time - tick(i - 1).time) > 0.00006 && abs(tick(i).time - tick(i - 1).time) < 0.0040)
        ind(t) = i;
        t = t + 1;
    end
end
if(t == 1)
    ind = [];
end
end

