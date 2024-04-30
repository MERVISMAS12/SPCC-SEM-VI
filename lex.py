import re
keywords=['if', 'else', 'while', 'for', 'return', 'int', 'char', 'float', 'string', 'do', 'printf', 'scanf', '#include', 'main()']
punctuation=[',','.',';','(',')','{','}','[',']']
operator=['=', '+', '-', '*', '/','<', '>', '<=', '>=', '++', '--', '==', '||', '&&']
code='''
int main() {
    int i = 0 ;
    printf ( "Hello World" ) ;
    return 0;
}
'''

splitcode = code.split()
length = len(splitcode)
print(splitcode)
for i in range(0, length):
    if splitcode[i] in keywords:
        print(f'Keyword: {splitcode[i]}')
    elif splitcode[i] in punctuation:
        print(f'Punctuation: {splitcode[i]}')
    elif splitcode[i] in operator:
        print(f'Operator: {splitcode[i]}')
    elif re.match(r'[a-zA-Z]+$', splitcode[i]):
        print(f'Identifier: {splitcode[i]}')
    elif re.match(r'[0-9]+$', splitcode[i]):
        print(f'Identifier: {splitcode[i]}')
