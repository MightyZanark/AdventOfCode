with open('aoc6.txt') as f:
    times = f.readline().split(':')[-1]
    dists = f.readline().split(':')[-1]

# Part 1
p2_time = int(times.replace(' ', ''))
p2_dist = int(dists.replace(' ', ''))
times = [int(time) for time in times.split(' ') if time]
dists = [int(dist) for dist in dists.split(' ') if dist]
comb = 1

for i, time in enumerate(times):
    dist = dists[i]
    count = 0
    for hold in range(1, time):
        if hold*(time-hold) > dist:
            count += 1
    comb *= count
    
print(f'Part 1: {comb}')

comb = 0
for hold in range(1, p2_time):
    if hold*(p2_time-hold) > p2_dist:
        comb += 1

print(f'Part 2: {comb}')
