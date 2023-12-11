# Very brute force

galaxies = []
data = []
empty_row = []
empty_col = []

with open('aoc11.txt') as f:
    for row, line in enumerate(f.readlines()):
        line = line.strip()
        data.append(line)
        cur_galaxy = len(galaxies)
        for col, char in enumerate(line):
            if char == '#':
                galaxies.append((row, col))
        
        if cur_galaxy == len(galaxies):
            empty_row.append(row)

for col in range(len(data[0])):
    empty = True
    for row in range(len(data)):
        if data[row][col] == '#':
            empty = False
            break
    
    if empty:
        empty_col.append(col)

visited = set()
dists = {}
for i, start_coords in enumerate(galaxies):
    row1, col1 = start_coords
    for j, end_coords in enumerate(galaxies):
        if (i == j) or ((i, j) in visited) or ((j, i) in visited):
            continue
        
        row2, col2 = end_coords
        additional_dist = 0
        for r in empty_row:
            if row1 < r < row2 or row1 > r > row2:
                additional_dist += 1000000 - 1 # for part 1 just change to 1
        for c in empty_col:
            if col1 < c < col2 or col1 > c > col2:
                additional_dist += 1000000 - 1 # for part 1 just change to 1
        visited.add((i, j))
        dists[(i, j)] = abs(row1-row2) + abs(col1-col2) + additional_dist

print(sum(dists.values()))    
