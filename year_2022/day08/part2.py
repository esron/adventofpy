import os

def look_up(map: list[list[int]], line: int, column: int) -> int:
    score = 1
    i = line - 1
    while (i > 0 and map[i][column] < map[line][column]):
        score += 1
        i -= 1
    return score
def look_down(map: list[list[int]], line: int, column: int) -> int:
    score = 1
    i = line + 1
    while (i < len(map) - 1 and map[i][column] < map[line][column]):
        score += 1
        i += 1
    return score
def look_right(map: list[list[int]], line: int, column: int) -> int:
    score = 1
    j = column + 1
    while (j < len(map[line]) - 1 and map[line][j] < map[line][column]):
        score += 1
        j += 1
    return score
def look_left(map: list[list[int]], line: int, column: int) -> int:
    score = 1
    j = column - 1
    while (j > 0 and map[line][j] < map[line][column]):
        score += 1
        j -= 1
    return score
def calculate_scenic_score(map: list[list[int]],
                           line: int, column: int) -> int:
    up_score = look_up(map, line, column)
    rigth_score = look_right(map, line, column)
    down_score = look_down(map, line, column)
    left_score = look_left(map, line, column)

    return up_score * rigth_score * down_score * left_score
def run():
    map = None
    with open(os.getcwd() + '/year_2022/day08/input.txt') as f:
        map = [[int(i) for i in line.rstrip()] for line in f.readlines()]

    highest_scenic_score = 0
    for i in range(1, len(map) - 1):
        for j in range(1, len(map[i]) - 1):
            scenic_score = calculate_scenic_score(map, i, j)
            if scenic_score > highest_scenic_score:
                highest_scenic_score = scenic_score

    print(highest_scenic_score)
if __name__ == "__main__":
    run()
