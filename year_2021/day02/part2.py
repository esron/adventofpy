import os


def run():
    f = open(os.getcwd() + '/year_2021/day02/input.txt')
    depth = 0
    position = 0
    aim = 0

    for line in f:
        comand, value = line.rstrip().split(' ')
        value = int(value)

        if comand == 'forward':
            position += value
            depth += value * aim
        if comand == 'down':
            aim += value
        if comand == 'up':
            aim -= value

    print(depth * position)


if __name__ == "__main__":
    run()
