import os
from typing import Optional

paths = []


class Node:
    nodes: 'list[Node]' = []
    start_node: Optional['Node'] = None
    end_node: Optional['Node'] = None

    def __init__(self, value: str):
        self.value = value
        self.links: list['Node'] = []
        self.visited = False

    def add_link(self, n: 'Node'):
        self.links.append(n)

    def is_big_cave(self):
        return self.value.isupper()

    def has_node(value):
        for n in Node.nodes:
            if value == n.value:
                return True
        return False

    def get_node(value):
        for n in Node.nodes:
            if value == n.value:
                return n


def has_small_cave_twice(path: list[str]):
    caves = []
    for cave in path:
        if cave.isupper():
            continue
        if cave in caves:
            return True
        else:
            caves.append(cave)
    return False


def can_visit(node: Node, path: list[str]):
    if node.is_big_cave():
        return True
    if has_small_cave_twice(path):
        return node.value not in path
    return True


def pathfinder(node: Node, path: list[str]):
    if not can_visit(node, path):
        return
    path.append(node.value)
    if node.value == 'end':
        paths.append(path.copy())
        return
    for n in node.links:
        pathfinder(n, path.copy())
    return


def run():
    f = open(os.getcwd() + '/year_2021/day12/input.txt')

    for line in f:
        line = line.rstrip()
        from_value, to_value = line.split('-')

        if Node.has_node(from_value):
            node_from = Node.get_node(from_value)
        else:
            node_from = Node(from_value)
            if from_value == 'start':
                Node.start_node = node_from
            if from_value == 'end':
                Node.end_node = node_from
            Node.nodes.append(node_from)

        if Node.has_node(to_value):
            node_to = Node.get_node(to_value)
        else:
            node_to = Node(to_value)
            if to_value == 'end':
                Node.end_node = node_to
            if to_value == 'start':
                Node.start_node = node_to
            Node.nodes.append(node_to)

        if node_to.value != 'start' and node_from.value != 'end':
            node_from.add_link(node_to)
        if node_from.value != 'start' and node_to.value != 'end':
            node_to.add_link(node_from)

    pathfinder(Node.start_node, [])

    print(len(paths))


if __name__ == "__main__":
    run()
