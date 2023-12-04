import string

symbols = string.punctuation.replace(".", "")

with open("aoc3.txt") as f:
    data = [line.strip() for line in f.readlines()]

matrix = [list(d) for d in data]
row_len = len(matrix)
col_len = len(matrix[0])
symbols_location = []
gear_pot_location = []
for row in range(len(matrix)):
    for col in range(len(matrix[row])):
        if matrix[row][col] in symbols:
            symbols_location.append((row, col))
            if matrix[row][col] == '*':
                gear_pot_location.append((row, col))

# Part 1
total = 0
visited = [[False for _ in range(col_len)] for _ in range(row_len)]
for location in symbols_location:
    row, col = location
    
    # If symbol is in first row
    if row == 0:
        # If symbol is left most
        if col == 0:
            # Right of symbol
            if matrix[row][col+1].isnumeric():
                num = ""
                cur_col = col+1
                cur_row = row
                while not visited[cur_row][cur_col] and cur_col != col_len and matrix[cur_row][cur_col].isnumeric():
                    num += matrix[cur_row][cur_col]
                    visited[cur_row][cur_col] = True
                    cur_col += 1
                total += int(num)
            
            # Below symbol
            below = False
            if matrix[row+1][col].isnumeric():
                below = True
                num = ""
                cur_row = row+1
                cur_col = col
                while cur_col != col_len and matrix[cur_row][cur_col].isnumeric():
                    num += matrix[cur_row][cur_col]
                    visited[cur_row][cur_col] = True
                    cur_col += 1
                total += int(num)
            
            # Right diagonal down of symbol
            if not below and matrix[row+1][col+1].isnumeric():
                num = ""
                cur_row = row+1
                cur_col = col+1
                while cur_col != col_len and matrix[cur_row][cur_col].isnumeric():
                    num += matrix[cur_row][cur_col]
                    visited[cur_row][cur_col] = True
                    cur_col += 1
                total += int(num)
        
        # If symbol is right most
        elif col == col_len:
            # Left of symbol
            if matrix[row][col-1].isnumeric():
                num = ""
                cur_col = col-1
                while cur_col >= 0 and matrix[row][cur_col].isnumeric():
                    num = matrix[row][cur_col] + num
                    visited[cur_row][cur_col] = True
                    cur_col -= 1
                total += int(num)
            
            # Below symbol
            below = False
            if matrix[row+1][col].isnumeric():
                below = True
                num = ""
                cur_row = row+1
                cur_col = col
                while cur_col >= 0 and matrix[cur_row][cur_col].isnumeric():
                    num = matrix[cur_row][cur_col] + num
                    visited[cur_row][cur_col] = True
                    cur_col -= 1
                total += int(num)
            
            # Left diagonal down of symbol
            if not below and matrix[row+1][col-1].isnumeric():
                num = ""
                cur_row = row+1
                cur_col = col-1
                while cur_col >= 0 and matrix[cur_row][cur_col].isnumeric():
                    num = matrix[cur_row][cur_col] + num
                    visited[cur_row][cur_col] = True
                    cur_col -= 1
                total += int(num)
        
        # If symbol not in left or right most
        else:
            # Left of symbol
            if matrix[row][col-1].isnumeric():
                num = ""
                cur_col = col-1
                while cur_col >= 0 and matrix[row][cur_col].isnumeric():
                    num = matrix[row][cur_col] + num
                    visited[cur_row][cur_col] = True
                    cur_col -= 1
                total += int(num)
            
            # Below symbol
            below = False
            if matrix[row+1][col].isnumeric():
                below = True
                num = ""
                cur_row = row+1
                cur_col = col
                below_left = matrix[cur_row][cur_col-1].isnumeric()
                below_right = matrix[cur_row][cur_col+1].isnumeric()
                if below_left and below_right:
                    while cur_col >= 0 and matrix[cur_row][cur_col].isnumeric():
                        cur_col -= 1
                    
                    cur_col += 1
                    while cur_col < col_len and matrix[cur_row][cur_col].isnumeric():
                        num += matrix[cur_row][cur_col]
                        cur_col += 1
                    total += int(num)
                
                elif below_left:
                    while cur_col >= 0 and matrix[cur_row][cur_col].isnumeric():
                        num = matrix[cur_row][cur_col] + num
                        cur_col -= 1
                    total += int(num)
                
                elif below_right:
                    while cur_col < col_len and matrix[cur_row][cur_col].isnumeric():
                        num += matrix[cur_row][cur_col]
                        cur_col += 1
                    total += int(num)
                
                else:
                    total += int(matrix[cur_row][cur_col])
            
            # Left diagonal down of symbol
            if not below and matrix[row+1][col-1].isnumeric():
                num = ""
                cur_row = row+1
                cur_col = col-1
                while cur_col >= 0 and matrix[cur_row][cur_col].isnumeric():
                    num = matrix[cur_row][cur_col] + num
                    visited[cur_row][cur_col] = True
                    cur_col -= 1
                total += int(num)
            
            # Right of symbol
            if matrix[row][col+1].isnumeric():
                num = ""
                cur_col = col+1
                while cur_col != col_len and matrix[row][cur_col].isnumeric():
                    num += matrix[row][cur_col]
                    visited[cur_row][cur_col] = True
                    cur_col += 1
                total += int(num)
            
            # Right diagonal down of symbol
            if not below and matrix[row+1][col+1].isnumeric():
                num = ""
                cur_row = row+1
                cur_col = col+1
                while cur_col != col_len and matrix[cur_row][cur_col].isnumeric():
                    num += matrix[cur_row][cur_col]
                    visited[cur_row][cur_col] = True
                    cur_col += 1
                total += int(num)
    
    # If symbol is in last row
    elif row == row_len:
        # If symbol is left most
        if col == 0:
            # Right of symbol
            if matrix[row][col+1].isnumeric():
                num = ""
                cur_col = col+1
                cur_row = row
                while not visited[cur_row][cur_col] and cur_col != col_len and matrix[cur_row][cur_col].isnumeric():
                    num += matrix[cur_row][cur_col]
                    visited[cur_row][cur_col] = True
                    cur_col += 1
                total += int(num)
            
            # Above symbol
            above = False
            if matrix[row-1][col].isnumeric():
                above = True
                num = ""
                cur_row = row-1
                cur_col = col
                while cur_col != col_len and matrix[cur_row][cur_col].isnumeric():
                    num += matrix[cur_row][cur_col]
                    visited[cur_row][cur_col] = True
                    cur_col += 1
                total += int(num)
            
            # Right diagonal above of symbol
            if not above and matrix[row-1][col+1].isnumeric():
                num = ""
                cur_row = row-1
                cur_col = col+1
                while cur_col != col_len and matrix[cur_row][cur_col].isnumeric():
                    num += matrix[cur_row][cur_col]
                    visited[cur_row][cur_col] = True
                    cur_col += 1
                total += int(num)
        
        # If symbol is right most
        elif col == col_len:
            # Left of symbol
            if matrix[row][col-1].isnumeric():
                num = ""
                cur_col = col-1
                while cur_col >= 0 and matrix[row][cur_col].isnumeric():
                    num = matrix[row][cur_col] + num
                    visited[cur_row][cur_col] = True
                    cur_col -= 1
                total += int(num)
            
            # Above symbol
            above = False
            if matrix[row-1][col].isnumeric():
                above = True
                num = ""
                cur_row = row-1
                cur_col = col
                while cur_col >= 0 and matrix[cur_row][cur_col].isnumeric():
                    num = matrix[cur_row][cur_col] + num
                    visited[cur_row][cur_col] = True
                    cur_col -= 1
                total += int(num)
            
            # Left diagonal above of symbol
            if not above and matrix[row-1][col-1].isnumeric():
                num = ""
                cur_row = row-1
                cur_col = col-1
                while cur_col >= 0 and matrix[cur_row][cur_col].isnumeric():
                    num = matrix[cur_row][cur_col] + num
                    visited[cur_row][cur_col] = True
                    cur_col -= 1
                total += int(num)
        
        # If symbol not in left or right most
        else:
            # Left of symbol
            if matrix[row][col-1].isnumeric():
                num = ""
                cur_col = col-1
                while cur_col >= 0 and matrix[row][cur_col].isnumeric():
                    num = matrix[row][cur_col] + num
                    visited[cur_row][cur_col] = True
                    cur_col -= 1
                total += int(num)
            
            # Above symbol
            below = False
            if matrix[row-1][col].isnumeric():
                below = True
                num = ""
                cur_row = row-1
                cur_col = col
                below_left = matrix[cur_row][cur_col-1].isnumeric()
                below_right = matrix[cur_row][cur_col+1].isnumeric()
                if below_left and below_right:
                    while cur_col >= 0 and matrix[cur_row][cur_col].isnumeric():
                        cur_col -= 1
                    
                    cur_col += 1
                    while cur_col < col_len and matrix[cur_row][cur_col].isnumeric():
                        num += matrix[cur_row][cur_col]
                        cur_col += 1
                    total += int(num)
                
                elif below_left:
                    while cur_col >= 0 and matrix[cur_row][cur_col].isnumeric():
                        num = matrix[cur_row][cur_col] + num
                        cur_col -= 1
                    total += int(num)
                
                elif below_right:
                    while cur_col < col_len and matrix[cur_row][cur_col].isnumeric():
                        num += matrix[cur_row][cur_col]
                        cur_col += 1
                    total += int(num)
                
                else:
                    total += int(matrix[cur_row][cur_col])
            
            # Left diagonal down of symbol
            if not below and matrix[row-1][col-1].isnumeric():
                num = ""
                cur_row = row-1
                cur_col = col-1
                while cur_col >= 0 and matrix[cur_row][cur_col].isnumeric():
                    num = matrix[cur_row][cur_col] + num
                    visited[cur_row][cur_col] = True
                    cur_col -= 1
                total += int(num)
            
            # Right of symbol
            if matrix[row][col+1].isnumeric():
                num = ""
                cur_col = col+1
                while cur_col != col_len and matrix[row][cur_col].isnumeric():
                    num += matrix[row][cur_col]
                    visited[cur_row][cur_col] = True
                    cur_col += 1
                total += int(num)
            
            # Right diagonal down of symbol
            if not below and matrix[row-1][col+1].isnumeric():
                num = ""
                cur_row = row-1
                cur_col = col+1
                while cur_col != col_len and matrix[cur_row][cur_col].isnumeric():
                    num += matrix[cur_row][cur_col]
                    visited[cur_row][cur_col] = True
                    cur_col += 1
                total += int(num)
    
    # If symbol is somewhere thats not first or last row
    else:
        # If symbol is left most
        if col == 0:
            # Right of symbol
            if matrix[row][col+1].isnumeric():
                num = ""
                cur_col = col+1
                cur_row = row
                while not visited[cur_row][cur_col] and cur_col != col_len and matrix[cur_row][cur_col].isnumeric():
                    num += matrix[cur_row][cur_col]
                    visited[cur_row][cur_col] = True
                    cur_col += 1
                total += int(num)
            
            # Above symbol
            above = False
            if matrix[row-1][col].isnumeric():
                above = True
                num = ""
                cur_row = row-1
                cur_col = col
                while cur_col != col_len and matrix[cur_row][cur_col].isnumeric():
                    num += matrix[cur_row][cur_col]
                    visited[cur_row][cur_col] = True
                    cur_col += 1
                total += int(num)
            
            # Below symbol
            below = False
            if matrix[row+1][col].isnumeric():
                below = True
                num = ""
                cur_row = row+1
                cur_col = col
                while cur_col != col_len and matrix[cur_row][cur_col].isnumeric():
                    num += matrix[cur_row][cur_col]
                    visited[cur_row][cur_col] = True
                    cur_col += 1
                total += int(num)
            
            # Right diagonal down of symbol
            if not below and matrix[row+1][col+1].isnumeric():
                num = ""
                cur_row = row+1
                cur_col = col+1
                while cur_col != col_len and matrix[cur_row][cur_col].isnumeric():
                    num += matrix[cur_row][cur_col]
                    visited[cur_row][cur_col] = True
                    cur_col += 1
                total += int(num)
            
            # Right diagonal above of symbol
            if not above and matrix[row-1][col+1].isnumeric():
                num = ""
                cur_row = row-1
                cur_col = col+1
                while cur_col != col_len and matrix[cur_row][cur_col].isnumeric():
                    num += matrix[cur_row][cur_col]
                    visited[cur_row][cur_col] = True
                    cur_col += 1
                total += int(num)
        
        # If symbol is right most
        elif col == col_len:
            # Left of symbol
            if matrix[row][col-1].isnumeric():
                num = ""
                cur_col = col-1
                while cur_col >= 0 and matrix[row][cur_col].isnumeric():
                    num = matrix[row][cur_col] + num
                    visited[cur_row][cur_col] = True
                    cur_col -= 1
                total += int(num)
                
            # Above symbol
            above = False
            if matrix[row-1][col].isnumeric():
                above = True
                num = ""
                cur_row = row-1
                cur_col = col
                while cur_col != col_len and matrix[cur_row][cur_col].isnumeric():
                    num = matrix[cur_row][cur_col] + num
                    visited[cur_row][cur_col] = True
                    cur_col -= 1
                total += int(num)
            
            # Below symbol
            below = False
            if matrix[row+1][col].isnumeric():
                below = True
                num = ""
                cur_row = row+1
                cur_col = col
                while cur_col >= 0 and matrix[cur_row][cur_col].isnumeric():
                    num = matrix[cur_row][cur_col] + num
                    visited[cur_row][cur_col] = True
                    cur_col -= 1
                total += int(num)
            
            # Left diagonal down of symbol
            if not below and matrix[row+1][col-1].isnumeric():
                num = ""
                cur_row = row+1
                cur_col = col-1
                while cur_col >= 0 and matrix[cur_row][cur_col].isnumeric():
                    num = matrix[cur_row][cur_col] + num
                    visited[cur_row][cur_col] = True
                    cur_col -= 1
                total += int(num)
            
            # Left diagonal above of symbol
            if not above and matrix[row+1][col-1].isnumeric():
                num = ""
                cur_row = row+1
                cur_col = col-1
                while cur_col >= 0 and matrix[cur_row][cur_col].isnumeric():
                    num = matrix[cur_row][cur_col] + num
                    visited[cur_row][cur_col] = True
                    cur_col -= 1
                total += int(num)
        
        # If symbol not in left or right most
        else:
            # Left of symbol
            if matrix[row][col-1].isnumeric():
                num = ""
                cur_col = col-1
                while cur_col >= 0 and matrix[row][cur_col].isnumeric():
                    num = matrix[row][cur_col] + num
                    visited[cur_row][cur_col] = True
                    cur_col -= 1
                total += int(num)
            
            # Below symbol
            below = False
            if matrix[row+1][col].isnumeric():
                below = True
                num = ""
                cur_row = row+1
                cur_col = col
                below_left = matrix[cur_row][cur_col-1].isnumeric()
                below_right = matrix[cur_row][cur_col+1].isnumeric()
                if below_left and below_right:
                    while cur_col >= 0 and matrix[cur_row][cur_col].isnumeric():
                        cur_col -= 1
                    
                    cur_col += 1
                    while cur_col < col_len and matrix[cur_row][cur_col].isnumeric():
                        num += matrix[cur_row][cur_col]
                        cur_col += 1
                    total += int(num)
                
                elif below_left:
                    while cur_col >= 0 and matrix[cur_row][cur_col].isnumeric():
                        num = matrix[cur_row][cur_col] + num
                        cur_col -= 1
                    total += int(num)
                
                elif below_right:
                    while cur_col < col_len and matrix[cur_row][cur_col].isnumeric():
                        num += matrix[cur_row][cur_col]
                        cur_col += 1
                    total += int(num)
                
                else:
                    total += int(matrix[cur_row][cur_col])
            
            # Above symbol
            above = False
            if matrix[row-1][col].isnumeric():
                above = True
                num = ""
                cur_row = row-1
                cur_col = col
                above_left = matrix[cur_row][cur_col-1].isnumeric()
                above_right = matrix[cur_row][cur_col+1].isnumeric()
                if above_left and above_right:
                    while cur_col >= 0 and matrix[cur_row][cur_col].isnumeric():
                        cur_col -= 1
                    
                    cur_col += 1
                    while cur_col < col_len and matrix[cur_row][cur_col].isnumeric():
                        num += matrix[cur_row][cur_col]
                        cur_col += 1
                    total += int(num)
                
                elif above_left:
                    while cur_col >= 0 and matrix[cur_row][cur_col].isnumeric():
                        num = matrix[cur_row][cur_col] + num
                        cur_col -= 1
                    total += int(num)
                
                elif above_right:
                    while cur_col < col_len and matrix[cur_row][cur_col].isnumeric():
                        num += matrix[cur_row][cur_col]
                        cur_col += 1
                    total += int(num)
                
                else:
                    total += int(matrix[cur_row][cur_col])
            
            # Left diagonal down of symbol
            if not below and matrix[row+1][col-1].isnumeric():
                num = ""
                cur_row = row+1
                cur_col = col-1
                while cur_col >= 0 and matrix[cur_row][cur_col].isnumeric():
                    num = matrix[cur_row][cur_col] + num
                    visited[cur_row][cur_col] = True
                    cur_col -= 1
                total += int(num)
            
            # Right of symbol
            if matrix[row][col+1].isnumeric():
                num = ""
                cur_col = col+1
                while cur_col != col_len and matrix[row][cur_col].isnumeric():
                    num += matrix[row][cur_col]
                    visited[cur_row][cur_col] = True
                    cur_col += 1
                total += int(num)
            
            # Right diagonal down of symbol
            if not below and matrix[row+1][col+1].isnumeric():
                num = ""
                cur_row = row+1
                cur_col = col+1
                while cur_col != col_len and matrix[cur_row][cur_col].isnumeric():
                    num += matrix[cur_row][cur_col]
                    visited[cur_row][cur_col] = True
                    cur_col += 1
                total += int(num)
            
            # Right diagonal above of symbol
            if not above and matrix[row-1][col+1].isnumeric():
                num = ""
                cur_row = row-1
                cur_col = col+1
                while cur_col != col_len and matrix[cur_row][cur_col].isnumeric():
                    num += matrix[cur_row][cur_col]
                    visited[cur_row][cur_col] = True
                    cur_col += 1
                total += int(num)
            
            # Left diagonal above of symbol
            if not above and matrix[row-1][col-1].isnumeric():
                num = ""
                cur_row = row-1
                cur_col = col-1
                while cur_col != col_len and matrix[cur_row][cur_col].isnumeric():
                    num = matrix[cur_row][cur_col] + num
                    visited[cur_row][cur_col] = True
                    cur_col -= 1
                total += int(num)

    # print(f'symbol = {matrix[row][col]}, row = {row}, col = {col}, total so far = {total}')
    
