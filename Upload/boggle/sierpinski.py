"""
File: sierpinski.py
Name: 
---------------------------
This file recursively prints the Sierpinski triangle on GWindow.
The Sierpinski triangle is a fractal described in 1915 by Waclaw Sierpinski.
It is a self similar structure that occurs at different levels of iterations.
"""

from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GLine
from campy.graphics.gobjects import GPolygon
from campy.gui.events.timer import pause

# Constants
ORDER =  6                 # Controls the order of Sierpinski Triangle
LENGTH = 600               # The length of order 1 Sierpinski Triangle
UPPER_LEFT_X = 150		   # The upper left x coordinate of order 1 Sierpinski Triangle
UPPER_LEFT_Y = 100         # The upper left y coordinate of order 1 Sierpinski Triangle
WINDOW_WIDTH = 950         # The width of the GWindow
WINDOW_HEIGHT = 700        # The height of the GWindow

# Global Variable
window = GWindow(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)  # The canvas to draw Sierpinski Triangle


def main():
	"""
	this program shows how to use recursion to draw several levels of sierpinski triangle
	"""
	sierpinski_triangle(ORDER, LENGTH, UPPER_LEFT_X, UPPER_LEFT_Y)


def sierpinski_triangle(order, length, upper_left_x, upper_left_y):
	"""
	:param order: level of triangles
	:param length: the length of original triangle
	:param upper_left_x: the initial x-coordination
	:param upper_left_y: the initial y-coordination
	:return: Sierpinski Triangle with specific order
	"""
	if order == 0:
		return
	else:

		triangle_up = GLine(upper_left_x, upper_left_y, upper_left_x + length, upper_left_y)
		triangle_left = GLine(upper_left_x, upper_left_y, upper_left_x + length * 0.5, upper_left_y + length * 0.866)
		triangle_right = GLine(upper_left_x + length, upper_left_y, upper_left_x + length * 0.5,
							   upper_left_y + length * 0.866)
		window.add(triangle_up)
		window.add(triangle_left)
		window.add(triangle_right)

		# triangle on the left : which has the same left corner as the biggest one
		sierpinski_triangle(order - 1, length / 2, upper_left_x, upper_left_y)

		# triangle on the right : which has the left corner on midpoint on the top one
		sierpinski_triangle(order - 1, length / 2, upper_left_x + length / 2, upper_left_y)

		# triangle on the bottom : which has the left corner on midpoint on midpoint of left-side line
		sierpinski_triangle(order - 1, length / 2, upper_left_x + length / 4, upper_left_y + length * 0.866 / 2)

		# if using the coordination to solve this problem
		# triangle =GPolygon()
		# triangle.add_vertex((upper_left_x, upper_left_y))
		# triangle.add_vertex((upper_left_x + length,upper_left_y))
		# triangle.add_vertex((upper_left_x + length * 0.5,upper_left_y + length * 0.866))
		# window.add(triangle)



if __name__ == '__main__':
	main()