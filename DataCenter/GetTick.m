function tick = GetTick(varargin)
st = today;
et = today + 1;
dt = datenum(0, 0, 0, 8, 0, 0);
switch(nargin)
    case 1
        tick = dbmain(3, varargin{1}, st - dt, et - dt);
    case 2
        tick = dbmain(3, varargin{1}, varargin{2} - dt, et - dt);
    case 3
        tick = dbmain(3, varargin{1}, varargin{2} - dt, varargin{3} - dt);
    otherwise
        error('GetTick参数个数错误[1-3]!');
end

end

