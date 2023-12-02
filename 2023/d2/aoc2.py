total = {'red': 12, 'green': 13, 'blue': 14, 'total': 39}

with open('aoc2.txt') as f:
    data = [line.strip() for line in f.readlines()]

# Part 1
valid = []
for d in data:
    game_id, game_result = d.split(":")
    game_id = int(game_id.split(" ")[-1])
    game_result = game_result.strip().split("; ")
    invalid = False
    for result in game_result:
        colors = result.split(", ")
        total_amt = 0
        for color in colors:
            amt, col = color.split(" ")
            amt = int(amt)
            if amt > total[col]:
                invalid = True
                break
            total_amt += amt
            if total_amt > total['total']:
                invalid = True
                break
        if invalid:
            break
    
    if not invalid:
        valid.append(game_id)

print(f'Part 1: {sum(valid)}')

# Part 2
total_amt = 0
for d in data:
    _, game_result = d.split(":")
    game_result = game_result.strip().split("; ")
    min_cubes = {'red': 0, 'green': 0, 'blue': 0}
    for result in game_result:
        colors = result.split(", ")
        for color in colors:
            amt, col = color.split(" ")
            amt = int(amt)
            if amt > min_cubes[col]:
                min_cubes[col] = amt
    total_amt += min_cubes['red'] * min_cubes['green'] * min_cubes['blue']

print(f'Part 2: {total_amt}')
