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

"""Explanation:
Part 1 and 2: 
The puzzle directs you to an approach to just update the list with fish and expand it everytime one creates
a new fish. This would exponentially increase the list size. Instead the list 'ex' is used to keep track how many
fish in theory should exist. The values in the list is (in total) the amount of fish in existence, and the position of each
value is the moment they should create a new fish with a loop through the list being a cycle of 9 days, because each new fish
is at most 9 days away from creating a new one. ex starts with the initialized amount of fish from the input.

The index counter starts at 0 and looks at the value of ex at index 0. That position corresponds to that day
of fish creating a new fish each as well as resetting their own timer. In order to cause that, that value at position
0 is added to 2 positions behind the current day (7 days away), because the reset fish will all create a new fish 7
days from now on top of those who where already prone to. The value that is already in that spot then corresponds to
the newly created fish, since all fish of that day create 1 it is the same value. Newly created fish
get a timer of 9 days (since 0 is included), that's the length of the list and cycle and therefore are put
in the same spot by doing nothing.

Index resets every cycle to move back to the first item, and this process is repeated until the input amount
of days have finished
"""