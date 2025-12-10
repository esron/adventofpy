from decimal import Decimal
import os
from queue import PriorityQueue
from typing import Iterable, Optional

class Point:
    def __init__(self, coord: tuple[int, int], value: str) -> None:
        self.x = coord[0]
        self.y = coord[1]
        self.total_cost = Decimal('Infinity')
        self.distance_from_root = Decimal('Infinity')
        self.father: Optional[Point] = None
        self.value = self.__initial_value(value)

    @staticmethod
    def __initial_value(value: str) -> int:
        if value == 'S':
            return 97
        if value == 'E':
            return 123
        else:
            return ord(value)

    def distance(self, point: 'Point') -> int:
        """Manhattan distance to point"""
        return abs(point.x - self.x) + abs(point.y - self.y)

    def __eq__(self, __o: object) -> bool:
        if isinstance(__o, Point):
            return self.x == __o.x and self.y == __o.y
        else:
            return False

    def __gt__(self, __o: object) -> bool:
        if isinstance(__o, Point):
            return self.total_cost > __o.total_cost
        raise Exception('Cannot compare different object types')

    def __lt__(self, __o: object) -> bool:
        if isinstance(__o, Point):
            return self.total_cost < __o.total_cost
        raise Exception('Cannot compare different object types')

    def __hash__(self) -> int:
        return hash((self.x, self.y))

    def __str__(self) -> str:
        return f'{{ x: {str(self.x)}, y: {str(self.y)}, f: {self.total_cost}, \
g: {self.distance_from_root} value: {self.value} }}'
def find_point_position(point: str, map: list[list[str]]) -> tuple[int, int]:
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == point:
                return i, j
    return 0, 0
def is_in_range(x: int, y: int, grid: list[list[Point]]) -> bool:
    return (0 <= x < len(grid)) and (0 <= y < len(grid[x]))
def append_if_in_range(grid: list[list[Point]], neighbors: list[Point],
                       direction: tuple[int, int], point: Point) -> None:
    if is_in_range(*direction, grid):
        n_ord = grid[direction[0]][direction[1]].value
        if point.value >= n_ord - 1:
            neighbors.append(grid[direction[0]][direction[1]])
def get_neighbors(point: Point,
                  grid: list[list[Point]]) -> Iterable[Point]:
    n = []
    append_if_in_range(grid, n, (point.x - 1, point.y), point)
    append_if_in_range(grid, n, (point.x, point.y - 1), point)
    append_if_in_range(grid, n, (point.x + 1, point.y), point)
    append_if_in_range(grid, n, (point.x, point.y + 1), point)
    return n
def pathfinder(A: Point, goal: Point,
               grid: list[list[Point]]) -> Optional[Point]:
    open_list = PriorityQueue()
    open_list.put(A)
    closed_list = set()

    while not open_list.empty():
        current: Point = open_list.get()
        closed_list.add(current)
        if current == goal:
            return current

        neighbors = get_neighbors(current, grid)

        for n in neighbors:
            if n in closed_list:
                continue

            dfr = current.distance_from_root + 1

            if dfr < n.distance_from_root:
                n.father = current
                n.distance_from_root = dfr
                n.total_cost = dfr + n.distance(goal)

                open_list.put(n)
def run():
    map = []
    with open(os.getcwd() + '/year_2022/day12/input.txt') as f:
        map = [list(ls.rstrip()) for ls in f.readlines()]
    start_position = find_point_position('S', map)
    goal_position = find_point_position('E', map)
    point_map = []
    for i in range(len(map)):
        point_list = []
        for j in range(len(map[i])):
            point_list.append(Point((i, j), map[i][j]))
        point_map.append(point_list)

    start = point_map[start_position[0]][start_position[1]]
    start.distance_from_root = 0
    start.total_cost = 0
    goal = point_map[goal_position[0]][goal_position[1]]

    point = pathfinder(start, goal, point_map)

    if point is None:
        print('No path found')
        exit(1)
    print(point.total_cost)
if __name__ == "__main__":
    run()
