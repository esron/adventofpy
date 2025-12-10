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


def run():
    f = open(os.getcwd() + '/year_2021/day13/input.txt')

    points = []
    instructions = []

    for line in f:
        if len(line.split(',')) == 2:
            points.append(Point(*tuple(map(int, line.rstrip().split(',')))))
        elif line != '\n':
            instructions.append(line.rstrip().split(' ')[2])

    execute(instructions[0], points)
    points = remove_equals(points)

    print(len(points))


if __name__ == "__main__":
    run()
