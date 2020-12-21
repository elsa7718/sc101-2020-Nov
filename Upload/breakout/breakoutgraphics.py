"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
from campy.gui.events.timer import pause
import random

BRICK_SPACING = 5  # Space between bricks (in pixels). This space is used for horizontal and vertical spacing.
BRICK_WIDTH = 40  # Height of a brick (in pixels).
BRICK_HEIGHT = 15  # Height of a brick (in pixels).
BRICK_ROWS = 10  # Number of rows of bricks.
BRICK_COLS = 10  # Number of columns of bricks.
BRICK_OFFSET = 50  # Vertical offset of the topmost brick from the window top (in pixels).
BALL_RADIUS = 10  # Radius of the ball (in pixels).
PADDLE_WIDTH = 75  # Width of the paddle (in pixels).
PADDLE_HEIGHT = 15  # Height of the paddle (in pixels).
PADDLE_OFFSET = 50  # Vertical offset of the paddle from the window bottom (in pixels).

INITIAL_Y_SPEED = 7.0  # Initial vertical speed for the ball.
MAX_X_SPEED = 5  # Maximum initial horizontal speed for the ball.


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH,
                 paddle_height=PADDLE_HEIGHT, paddle_offset=PADDLE_OFFSET,
                 brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS,
                 brick_width=BRICK_WIDTH, brick_height=BRICK_HEIGHT,
                 brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING,
                 title='Breakout'):
        # Create a graphical window, with some extra space.
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle.
        self.paddle = GRect(paddle_width, paddle_height)
        self.paddle.filled = True
        self.paddle.fill_color = 'royalblue'
        self.paddle.color='royalblue'
        self.window.add(self.paddle, x=(window_width - paddle_width) / 2, y=window_height - paddle_offset)


        # Center a filled ball in the graphical window.
        self.ball = GOval(BALL_RADIUS * 2, BALL_RADIUS * 2)
        self.ball.filled = True
        self.ball.fill_color = 'darkslategray'
        self.ball.color='darkslategray'
        self.window.add(self.ball, x=window_width / 2 - BALL_RADIUS, y=window_height / 2 - BALL_RADIUS)


        # Initialize our mouse listeners.
        onmousemoved(self.mouse_move)


        # Default initial velocity for the ball.
        self.__vy = INITIAL_Y_SPEED
        self.__vx = random.randint(1,MAX_X_SPEED)
        if (random.random()>0.5):
            self.__vx=-self.__vx

        # Default the score and total bricks
        self.total_brick = BRICK_ROWS * BRICK_COLS
        self.score=0
        self.score_label = GLabel(f'Score: {self.score}')
        self.score_label.font = 'Courier-15-bold-italic'
        self.window.add(self.score_label, 150, self.window.height - 10)
        self.life_count = GLabel('Live: ')
        self.life_count.font='Courier-15-bold-italic'
        self.window.add(self.life_count,self.window.width-self.life_count.width-20, self.window.height - 10)

        # Draw bricks.
        self.a = 0
        for i in range(BRICK_COLS):
            self.b = 0
            for j in range(BRICK_ROWS):
                self.brick = GRect(BRICK_WIDTH, BRICK_HEIGHT)
                self.brick.filled = True
                if 0<=j<=BRICK_ROWS:
                    self.brick.color = 'tomato'
                    self.brick.fill_color = 'tomato'
                if 2<=j<4:
                    self.brick.color = 'salmon'
                    self.brick.fill_color = 'salmon'
                if 4<=j<6:
                    self.brick.color='pink'
                    self.brick.fill_color='pink'
                if 6<=j<8:
                    self.brick.color='peachpuff'
                    self.brick.fill_color='peachpuff'
                if 8<=j<BRICK_ROWS:
                    self.brick.color='rosybrown'
                    self.brick.fill_color='rosybrown'
                self.window.add(self.brick,x=self.a,y=BRICK_OFFSET+self.b)
                self.b += BRICK_HEIGHT + BRICK_SPACING
            self.a += BRICK_WIDTH + BRICK_SPACING

    # to keep the paddle follow the mouse
    def mouse_move(self, mouse):
        self.paddle.x = mouse.x - PADDLE_WIDTH/2
        if self.paddle.x+PADDLE_WIDTH >self.window.width:
            self.paddle.x=self.window.width-PADDLE_WIDTH
        if (mouse.x - PADDLE_WIDTH/2)<=0:
            self.paddle.x=0

    # to return the data of vx and vy
    def get_vx(self):
        return self.__vx

    def get_vy(self):
        return self.__vy

    # to make ball rebound when hitting walls
    def wall_rebound_y(self):
        self.wall_y_collision = self.ball.y<=0
        return self.wall_y_collision

    def wall_rebound_x(self):
        self.wall_x_collision = self.ball.x<=0 or self.ball.x>=self.window.width-self.ball.width
        return self.wall_x_collision

    # stop looping if player lost 1 live
    def out_of_bottom(self):
        out= self.ball.y >= self.window.height
        return out

    def game_over(self):
        self.qq = GLabel('Ooops ! GAME OVER!') # label of fail
        self.qq.font = 'Dialog-20-bold'
        self.window.add(self.qq, (self.window.width - self.qq.width) / 2,self. window.height / 2)

    # stop the loop if player breaks all bricks
    def win_the_game(self):
        if self.total_brick==0:
            self.success()

    def success(self):
        self.congratulation = GLabel('You win!') # label of success
        self.congratulation.font = 'Verdana-40-bold-italic'
        self.window.add(self.congratulation, (self.window.width - self.congratulation.width) / 2, self.window.height / 2)

    # to check if the ball hit bricks or paddle
    def detect(self):
        self.h = self.window.get_object_at(self.ball.x, self.ball.y)
        self.i = self. window.get_object_at(self.ball.x + self.ball.width, self.ball.y)
        self.j = self.window.get_object_at(self.ball.x, self.ball.y +self.ball.height)
        self.k = self.window.get_object_at(self.ball.x + self.ball.width, self.ball.y + self.ball.height)
        if self.h is not None and self.h is not self.paddle and self.h is not self.score_label and self.h is not self.life_count:
            return self.h
        if self.i is not None and self.i is not self.paddle and self.i is not self.score_label and self.i is not self.life_count:
            return self.i
        if self.j is not None and self.j is not self.paddle and self.j is not self.score_label and self.j is not self.life_count:
            return self.j
        if self.k is not None and self.k is not self.paddle and self.k is not self.score_label and self.k is not self.life_count:
            return self.k

    def remove_brick(self):
        if self.detect():
            self.window.remove(self.h) or self.window.remove(self.i) or self.window.remove(self.j) or self.window.remove(self.k)
            self.total_brick-=1
            self.score+=10
            self.score_label.text = 'Score: ' + str(self.score)


    def detect_paddle(self):
        self.hit_paddle= self.j is self.paddle or self.k is self.paddle
        return self.hit_paddle











