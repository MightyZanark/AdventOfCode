with open("aoc1.txt") as f:
    data = [line.strip() for line in f.readlines()]

ones = ['o', 's', 'e', 't', 'f', 'n']
twos = ['on', 'tw', 'th', 'fo', 'fi', 'si', 'se', 'ei', 'ni']
threes = ['one', 'two', 'thr', 'fou', 'fiv', 'six', 'sev', 'eig', 'nin']
fours = ['one', 'two', 'thre', 'four', 'five', 'six', 'seve', 'eigh', 'nine']
fives = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
lst = [ones, twos, threes, fours, fives]

convert = {string:str(i) for i, string in enumerate(fives, 1)}

new_data = []
for line in data:
    word = ""
    tmp = ""
    for i in range(len(line)):
        if line[i].isnumeric():
            word += line[i]
        else:
            for digits in fives:
                if line[i:i+len(digits)] == digits:
                    word += convert[digits]
        # if c.isnumeric():
            # word += c
            # continue
            
        # tmp += c
        # tmp_len = len(tmp)
        # if tmp_len == 1 and tmp not in lst[0]:
            # tmp = ""
        # elif tmp_len == 2 and tmp not in lst[1]:
            # tmp = ""
        # elif tmp_len == 3:
            # if tmp not in lst[2]:
                # tmp = ""
            # else:
                # num = convert.get(tmp, None)
                # if num:
                    # word += num
                    # tmp = ""
        # elif tmp_len == 4:
            # if tmp not in lst[3]:
                # tmp = ""
            # else:
                # num = convert.get(tmp, None)
                # if num:
                    # word += num
                    # tmp = ''
        # elif tmp_len == 5:
            # if tmp not in lst[4]:
                # tmp = ""
            # else:
                # if i == 132:
                    # print(tmp)
                # num = convert.get(tmp, None)
                # if num:
                    # word += num
                    # tmp = ''
    new_data.append(word)
    
res = 0
print(f'{new_data[132] = }, {data[132] = }')
for num in new_data:
    cal = num[0] + num[-1]
    res += int(cal)
print(res)