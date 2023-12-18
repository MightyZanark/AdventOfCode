import turtle as t

with open('aoc18.txt') as f:
    data = [line.strip().split(' ') for line in f.readlines()]

def draw(data):
    """
        Draws part 1 of this puzzle, part 2 too big
    """
    t.screensize(5000, 5000)
    t.pensize(5)
    t.penup()
    t.hideturtle()
    t.speed(0)
    t.delay(0)

    for dir, length, color in data:
        length = int(length)
        color = color[1:-1]
        
        t.pencolor(color)
        t.pendown()
        if dir == 'L':
            t.seth(180)
        
        elif dir == 'U':
            t.seth(90)

        elif dir == 'R':
            t.seth(0)

        else:
            t.seth(270)
        # print(f'Before: {t.pos()}')
        t.forward(10 * length)
        # print(f'After: {t.pos()}')
        t.penup()

    t.color('red')
    t.dot(10)

    t.mainloop()

points = []
x = 0
y = 0
outer = 0
for dir, length, color in data[::-1]:
    # Backwards because wiki said 
    # for Shoelace formula the polygon is given with
    # positively oriented sequence of points
    
    # Part 1 dont modify length
    color = color[2:-1]
    length = int(color[:-1], 16)
    dir = color[-1]
    outer += length
    
    if dir == 'L' or dir == '2':
        x += (length)
    
    elif dir == 'R' or dir == '0':
        x -= (length)
    
    elif dir == 'U' or dir == '3':
        y -= length
    
    else:
        y += length
    
    points.append((x, y))

max_x = max(points, key=lambda z: z[0])[0]
min_x = min(points, key=lambda z: z[0])[0]
max_y = max(points, key=lambda z: z[1])[1]
min_y = min(points, key=lambda z: z[1])[1]

print(f'{max_x = } {min_x = }, {max_y = } {min_y = }')

if min_x != 0 or min_y != 0:
    for i in range(len(points)):
        points[i] = points[i][0] + abs(min_x), abs(points[i][1] + abs(min_y))

max_x = max(points, key=lambda z: z[0])[0]
min_x = min(points, key=lambda z: z[0])[0]
max_y = max(points, key=lambda z: z[1])[1]
min_y = min(points, key=lambda z: z[1])[1]

print(f'{max_x = } {min_x = }, {max_y = } {min_y = }')

# Shoelace Formula (https://en.wikipedia.org/wiki/Shoelace_formula)
# Hint from subreddit that used this for Day 10 Part 2
total = 0
points_len = len(points)
for i in range(points_len):
    # P_0 = P_n, P_(n+1) = P_1
    total += (points[i][1] + points[(i+1) % points_len][1]) * (points[i][0] - points[(i+1) % points_len][0])

area = abs(total) // 2
print(f'Ans: {area - (outer//2) + 1 + outer}') # Pick's theorem to get internal points (https://en.wikipedia.org/wiki/Pick%27s_theorem)
