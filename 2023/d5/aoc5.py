def calc(mapping: dict[tuple[int,int], int], key: int, left: int, right: int, limit: int) -> int:
    res = key
    nearest_lower = (float('inf'), 0)
    nearest_upper = (float('inf'), 0)
    for lower, upper in mapping:
        if lower <= key <= upper:
            res = (key-lower) + mapping[(lower, upper)]
            left = min(upper-key+1, right, limit)
            return res, left
        
        elif lower > key:
            if lower-key < nearest_lower[0]:
                nearest_lower = (lower-key, lower)
        
        elif upper < key:
            if key-upper < nearest_upper[0]:
                nearest_upper = (key-upper, upper)

    if nearest_upper[1] < nearest_lower[1] and nearest_lower[0] != float('inf'):
        left = nearest_lower[0]
    
    elif nearest_upper[1] > nearest_lower[1] and nearest_lower[0] != float('inf'):
        left = nearest_lower[0]

    return res, left


with open("aoc5.txt") as f:
    data = f.read().split("\n\n")

seeds = [int(s) for s in data[0].split(" ")[1:]]
seeds = [(seeds[i], seeds[i+1]) for i in range(0, len(seeds), 2)] # remove for part 1
seed_soil = {}
soil_fert = {}
fert_water = {}
water_light = {}
light_temp = {}
temp_humid = {}
humid_loc = {}

for item in data[1:]:
    item = item.split("\n")
    header = item[0]
    item_lst = item[1:]
    for nums in item_lst:
        dest, src, length = (int(n) for n in nums.split(" "))
        if header.startswith("seed"):
            seed_soil[(src, src+length-1)] = dest
        elif header.startswith("soil"):
            soil_fert[(src, src+length-1)] = dest
        elif header.startswith("fertilizer"):
            fert_water[(src, src+length-1)] = dest
        elif header.startswith("water"):
            water_light[(src, src+length-1)] = dest
        elif header.startswith("light"):
            light_temp[(src, src+length-1)] = dest
        elif header.startswith("temperature"):
            temp_humid[(src, src+length-1)] = dest
        elif header.startswith("humidity"):
            humid_loc[(src, src+length-1)] = dest

smallest = float("inf")
for seed, length in seeds:
    limit = seed + length
    while seed < limit:
        amt = 1
        independent = False
        
        soil, amt = calc(seed_soil, seed, amt, length, limit-seed)
        fert, amt2 = calc(soil_fert, soil, amt, length, limit-seed)
        water, amt3 = calc(fert_water, fert, amt, length, limit-seed)
        light, amt4 = calc(water_light, water, amt, length, limit-seed)
        temp, amt5 = calc(light_temp, light, amt, length, limit-seed)
        humid, amt6 = calc(temp_humid, temp, amt, length, limit-seed)
        loc, amt7 = calc(humid_loc, humid, amt, length, limit-seed)

        offset = min(amt, amt2, amt3, amt4, amt5, amt6, amt7)
        if loc < smallest:
            smallest = loc
        
        if smallest == 0:
            break
        
        seed += offset
        length -= offset

print(smallest)
