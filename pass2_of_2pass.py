import re

IS=['STOP', 'ADD', 'SUB', 'MULT', 'MOVER', 'MOVEM', 'COMP', 'BC', 'DIV', 'READ', 'PRINT']
AD=['START', 'END', 'EQU', 'ORG', 'LTORG']
DL=['DC','DS']
REG=['AREG', 'BREG', 'CREG', 'DREG']

code=[
    'START 200',
    'READ M',
    'MOVEM AREG , M',
    "SUB AREG , ='3' ",
    'M DS 2',
    'LTORG',
    'END'
    ]
lcode = len(code)

SYM = []
LT = []
lc=0
LC = []
for i in range(0, lcode):
    LC.append(lc)
    splitcode = code[i].split()
    lensplit = len(splitcode)
    for j in range(0, lensplit):
        if j == 0 and ((splitcode[j] not in IS) and (splitcode[j] not in AD) and (splitcode[j] not in DL)):
            sym = [splitcode[j],lc]
            SYM.append(sym)
        elif splitcode[j] == AD[0]:
            lc = int(splitcode[j+1])-1
        elif re.match(r"\='([0-9]+)\'",splitcode[j]):
            LT.append([splitcode[j], 0])
        elif splitcode[j] == 'DS':
            if int(splitcode[j+1]) > 1:
                lc = lc + int(splitcode[j+1]) -1
        elif splitcode[j] == AD[4]:
            temp = 1
            for m in LT:
                if m[1] == 0:
                    m[1] = lc
                    temp+=1
                    if temp > 2:
                        lc+=1
        else:
            continue
    lc+=1
print(f"SYMBOL TABLE: {SYM}")
print(f"LITERAL TABLE: {LT}")


#pass1

for i in range(0, lcode):
    line = []
    line.append(LC[i])
    splitcode = code[i].split()
    lensplit = len(splitcode)
    for j in range(0, lensplit):
        if j > 0 and (splitcode[j] not in IS) and (splitcode[j] not in AD) and (splitcode[j] not in DL) and (splitcode[j] not in REG):
            for p in SYM:
                if p[0] == splitcode[j]:
                    line.append(p[1])
        elif re.match(r"\='([0-9]+)\'",splitcode[j]):
            for q in LT:
                if q[0] == splitcode[j]:
                    line.append(q[1])
        elif splitcode[j] in IS:
            for a in range(0, len(IS)):
                if IS[a] == splitcode[j]:
                    line.append(a)
        elif splitcode[j] in AD:
            for a in range(0, len(AD)):
                if AD[a] == splitcode[j]:
                    line.append(a+1)
        elif splitcode[j] in DL:
            for a in range(0, len(DL)):
                if DL[a] == splitcode[j]:
                    line.append(a+1)
        elif splitcode[j] in REG:
            for a in range(0, len(REG)):
                if REG[a] == splitcode[j]:
                    line.append(a+1)
            
    print(f"{line}")


