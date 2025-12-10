import os
from collections import deque


def run():
    f = open(os.getcwd() + '/year_2021/day10/input.txt')
    closing = {
        ')': ['(', 3],
        ']': ['[', 57],
        '}': ['{', 1197],
        '>': ['<', 25137],
    }

    score = 0
    for line in f:
        line = line.rstrip()
        q = deque()

        for c in line:
            if c in ('(', '[', '{', '<'):
                q.append(c)
            elif q[-1] == closing[c][0]:
                q.pop()
            else:
                score += closing[c][1]
                break

    print(score)


if __name__ == "__main__":
    run()
