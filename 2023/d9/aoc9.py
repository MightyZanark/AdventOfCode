with open('aoc9.txt') as f:
    data = [line.strip() for line in f.readlines()]

forward = 0
backward = 0
for line in data:
    arr = [[int(num) for num in line.split(' ')]]
    cur_arr = arr[-1]
    while not all(num == 0 for num in cur_arr):
        diff = []
        for i in range(0, len(cur_arr)-1):
            diff.append(cur_arr[i+1] - cur_arr[i])
        arr.append(diff)
        cur_arr = arr[-1]
    
    fwd = 0
    bwd = 0
    for i in range(len(arr)-1, -1, -1):
        fwd += arr[i][-1]
        bwd = arr[i][0] - bwd
    
    forward += fwd
    backward += bwd

print(f'Part 1: {forward}')
print(f'Part 2: {backward}')
