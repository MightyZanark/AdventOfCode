def aoc_hash(inp: str) -> int:
    val = 0
    for char in inp:
        val += ord(char)
        val *= 17
        val %= 256
    
    return val

with open('aoc15.txt') as f:
    strings = f.read().strip().split(',')

total = 0
boxes = [[] for _ in range(256)]
for string in strings:
    total += aoc_hash(string)
    
    if '=' in string:
        label, foc_len = string.split('=')
        idx = aoc_hash(label)
        found = False
        for i, lens in enumerate(boxes[idx]):
            if label in lens:
                boxes[idx][i] = (label, int(foc_len))
                found = True
                break
        
        if not found:
            boxes[idx].append((label, int(foc_len)))
    
    elif '-' in string:
        label = string[:-1]
        idx = aoc_hash(label)
        found = -1
        for i, lens in enumerate(boxes[idx]):
            if label in lens:
                found = i
                break
        
        if found != -1:
            boxes[idx].pop(found)

foc_pow = 0
for i, box in enumerate(boxes, 1):
    for j, lens in enumerate(box, 1):
        foc_pow += i * j * lens[-1]

print(f'Part 1: {total}')
print(f'Part 2: {foc_pow}')
