import os


def run():
    f = open(os.getcwd() + '/year_2021/day08/input.txt')
    count = 0

    for line in f:
        output = line.rstrip().split('|')[1].lstrip().split(' ')
        for s in output:
            if len(s) in (2, 3, 4, 7):
                count += 1

    print(count)


if __name__ == "__main__":
    run()