print(f'Part1: {total}')

############################################################
# Part 2
sum_gear_ratio = 0
for location in gear_pot_location:
    row, col = location
    nums = []
    
    # If symbol is in first row
    if row == 0:
        # If symbol is left most
        if col == 0:
            # Right of symbol
            if matrix[row][col+1].isnumeric():
                num = ""
                cur_col = col+1
                cur_row = row
                while not visited[cur_row][cur_col] and cur_col != col_len and matrix[cur_row][cur_col].isnumeric():
                    num += matrix[cur_row][cur_col]
                    visited[cur_row][cur_col] = True
                    cur_col += 1
                nums.append(int(num))
            
            # Below symbol
            below = False
            if matrix[row+1][col].isnumeric():
                below = True
                num = ""
                cur_row = row+1
                cur_col = col
                while cur_col != col_len and matrix[cur_row][cur_col].isnumeric():
                    num += matrix[cur_row][cur_col]
                    visited[cur_row][cur_col] = True
                    cur_col += 1
                nums.append(int(num))
            
            # Right diagonal down of symbol
            if not below and matrix[row+1][col+1].isnumeric():
                num = ""
                cur_row = row+1
                cur_col = col+1
                while cur_col != col_len and matrix[cur_row][cur_col].isnumeric():
                    num += matrix[cur_row][cur_col]
                    visited[cur_row][cur_col] = True
                    cur_col += 1
                nums.append(int(num))
        
        # If symbol is right most
        elif col == col_len:
            # Left of symbol
            if matrix[row][col-1].isnumeric():
                num = ""
                cur_col = col-1
                while cur_col >= 0 and matrix[row][cur_col].isnumeric():
                    num = matrix[row][cur_col] + num
                    visited[cur_row][cur_col] = True
                    cur_col -= 1
                nums.append(int(num))
            
            # Below symbol
            below = False
            if matrix[row+1][col].isnumeric():
                below = True
                num = ""
                cur_row = row+1
                cur_col = col
                while cur_col >= 0 and matrix[cur_row][cur_col].isnumeric():
                    num = matrix[cur_row][cur_col] + num
                    visited[cur_row][cur_col] = True
                    cur_col -= 1
                nums.append(int(num))
            
            # Left diagonal down of symbol
            if not below and matrix[row+1][col-1].isnumeric():
                num = ""
                cur_row = row+1
                cur_col = col-1
                while cur_col >= 0 and matrix[cur_row][cur_col].isnumeric():
                    num = matrix[cur_row][cur_col] + num
                    visited[cur_row][cur_col] = True
                    cur_col -= 1
                nums.append(int(num))
        
        # If symbol not in left or right most
        else:
            # Left of symbol
            if matrix[row][col-1].isnumeric():
                num = ""
                cur_col = col-1
                while cur_col >= 0 and matrix[row][cur_col].isnumeric():
                    num = matrix[row][cur_col] + num
                    visited[cur_row][cur_col] = True
                    cur_col -= 1
                nums.append(int(num))
            
            # Below symbol
            below = False
            if matrix[row+1][col].isnumeric():
                below = True
                num = ""
                cur_row = row+1
                cur_col = col
                below_left = matrix[cur_row][cur_col-1].isnumeric()
                below_right = matrix[cur_row][cur_col+1].isnumeric()
                if below_left and below_right:
                    while cur_col >= 0 and matrix[cur_row][cur_col].isnumeric():
                        cur_col -= 1
                    
                    cur_col += 1
                    while cur_col < col_len and matrix[cur_row][cur_col].isnumeric():
                        num += matrix[cur_row][cur_col]
                        cur_col += 1
                    nums.append(int(num))
                
                elif below_left:
                    while cur_col >= 0 and matrix[cur_row][cur_col].isnumeric():
                        num = matrix[cur_row][cur_col] + num
                        cur_col -= 1
                    nums.append(int(num))
                
                elif below_right:
                    while cur_col < col_len and matrix[cur_row][cur_col].isnumeric():
                        num += matrix[cur_row][cur_col]
                        cur_col += 1
                    nums.append(int(num))
                
                else:
                    nums.append(int(matrix[cur_row][cur_col]))
            
            # Left diagonal down of symbol
            if not below and matrix[row+1][col-1].isnumeric():
                num = ""
                cur_row = row+1
                cur_col = col-1
                while cur_col >= 0 and matrix[cur_row][cur_col].isnumeric():
                    num = matrix[cur_row][cur_col] + num
                    visited[cur_row][cur_col] = True
                    cur_col -= 1
                nums.append(int(num))
            
            # Right of symbol
            if matrix[row][col+1].isnumeric():
                num = ""
                cur_col = col+1
                while cur_col != col_len and matrix[row][cur_col].isnumeric():
                    num += matrix[row][cur_col]
                    visited[cur_row][cur_col] = True
                    cur_col += 1
                nums.append(int(num))
            
            # Right diagonal down of symbol
            if not below and matrix[row+1][col+1].isnumeric():
                num = ""
                cur_row = row+1
                cur_col = col+1
                while cur_col != col_len and matrix[cur_row][cur_col].isnumeric():
                    num += matrix[cur_row][cur_col]
                    visited[cur_row][cur_col] = True
                    cur_col += 1
                nums.append(int(num))
    
    # If symbol is in last row
    elif row == row_len:
        # If symbol is left most
        if col == 0:
            # Right of symbol
            if matrix[row][col+1].isnumeric():
                num = ""
                cur_col = col+1
                cur_row = row
                while not visited[cur_row][cur_col] and cur_col != col_len and matrix[cur_row][cur_col].isnumeric():
                    num += matrix[cur_row][cur_col]
                    visited[cur_row][cur_col] = True
                    cur_col += 1
                nums.append(int(num))
            
            # Above symbol
            above = False
            if matrix[row-1][col].isnumeric():
                above = True
                num = ""
                cur_row = row-1
                cur_col = col
                while cur_col != col_len and matrix[cur_row][cur_col].isnumeric():
                    num += matrix[cur_row][cur_col]
                    visited[cur_row][cur_col] = True
                    cur_col += 1
                nums.append(int(num))
            
            # Right diagonal above of symbol
            if not above and matrix[row-1][col+1].isnumeric():
                num = ""
                cur_row = row-1
                cur_col = col+1
                while cur_col != col_len and matrix[cur_row][cur_col].isnumeric():
                    num += matrix[cur_row][cur_col]
                    visited[cur_row][cur_col] = True
                    cur_col += 1
                nums.append(int(num))
        
        # If symbol is right most
        elif col == col_len:
            # Left of symbol
            if matrix[row][col-1].isnumeric():
                num = ""
                cur_col = col-1
                while cur_col >= 0 and matrix[row][cur_col].isnumeric():
                    num = matrix[row][cur_col] + num
                    visited[cur_row][cur_col] = True
                    cur_col -= 1
                nums.append(int(num))
            
            # Above symbol
            above = False
            if matrix[row-1][col].isnumeric():
                above = True
                num = ""
                cur_row = row-1
                cur_col = col
                while cur_col >= 0 and matrix[cur_row][cur_col].isnumeric():
                    num = matrix[cur_row][cur_col] + num
                    visited[cur_row][cur_col] = True
                    cur_col -= 1
                nums.append(int(num))
            
            # Left diagonal above of symbol
            if not above and matrix[row-1][col-1].isnumeric():
                num = ""
                cur_row = row-1
                cur_col = col-1
                while cur_col >= 0 and matrix[cur_row][cur_col].isnumeric():
                    num = matrix[cur_row][cur_col] + num
                    visited[cur_row][cur_col] = True
                    cur_col -= 1
                nums.append(int(num))
        
        # If symbol not in left or right most
        else:
            # Left of symbol
            if matrix[row][col-1].isnumeric():
                num = ""
                cur_col = col-1
                while cur_col >= 0 and matrix[row][cur_col].isnumeric():
                    num = matrix[row][cur_col] + num
                    visited[cur_row][cur_col] = True
                    cur_col -= 1
                nums.append(int(num))
            
            # Above symbol
            below = False
            if matrix[row-1][col].isnumeric():
                below = True
                num = ""
                cur_row = row-1
                cur_col = col
                below_left = matrix[cur_row][cur_col-1].isnumeric()
                below_right = matrix[cur_row][cur_col+1].isnumeric()
                if below_left and below_right:
                    while cur_col >= 0 and matrix[cur_row][cur_col].isnumeric():
                        cur_col -= 1
                    
                    cur_col += 1
                    while cur_col < col_len and matrix[cur_row][cur_col].isnumeric():
                        num += matrix[cur_row][cur_col]
                        cur_col += 1
                    nums.append(int(num))
                
                elif below_left:
                    while cur_col >= 0 and matrix[cur_row][cur_col].isnumeric():
                        num = matrix[cur_row][cur_col] + num
                        cur_col -= 1
                    nums.append(int(num))
                
                elif below_right:
                    while cur_col < col_len and matrix[cur_row][cur_col].isnumeric():
                        num += matrix[cur_row][cur_col]
                        cur_col += 1
                    nums.append(int(num))
                
                else:
                    nums.append(int(matrix[cur_row][cur_col]))
            
            # Left diagonal down of symbol
            if not below and matrix[row-1][col-1].isnumeric():
                num = ""
                cur_row = row-1
                cur_col = col-1
                while cur_col >= 0 and matrix[cur_row][cur_col].isnumeric():
                    num = matrix[cur_row][cur_col] + num
                    visited[cur_row][cur_col] = True
                    cur_col -= 1
                nums.append(int(num))
            
            # Right of symbol
            if matrix[row][col+1].isnumeric():
                num = ""
                cur_col = col+1
                while cur_col != col_len and matrix[row][cur_col].isnumeric():
                    num += matrix[row][cur_col]
                    visited[cur_row][cur_col] = True
                    cur_col += 1
                nums.append(int(num))
            
            # Right diagonal down of symbol
            if not below and matrix[row-1][col+1].isnumeric():
                num = ""
                cur_row = row-1
                cur_col = col+1
                while cur_col != col_len and matrix[cur_row][cur_col].isnumeric():
                    num += matrix[cur_row][cur_col]
                    visited[cur_row][cur_col] = True
                    cur_col += 1
                nums.append(int(num))
    
    # If symbol is somewhere thats not first or last row
    else:
        # If symbol is left most
        if col == 0:
            # Right of symbol
            if matrix[row][col+1].isnumeric():
                num = ""
                cur_col = col+1
                cur_row = row
                while not visited[cur_row][cur_col] and cur_col != col_len and matrix[cur_row][cur_col].isnumeric():
                    num += matrix[cur_row][cur_col]
                    visited[cur_row][cur_col] = True
                    cur_col += 1
                nums.append(int(num))
            
            # Above symbol
            above = False
            if matrix[row-1][col].isnumeric():
                above = True
                num = ""
                cur_row = row-1
                cur_col = col
                while cur_col != col_len and matrix[cur_row][cur_col].isnumeric():
                    num += matrix[cur_row][cur_col]
                    visited[cur_row][cur_col] = True
                    cur_col += 1
                nums.append(int(num))
            
            # Below symbol
            below = False
            if matrix[row+1][col].isnumeric():
                below = True
                num = ""
                cur_row = row+1
                cur_col = col
                while cur_col != col_len and matrix[cur_row][cur_col].isnumeric():
                    num += matrix[cur_row][cur_col]
                    visited[cur_row][cur_col] = True
                    cur_col += 1
                nums.append(int(num))
            
            # Right diagonal down of symbol
            if not below and matrix[row+1][col+1].isnumeric():
                num = ""
                cur_row = row+1
                cur_col = col+1
                while cur_col != col_len and matrix[cur_row][cur_col].isnumeric():
                    num += matrix[cur_row][cur_col]
                    visited[cur_row][cur_col] = True
                    cur_col += 1
                nums.append(int(num))
            
            # Right diagonal above of symbol
            if not above and matrix[row-1][col+1].isnumeric():
                num = ""
                cur_row = row-1
                cur_col = col+1
                while cur_col != col_len and matrix[cur_row][cur_col].isnumeric():
                    num += matrix[cur_row][cur_col]
                    visited[cur_row][cur_col] = True
                    cur_col += 1
                nums.append(int(num))
        
        # If symbol is right most
        elif col == col_len:
            # Left of symbol
            if matrix[row][col-1].isnumeric():
                num = ""
                cur_col = col-1
                while cur_col >= 0 and matrix[row][cur_col].isnumeric():
                    num = matrix[row][cur_col] + num
                    visited[cur_row][cur_col] = True
                    cur_col -= 1
                nums.append(int(num))
                
            # Above symbol
            above = False
            if matrix[row-1][col].isnumeric():
                above = True
                num = ""
                cur_row = row-1
                cur_col = col
                while cur_col != col_len and matrix[cur_row][cur_col].isnumeric():
                    num = matrix[cur_row][cur_col] + num
                    visited[cur_row][cur_col] = True
                    cur_col -= 1
                nums.append(int(num))
            
            # Below symbol
            below = False
            if matrix[row+1][col].isnumeric():
                below = True
                num = ""
                cur_row = row+1
                cur_col = col
                while cur_col >= 0 and matrix[cur_row][cur_col].isnumeric():
                    num = matrix[cur_row][cur_col] + num
                    visited[cur_row][cur_col] = True
                    cur_col -= 1
                nums.append(int(num))
            
            # Left diagonal down of symbol
            if not below and matrix[row+1][col-1].isnumeric():
                num = ""
                cur_row = row+1
                cur_col = col-1
                while cur_col >= 0 and matrix[cur_row][cur_col].isnumeric():
                    num = matrix[cur_row][cur_col] + num
                    visited[cur_row][cur_col] = True
                    cur_col -= 1
                nums.append(int(num))
            
            # Left diagonal above of symbol
            if not above and matrix[row+1][col-1].isnumeric():
                num = ""
                cur_row = row+1
                cur_col = col-1
                while cur_col >= 0 and matrix[cur_row][cur_col].isnumeric():
                    num = matrix[cur_row][cur_col] + num
                    visited[cur_row][cur_col] = True
                    cur_col -= 1
                nums.append(int(num))
        
        # If symbol not in left or right most
        else:
            # Left of symbol
            if matrix[row][col-1].isnumeric():
                num = ""
                cur_col = col-1
                while cur_col >= 0 and matrix[row][cur_col].isnumeric():
                    num = matrix[row][cur_col] + num
                    visited[cur_row][cur_col] = True
                    cur_col -= 1
                nums.append(int(num))
            
            # Below symbol
            below = False
            if matrix[row+1][col].isnumeric():
                below = True
                num = ""
                cur_row = row+1
                cur_col = col
                below_left = matrix[cur_row][cur_col-1].isnumeric()
                below_right = matrix[cur_row][cur_col+1].isnumeric()
                if below_left and below_right:
                    while cur_col >= 0 and matrix[cur_row][cur_col].isnumeric():
                        cur_col -= 1
                    
                    cur_col += 1
                    while cur_col < col_len and matrix[cur_row][cur_col].isnumeric():
                        num += matrix[cur_row][cur_col]
                        cur_col += 1
                    nums.append(int(num))
                
                elif below_left:
                    while cur_col >= 0 and matrix[cur_row][cur_col].isnumeric():
                        num = matrix[cur_row][cur_col] + num
                        cur_col -= 1
                    nums.append(int(num))
                
                elif below_right:
                    while cur_col < col_len and matrix[cur_row][cur_col].isnumeric():
                        num += matrix[cur_row][cur_col]
                        cur_col += 1
                    nums.append(int(num))
                
                else:
                    nums.append(int(matrix[cur_row][cur_col]))
            
            # Above symbol
            above = False
            if matrix[row-1][col].isnumeric():
                above = True
                num = ""
                cur_row = row-1
                cur_col = col
                above_left = matrix[cur_row][cur_col-1].isnumeric()
                above_right = matrix[cur_row][cur_col+1].isnumeric()
                if above_left and above_right:
                    while cur_col >= 0 and matrix[cur_row][cur_col].isnumeric():
                        cur_col -= 1
                    
                    cur_col += 1
                    while cur_col < col_len and matrix[cur_row][cur_col].isnumeric():
                        num += matrix[cur_row][cur_col]
                        cur_col += 1
                    nums.append(int(num))
                
                elif above_left:
                    while cur_col >= 0 and matrix[cur_row][cur_col].isnumeric():
                        num = matrix[cur_row][cur_col] + num
                        cur_col -= 1
                    nums.append(int(num))
                
                elif above_right:
                    while cur_col < col_len and matrix[cur_row][cur_col].isnumeric():
                        num += matrix[cur_row][cur_col]
                        cur_col += 1
                    nums.append(int(num))
                
                else:
                    nums.append(int(matrix[cur_row][cur_col]))
            
            # Left diagonal down of symbol
            if not below and matrix[row+1][col-1].isnumeric():
                num = ""
                cur_row = row+1
                cur_col = col-1
                while cur_col >= 0 and matrix[cur_row][cur_col].isnumeric():
                    num = matrix[cur_row][cur_col] + num
                    visited[cur_row][cur_col] = True
                    cur_col -= 1
                nums.append(int(num))
            
            # Right of symbol
            if matrix[row][col+1].isnumeric():
                num = ""
                cur_col = col+1
                while cur_col != col_len and matrix[row][cur_col].isnumeric():
                    num += matrix[row][cur_col]
                    visited[cur_row][cur_col] = True
                    cur_col += 1
                nums.append(int(num))
            
            # Right diagonal down of symbol
            if not below and matrix[row+1][col+1].isnumeric():
                num = ""
                cur_row = row+1
                cur_col = col+1
                while cur_col != col_len and matrix[cur_row][cur_col].isnumeric():
                    num += matrix[cur_row][cur_col]
                    visited[cur_row][cur_col] = True
                    cur_col += 1
                nums.append(int(num))
            
            # Right diagonal above of symbol
            if not above and matrix[row-1][col+1].isnumeric():
                num = ""
                cur_row = row-1
                cur_col = col+1
                while cur_col != col_len and matrix[cur_row][cur_col].isnumeric():
                    num += matrix[cur_row][cur_col]
                    visited[cur_row][cur_col] = True
                    cur_col += 1
                nums.append(int(num))
            
            # Left diagonal above of symbol
            if not above and matrix[row-1][col-1].isnumeric():
                num = ""
                cur_row = row-1
                cur_col = col-1
                while cur_col != col_len and matrix[cur_row][cur_col].isnumeric():
                    num = matrix[cur_row][cur_col] + num
                    visited[cur_row][cur_col] = True
                    cur_col -= 1
                nums.append(int(num))
    
    if len(nums) == 2:
        sum_gear_ratio += nums[0] * nums[1]

print(f'Part 2: {sum_gear_ratio}')

