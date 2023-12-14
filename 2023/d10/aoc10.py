from collections import deque

with open('aoc10.txt') as f:
    data = [[*line.strip()] for line in f.readlines()]
    maze = [[-1] * len(data[0]) for _ in range(len(data))]

start_col = 0
start_row = 0
for i, line in enumerate(data):
    if 'S' in line:
        start_col = line.index('S')
        start_row = i
        maze[i][start_col] = 0
        break

tiles = {
    '|': {'S': ['L', 'J', '|'], 'N': ['7', 'F', '|'], 'W': [], 'E': []},
    '-': {'W': ['F', 'L', '-'], 'E': ['7', 'J', '-'], 'N': [], 'S': []},
    'L': {'E': ['J', '7', '-'], 'N': ['|', 'F', '7'], 'W': [], 'S': []},
    'J': {'W': ['L', 'F', '-'], 'N': ['|', 'F', '7'], 'E': [], 'S': []},
    '7': {'S': ['L', 'J', '|'], 'W': ['-', 'F', 'L'], 'E': [], 'N': []},
    'F': {'S': ['L', 'J', '|'], 'E': ['-', 'J', '7'], 'W': [], 'N': []},
    'S': {'S': ['L', 'J', '|'], 'E': ['-', 'J', '7'], 'W': ['-', 'F', 'L'], 'N': ['|', 'F', '7']},
    '.': {'S': [], 'E': [], 'W': [], 'N': []}
}

row = len(maze)
col = len(maze[0])

def is_valid(data, maze, row, col, x, y, prev_tile, direction):
    coord_valid = x >= 0 and x < row and y >= 0 and y < col and maze[x][y] == -1
    
    if coord_valid:
        prev_tile = ''
        if direction == 'E':
            prev_tile = data[x][y-1]
        elif direction == 'S':
            prev_tile = data[x-1][y]
        elif direction == 'W':
            prev_tile = data[x][y+1]
        else:
            prev_tile = data[x+1][y]
        
        return data[x][y] in tiles[prev_tile][direction]
        
    return False

def flood_fill(data, maze, row, col):
    # Copied from https://www.geeksforgeeks.org/flood-fill-algorithm/
    queue = deque()
    queue.append((start_row, start_col))
    max_dist = -1
    
    while queue:
        x, y = queue.popleft()
        cur_tile = data[x][y]
        new_dist = maze[x][y] + 1
        
        # East
        if is_valid(data, maze, row, col, x, y+1, cur_tile, 'E'):
            maze[x][y+1] = new_dist
            if new_dist > max_dist:
                max_dist = new_dist
            queue.append((x, y+1))
            
        # South
        if is_valid(data, maze, row, col, x+1, y, cur_tile, 'S'):
            maze[x+1][y] = maze[x][y] + 1
            if new_dist > max_dist:
                max_dist = new_dist
            queue.append((x+1, y))
            
        # West
        if is_valid(data, maze, row, col, x, y-1, cur_tile, 'W'):
            maze[x][y-1] = maze[x][y] + 1
            if new_dist > max_dist:
                max_dist = new_dist
            queue.append((x, y-1))
            
        # North
        if is_valid(data, maze, row, col, x-1, y, cur_tile, 'N'):
            maze[x-1][y] = maze[x][y] + 1
            if new_dist > max_dist:
                max_dist = new_dist
            queue.append((x-1, y))
    
    return max_dist

print(f'Part 1: {flood_fill(data, maze, row, col)}')

# Replace the 'S' tile with the correct pipe
if start_row-1 >= 0 and maze[start_row-1][start_col] == 1:
    if start_col-1 >= 0 and maze[start_row][start_col-1] == 1:
        data[start_row][start_col] = 'J'
    elif start_col+1 < len(maze[0]) and maze[start_row][start_col+1] == 1:
        data[start_row][start_col] = 'L'
    elif start_row+1 < len(maze) and maze[start_row+1][start_col] == 1:
        data[start_row][start_col] = '|'

elif start_row+1 < len(maze) and maze[start_row+1][start_col] == 1:
    if start_col-1 >= 0 and maze[start_row][start_col-1] == 1:
        data[start_row][start_col] = '7'
    elif start_col+1 < len(maze[0]) and maze[start_row][start_col+1] == 1:
        data[start_row][start_col] = 'F'

else:
    data[start_row][start_col] = '-'

# Replace all tiles that are not part of the loop
# with '.'
for i, row in enumerate(data):
    j = 0
    while j < len(row):
        while j < len(row) and maze[i][j] == -1:
            row[j] = '.'
            j += 1
        
        if j == len(row):
            break
        
        while j < len(row) and maze[i][j] != -1:
            j += 1
            k += 1

enclosed = 0
for row in data:
    inside = False
    count = 0
    last_corner = ''
    for col in row:
        # Credit to subreddit for the hint of counting 'bars'
        # to determine whether the '.' is outside or inside
        # the loop
        if col == '|':
            inside = 1 - inside
        
        elif col == 'L' or col == 'F':
            last_corner = col
        
        elif col == 'J':
            if last_corner == 'F':
                inside = 1 - inside
            last_corner = ''
        
        elif col == '7':
            if last_corner == 'L':
                inside = 1 - inside
            last_corner = ''
        
        elif col == '.':
            if inside:
                count += 1
    
    enclosed += count

print(f'Part 2: {enclosed}')
