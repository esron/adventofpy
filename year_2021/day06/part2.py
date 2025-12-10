import os
from collections import deque


def count_fish(fishes, days):
    q = deque(fishes)

    for _ in range(days):
        spawn = q.popleft()
        q[-2] += spawn
        q.append(spawn)
    return sum(q)


def run():
    f = open(os.getcwd() + '/year_2021/day06/input.txt')
    input = f.readline()
    input = list(map(int, input.rstrip().split(',')))

    fishes = [0] * 9

    for i in input:
        fishes[int(i)] += 1

    print(count_fish(fishes, 256))


if __name__ == "__main__":
    run()
