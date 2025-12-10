import os


def calculate_basin_size(map, i, j):
    if i < 0 or j < 0:
        return 0
    try:
        if map[i][j] == '9':
            return 0
        if map[i][j] == 'X':
            return 0
    except IndexError:
        return 0
    map[i][j] = 'X'
    return 1 + calculate_basin_size(map, i, j-1) + \
        calculate_basin_size(map, i + 1, j) + \
        calculate_basin_size(map, i, j + 1) + \
        calculate_basin_size(map, i - 1, j)


def run():
    f = open(os.getcwd() + '/year_2021/day09/input.txt')
    basins = []
    map = []
    for line in f:
        map.append(list(line.rstrip()))

    # First line first cell
    if map[0][1] > map[0][0] < map[1][0]:
        basins.append(calculate_basin_size(map, 0, 0))

    # First line
    for i in range(1, len(map[0]) - 1):
        if map[0][i + 1] > map[0][i] < map[0][i - 1] \
                and map[0][i] < map[1][i]:
            basins.append(calculate_basin_size(map, 0, i))

    # First line last cell
    if map[0][-2] > map[0][-1] < map[1][-1]:
        basins.append(calculate_basin_size(map, 0, len(map[0]) - 1))

    # Main loop
    for i in range(1, len(map) - 1):
        # First cell
        if map[i][0] < map[i][1] \
                and map[i + 1][0] > map[i][0] < map[i - 1][0]:
            basins.append(calculate_basin_size(map, i, 0))

        # Line
        for j in range(1, len(map[i]) - 1):
            if map[i][j + 1] > map[i][j] < map[i][j - 1] \
                    and map[i + 1][j] > map[i][j] < map[i - 1][j]:
                basins.append(calculate_basin_size(map, i, j))

        # Last cell
        if map[i][-1] < map[i][-2] \
                and map[i + 1][-1] > map[i][-1] < map[i - 1][-1]:
            basins.append(calculate_basin_size(map, i, len(map[i]) - 1))

    # Last line first cell
    if map[-1][1] > map[-1][0] < map[-2][0]:
        basins.append(calculate_basin_size(map, len(map) - 1, 0))

    # Last line
    for i in range(1, len(map[-1]) - 1):
        if map[-1][i + 1] > map[-1][i] < map[-1][i - 1] \
                and map[-1][i] < map[-2][i]:
            basins.append(calculate_basin_size(map, len(map) - 1, i))

    # Last line last cell
    if map[-1][-2] > map[-1][-1] < map[-2][-1]:
        basins.append(calculate_basin_size(
            map, len(map) - 1, len(map[-1]) - 1))

    basins = sorted(basins, reverse=True)

    output = 1

    for b in basins[:3]:
        output *= b

    print(output)


if __name__ == "__main__":
    run()
