from collections import deque

def is_valid(data, visited, row, col, x, y, direction):
    return x >= 0 and x < row and y >= 0 and y < col and not visited[x][y][direction]

def flood_fill(data, row, col, start_row, start_col, start_dir):
    queue = deque()
    queue.append((start_row, start_col, start_dir))
    
    visited = []
    for _ in range(len(data)):
        a = []
        for _ in range(len(data[0])):
            a.append({'L': False, 'R': False, 'U': False, 'D': False})
        visited.append(a)
    
    while queue:
        r, c, direction = queue.popleft()
        if not is_valid(data, visited, row, col, r, c, direction):
            continue
        
        cur_tile = data[r][c]
        visited[r][c][direction] = True
        next_coord = (r, c+1) # Right
        if direction == 'L': # Left
            next_coord = (r, c-1)
        elif direction == 'U': # Up
            next_coord = (r-1, c)
        elif direction == 'D': # Down
            next_coord = (r+1, c)
        else:
            pass
        
        if cur_tile == '.':
            queue.append(next_coord + (direction,))
        
        elif cur_tile == '-':
            if direction in ['L', 'R']:
                queue.append(next_coord + (direction,))
            else:
                queue.append((r, c-1, 'L'))
                queue.append((r, c+1, 'R'))
        
        elif cur_tile == '|':
            if direction in ['U', 'D']:
                queue.append(next_coord + (direction,))
            else:
                queue.append((r-1, c, 'U'))
                queue.append((r+1, c, 'D'))
        
        elif cur_tile == '\\':
            if direction == 'R':
                queue.append((r+1, c, 'D'))
            elif direction == 'U':
                queue.append((r, c-1, 'L'))
            elif direction == 'D':
                queue.append((r, c+1, 'R'))
            else:
                queue.append((r-1, c, 'U'))
        
        else:
            if direction == 'R':
                queue.append((r-1, c, 'U'))
            elif direction == 'U':
                queue.append((r, c+1, 'R'))
            elif direction == 'D':
                queue.append((r, c-1, 'L'))
            else:
                queue.append((r+1, c, 'D'))
    
    return visited

def count_energized(visited):
    energized = 0
    for row in visited:
        for col in row:
            if any(col.values()):
                energized += 1
    
    return energized

with open('aoc16.txt') as f:
    data = [[*line.strip()] for line in f.readlines()]

row = len(data)
col = len(data[0])

top_row = [(0, c, 'D') for c in range(col)]
bottom_row = [(row-1, c, 'U') for c in range(col)]
left_col = [(r, 0, 'R') for r in range(row)]
right_col = [(r, col-1, 'L') for r in range(row)]

comb = top_row + bottom_row + left_col + right_col

highest = -1
for r, c, d in comb:
    visited = flood_fill(data, row, col, r, c, d)
    count = count_energized(visited)
    if count > highest:
        print(f'New Highest! {highest} -> {count}')
        highest = count

# part 1: count_energized(flood_fill(data, row, col, 0, 0, 'R'))
print(highest)
