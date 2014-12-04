import re
f = open("..\\include\\ThostFtdcUserApiDataType.h")

out = open(".\\CTPApiDataType.py", 'a')
line = f.readline()
charnumPattern = re.compile('[1-9]+')
typedefPattern = re.compile('([a-z]|[A-Z])+')
out.write('from ctypes import *\n')
while line:
    
    
    if len(line) > 8:
        if line[0] != '/':
            if line[0:7] == '#define':
                line = re.split(' *', line)
                if len(line) == 3:
                    out.write(line[1] + ' = ' + line[2])
                    
            elif line[0:7] == 'typedef':
                line = re.split(' *', line)
                typestring = line[1]
                typename = typedefPattern.search(line[2])
                charnum = charnumPattern.search(line[2])
                print typename.group()
                resstring = typename.group() + ' =' + ' c_' + typestring
                if charnum != None:
                    resstring = resstring + '*' + charnum.group()
                out.write(resstring + '\n')
    line = f.readline()
    
f.close()
out.close()

