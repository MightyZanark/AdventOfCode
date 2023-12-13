with open('aoc13.txt') as f:
    patterns = [[row for row in pattern.split('\n')] for pattern in f.read().split('\n\n')]

total = 0
for p, pattern in enumerate(patterns):
    # Remove everything smudge related for part 1
    row_loc = []
    for i in range(len(pattern)-1):
        if pattern[i] == pattern[i+1]:
            row_loc.append((i, i+1))
        else:
            smudge_count = sum(pattern[i][k] != pattern[i+1][k] for k in range(len(pattern[0])))
            if smudge_count == 1:
                row_loc.append((i, i+1))
    
    row_reflect = False
    row_count = 0
    found = -1
    for upper, lower in row_loc:
        i = upper
        j = lower
        row_count = 1
        smudge = True
        while i >= 0 and j < len(pattern):
            if pattern[i] != pattern[j]:
                if smudge:
                    smudge_count = sum(pattern[i][k] != pattern[j][k] for k in range(len(pattern[0])))
                    if smudge_count == 1:
                        i -= 1
                        j += 1
                        smudge = False
                        continue
                else:
                    break
            
            row_count += 1
            i -= 1
            j += 1
        
        if (i != -1 and j != len(pattern)) or smudge:
            row_reflect = False
        
        else:
            row_reflect = True
            break
    
    if row_reflect:
        total += 100 * lower
        continue
    
    col_loc = []
    for i in range(len(pattern[0])-1):
        if all(pattern[j][i] == pattern[j][i+1] for j in range(len(pattern))):
            col_loc.append((i, i+1))
        else:
            smudge_count = sum(pattern[k][i] != pattern[k][i+1] for k in range(len(pattern)))
            if smudge_count == 1:
                col_loc.append((i, i+1))
    
    col_reflect = False
    col_count = 0
    for left, right in col_loc:
        i = left
        j = right
        col_count = 1
        smudge = True
        while i >= 0 and j < len(pattern[0]):
            if not all(pattern[k][i] == pattern[k][j] for k in range(len(pattern))):
                if smudge:
                    smudge_count = sum(pattern[k][i] != pattern[k][j] for k in range(len(pattern)))
                    if smudge_count == 1:
                        i -= 1
                        j += 1
                        smudge = False
                        continue
                else:
                    break
            col_count += 1
            i -= 1
            j += 1
        
        if (i != -1 and j != len(pattern[0])) or smudge:
            col_reflect = False
        else:
            col_reflect = True
            break
    
    if col_reflect:
        total += right

print(total)
