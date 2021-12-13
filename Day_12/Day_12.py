lines = [i.split("-") for i in open('input.txt', 'r').read().split()]
caves = {}

for f, t in lines:
    caves[f] = caves.get(f, []) + [t]
    caves[t] = caves.get(t, []) + [f]

def part1(c, s):
    s = s + [c] * c.islower()
    if c == "end":
        return 1
    return sum(part1(i, s) for i in caves[c] if i not in s)

def part2(c, s):
    s = s + [c] * c.islower()
    if c == "end":
        return 1
    return sum(part2(i, s) for i in caves[c] if (len(s) == len(set(s)) or i not in s) and i != "start")

print(part1("start", []))
print(part2("start", []))
