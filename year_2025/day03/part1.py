import os

def solve(input_path):
    sum = 0
    with open(input_path, "r") as f:
        for line in f:
            line = line.strip()
            first_index = None
            for i in range(9, -1, -1):
                try:
                    first_index = line.index(str(i))
                except ValueError:
                    continue
                if first_index == len(line) - 1:
                    continue
                if first_index is not None:
                    break
            second_index = None
            for i in range(9, -1, -1):
                try:
                    second_index = line[first_index+1:].index(str(i)) + first_index + 1
                except ValueError:
                    continue
                if second_index is not None:
                    break
            joltage = int(f"{line[first_index]}{line[second_index]}")
            sum += joltage
    print(sum)

def run():
    print("Example:")
    solve(os.getcwd() + "/year_2025/day03/example.txt")
    print("Input:")
    solve(os.getcwd() + "/year_2025/day03/input.txt")

if __name__ == "__main__":
    run()
