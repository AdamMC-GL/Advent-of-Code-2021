lines = list(map(int, open('input.txt', 'r').readlines()))
print(sum(lines[i-1] < lines[i] for i in range(len(lines))))  # part 1
print(sum(lines[i-3] < lines[i] for i in range(len(lines))))  # part 2

"""Explanation:
Part 1: 
For each 2 consecutive values in 'lines' a 1 is added to a generator if the second value is bigger than the first,
this total is summed up and printed.

Part 2:
The same as part 1 but comparing with the first and fourth value, 
because comparing a+b+c with b+c+d is the same as just comparing a and d directly."""
