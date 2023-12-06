from math import ceil
from sys import argv

if len(argv) != 2:
    print(f"Usage: python {argv[0]} <filename>")
    exit(1)

with open(f"{argv[1]}.txt") as f:
    data = f.read().split("\n\n")

seeds = [int(s) for s in data[0].split(" ")[1:]]
seeds = [(seeds[i], seeds[i+1]) for i in range(0, len(seeds), 2)]
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

def calc(mapping: dict[tuple[int,int], int], key: int, left: int, right: int, limit: int) -> int:
    res = key
    for lower, upper in mapping:
        if lower <= key <= upper:
            res = (key-lower) + mapping[(lower, upper)]
            left = upper-key
            break

    return res, left

smallest = float("inf")
it = 0
for seed, length in seeds:
    limit = seed + length
    while seed < limit:
        amt = 0
        independent = False
        
        soil, amt = calc(seed_soil, seed, amt, length, limit)
        # for lower, upper in seed_soil:
        #     if lower <= seed <= upper:
        #         soil = (seed-lower) + seed_soil[(lower, upper)]
        #         amt = min(upper-seed, length-1, limit-seed)
        #         print(seed, lower, amt)
        #         print(upper-seed, length-1, limit-seed)
        #         seed += amt
        #         length -= amt
        #         break
        # if soil == seed:
        #     amt -= 1
        #     length += amt
        #     seed -= length
        #     independent = True

        fert = soil
        for lower, upper in soil_fert:
            if lower <= soil <= upper:
                fert = (soil-lower) + soil_fert[(lower, upper)]
                if soil+amt-upper > 0 and not independent:
                    amt -= upper-soil
                    amt = min(upper-soil, length-1, limit-seed)
                    length += amt
                    seed -= amt
                break
        if fert == soil and not independent:
            amt -= 1
            length += amt
            seed -= amt
            independent = True

        water = fert
        for lower, upper in fert_water:
            if lower <= fert <= upper:
                water = (fert-lower) + fert_water[(lower, upper)]
                if water+amt-upper > 0 and not independent:
                    amt -= upper-fert
                    amt = min(upper-fert, length-1, limit-seed)
                    length += amt
                    seed -= amt
                break
        if water == fert and not independent:
            amt -= 1
            length += amt
            seed -= amt
            independent = True
        
        light = water
        for lower, upper in water_light:
            if lower <= water <= upper:
                light = (water-lower) + water_light[(lower, upper)]
                if light+amt-upper > 0 and not independent:
                    amt -= upper-water
                    amt = min(upper-water, length-1, limit-seed)
                    length += amt
                    seed -= amt
                break
        if light == water and not independent:
            amt -= 1
            length += amt
            seed -= amt
            independent = True
        
        temp = light
        for lower, upper in light_temp:
            if lower <= light <= upper:
                temp = (light-lower) + light_temp[(lower, upper)]
                if temp+amt-upper > 0 and not independent:
                    amt -= upper-light
                    amt = min(upper-light, length-1, limit-seed)
                    length += amt
                    seed -= amt
                break
        if temp == light and not independent:
            amt -= 1
            length += amt
            seed -= amt
            independent = True

        humid = temp
        for lower, upper in temp_humid:
            if lower <= temp <= upper:
                humid = (temp-lower) + temp_humid[(lower, upper)]
                if humid+amt-upper > 0 and not independent:
                    amt -= upper-temp
                    amt = min(upper-temp, length-1, limit-seed)
                    length += amt
                    seed -= amt
                break
        if humid == temp and not independent:
            amt -= 1
            length += amt
            seed -= amt
            independent = True
        
        loc = humid
        for lower, upper in humid_loc:
            if lower <= humid <= upper:
                loc = (humid-lower) + humid_loc[(lower, upper)]
                if loc+amt-upper > 0 and not independent:
                    amt -= upper-humid
                    amt = min(upper-humid, length-1, limit-seed)
                    length += amt
                    seed -= amt
                break
        if loc == humid and not independent:
            amt -= 1
            length += amt
            seed -= amt
            independent = True
        
        print(f"Iteration {it}: {seed = } {seed/limit * 100:.2f}%", end="\r")
        # print(f"{soil = }, {fert = }, {water = }, {light = }, {temp = }, {humid = }, {loc = }")
        # print(f"{seed = }, {length = }, {amt = }")
        if loc < smallest:
            smallest = loc
        
        if smallest == 0:
            break
        
        # seed += 1
    
    print()
    it += 1

print(smallest)
