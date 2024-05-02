import re
code = [
    'MACRO',
    'TEST &X , &Y',
    'LOAD A , &X',
    'ADD A , 20',
    'STORE A , &Y',
    'MEND',
    'START 0',
    'TEST 10 , M',
    "M DS F'4'",
    'END']
MNT=[]
ALA=[]
for i in range(len(code)):
    splitcode = code[i].split()
    lsplit =len(splitcode)
    for j in splitcode:
        if j == 'MACRO':
            kp, dp, pp = 0,0,0
            line = code[i+1].split()
            for n in line:
                ala=[]
                if n[-1] == '=' and n[0] == '&':
                    kp+=1
                    ala = [line[0], n, '-', '-', 0]
                elif ('=' in n) and n[0] == '&':
                    dp+=1
                    ala = [line[0], '-', n, '-', 0]
                elif n[0] == '&':
                    pp+=1
                    ala = [line[0], '-', '-', n, 0]
                else:
                    continue
                ALA.append(ala)
                
            name = (line[0], pp, kp, dp)
            MNT.append(name)
        break
    break
print(f"MACRO NAME TABLE \n {MNT}")
test = code.index('MEND')
for j in range( test, len(code)):
    testcode = code[j].split()
    if testcode[0] == MNT[0][0]:
        x = 0
        for m in range(1, len(testcode)):
            if testcode[m] != ',':
                ALA[x][4] = testcode[m]
                x+=1
    else:
        continue
print(f"ARGUMENT LIST ARRAY \n {ALA}")
