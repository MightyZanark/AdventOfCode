from copy import deepcopy

def north(data):
    valid = {}
    data = deepcopy(data)
    for row, line in enumerate(data):
        valid[row] = {}
        for col, c in enumerate(line):
            if c == '.':
                valid[row][col] = True
            
            elif c == 'O':
                rows = [r for r in valid.keys() if r != row]
                for r in rows:
                    v = valid[r].get(col, False)
                    if v:
                        data[r][col] = 'O'
                        data[row][col] = '.'
                        valid[row][col] = valid[r].pop(col)
                        break
            
            else:
                for r in range(row):
                    valid[r][col] = False
    
    return data


def west(data):
    valid = {}
    data = deepcopy(data)
    for col in range(len(data[0])):
        valid[col] = {}
        for row, line in enumerate(data):
            if line[col] == '.':
                valid[col][row] = True
            
            elif line[col] == 'O':
                cols = [c for c in valid.keys() if c != col]
                for c in cols:
                    v = valid[c].get(row, False)
                    if v:
                        data[row][c] = 'O'
                        data[row][col] = '.'
                        valid[col][row] = valid[c].pop(row)
                        break
            
            else:
                for c in range(col):
                    valid[c][row] = False
    
    return data


def south(data):
    return north(data[::-1])[::-1]


def east(data):
    data = [line[::-1] for line in data]
    data = west(data)
    data = [line[::-1] for line in data]
    return data


with open('aoc14.txt') as f:
    valid = {}
    data = [[*line.strip()] for line in f.readlines()]

unique = []
cycle = 0
# for part 1, do data = north(data) and thats it
for i in range(1000000000):
    data = north(data)
    data = west(data)
    data = south(data)
    data = east(data)
    
    if data in unique:
        cycle = i-unique.index(data)
        j = i + cycle * ((1000000000 - i) // cycle)
        data = unique[(1000000000 - j + i - cycle - 1) % len(unique)])
        break
    
    unique.append(deepcopy(data))

total = 0
multiplier = len(data)
for line in data:
    total += line.count('O') * multiplier
    multiplier -= 1

print(total)
