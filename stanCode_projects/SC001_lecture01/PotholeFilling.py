"""
File: PotholeFilling.py
Name: TODO:
--------------------------
This program shows karel filling 3
potholes. Students learn the concept of
decomposition through the process.
"""

from karel.stanfordkarel import *

def go_in():
    """
    Pre-condition: Karel is at the upper left of the pothole, facing East.
    Post-condition: Karel is in the pothole, facing South.
    :return:
    """
    move()
    turn_right()
    move()

def go_out():
    """
    Pre-condition: Karel is in the pothole, facing South.
    Post-condition: Karel is at the upper left of the pothole, facing East.
    :return:
    """
    turn_around()
    move()
    turn_right()
    move()

def put_99_beepers():
    """
    Karel will put 99 beepers.
    :return:
    """
    for i in range(99):
        put_beeper()

def turn_right():
    """
    Turn left three times.
    :return:
    """
    turn_left()
    turn_left()
    turn_left()

def turn_around():
    """
    Turn left two times.
    :return:
    """
    turn_left()
    turn_left()


def main():
    """
    TODO:
    Pre-condition: Karel starts from (1,2), and put 99 beepers into each pothole.
    Post-condition: Karel stops moving at (7,2), facing East..
    :return:
    """

    for i in range(3):
        go_in()
        put_99_beepers()
        go_out()



# ----- DO NOT EDIT CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
