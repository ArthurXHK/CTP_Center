function ind = Login(varargin)

inifile = '..\server.ini';
server = 'SimServer';
if nargin >= 1
    server = varargin{1};
end
if nargin == 2
    inifile = varargin{2};
end
ind = TraderMain(2, inifile, server);

end

