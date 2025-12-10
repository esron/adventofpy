import os

OP_ROCK = 'A'
OP_PAPPER = 'B'
OP_SCISSORS = 'C'
MY_ROCK = 'X'
MY_PAPPER = 'Y'
MY_SCISSORS = 'Z'
WANT_LOOSE = 'X'
WANT_DRAW = 'Y'
WANT_WIN = 'Z'

prs_map = {
    OP_ROCK: {
        MY_ROCK: 'draw',
        MY_PAPPER: 'win',
        MY_SCISSORS: 'loose',
    },
    OP_PAPPER: {
        MY_ROCK: 'loose',
        MY_PAPPER: 'draw',
        MY_SCISSORS: 'win',
    },
    OP_SCISSORS: {
        MY_ROCK: 'win',
        MY_PAPPER: 'loose',
        MY_SCISSORS: 'draw',
    },
}

points_map = {
    MY_ROCK: 1,
    MY_PAPPER: 2,
    MY_SCISSORS: 3,
}

outcome_map = {
    'loose': 0,
    'draw': 3,
    'win': 6,
}

wanted_outcome_map = {
    WANT_WIN: 'win',
    WANT_DRAW: 'draw',
    WANT_LOOSE: 'loose',
}

def invert_map(my_map):
    return {v: k for k, v in my_map.items()}
def choose_my_play(op_play, wanted_value):
    wanted_outcome = wanted_outcome_map[wanted_value]
    return invert_map(prs_map[op_play])[wanted_outcome]
def score(outcome, my_play):
    return outcome_map[outcome] + points_map[my_play]
def run():
    points = 0
    f = open(os.getcwd() + '/year_2022/day02/input.txt')
    for line in f:
        op_play, wanted_outcome = line.rstrip().split(' ')
        my_play = choose_my_play(op_play, wanted_outcome) 
        outcome = prs_map[op_play][my_play]
        points += score(outcome, my_play) 
    print(points)
if __name__ == "__main__":
    run()
