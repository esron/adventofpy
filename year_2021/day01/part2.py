import os


def run():
    f = open(os.getcwd() + '/year_2021/day01/input.txt')
    increased = 0
    values = []

    line: str
    for line in f:
        values.append(int(line))

    first_window: int = values[0] + values[1] + values[2]
    second_window: int = values[1] + values[2] + values[3]

    i: int
    for i in range(2, len(values) - 2):
        third_window = values[i] + values[i + 1] + values[i + 2]

        if second_window > first_window:
            increased += 1

        first_window = second_window
        second_window = third_window

    if second_window > first_window:
        increased += 1

    print(increased)


if __name__ == "__main__":
    run()
