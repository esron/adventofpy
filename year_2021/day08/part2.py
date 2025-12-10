import os


def sort_and_split(input):
    return [''.join(sorted(s)) for s in input.strip().split(' ')]


def easy_numbers(numbers, input):
    for s in input:
        if len(s) == 2:
            numbers[1] = s
        elif len(s) == 3:
            numbers[7] = s
        elif len(s) == 4:
            numbers[4] = s
        elif len(s) == 7:
            numbers[8] = s

    return numbers


def calculate_line(numbers, output):
    total = ''
    for s in output:
        total += str(numbers.index(s))
    return int(total)


def doesnt_have_one(one, input):
    return not one[0] in input or not one[1] in input


def has_number(number, input):
    for c in number:
        if c not in input:
            return False
    return True


def run():
    f = open(os.getcwd() + '/year_2021/day08/input.txt')

    total = 0
    for line in f:
        numbers = [''] * 10
        input, output = line.rstrip().split('|')
        input = sort_and_split(input)
        output = sort_and_split(output)

        numbers = easy_numbers(numbers, input)

        for i in input:
            if len(i) == 6:
                if doesnt_have_one(numbers[1], i):
                    numbers[6] = i
                elif has_number(numbers[4], i):
                    numbers[9] = i
                else:
                    numbers[0] = i
        for i in input:
            if len(i) == 5:
                if has_number(numbers[1], i):
                    numbers[3] = i
                elif has_number(i, numbers[6]):
                    numbers[5] = i
                else:
                    numbers[2] = i
        total += calculate_line(numbers, output)

    print(total)


if __name__ == "__main__":
    run()
