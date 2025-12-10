import os
from typing import IO, Optional, Union
SIZE_TRESHOLD = 100000
class File:
    def __init__(self, name: str, size: int) -> None:
        self.name = name
        self.size = size

    def __str__(self) -> str:
        return f'File: {self.name} - size {self.size}'
class Dir:
    def __init__(self, name: str, parent: Optional['Dir']) -> None:
        self.name = name
        self.parent = parent
        self.size = 0
        self.children: list[Union['Dir', File]] = []

    def add_children(self, child: Union['Dir', File]) -> None:
        self.children.append(child)

    def __str__(self) -> str:
        return f'Dir: {self.name} - size {self.size}'
def read_input(file: IO) -> list[str]:
    return file.readline().rstrip().split(' ')
def is_command(line: list[str]) -> bool:
    return line[0] == '$'
def mount_tree(file: IO) -> Dir:
    current_dir: Optional[Dir] = None
    line = read_input(file)
    while (line != ['']):
        if is_command(line):
            command = line[1]
            if command == 'cd':
                argument = line[2]
                if argument != '..':
                    if current_dir is None:
                        current_dir = Dir(argument, None)
                    for child in current_dir.children:
                        if child.name == argument and isinstance(child, Dir):
                            current_dir = child
                else:
                    if isinstance(current_dir, Dir):
                        current_dir = current_dir.parent
        else:
            if line[0] == 'dir':
                name = line[1]
                new_dir = Dir(name, current_dir)
                if isinstance(current_dir, Dir):
                    current_dir.add_children(new_dir)
            else:
                name, size = line[1], line[0]
                if isinstance(current_dir, Dir):
                    current_dir.add_children(File(name, int(size)))
        line = read_input(file)
    while isinstance(current_dir, Dir) and current_dir.parent is not None:
        current_dir = current_dir.parent
    return current_dir if isinstance(current_dir, Dir) else Dir('/', None)
def print_tree(root: Dir, depth: int) -> None:
    print(('--' * depth) + ' ' + str(root))
    for child in root.children:
        if isinstance(child, Dir):
            print_tree(child, depth + 2)
        else:
            print(('--' * (depth + 1)) + ' ' + str(child))
    return
def calculate_dir_sizes(root: Dir) -> None:
    if len(root.children) == 0:
        return
    for child in root.children:
        if isinstance(child, Dir):
            calculate_dir_sizes(child)
        root.size += child.size
def extract_sizes_of_dir_list(root: Dir, sizes: list) -> None:
    sizes.append(root.size)
    for child in root.children:
        if isinstance(child, Dir):
            extract_sizes_of_dir_list(child, sizes)
def run():
    with open(os.getcwd() + '/year_2022/day07/input.txt') as f:
        root_dir = mount_tree(f)
        calculate_dir_sizes(root_dir)
        # print_tree(root_dir, 0)
        sizes = []
        extract_sizes_of_dir_list(root_dir, sizes)
        selected = [s for s in sizes if s <= SIZE_TRESHOLD]
        print(sum(selected))
if __name__ == "__main__":
    run()
