import os


def run():
    f = open(os.getcwd() + '/year_2021/day02/input.txt')
    depth = 0
    position = 0

    for line in f:
        comand, value = line.rstrip().split(' ')
        if comand == 'forward':
            position += int(value)
        if comand == 'down':
            depth += int(value)
        if comand == 'up':
            depth -= int(value)

    print(depth * position)


if __name__ == "__main__":
    run()
