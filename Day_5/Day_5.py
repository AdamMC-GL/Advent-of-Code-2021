lines = [list(map(int, i.replace(" -> ", ",").split(','))) for i in open('input.txt', 'r').readlines()]

# Part 1
all_coords = {}
for i in lines:
    if i[0] == i[2]:
        uniques, dupe = [i[1], i[3]], i[0]
        for j in range(min(uniques), max(uniques) + 1):
            all_coords[(dupe, j)] = all_coords.get((dupe, j), 0) + 1
    elif i[1] == i[3]:
        uniques, dupe = [i[0], i[2]], i[1]
        for j in range(min(uniques), max(uniques) + 1):
            all_coords[(j, dupe)] = all_coords.get((j, dupe), 0) + 1

print(sum(1 for i in all_coords.values() if i > 1))

# Part 2
for i in lines:
    if i[1] != i[3] and i[0] != i[2]:
        diff = max(i[0], i[2])+1 - min(i[0], i[2])
        x = list(range(min(i[0], i[2]), max(i[0], i[2]) + 1))
        y = list(range(min(i[1], i[3]), max(i[1], i[3]) + 1))
        if (i[0] > i[2]) + (i[1] > i[3]) == 1:
            x.reverse()
        for j in range(0, diff):
            all_coords[(x[j], y[j])] = all_coords.get((x[j], y[j]), 0) + 1

print(sum(1 for i in all_coords.values() if i > 1))

"""Explanation:
Part 1: 
For every line its checked whether x or y are the same, to see if the line is horizontal or vertical. Then the numbers
that are not the same, and the number that is are extracted and used to make a iterator containing every
coordinate. Each coordinate is put in a dict with the value being how often the coordinate has appeared.
Then the amount of keys containing a value above 1 is counted.

Part 2:
Since the horizontal and vertical lines are still needed, part 2 just adds onto part 1. First it checks
if the line is diagonal. Then obtains the difference between the two x's (which is the same for the 2 y's), 
2 lists are then made with every value between the 2 x's and y's. The difference number is then
used to increment through the 2 lists equally to get the all the diagonal values, which are put in the
dict again. There is also a check to reverse the x list to make sure the x and y list match in order."""
