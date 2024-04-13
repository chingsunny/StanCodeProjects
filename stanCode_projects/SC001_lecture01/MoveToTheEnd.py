"""
File: Steeplechase.py
Name: TODO:
---------------------------------
TODO:
"""

from karel.stanfordkarel import *

def jump():
    """
    Pre-condition:Karel is on the left side of the wall, facing East.
    Post-condition:Karel is on the right side of the wall.
    :return:
    """
    up()
    cross()
    down()

def up():
    """
    pre-condition: Karel is on the left side of the wall, facing East.
    Post-condition: Karel is facing North.
    :return:
    """

    """
    turn_left()
    # Karel is facing North.
    while not right_is_clear():
        move()
    """

    while not front_is_clear():
        turn_left()
        move()
        turn_right()

def cross():
    """
    pre-condition:Karel is facing North.
    post-condition:Karel is facing South.
    :return:
    """
    move()
    turn_right()

def down():
    """
    pre-condition: Karel is on the right side of the wall, facing South.
    Post-condition:Karel is facing East.
    :return:
    """
    while front_is_clear():
        move()

def turn_right():
    turn_left()
    turn_left()
    turn_left()


def main():
    """
    Karel crosses hurdles in a 12x12 world
    with a for loop 
    """
    for i in range(11):
        if front_is_clear():
            move()
        else:
            jump()
            turn_left()


# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
