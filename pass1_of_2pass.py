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

for i in range(0, lcode):
    splitcode = code[i].split()
    lensplit = len(splitcode)
    for j in range(0, lensplit):
        if j == 0 and ((splitcode[j] not in IS) and (splitcode[j] not in AD) and (splitcode[j] not in DL)):
            sym = [(splitcode[j],lc)]
            SYM.append(sym)
        elif splitcode[j] == AD[0]:
            lc = int(splitcode[j+1])
        elif re.match(r"\='([0-9]+)\'",splitcode[j]):
            LT.append([splitcode[j], 0])
        elif splitcode[j] == AD[4]:
            for m in LT:
                if m[1] == 0:
                    m[1] = lc
                    lc+=1
        else:
            continue
    lc+=1
print(f"SYMBOL TABLE: {SYM}")
print(f"LITERAL TABLE: {LT}")

            
            
