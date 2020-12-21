"""
File: draw_line.py
Name: Elsa
-------------------------
TODO:
"""
"""
This program creates lines on an instance of GWindow class.
There is a circle indicating the user’s first click. A line appears
at the condition where the circle disappears as the user clicks
on the canvas for the second time.
"""

from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked
from campy.graphics.gobjects import GOval
from campy.graphics.gobjects import GLine

# This constant controls the size of the GOval
SIZE=10

# Constants control the diameter of the window
WINDOW_WIDTH = 700
WINDOW_HEIGHT = 700
window=GWindow(width=WINDOW_WIDTH,height=WINDOW_HEIGHT,title='Draw a line')

# global variable to record the coordinates
x=0
y=0
x1=0
y1=0

# the counter is to define odd or even
counter=0
hole = GOval(SIZE, SIZE)


def main():
    hole.color = 'black'
    onmouseclicked(one)


def one(a):
    global x,y,x1,y1,counter,hole
    counter += 1
    if counter % 2 == 1:
        window.add(hole,a.x,a.y)

        # to provide the initial coordinates
        x = a.x + SIZE / 2
        y = a.y + SIZE / 2

    if counter % 2 == 0:
        window.remove(hole)

        # to provide the final coordinates
        x1 = a.x + SIZE / 2
        y1 = a.y + SIZE / 2

        # use above coordinates to draw the line
        line = GLine(x, y, x1, y1)
        window.add(line)


if __name__ == "__main__":
    main()
