lines = list(map(int, open('input.txt', 'r').readlines()))
print(sum(1 for i in range(len(lines)) if lines[i-1] < lines[i]))  # part 1
print(sum(1 for i in range(len(lines)) if lines[i-3] < lines[i]))  # part 2
