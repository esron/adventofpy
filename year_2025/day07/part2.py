import os
import operator
from functools import reduce


def solve(input_path):
    with open(input_path, "r") as f:
        diagram = [list(line.strip()) for line in f.readlines()]

    result = [0 for _ in diagram[0]]
    for i in range(0, len(diagram), 2):
        for j in range(len(diagram[i])):
            match diagram[i][j]:
                case "S":
                    result[j] = 1
                case "^":
                    result[j-1] += result[j]
                    result[j+1] += result[j]
                    result[j] = 0

    print(reduce(operator.add, result))


def run():
    print("Example:")
    solve(os.getcwd() + "/year_2025/day07/example.txt")
    print("Input:")
    solve(os.getcwd() + "/year_2025/day07/input.txt")


if __name__ == "__main__":
    run()
