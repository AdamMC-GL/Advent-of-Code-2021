lines = list(map(int, open('input.txt', 'r').read().split(',')))


def day_6(days):
    index = 0
    ex = [lines.count(i) for i in range(9)]

    for i in range(days):
        ex[index-2] += ex[index]
        index += 1
        if index > 8:
            index = 0
    print(sum(ex))


day_6(80)
day_6(256)
