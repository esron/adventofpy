import os

class Point:
    def __init__(self, x, y, z, id):
        self.x = x
        self.y = y
        self.z = z
        self.id = id
        self.connected = False
    def __repr__(self):
        return f"Point({self.x}, {self.y}, {self.z}) id: {self.id} connected: {self.connected}"

    def connect(self):
        self.connected = True

    def is_connected(self):
        return self.connected

class Circuit:
    def __init__(self, points):
        self.points = points
    def __repr__(self):
        return f"Circuit({self.points})"
    def __len__(self):
        return len(self.points)

    def add_point(self, point):
        self.points.append(point)

def distance(a, b):
    """
    Calculate the quadratic distance between two points
    Args:
        a: Point object
        b: Point object
    Returns:
        quadratic distance
    """
    return (a.x - b.x) ** 2 + (a.y - b.y) ** 2 + (a.z - b.z) ** 2

def recursive_closest_distance(left, right):
    """
    Using divide and conquer to find the closest pair of points
    Args:
        left: list of points to the left of the midpoint
        right: list of points to the right of the midpoint
    Returns:
        closest distance between two points
    """
    if len(left) <= 3:
        closest_distance = float('inf')
        best_pair = None
        for i in range(len(left)):
            for j in range(i+1, len(left)):
                if distance(left[i], left[j]) < closest_distance:
                    closest_distance = distance(left[i], left[j])
                    best_pair = (left[i], left[j])
        return closest_distance, best_pair
    mid = len(left) // 2
    mid_point = left[mid]
    closest_left_distance, best_left_pair = recursive_closest_distance(left[:mid], right)
    closest_right_distance, best_right_pair = recursive_closest_distance(left[mid:], right)
    d = min(closest_left_distance, closest_right_distance)

    s = []
    for point in left:
        if abs(point.x - mid_point.x) < d:
            s.append(point)

    best_pair = None
    for i in range(len(s)):
        for j in range(i+1, len(s)):
            if distance(s[i], s[j]) < d:
                d = distance(s[i], s[j])
                best_pair = (s[i], s[j])
    return d, best_pair


def solve(input_file):
    with open(input_file, "r") as f:
        lines = [( int(i), int(j), int(k)) for i, j, k in (line.strip().split(",") for line in f)]

    # brute force solution
    # closest_distance = float('inf')
    # best_pair = None
    # for line in lines:
    #     for other_line in lines:
    #         if line is other_line:
    #             continue
    #         d = distance(line, other_line)
    #         if d < closest_distance:
    #             closest_distance = d
    #             best_pair = (line, other_line)
    #             print(best_pair)
    # print(closest_distance)
    # print(best_pair)

    # divide and conquer solution
    lines = sorted(lines)
    points = [Point(x, y, z, i) for i, (x, y, z) in enumerate(lines)]
    mid = len(points) // 2
    closest_distance, best_pair = recursive_closest_distance(points[:mid], points[mid:])
    print(closest_distance)
    print(best_pair)
    if best_pair is not None:
        best_pair[0].connect()
        best_pair[1].connect()
        circuit = Circuit([best_pair[0], best_pair[1]])
        print(circuit)

    for point in points:
        print(point)

def run():
    print("Example:")
    solve(os.getcwd() + '/year_2025/day08/example.txt')
    print("Input:")
    solve(os.getcwd() + '/year_2025/day08/input.txt')

if __name__ == "__main__":
    run()
