import os
def space_is_empty(coordinate: tuple[int, int], walls: set) -> bool:
    return coordinate not in walls
def run():
    low_boundary = 0  # Start at the top the bigger the better
    walls = set()
    with open(os.getcwd() + '/year_2022/day14/input.txt') as f:
        for line in f:
            # Coordinate[0] -> y
            # Coordinate[1] -> x
            coordinates = [
                    tuple(int(x) for x in pair.split(','))
                    for pair in line.rstrip().split(' -> ')]
            for c in coordinates:
                if c[1] > low_boundary:
                    low_boundary = c[1]
            for i in range(len(coordinates) - 1):
                c1 = coordinates[i]
                c2 = coordinates[i + 1]
                dy = c1[0] - c2[0]
                dx = c1[1] - c2[1]
                if dy > 0:
                    for i in range(c2[0], c1[0] + 1):
                        walls.add((i, c1[1]))
                elif dy < 0:
                    for i in range(c1[0], c2[0] + 1):
                        walls.add((i, c1[1]))
                elif dx > 0:
                    for i in range(c2[1], c1[1] + 1):
                        walls.add((c1[0], i))
                elif dx < 0:
                    for i in range(c1[1], c2[1] + 1):
                        walls.add((c1[0], i))
    how_many_sands = 0
    is_in_abyss = False
    while(not is_in_abyss):
        sand = [500, 0]
        how_many_sands += 1
        rested = False
        while(not (rested or is_in_abyss)):
            print(sand)
            if space_is_empty((sand[0], sand[1] + 1), walls):
                sand[1] += 1
            elif space_is_empty((sand[0] - 1, sand[1] + 1), walls):
                sand[0] -= 1
                sand[1] += 1
            elif space_is_empty((sand[0] + 1, sand[1] + 1), walls):
                sand[0] += 1
                sand[1] += 1
            else:
                walls.add(tuple(sand))
                rested = True
            if sand[1] > low_boundary:
                is_in_abyss = True
    print(how_many_sands - 1)
if __name__ == "__main__":
    run()
