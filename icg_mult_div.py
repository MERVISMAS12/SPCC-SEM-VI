ins = {
    '*':'MULT',
    '/':'DIV'}
def codegen(tac):
    i=0
    for line in tac:
        if len(line)== 4:
            print(f"MOV M{i}, {line[1]} ")
            print(f"{ins[line[3]]} M{i}, {line[2]} ")
            print(f"MOV {line[0]}, M{i}")
            i +=1
        else:
            print(f"MOV {line[0]}, {line[1]} ")

tac = [
    ['t1', 'a', 'b', '*'],
    ['t2', 't1', 'c', '/'],
    ['r', 't2']
    ]
codegen(tac)
