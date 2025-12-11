import os

def solve(file_path: str):
    dial = 50
    zero_count = 0
    with open(os.getcwd() + file_path) as f:
        for line in f:
            direction = line[0]
            rotation = int(line[1:])
            if direction == 'L':
                dial -= rotation
            if direction == 'R':
                dial += rotation
            dial = dial % 100
            if dial == 0:
                zero_count += 1
    print(zero_count)


def run():
    print("Example:")
    solve("/year_2025/day01/example.txt")
    print("Input:")
    solve("/year_2025/day01/input.txt")

if __name__ == "__main__":
    run()
