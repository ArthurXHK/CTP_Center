function ConnectServer(varargin)
inifile = '..\server.ini';
server = 'DataServer';
if nargin >= 1
    server = varargin{1};
end
if nargin >= 2
    inifile = varargin{2};
end
TraderMain(1, inifile, server);
end

