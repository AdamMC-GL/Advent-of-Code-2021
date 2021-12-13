lines = [list(i) for i in open('input.txt', 'r').read().split()]

table = {")": ["(", 3], "]": ["[", 57], "}": ["{", 1197], ">": ["<", 25137]}
total = 0
inc_lines = []
for line in lines:
    i = 0
    corrupt = False
    while i < len(line):
        if line[i] in table:
            if table[line[i]][0] == line[i-1]:
                del line[i-1:i+1]
                i -= 2
            else:
                total += table[line[i]][1]
                corrupt = True
                break
        i += 1
    if not corrupt:
        inc_lines.append(line)

print(total)

total = []
table = {"(": 1, "[": 2, "{": 3, "<": 4}
for line in inc_lines:
    score = 0
    for char in reversed(line):
        score *= 5
        score += table[char]
    total.append(score)

print(total[len(total)//2])

