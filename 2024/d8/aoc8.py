from itertools import combinations

with open("aoc8.txt") as f:
    graph = [[*row] for row in f.read().strip().split()]

def get_antenna_locs(graph, R, C):
    mapping = {}
    for r in range(R):
        for c in range(C):
            char = graph[r][c]
            if char != '.':
                mapping[char] = mapping.get(char, []) + [(r, c)]
    
    return mapping


def oob(pos, R, C):
    return pos[0] < 0 or pos[0] >= R or pos[1] < 0 or pos[1] >= C


def get_antinodes(antenna_locs, R, C, to_limit=False):
    antinodes = set()
    for nodes in antenna_locs.values():
        for node1, node2 in combinations(nodes, 2):
            direction = node1[0] - node2[0], node1[1] - node2[1]
            
            if not to_limit: # part A
                anode1 = node1[0] + direction[0], node1[1] + direction[1]
                anode2 = node2[0] - direction[0], node2[1] - direction[1]
                
                if not oob(anode1, R, C):
                    antinodes.add(anode1)
                if not oob(anode2, R, C):
                    antinodes.add(anode2)
            else: # part B
                step_r = direction[0]
                step_c = direction[1]
            
                start_r1 = node1[0]
                stop_r1 = -1
                start_c1 = node1[1]
                stop_c1 = -1 if step_c < 0 else C
                for r, c in zip(range(start_r1, stop_r1, step_r), range(start_c1, stop_c1, step_c)):
                    antinodes.add((r, c))
                
                start_r2 = node2[0]
                stop_r2 = R
                start_c2 = node2[1]
                stop_c2 = C if step_c < 0 else -1
                for r, c in zip(range(start_r2, stop_r2, -step_r), range(start_c2, stop_c2, -step_c)):
                    antinodes.add((r, c))
    
    return antinodes

R = len(graph)
C = len(graph[0])
antenna_locs = get_antenna_locs(graph, R, C)
print(antenna_locs)
antinodes = get_antinodes(antenna_locs, R, C, True)
print(antinodes)
print(len(antinodes))
