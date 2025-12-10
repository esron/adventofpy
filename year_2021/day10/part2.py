import os
from collections import deque


def run():
    f = open(os.getcwd() + '/year_2021/day10/input.txt')
    scores = []

    closing = {
        ')': '(',
        ']': '[',
        '}': '{',
        '>': '<',
    }

    values = {
        '(': 1,
        '[': 2,
        '{': 3,
        '<': 4,
    }

    for line in f:
        line = line.rstrip()
        q = deque()
        score = 0

        for c in line:
            if c in ('(', '[', '{', '<'):
                q.append(c)
            elif q[-1] == closing[c]:
                q.pop()
            else:
                q.clear()
                break

        if len(q) > 0:
            while len(q) > 0:
                c = q.pop()
                score *= 5
                score += values[c]

            scores.append(score)

    print(sorted(scores)[int(len(scores) / 2)])


if __name__ == "__main__":
    run()
