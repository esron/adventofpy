import os

def run():
    f = open(os.getcwd() + '/year_2022/day03/input.txt')
    priority_sum = 0
    elf_a = set(f.readline().rstrip())
    elf_b = set(f.readline().rstrip())
    elf_c = set(f.readline().rstrip())

    while(elf_a != set()):
        intersect = elf_a.intersection(elf_b)
        intersect = intersect.intersection(elf_c)
        item = ''.join(intersect)
        priority_sum += ord(item) - 38 if item.isupper() else ord(item) - 96
        elf_a = set(f.readline().rstrip())
        elf_b = set(f.readline().rstrip())
        elf_c = set(f.readline().rstrip())
    print(priority_sum)
if __name__ == "__main__":
    run()
