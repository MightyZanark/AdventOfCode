from collections import deque

with open("aoc7.txt") as f:
    data = f.read().strip().split('\n')

eq_split = lambda x: (int(x[0]), [int(n) for n in x[1].strip().split()])
data = [eq_split(line.split(':')) for line in data]

def check_eqs(data, ops, already_valid_idx=set()):
    valid = 0
    valid_idx = set()
    for i, (res, nums) in enumerate(data):
        if i in already_valid_idx:
            valid += res
            continue
        
        N = len(nums)
        first_num = nums[0]
        queue = deque([(first_num, op, 1) for op in ops])
        while queue:
            n1, op, idx = queue.popleft()
            if idx >= N:
                continue
            
            n2 = nums[idx]
            if op in {'+', '*'}:
                result = eval(f"{n1} {op} {n2}")
            else:
                result = int(f"{n1}{n2}")
            
            if result > res:
                continue
            
            if result == res and idx == (N-1):
                valid += res
                valid_idx.add(i)
                break
            
            for op_ in ops:
                queue.append((result, op_, idx+1))
    
    return valid, valid_idx

A, valid_idx = check_eqs(data, ('*', '+'))
B, _ = check_eqs(data, ('*', '+', '||'), valid_idx)
print(f"A: {A}")
print(f"B: {B}")
