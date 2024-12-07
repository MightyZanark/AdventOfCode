with open("aoc6.txt") as f:
    graph = [[*row] for row in f.read().strip().split()]

def find_start(graph, R, C):
    for r in range(R):
        for c in range(C):
            if graph[r][c] == '^':
                return (r, c)

def partA(graph, start, R, C):
    visited = [[0 for _ in range(C)] for _ in range(R)]
    dirs = { # (row, col)
        '^': (-1, 0),
        '>': (0, 1),
        '<': (0, -1),
        'v': (1, 0)
    }
    next_dirs = {'^': '>', '>': 'v', 'v': '<', '<': '^'}
    stack = [(start, '^')]
    while stack:
        (row, col), cur_dir = stack.pop()
        
        visited[row][col] = 1
        next_dir = dirs[cur_dir]
        next_pos = row + next_dir[0], col + next_dir[1]
        if next_pos[0] < 0 or next_pos[0] >= R or next_pos[1] < 0 or next_pos[1] >= C:
            return sum(sum(row) for row in visited), visited

        if graph[next_pos[0]][next_pos[1]] == '#':
            stack.append(((row, col), next_dirs[cur_dir]))
        else:
            stack.append((next_pos, cur_dir))

def partB(graph, visited, start, R, C):
    # brute force but keep the search space only to points
    # that gets visited
    valid_spots = [(r, c) for r in range(R) for c in range(C) if visited[r][c] and (r, c) != start]
    dirs = { # (row, col)
        '^': (-1, 0),
        '>': (0, 1),
        '<': (0, -1),
        'v': (1, 0)
    }
    next_dirs = {'^': '>', '>': 'v', 'v': '<', '<': '^'}
    cnt = 0
    for (mod_r, mod_c) in valid_spots:
        graph[mod_r][mod_c] = '#'
        loop_checker = set()
        loop = False
        stack = [(start, '^')]
        while stack:
            (row, col), cur_dir = stack.pop()
            
            if ((row, col), cur_dir) in loop_checker:
                loop = True
                break
            
            loop_checker.add(((row, col), cur_dir))
            next_dir = dirs[cur_dir]
            next_pos = row + next_dir[0], col + next_dir[1]
            if next_pos[0] < 0 or next_pos[0] >= R or next_pos[1] < 0 or next_pos[1] >= C:
                break

            if graph[next_pos[0]][next_pos[1]] == '#':
                stack.append(((row, col), next_dirs[cur_dir]))
            else:
                stack.append((next_pos, cur_dir))
        
        graph[mod_r][mod_c] = '.'
        if loop:
            cnt += 1
    
    return cnt

R = len(graph)
C = len(graph[0])
start = find_start(graph, R, C)
A, visited = partA(graph, start, R, C)
print(f"{A = }")
print(f"B: {partB(graph, visited, start, R, C)}")
