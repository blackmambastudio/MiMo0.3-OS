import random


COLORS = ['r', 'g', 'b']


def mimo_button():
    return COLORS[random.randrange(len(COLORS))]
