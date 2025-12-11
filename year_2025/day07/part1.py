import os


def solve(input_path):
    with open(input_path, "r") as f:
        diagram = [list(line.strip()) for line in f.readlines()]

    for i in range(len(diagram)):
        for j in range(len(diagram[i])):
            match diagram[i][j]:
                case "S":
                    diagram[i+1][j] = "|"
                case "^":
                    if diagram[i-1][j] == "|":
                        diagram[i][j-1] = "|"
                        diagram[i][j+1] = "|"
                        diagram[i+1][j-1] = "|"
                        diagram[i+1][j+1] = "|"
                case ".":
                    if i > 0 and diagram[i-1][j] == "|":
                        diagram[i][j] = "|"

    count = 0
    for i in range(len(diagram)):
        for j in range(len(diagram[i])):
            if diagram[i][j] == "^" and diagram[i-1][j] == "|":
                count += 1
    print(count)


def run():
    print("Example:")
    solve(os.getcwd() + "/year_2025/day07/example.txt")
    print("Input:")
    solve(os.getcwd() + "/year_2025/day07/input.txt")


if __name__ == "__main__":
    run()
