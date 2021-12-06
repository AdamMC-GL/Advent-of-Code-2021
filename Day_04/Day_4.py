lines = list(open('input.txt', 'r').read().split('\n\n'))
numbers = list(map(int, lines[0].split(',')))
boards = [[list(map(int, k.split())) for k in j] for j in [i.split('\n') for i in lines[1:]]]


def part1():
    for i in numbers:
        for board in boards:
            for row in board:
                for j in range(len(row)):
                    if i == row[j]:
                        row[j] = 0
                    if sum(row) == 0 or sum(board[x][j] for x in range(5)) == 0:
                        print(sum(sum(row) for row in board) * i)
                        return


def part2():
    for i in numbers:
        j = 0
        while j < len(boards):
            for row in boards[j]:
                for k in range(len(row)):
                    if i == row[k]:
                        row[k] = 0
                    if sum(row) == 0 or sum(boards[j][x][k] for x in range(5)) == 0:
                        if len(boards) < 2:
                            print(sum(sum(row) for row in boards[0]) * i)
                            return
                        boards.pop(j)
                        j -= 1
            j += 1


part1()
part2()
