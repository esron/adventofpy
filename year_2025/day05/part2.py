import os
from functools import reduce

def solve(input_path):
    ranges = []
    with open(input_path, "r") as f:
        for line in f:
            line = line.strip()
            if line == "":
                break
            start, end = line.split("-")
            ranges.append((int(start), int(end)))

    ranges = sorted(ranges)

    no_intersections_ranges = []
    while len(ranges) != 0:
        testing = ranges.pop(0)
        start = testing[0]
        end = testing[1]
        for i in range(len(ranges)):
            if end < ranges[i][0]:
                i -= 1
                break
            if ranges[i][0] <= end < ranges[i][1]:
                end = ranges[i][1]
        no_intersections_ranges.append((start, end))
        ranges = ranges[i+1:]

    sum = reduce(lambda x, r: x + (r[1] - r[0]) + 1, no_intersections_ranges, 0)
    print(sum)

def run():
    print("Example:")
    solve(os.getcwd() + "/year_2025/day05/example.txt")
    print("Input:")
    solve(os.getcwd() + "/year_2025/day05/input.txt")

if __name__ == "__main__":
    run()
