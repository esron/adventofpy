import os

def run():
    with open(os.getcwd() + '/year_2022/day04/input.txt') as f:
        contains = 0
        for line in f:
            bounds = []
            for pair in line.rstrip().split(','):
                bounds.append(tuple(int(n) for n in pair.split('-')))
            if (bounds[0][0] <= bounds[1][0] and bounds[0][1] >= bounds[1][1]) or \
                    (bounds[0][0] >= bounds[1][0] and bounds[0][1] <= bounds[1][1]):
                contains += 1
        print(contains)
if __name__ == "__main__":
    run()
