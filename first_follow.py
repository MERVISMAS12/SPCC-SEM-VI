# S -> AB
# A -> aB
# B -> b
import re
grm = {
    'A':[('aB')],
    'S':[('AB')],
    'B':[('b')]
    }
first=[]
m=['A','B','S']
for i in m:
    if re.match(r"[a-z]",grm[i][0][0]):
        f = [i, grm[i][0][0]]
        first.append(f)
    if re.match(r"[A-Z]",grm[i][0][0]):
        temp = grm[i][0][0]
        for fst in first:
            if fst[0] == temp:
                f = [i, fst[1]]
                first.append(f)

                
print(f"First {first}")
