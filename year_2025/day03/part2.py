import os

def solve(input_path):
    sum = 0
    with open(input_path, "r") as f:
        for line in f:
            line = line.strip()
            previous_index = 0
            joltage = ""
            for i in range(12, 0, -1):
                for j in range(9, -1, -1):
                    index = -1
                    try:
                        index = line.index(str(j), previous_index)
                    except ValueError:
                        continue
                    if index >= len(line) - i + 1:
                        continue
                    if index != -1:
                        joltage += str(j)
                        previous_index = index + 1
                        break
            sum += int(joltage)
    print(sum)

def run():
    print("Example:")
    solve(os.getcwd() + "/year_2025/day03/example.txt")
    print("Input:")
    solve(os.getcwd() + "/year_2025/day03/input.txt")

if __name__ == "__main__":
    run()
