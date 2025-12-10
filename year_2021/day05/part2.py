import os


def run():
    f = open(os.getcwd() + '/year_2021/day05/input.txt')
    diagram_size = 1000
    diagram = []
    for i in range(diagram_size):
        diagram.append([0] * diagram_size)

    for line in f:
        p1, _, p2 = line.rstrip().split(' ')

        x1, y1 = list(map(int, p1.split(',')))
        x2, y2 = list(map(int, p2.split(',')))

        if x1 == x2:
            if y1 > y2:
                for i in range(y2, y1 + 1):
                    diagram[i][x1] += 1
            else:
                for i in range(y1, y2 + 1):
                    diagram[i][x1] += 1
            continue
        if y1 == y2:
            if x1 > x2:
                for i in range(x2, x1 + 1):
                    diagram[y2][i] += 1
            else:
                for i in range(x1, x2 + 1):
                    diagram[y2][i] += 1
            continue
        i = x1
        j = y1
        if x2 > x1:
            if y2 > y1:
                while i <= x2:
                    diagram[j][i] += 1
                    i += 1
                    j += 1
            else:
                while i <= x2:
                    diagram[j][i] += 1
                    i += 1
                    j -= 1
        else:
            if y2 > y1:
                while i >= x2:
                    diagram[j][i] += 1
                    i -= 1
                    j += 1
            else:
                while i >= x2:
                    diagram[j][i] += 1
                    i -= 1
                    j -= 1

    gt_2 = 0
    for line in diagram:
        gt_2 += len(list(filter(lambda x: x >= 2, line)))

    print(gt_2)


if __name__ == "__main__":
    run()
