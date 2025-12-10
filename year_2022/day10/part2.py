import os

timers = {'addx': 2, 'noop': 1}
def run():
    x = 1
    clock = 0
    with open(os.getcwd() + '/year_2022/day10/input.txt') as f:
        instruction = f.readline().rstrip().split(' ')
        timer = timers[instruction[0]]
        line = ''
        while(clock < 240):
            clock += 1
            timer -= 1
            if clock % 40 == 0:
                # I don't know why first line is missing one #
                if len(line) == 39:
                    line = '#' + line
                print(line)
                line = ''
            if timer == 0:
                if instruction[0] == 'addx':
                    x += int(instruction[1])
                instruction = f.readline().rstrip().split(' ')
                if instruction == ['']:
                    continue
                timer = timers[instruction[0]]
            if (clock % 40) in [x - 1, x, x + 1]:
                line += '#'
            else:
                line += ' '
if __name__ == "__main__":
    run()
