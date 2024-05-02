#ADD object.tx in the same file directory
def objcode(memory, obj):
    for line in obj:
        part = line.strip().split('\t')
        if part[0] == 'T':
            address, length = int(part[1],16), int(part[2],16)
            data = ''.join(part[3:])
            memory[address:address+length] = [int(data[i:i+2], 16) for i in range(0, length*2,2)]

memory_size = 0xFFFFFF
memory = [0] * memory_size
with open('object.txt') as obj:
    objcode(memory, obj)

print("Memory \t\t data")
for i, content in enumerate(memory):
    if content != 0:
        print(f"{i:06X} \t\t {content:02X}")

            
