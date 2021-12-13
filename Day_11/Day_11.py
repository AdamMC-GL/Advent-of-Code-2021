lines = [list(map(int, j)) for j in [i for i in open('input.txt', 'r').read().split()]]
print(lines)
explosions = []
ex_num = 0


def explode(coord):
    explosions.append(coord)
    x, y = coord
    neighbours = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1),
                  (x - 1, y - 1), (x + 1, y + 1), (x + 1, y - 1), (x - 1, y + 1)]
    for x2, y2 in neighbours:
        if 0 <= y2 < len(lines) and 0 <= x2 < len(lines[y]) and (x2, y2) not in explosions:
            lines[y2][x2] += 1
            if lines[y2][x2] > 9:
                lines[y2][x2] = 0
                explode((x2, y2))


for i in range(502):
    for y in range(len(lines)):
        for x in range(len(lines[y])):
            if (x, y) not in explosions:
                lines[y][x] += 1
                if lines[y][x] > 9:
                    lines[y][x] = 0
                    explode((x, y))
    ex_num += len(explosions)
    if len(explosions) == len(lines) * len(lines[0]):
        print(i+1)
    explosions = []

print("ex_num:", ex_num)
