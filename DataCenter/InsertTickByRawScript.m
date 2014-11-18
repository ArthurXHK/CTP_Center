connectdb('198.16.100.88', 'MarketData');

rawdir = 'F:\rawdata';
filedir = dir(rawdir);
filedir = {filedir.name}';
for i = 3:length(filedir)
    
    file = dir(fullfile(rawdir, filedir{i}));
    file = {file.name}';
    for j = 1:length(file);
        %         disp(length(file(j)));
        if(length(cellstr(file)) < 3)
            disp(length(file(j)));
        else
            filepath = cell2mat(fullfile(rawdir, filedir(i), file(j)));
            
            ind = find(filepath == '_');
            ind2 = find(filepath == '\');
            if(length(ind) ~= 2 || ind(2) - ind(1) < 8)
                warning(['�Ƿ��ļ���: ', filepath]);
            else
                inst = filepath(ind2(3) + 1 : ind(1) - 1);
                date = datenum(filepath(ind(1)  + 1 : ind(2) - 1), 'yyyymmdd');
                disp(['����ɾ��: ', filepath]);
                RemoveTick(inst, date - datenum(0, 0, 0, 7, 0, 0), date + datenum(0, 0, 0, 16, 0, 0));
                disp(['����д��: ', filepath]);
                ok = InsertTickByRaw(filepath);
                if(~ok)
                    warning(['д���ļ�����: ', filepath]);
                end
            end
        end
    end
end

disconnectdb;