"""
File: bouncing_ball.py
Name: Elsa
-------------------------
TODO:
"""

from campy.gui.events.mouse import onmouseclicked
from campy.gui.events.timer import pause
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval

VX = 3
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40


window = GWindow(800, 500, title='bouncing_ball.py')
ball=GOval(SIZE, SIZE)
counter = 0


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    ball.filled=True
    ball.fill_color='darkblue'
    ball.color='greenyellow'
    window.add(ball, START_X, START_Y)
    onmouseclicked(drop)


def drop(e):
    global counter
    vy = 0

    # conditions to limit the number of clicks and to fix the initial position
    if ball.x == START_X and ball.y == START_Y and counter <= 2:

        # movement of the ball and how to stop it
        while True:
            vy += GRAVITY
            ball.move(VX,vy)
            if vy > 0 and ball.y+SIZE >= window.height:
                vy=-vy*REDUCE
            if ball.x >= window.width:
                ball.x=START_X
                ball.y=START_Y
                counter += 1
                break
            pause(DELAY)




if __name__ == "__main__":
    main()
