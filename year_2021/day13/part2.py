import os
from typing import Iterable


class Point:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def distance_x(self, x: int) -> int:
        return abs(x - self.x)

    def distance_y(self, y: int) -> int:
        return abs(y - self.y)

    def move_x(self, x: int) -> None:
        self.x = x

    def move_y(self, y: int) -> None:
        self.y = y

    def __eq__(self, __o: object) -> bool:
        return self.x == __o.x and self.y == __o.y


def execute(instruction: str, points: Iterable[Point]) -> None:
    axis, value = instruction.split('=')
    value = int(value)

    for p in points:
        if axis == 'y':
            if p.y > value:
                p.move_y(value - p.distance_y(value))
        if axis == 'x':
            if p.x > value:
                p.move_x(value - p.distance_x(value))


def remove_equals(points: Iterable[Point]) -> Iterable[Point]:
    filtered = []
    while(len(points) > 0):
        filtered.append(points[0])
        points = list(filter(lambda x: x != points[0], points))
    return filtered


def draw(points, size_x, size_y):
    display = []
    for _ in range(size_y + 1):
        line = [' '] * (size_x + 1)
        line.append('\n')
        display.append(line)

    for p in points:
        display[p.y][p.x] = '#'
    print(''.join([''.join(line) for line in display]))


def run():
    f = open(os.getcwd() + '/year_2021/day13/input.txt')
    points = []
    instructions = []

    for line in f:
        if len(line.split(',')) == 2:
            points.append(Point(*tuple(map(int, line.rstrip().split(',')))))
        elif line != '\n':
            instructions.append(line.rstrip().split(' ')[2])

    for i in instructions:
        execute(i, points)
        points = remove_equals(points)

    size_x = 0
    size_y = 0
    for p in points:
        if p.x > size_x:
            size_x = p.x
        if p.y > size_y:
            size_y = p.y

    draw(points, size_x, size_y)


if __name__ == "__main__":
    run()
