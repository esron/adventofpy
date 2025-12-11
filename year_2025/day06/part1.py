import os
import operator
from functools import reduce


def solve(input_path):
    with open(input_path, "r") as f:
        lines = f.readlines()

    operators = [operator.add if o == '+' else operator.mul
        for o in lines.pop().split()]

    operands = [
        [int(i) for i in line.split()]
        for line in lines
    ]

    sum = 0
    for i in range(len(operators)):
        sum += reduce(operators[i],[o[i] for o in operands])
    print(sum)

def run():
    print("Example:")
    solve(os.getcwd() + "/year_2025/day06/example.txt")
    print("Input:")
    solve(os.getcwd() + "/year_2025/day06/input.txt")

if __name__ == "__main__":
    run()
