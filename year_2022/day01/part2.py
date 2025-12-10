import os

def run():
    file = open(os.getcwd() + '/year_2022/day01/input.txt')
    lines = []
    for line in file:
        lines.append(line.rstrip())

    sums = []
    s = 0
    for line in lines:
        if (line == ''):
            sums.append(s)
            s = 0
            continue
        s += int(line)
    sums.sort(reverse=True)
    print(sum(sums[:3]))
if __name__ == "__main__":
    run()
