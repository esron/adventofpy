import os

def solve(input_path):
    sum = 0
    with open(input_path, "r") as f:
        ranges = f.read().split(",")
        for r in ranges:
            start, end = r.split("-")
            start = int(start)
            end = int(end)
            for id_num in range(start, end + 1):
                id_str = str(id_num)
                midpoint = len(id_str) // 2
                for i in range(midpoint):
                    sub_str = id_str[:i+1]
                    for j in range(0, len(id_str), i+1):
                        if sub_str != id_str[j:j+i+1]:
                            break
                    else:
                        sum += id_num
                        break
    print(sum)

def run():
    print("Example:")
    solve(os.getcwd() + "/year_2025/day02/example.txt")
    print("Input:")
    solve(os.getcwd() + "/year_2025/day02/input.txt")

if __name__ == "__main__":
    run()
