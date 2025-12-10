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
        self.d = \
            abs(self.x - self.beacon_x) + abs(self.y - self.beacon_y)

    def coords(self) -> tuple[int, int]:
        return (self.x, self.y)

    def beacon(self) -> tuple[int, int]:
        return (self.beacon_x, self.beacon_y)

    def __repr__(self) -> str:
        return f'<s ({self.x},{self.y})' + \
            f' b ({self.beacon_x}, {self.beacon_y})' + \
            f' d={self.d}>'
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

    # This is slow as f.
    for y in range(4000000):
        intervals: list[tuple[int, int]] = []
        for s in sensors:
            if s.y - s.d <= y <= s.y + s.d:
                dy = abs(y - s.y)
                xo = s.x - (s.d - dy)
                xf = s.x + (s.d - dy)
                intervals.append((xo, xf))

        intervals = mergeIntervals(intervals)
        if len(intervals) == 2:
            x = intervals[0][1] + 1
            print(x * 4000000 + y)
            break
if __name__ == "__main__":
    run()
