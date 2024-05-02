OPERATOR = {'+','-','/','*','(',')'}
PRI = {'+':1, '-':1, '/':2, '*':2}
def post(exp):
    stack=[]
    output = ""
    for ch in exp:
        if ch not in OPERATOR:
            output+=ch
        elif ch == '(':
            stack.append(ch)
        elif ch == ')':
            while stack and stack[-1] != '(':
                output+=stack.pop()
            stack.pop()
        else:
            while stack and stack[-1] != '(' and PRI[ch] <= PRI[stack[-1]]:
                output+=stack.pop()
            stack.append(ch)
    output += "".join(reversed(stack))
    return output

def icg(pos):
    stack = []
    t = 1
    for i in pos:
        if i not in OPERATOR:
            stack.append(i)
        else:
            print(f"t{t} = {stack.pop(-2)} {i} {stack.pop()}")
            stack.append(f"t{t}")
            t +=1

exp = input(" Enter the Expression: ")

pos = post(exp)
print(f"{pos}")
icg(pos)

