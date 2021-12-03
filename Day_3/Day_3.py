lines = open('input.txt', 'r').read().splitlines()

# Part 1
gamma, ep = "", ""
for i in range(len(lines[0])):
    count = sum(int(_[i]) for _ in lines) - len(lines)/2
    gamma += str(int(count > 0))
    ep += str(int(count < 0))
print(int(gamma, 2) * int(ep, 2))

# Part 2
ox, co = lines[:], lines
for i in range(len(lines[0])):
    ox_ = sum(int(_[i]) for _ in ox) - len(ox)/2
    co_ = sum(int(_[i]) for _ in co) - len(co)/2
    ox = [x for x in ox if x[i] == str(int(ox_ >= 0))]
    co = [x for x in co if x[i] == str(int(co_ < 0)) or len(co) < 2]
print(int(ox[0], 2) * int(co[0], 2))
