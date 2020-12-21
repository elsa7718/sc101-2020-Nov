"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao

File: breakout.py
Name: Elsa
---------------------------
This program plays a game called "Break out"
in which players rebounding the ball to break bricks
to gain scores.
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics
from campy.gui.events.mouse import onmouseclicked


FRAME_RATE = 1000 / 120  # 120 frames per second.
NUM_LIVES = 3

graphics = BreakoutGraphics()
vx = graphics.get_vx()
vy = graphics.get_vy()
INITIAL = graphics.get_vy() # the solution from tutors that solve the problem that the ball sticks at the paddle
ball = graphics.ball
window = graphics.window
life_left = NUM_LIVES
life_count = graphics.life_count


# Add animation loop here!

def main():
    """
    This program is the game that the player controls a paddle to rebound the ball.
    And the ball will break bricks that it hits.
    :return:
    """
    life_count.text = 'Live: ' + str(life_left)
    onmouseclicked(click_start)

def click_start(event):
        """
        Resets the ball if the ball fall out of the bottom
        Input:
            event (GMouseEvent) : mouse clicked event
        """
        global vy,vx,life_count,life_left
        if ball.x == (window.width - ball.width) / 2 and ball.y == (window.height - ball.height) / 2 and life_left >0:
            while True:
                ball.move(vx,vy)
                pause(FRAME_RATE)
                if graphics.wall_rebound_y():
                    vy*=-1
                if graphics.wall_rebound_x():
                    vx*=-1
                if graphics.detect():
                    vy*=-1
                    graphics.remove_brick()
                if graphics.detect_paddle():
                    vy=-INITIAL # the solution from tutors that solve the problem that the ball sticks at the paddle
                if graphics.out_of_bottom():
                    ball.x = (window.width - ball.width) / 2
                    ball.y = (window.height - ball.height) / 2
                    life_left-=1
                    life_count.text = 'Live: ' + str(life_left)
                    break
                if graphics.total_brick==0:
                    graphics.win_the_game()
                    break
        if life_left == 0:  # if player lost 3 lives
            graphics. game_over()


if __name__ == '__main__':
    main()
