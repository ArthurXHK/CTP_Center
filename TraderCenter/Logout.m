function Logout(varargin)
if (nargin > 0)
    TraderMain(3, varargin{1});
else
    TraderMain(3);
    clear TraderMain;
end

end

