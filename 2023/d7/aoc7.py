# For part 1, change the string to AKQJT98765432
power = {char: val for char, val in zip("AKQT98765432J", range(13, 0, -1))}

class Card:
    def __init__(self, card, bid):
        self.card = card
        self.bid = bid
    
    def __lt__(self, other):
        for c1, c2 in zip(self.card, other.card):
            if power[c1] < power[c2]:
                return True
            elif power[c1] > power[c2]:
                return False
        return False
    
    def __gt__(self, other):
        for c1, c2 in zip(self.card, other.card):
            if power[c1] < power[c2]:
                return False
            elif power[c1] > power[c2]:
                return True
        return False
    
    def __str__(self):
        return self.card
    
    def __repr__(self):
        return str(self)

with open('aoc7.txt') as f:
    data = [line.strip() for line in f.readlines()]

# because Python's dict is iterated by insertion order this works
strength = {
    "five": [],
    "four": [],
    "full": [],
    "three": [],
    "two_p": [],
    "one_p": [],
    "high": []
}

rank = 0
for d in data:
    card, bid = d.split(" ")
    bid = int(bid)
    rank += 1
    
    count = {}
    for c in card:
        count[c] = count.get(c, 0) + 1
    
    if len(count) == 1:
        strength["five"].append(Card(card, bid))
    
    elif len(count) == 2:
        if "J" in count: # remove for part 1
            strength["five"].append(Card(card,bid))
            
        elif 4 in count.values():
            strength["four"].append(Card(card, bid))
            
        else:
            strength["full"].append(Card(card, bid))
    
    elif len(count) == 3:
        if "J" in count: # remove for part 1
            highest = max(count.values())
            j = count["J"]
            if j > 1:
                strength["four"].append(Card(card, bid))
            else:
                if highest == 2:
                    strength["full"].append(Card(card, bid))
                elif highest == 3:
                    strength["four"].append(Card(card, bid))
                    
        elif 3 in count.values():
            strength["three"].append(Card(card, bid))
            
        else:
            strength["two_p"].append(Card(card, bid))
    
    elif len(count) == 4:
        if "J" in count: # remove for part 1
            strength["three"].append(Card(card, bid))
        
        else:
            strength["one_p"].append(Card(card, bid))
    
    else:
        if "J" in count: # remove for part 1
            strength["one_p"].append(Card(card, bid))
        else:
            strength["high"].append(Card(card, bid))

total = 0
for key, values in strength.items():
    if not values:
        continue
    
    values.sort(reverse=True)
    for card in values:
        total += rank * card.bid
        rank -= 1

print(total)
