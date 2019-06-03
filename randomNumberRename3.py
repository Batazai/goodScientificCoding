#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# team: Armin, Baltasar, Claudia

import random
import time
import sys

def get_random_number(start, end):
    num = random.randint(start, end)
    return num


def write_log_file(outputfilename, data):
    f = open(outputfilename + ".log", "a")
    f.write("My randomly generated number is " + str(data) + " (" + time.strftime("%H:%M:%S") + ")\n")
    f.close()


if __name__ == "__main__":
    outputfilename = "randomNumber2"
    roll = get_random_number(1, 6)
    write_log_file(outputfilename, roll)

def get_color_by_dice_naive(spots):
    if spots == 1:
        color = 'blue'
    elif spots == 2:
        color = 'green'
    elif spots == 3:
        color = 'red'
    elif spots == 4:
        color = 'yellow'
    elif spots == 5:
        color = 'purple'
    else: # spots == 6:
        color = 'orange'
    return color