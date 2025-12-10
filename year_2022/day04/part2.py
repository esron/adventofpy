import os

def run():
    with open(os.getcwd() + '/year_2022/day04/input.txt') as f:
        overlaps = 0
        for line in f:
            bounds = []
            for pair in line.rstrip().split(','):
                bounds.append(tuple(int(n) for n in pair.split('-')))
            if not (bounds[0][1] < bounds[1][0] or bounds[1][1] < bounds[0][0]):
                overlaps += 1
        print(overlaps)
if __name__ == "__main__":
    run()
