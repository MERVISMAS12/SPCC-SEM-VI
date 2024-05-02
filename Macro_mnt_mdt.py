import re
code = [
    'MACRO',
    'SAMPLE',
    'LOAD A , 10',
    'ADD A , 20',
    'STORE A , 30',
    'MEND',
    'START 0',
    'SAMPLE',
    "X DS F'4'",
    'END']
MNT=[]
MDT=[]
for i in range(len(code)):
    splitcode = code[i].split()
    lsplit =len(splitcode)
    for j in splitcode:
        if j == 'MACRO':
            kp, dp, pp = 0,0,0
            line = code[i+1].split()
            for n in line:
                if n[-1] == '=' and n[0] == '&':
                    kp+=1
                elif ('=' in n) and n[0] == '&':
                    dp+=1
                elif n[0] == '&':
                    pp+=1
                
            name = (line[0], pp, kp, dp)
            MNT.append(name)
        break
    break
print(f"MACRO NAME TABLE \n {MNT}")
for i in code:
    if i == 'MACRO' or i== MNT[0][0]:
        continue
    elif i == 'MEND':
        MDT.append(i);
        break
    else:
        MDT.append(i);
        
print(f"MACRO DEFINATION TABLE \n {MDT}")
            
