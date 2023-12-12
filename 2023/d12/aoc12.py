# Props to subreddit for the hint of it using recursion
# and memoization

import functools

data = []
with open('aoc12.txt') as f:
    for line in f:
        record, groups = line.strip().split(' ')
        data.append((record, tuple(int(size) for size in groups.split(','))))

@functools.cache
def check(s, groups):
    if s == "":
        return len(groups) == 0
    
    if len(groups) == 0:
        # print(f"{s = }")
        return "#" not in s
    
    if s[0] == ".":
        return check(s[1:], groups)
    
    if s[0] == "#":
        count = 1
        i = 1
        while i < len(s) and (s[i] == "#"):
            i += 1
            count += 1
        
        if "." in s[:groups[0]] or len(s[:groups[0]]) < groups[0]:
            # print(f"{s = }, {s[:groups[0]] = }, {groups[0] = }")
            return False
        else:
            l = len(s[:groups[0]+1])
            if count > groups[0] or (l > len(s[:groups[0]]) and s[groups[0]] == "#"):
                return False
            # print(f"{s = }, {s[:groups[0]] = }, {groups[0] = }")
            return check(s[groups[0]+1:], groups[1:])
    
    if s[0] == "?":
        dot = check("." + s[1:], groups)
        tag = check("#" + s[1:], groups)
        return dot + tag

total = 0
for records, groups in data:
    # part 1 just check(records, groups)
    val = check(records + ("?" + records) * 4, groups * 5)
    print(f"{val = }, {records = }, {groups = }")
    total += val

print(total)
