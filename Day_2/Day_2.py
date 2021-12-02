lines = [[j[0], int(j[1])] for j in map(lambda i: i.split(), open('input.txt', 'r').readlines())]

# Part 1
depth, hor, aim = 0, 0, 0
for pos, x in lines:
    hor += x * (pos == "forward")
    depth += x * (pos == "down") or -(x * (pos == "up"))
print(hor*depth)

# Part 2
depth, hor, aim = 0, 0, 0
for pos, x in lines:
    hor += x * (pos == "forward")
    depth += aim * x * (pos == "forward")
    aim += x * (pos == "down") or -(x * (pos == "up"))
print(hor*depth)
