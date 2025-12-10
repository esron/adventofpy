import os
import re
class Sensor:
    def __init__(self,
                 coords: tuple[int, int],
                 beacon_coords: tuple[int, int]) -> None:
        self.x = coords[0]
        self.y = coords[1]
        self.beacon_x = beacon_coords[0]
        self.beacon_y = beacon_coords[1]
        self.distance_to_beacon = \
            abs(self.x - self.beacon_x) + abs(self.y - self.beacon_y)

    def coords(self) -> tuple[int, int]:
        return (self.x, self.y)

    def beacon(self) -> tuple[int, int]:
        return (self.beacon_x, self.beacon_y)

    def __repr__(self) -> str:
        return f'<s ({self.x},{self.y})' + \
            f' b ({self.beacon_x}, {self.beacon_y})' + \
            f' d={self.distance_to_beacon}>'
def mergeIntervals(intervals: list[tuple[int, int]]) -> list[tuple[int, int]]:
    # Sort the array on the basis of start values of intervals.
    intervals.sort()
    stack = []
    # insert first interval into stack
    stack.append(intervals[0])
    for i in intervals[1:]:
        # Check for overlapping interval,
        # if interval overlap
        if stack[-1][0] <= i[0] <= stack[-1][-1]:
            stack[-1] = (stack[-1][0], max(stack[-1][-1], i[-1]))
        else:
            stack.append(i)

    return stack
def run():
    regex = r'x=(-?\d*), y=(-?\d*)'
    sensors: list[Sensor] = []
    with open(os.getcwd() + '/year_2022/day15/input.txt') as f:
        for line in f:
            line = line.rstrip()
            sensor, beacon = [tuple((int(m[0]), int(m[1])))
                              for m in re.findall(regex, line)]
            sensors.append(Sensor(sensor, beacon))

    # Given by problem statement
    y = 2000000
    intervals: list[tuple[int, int]] = []
    for s in sensors:
        if s.y - s.distance_to_beacon <= y <= s.y + s.distance_to_beacon:
            dy = abs(y - s.y)
            xo = s.x - (s.distance_to_beacon - dy)
            xf = s.x + (s.distance_to_beacon - dy)
            intervals.append((xo, xf))

    intervals = mergeIntervals(intervals)
    sum = 0
    for inter in intervals:
        sum += inter[1] - inter[0] + 1

    beacons = set([s.beacon() for s in sensors])
    for b in beacons:
        if b[1] == y:
            for i in intervals:
                if b[0] in range(i[0], i[1] + 1):
                    sum -= 1
    print(sum)
if __name__ == "__main__":
    run()
