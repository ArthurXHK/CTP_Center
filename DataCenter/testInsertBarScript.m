connectdb('198.16.100.11', 'MarketData');

rawdir = dir('E:\rawdata');
rawdir = {rawdir.name}';
for i = 3:length(rawdir)
    filedir = fullfile('E:\rawdata', rawdir{i});
    file = dir(filedir);
    file = {file.name}';
    for j = 3:length(file)
        File = fullfile(filedir, file{j});
        
        disp(File);
        InsertTickByRaw(File);
        
    end
end

disconnectdb;