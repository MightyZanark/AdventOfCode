from math import gcd

with open('aoc8.txt') as f:
    data = [line.strip() for line in f.readlines() if line.strip()]

moves = data[0]
data = data[1:]
graph = {}

# For part 1, first_nodes = ['AAA']
first_nodes = []
for d in data:
    node, elems = d.split(' = ')
    elems = elems[1:-1]
    graph[node] = elems.split(', ')
    
    # For part 1, remove the if
    if node.endswith('A'):
        first_nodes.append(node)

next_nodes = []
for node in first_nodes:
    next_nodes.append(graph[node][0 if moves[0] == 'L' else 1])

total = 1
move_len = len(moves)
for i in range(len(first_nodes)):
    step = 1
    while not next_nodes[i].endswith('Z'):
        next_nodes[i] = graph[next_nodes[i]][0 if moves[step % move_len] == 'L' else 1]
        step += 1

    # LCM because the distance from the beginning to the end is the same
    # from each node and each starting point has their own endpoint
    # Hint from subreddit, otherwise bruteforce can work (just takes a fair amount of time)
    total = (total * step) // gcd(total, step)

print(total)
