import re

with open("aoc3.txt") as f:
    inp = f.read().replace('\n', '')

partA = re.compile("mul\\((?P<a>\d*),(?P<b>\d*)\\)")
# sampleA = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"

totalA = 0
for a, b in partA.findall(inp):
    totalA += int(a) * int(b)
print(f"A: {totalA}")

partB = re.compile("don't\\(\\).*?do\\(\\)")
# sampleB = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"

totalB = 0
for a, b in partA.findall(partB.sub("", inp)):
    totalB += int(a) * int(b)

print(f"B: {totalB}")