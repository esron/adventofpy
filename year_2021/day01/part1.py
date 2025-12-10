import os


def run():
    file = open(os.getcwd() + '/year_2021/day01/input.txt')
    increased = 0
    previous = int(file.readline())
    actual = int(file.readline())
    if actual > previous:
        increased += 1
    for line in file:
        previous = actual
        actual = int(line)
        if actual > previous:
            increased += 1
    print(increased)


if __name__ == "__main__":
    run()
