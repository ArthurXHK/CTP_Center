function tick = GetTick(varargin)
st = today;
et = today + 1;
switch(nargin)
    case 1
        tick = dbmain(3, varargin{1}, st, et);
    case 2
        tick = dbmain(3, varargin{1}, varargin{2}, et);
    case 3
        tick = dbmain(3, varargin{1}, varargin{2}, varargin{3});
    otherwise
        error('GetTick参数个数错误[1-3]!');
end

end

