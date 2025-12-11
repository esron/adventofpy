import os
from re import X

def solve(file_path: str):
    dial = 50
    zero_count = 0
    with open(os.getcwd() + file_path) as f:
        for line in f:
            direction = line[0]
            rotation = int(line[1:])
            # corner case where the dial is at 0 an we move by a small amount
            # i.e dial = 0, rotation = 5, direction = 'L'
            # zero_count should NOT be incremented by 1
            if dial == 0 and direction == 'L':
                dial -= rotation
                zero_count += (dial // -100)
                dial = dial % 100
                continue
            if direction == 'L':
                dial -= rotation
            if direction == 'R':
                dial += rotation
            if dial == 0:
                zero_count += 1
            if dial < 0:
                zero_count += (dial // -100) + 1
            if dial > 99:
                zero_count += (dial // 100)
            dial = dial % 100
    print(zero_count)


def run():
    print("Example:")
    solve("/year_2025/day01/example.txt")
    print("Input:")
    solve("/year_2025/day01/input.txt")

if __name__ == "__main__":
    run()
