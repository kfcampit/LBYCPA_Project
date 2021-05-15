from stanfordkarel import *

def reverse():
    for x in range(2):
        turn_left()
def main():
    """ Karel code goes here! """
    move()
    turn_left()
    for x in range(7):
        move()
    reverse()
    put_beeper()
    for x in range(6):
        move()
        put_beeper()
    turn_left()
    for x in range(4):
        move()
        put_beeper()
  
if __name__ == "__main__":
    run_karel_program()