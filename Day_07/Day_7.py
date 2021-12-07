lines = list(map(int, open('input.txt', 'r').read().split(',')))

# Part 1
n = min(lines)
old, new = 1, 0
while new < old or old == 0:
    n += 1
    old = new
    new = sum(abs(n-j) for j in lines)
print(n, int(old))

# Part 2
n = min(lines)
old, new = 1, 0
while new < old or old == 0:
    n += 1
    old = new
    new = sum((abs(n - j) + 1)*(abs(n - j))/2 for j in lines)
print(n, int(old))



