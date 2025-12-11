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
                if len(id_str) % 2 == 0:
                    midpoint = len(id_str) // 2
                    start_str = id_str[:midpoint]
                    end_str = id_str[midpoint:]
                    if start_str == end_str:
                        sum += id_num
    print(sum)

def run():
    print("Example:")
    solve(os.getcwd() + "/year_2025/day02/example.txt")
    print("Input:")
    solve(os.getcwd() + "/year_2025/day02/input.txt")

if __name__ == "__main__":
    run()
