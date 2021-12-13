lines, ins = open('input.txt', 'r').read().split("\n\n")
lines = [list(map(int, i.split(","))) for i in lines.split("\n")]
ins = [(i[11], int(i[13:])) for i in ins.split("\n")]

# Part 1
for d, n in ins:
    for i in lines:
        if i[d == "y"] > n:
            i[d == "y"] -= (i[d == "y"] - n) * 2
    print(len(set(map(tuple, lines))))

# Part 2
for y in range(6):
    for x in range(40):
        print("█" if [x, y] in lines else " ", end="")
    print("")
