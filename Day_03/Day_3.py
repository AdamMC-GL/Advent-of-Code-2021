lines = open('input.txt', 'r').read().splitlines()

# Part 1
gamma, ep = "", ""
for i in range(len(lines[0])):
    count = sum(int(_[i]) for _ in lines) - len(lines)/2
    gamma += str(int(count > 0))
    ep += str(int(count < 0))
print(int(gamma, 2) * int(ep, 2))

# Part 2
ox, co = lines, lines
for i in range(len(lines[0])):
    ox_ = sum(int(_[i]) for _ in ox) - len(ox)/2
    co_ = sum(int(_[i]) for _ in co) - len(co)/2
    ox = [x for x in ox if x[i] == str(int(ox_ >= 0))]
    co = [x for x in co if x[i] == str(int(co_ < 0)) or len(co) < 2]
print(int(ox[0], 2) * int(co[0], 2))

"""Explanation:
Part 1: 
count is the sum of the total 1's per column of bytes (top to bottom), 
it is than subtracted with half the length of the column, if there are more 1's than 0's
the end result should give a number above 0, else below 0. If its above 0 a '1' is appended
to gamma, else a 0. The opposite for epsilon.

Part 2:
ox_ and co_ are same as for count in part 1, but for each respective list of ox (oxygen) and co (CO2). 
This outcome is then applied in the lines below. If the bit is a one and the statement is true (there where more ones), 
than that byte stays in the list."""
