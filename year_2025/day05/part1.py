import os

class IdRange:
    def __init__(self, range_str):
        start, end = range_str.split("-")
        self.start = int(start)
        self.end = int(end)
    def contains(self, id_num):
        return self.start <= id_num <= self.end

def solve(input_path):
    count = 0
    with open(input_path, "r") as f:
        lines = f.read().splitlines()
        i = 0
        id_ranges = []
        while lines[i] != "":
            id_ranges.append(IdRange(lines[i]))
            i += 1

        i += 1
        while i < len(lines):
            id_num = int(lines[i])
            if any(id_range.contains(id_num) for id_range in id_ranges):
                count += 1
            i += 1

    print(count)

def run():
    print("Example:")
    solve(os.getcwd() + "/year_2025/day05/example.txt")
    print("Input:")
    solve(os.getcwd() + "/year_2025/day05/input.txt")

if __name__ == "__main__":
    run()
