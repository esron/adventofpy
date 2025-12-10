import os


def filter_ones(values, index):
    return list(filter(lambda e: e[index] == '1', values))


def filter_zeros(values, index):
    return list(filter(lambda e: e[index] == '0', values))


def oxygen_generator_rating(values, index):
    if len(values) == 1:
        return values[0]

    ones = filter_ones(values, index)
    zeros = filter_zeros(values, index)

    if len(ones) >= len(zeros):
        return oxygen_generator_rating(ones, index+1)
    else:
        return oxygen_generator_rating(zeros, index+1)


def CO2_scrubber_rating(values, index):
    if len(values) == 1:
        return values[0]

    ones = filter_ones(values, index)
    zeros = filter_zeros(values, index)

    if len(zeros) > len(ones):
        return CO2_scrubber_rating(ones, index+1)
    else:
        return CO2_scrubber_rating(zeros, index+1)


def run():
    f = open(os.getcwd() + '/year_2021/day03/input.txt')
    input = []

    for line in f:
        input.append(line.rstrip())
    ogr = int(oxygen_generator_rating(input, 0), 2)
    csr = int(CO2_scrubber_rating(input, 0), 2)

    print(ogr * csr)


if __name__ == "__main__":
    run()
