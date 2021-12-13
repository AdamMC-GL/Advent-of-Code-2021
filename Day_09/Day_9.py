lines = open('input.txt', 'r').read().split()

total = 0
all_mins = []
for y in range(len(lines)):
    for x in range(len(lines[y])):
        neighbours = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
        if not sum(int(lines[a][b]) <= int(lines[y][x]) for b, a in neighbours if 0 <= a < len(lines) and 0 <= b < len(lines[y])):
            total += int(lines[y][x])+1
            all_mins.append((x, y))

print(total)


def get_neigh(coords, prev=[]):
    prev += [coords]
    total_coords = [coords]
    x, y = coords
    neighbours = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
    for x2, y2 in neighbours:
        if 0 <= y2 < len(lines) and 0 <= x2 < len(lines[y]) and lines[y2][x2] != '9' and (x2, y2) not in prev:
            total_coords += get_neigh((x2, y2), prev)
    return total_coords


b = sorted([len(set(get_neigh(c))) for c in all_mins])[-3:]
print(b[0] * b[1] * b[2])
