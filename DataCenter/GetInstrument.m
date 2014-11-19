function res = GetInstrument(inst)
old = feature('DefaultCharacterSet', 'UTF8');
res = dbmain(8, inst);
feature('DefaultCharacterSet', old);
end

