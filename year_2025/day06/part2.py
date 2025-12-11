import os
import operator
from functools import reduce


def solve(input_path):
    with open(input_path, "r") as f:
        lines = list(reversed(f.readlines()))

    sum = 0
    operands = []
    for i in range(len(lines[0])):
        column = [l[i] for l in lines]
        if all(c == " " or c == "\n" for c in column):
            # calculate operation
            sum += reduce(op, operands)
            operands = []
            continue
        # define operation
        match column[0]:
            case "*":
                op = operator.mul
            case "+":
                op = operator.add
        # find operands
        column = "".join(column[1:])[::-1]
        operands.append(int(column))

    print(sum)

def run():
    print("Example:")
    solve(os.getcwd() + "/year_2025/day06/example.txt")
    print("Input:")
    solve(os.getcwd() + "/year_2025/day06/input.txt")

if __name__ == "__main__":
    run()
