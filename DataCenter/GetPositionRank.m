function res = GetPositionRank( varargin )
old = feature('DefaultCharacterSet', 'UTF8');
date = today;
inst = '';
type = '';
switch (nargin)
    case 1
        date = varargin{1};
    case 2
        date = varargin{1};
        inst = varargin{2};
    case 3
        date = varargin{1};
        inst = varargin{2};
        type = varargin{3};
    otherwise
        error('arg num error ');
end

res = dbmain(9, date, inst, type);
feature('DefaultCharacterSet', old);
end

