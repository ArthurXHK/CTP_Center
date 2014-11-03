function connectdb( varargin )
switch(nargin)
    case 0
        dbmain(1);
    case 1
        dbmain(1, varargin{1});
    case 2
        dbmain(1, varargin{1}, varargin{2});
    otherwise
        error('connectdb参数个数错误[0-2]!');
end
end

