import os

class Tree:
    def __init__(self, value: str) -> None:
        self.value = int(value)
        self.visited = False
def run():
    map = None
    with open(os.getcwd() + '/year_2022/day08/input.txt') as f:
        map = [[Tree(i) for i in line.rstrip()] for line in f.readlines()]
    # Perimeter formula for a discrete rectangle
    map_perimeter = 2 * (len(map) + len(map[0])) - 4
    visible = map_perimeter

    # Check lines
    for i in range(1, len(map) - 1):
        highest = map[i][0].value
        if highest == 9:
            continue
        for j in range(1, len(map[0]) - 1):
            if map[i][j].value > highest:
                highest = map[i][j].value
                if not map[i][j].visited:
                    visible += 1
                map[i][j].visited = True
                if highest == 9:
                    break

    # Check lines reversed
    for i in range(len(map) - 2, 0, -1):
        highest = map[i][len(map[0]) - 1].value
        if highest == 9:
            continue
        for j in range(len(map[0]) - 2, 0, -1):
            if map[i][j].value > highest:
                highest = map[i][j].value
                if not map[i][j].visited:
                    visible += 1
                map[i][j].visited = True
                if highest == 9:
                    break

    # Check columns
    for i in range(1, len(map[0]) - 1):
        highest = map[0][i].value
        if highest == 9:
            continue
        for j in range(1, len(map) - 1):
            if map[j][i].value > highest:
                highest = map[j][i].value
                if not map[j][i].visited:
                    visible += 1
                map[j][i].visited = True
                if highest == 9:
                    break

    # Check columns reversed
    for i in range(len(map[0]) - 2, 0, -1):
        highest = map[len(map) - 1][i].value
        if highest == 9:
            continue
        for j in range(len(map) - 2, 0, -1):
            if map[j][i].value > highest:
                highest = map[j][i].value
                if not map[j][i].visited:
                    visible += 1
                map[j][i].visited = True
                if highest == 9:
                    break

    print(visible)
if __name__ == "__main__":
    run()
