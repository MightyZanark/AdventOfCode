with open("aoc4.txt") as f:
    data = [line.strip() for line in f.readlines()]

# Part 1
total = 0
# Part 2
wins = [1 for _ in range(len(data))]
for d in data:
    card, nums = d.split(": ")
    card = int(card.split(" ")[-1])
    card_amt = wins[card-1]
    win, our = nums.split(" | ")
    win = {n for n in win.split(" ") if n}
    our = {n for n in our.split(" ") if n}
    count = 0
    for n in our:
        if n in win:
            wins[card] += card_amt
            card += 1
            if count:
                count <<= 1
            else:
                count += 1
    total += count

print(f"Part 1: {total}")
print(f"Part 2: {sum(wins)}")
