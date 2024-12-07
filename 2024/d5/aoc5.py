with open("aoc5.txt") as f:
    rules, updates = f.read().strip().split("\n\n")

rules = [rule.strip().split('|') for rule in rules.split()]
updates = [update.strip().split(',') for update in updates.split()]

x_to_y = {}
y_to_x = {}

for x, y in rules:
    x_to_y[x] = x_to_y.get(x, set()) | {y}
    y_to_x[y] = y_to_x.get(y, set()) | {x}

def is_correct(update, num_to_idx, y_to_x):
    for num in update:
        if num in y_to_x:
            for x in y_to_x[num]:
                if x in num_to_idx and num_to_idx[x] > num_to_idx[num]:
                    return False
    
    return True

partA = 0
partB = 0
for update in updates:
    num_to_idx = {num: idx for idx, num in enumerate(update)}
    if is_correct(update, num_to_idx, y_to_x):
        partA += int(update[(len(update)-1)//2])
    else:
        dependencies = {num: y_to_x[num] for num in update}
        mid = (len(update)-1)//2
        for y in update:
            dependency = dependencies[y]
            exists = set()
            for x in update:
                if x == y:
                    continue
                
                if x in dependency:
                    exists.add(x)
            if len(exists) == mid:
                partB += int(y)
                break

print(partA)
print(partB)
