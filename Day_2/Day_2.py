lines = [[j[0], int(j[1])] for j in map(lambda i: i.split(), open('input.txt', 'r').readlines())]

# Part 1
depth, hor = 0, 0
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

# part 1 one-line
print(sum(x * ("f" in pos) for pos, x in lines) * sum(x * ("n" in pos) or -(x * ("u" in pos)) for pos, x in lines))


"""Explanation:
Part 1: 
Each item in lines contains a list of 2 items, a string and an int (pos, x). x is multiplied by the
condition behind so that x is added or not if the condition is true or false respectively. With
depth there are 2 conditions that either lets x either be added or subtracted. Each outcome is either 0
or a value that is not 0. The or statement always chooses the side that is not 0.

Part 2:
The same logic applies as with part one but now with the added rules for part one. No change in implementation."""