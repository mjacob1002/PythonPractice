import numpy as np


# given a function random that gives a random from [0,1)
def jomaTech(k):
    points_in_circle = 0
    points = 0
    for i in range(k):
        x = np.random.uniform()
        y = np.random.uniform()
        if (x ** 2 + y ** 2) < 1:
            points_in_circle = points_in_circle + 1
        points = points + 1
    return 4 * points_in_circle / points


def closestNumber(n: int, m: int):
    pass


def printPat(n: int):
    count = n
    while count > 0:
        c = count ** 2
        while c > 0:
            x = np.ceil(c / count)
            print(str(int(x)) + " ", end="")
            c = c - 1
        count = count - 1
        print()


def fibonacci(n):  # write a short algorithm that produces the nth term in the fibonacci sequence
    if (n is 1):
        return 0
    if (n is 2):
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


# takes the position of a night and returns all of the possible moves


def knight_moves(pos: list):
    moves = []
    for place in pos:
        if place[0] - 1 > -1:
            moves.append([place[0] - 1, place[1]])


def target(n: int, arr: list, arr_two: list):  # best solution is to sort each array then binary search one and linear
    # scan the other
    min = abs(n - (arr[0] + arr_two[0]))
    nums = [0, 0]
    for i in range(len(arr)):
        for j in range(len(arr_two)):
            sum = arr[i] + arr_two[j]
            if min > abs(n - sum):
                min = abs(n - sum)
                nums.pop(0)
                nums.pop(0)
                nums.append(i)
                nums.append(j)
    ans = [arr[nums[0]], arr_two[nums[1]]]
    return ans


def pentagonal_number(n: int):
    return int(2.5 * n ** 2 - 2.5 * n + 1)


def duplicate_letters(phrase: str):
    list = phrase.split()
    for i in list:
        seen: set
        seen = set({})
        for j in range(len(i)):
            if i[j] not in seen:
                seen.add(i[j])
            else:
                return False
    return True


def majority_vote(votes: list):
    dict = {}
    for vote in votes:
        if dict.get(vote, "empty") == "empty":
            dict.add(vote, 1)
        else:
            dict.update(vote, dict.get(vote) + 1)
            if 2 * dict.get(vote) >= len(votes):
                return vote
    return None


def next_prime(n):
    pass


def primorial(n):
    pass


def freed_prisoners(cells: list):
    count = 0
    copy = cells
    for cell in copy:
        if cell == 1:
            count += 1
            for j in range(len(copy)):
                if copy[j] == 0:
                    copy[j] = 1
                else:
                    copy[j] = 0
    return count


def simplify(fraction: str):
    pass


# work in progress
def cannon(location: tuple, angle: float, distance: int):  # return landing location of cannon shell
    coordinate = list(location)
    x = coordinate[0]
    y = coordinate[1]
    new_angle = 90 - angle
    xnew = int(x + distance * np.cos(new_angle))
    ynew = int(y + distance * np.sin(new_angle))
    return xnew, ynew



