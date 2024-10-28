f=open("al-khaser.exe_8036_4076.txt", 'rb')
apis = []
instr = []
for ln in f.readlines():
    ln=ln.strip()
    if b"API CALL" in ln:
        p1 = ln.find(b"! ")
        p2 = ln.find(b" ", p1 + 4)    
        apis += [ln[p1+2:p2]]
    elif b"->" in ln:
        continue
    else:
        instr += [ln]

        
apis = set(apis)
instr = set(instr)

print(len(apis))
print(len(instr))
