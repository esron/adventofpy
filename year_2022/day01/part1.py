import os

def run():
    file = open(os.getcwd() + '/year_2022/day01/input.txt')
    lines = []
    for line in file:
        lines.append(line.rstrip())

    max = 0
    sum = 0
    for line in lines:
        if (line == ''):
            if (sum > max):
                max = sum
            sum = 0
            continue
        sum += int(line)
    print(max)
if __name__ == "__main__":
    run()
