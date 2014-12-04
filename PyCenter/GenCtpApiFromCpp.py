import re

f = open("..\\include\\ThostFtdcUserApiDataType.h")

out = open(".\\CTPApiDataType.py", 'a')
line = f.readline()

out.write('from ctypes import *\n')
while line:
    
    defineGroup = re.search('#define( +|\t+)(\w+)( +|\t+)((\'|\d|\w|#)+)', line)
    
    if defineGroup != None:
        print defineGroup.group()
        resstring = defineGroup.group(2) + ' = ' + defineGroup.group(4) + '\n'
        out.write(resstring)
    
    typedefGroup = re.search('typedef( +|\t+)(\w+)( +|\t+)(\w+)\[*(\d*)\]*', line)
    if typedefGroup != None:
        resstring = typedefGroup.group(4) + ' = c_' + typedefGroup.group(2)
        print typedefGroup.group()
        if len(typedefGroup.group(5)):
            print typedefGroup.group(5)
            resstring += ' * ' + typedefGroup.group(5)
            
        out.write(resstring + '\n')
    line = f.readline()
    
f.close()
out.close()

f = open('..\\include\\ThostFtdcUserApiStruct.h')
out = open(".\\CTPUserApiStruct.py", 'a')
out.write('from CTPApiDataType import *\n')

line = f.readline()

while line:
    #print line
    structGroup = re.search('struct( +|\t+)(\w+)', line)
    if structGroup != None:
        print structGroup.group(2)
        out.write('class ' + structGroup.group(2) + '(Structure):\n' + ' '*4 + '_fields_ = [\n')
        line = f.readline()
        line = f.readline()
        isOverGroup = re.search('}', line);
        while isOverGroup == None:
            memberGroup = re.search('(\w+)( +|\t+)(\w+)', line)
            if memberGroup != None:
                print memberGroup.group(1), memberGroup.group(3)
                out.write(' '*11 + '(\'' + memberGroup.group(3) + '\', ' + memberGroup.group(1) + '),\n')
            line = f.readline()
            isOverGroup = re.search('}', line);
        out.write(' '*11 + ']\n')
    line = f.readline()
f.close()
out.close()