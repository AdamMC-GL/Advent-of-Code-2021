lines = list(map(lambda i: i.split("|"), open('input.txt', 'r').readlines()))

total = 0
for i in lines:
    seven, four = sorted(i[0].split(), key=len)[1:3]
    output = ""
    for nr in i[1].split():
        if len(nr) == 2: output += "1"
        if len(nr) == 3: output += "7"
        if len(nr) == 4: output += "4"
        if len(nr) == 7: output += "8"
        if len(nr) == 5:
            if len(set(nr) - set(four)) == 3: output += "2"
            elif len(set(nr) - set(seven)) == 2: output += "3"
            else: output += "5"
        if len(nr) == 6:
            if len(set(nr) - set(four)) == 2: output += "9"
            elif len(set(nr) - set(seven)) == 3: output += "0"
            else: output += "6"
    total += int(output)
print(total)