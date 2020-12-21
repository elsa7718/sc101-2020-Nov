"""
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.

YOUR DESCRIPTION HERE
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index of the current year in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                              with the specified year.
    """

    x_coordinate=GRAPH_MARGIN_SIZE+(year_index*((width-GRAPH_MARGIN_SIZE*2)/len(YEARS)))
    return x_coordinate



def draw_fixed_lines(canvas):
    """
    Erases all existing information on the given canvas and then
    draws the fixed background lines on it.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.

    Returns:
        This function does not return any value.
    """
    canvas.delete('all')            # delete all existing lines from the canvas

    # Write your code below this line
    #################################

    # to draw the top and bottom straight line
    canvas.create_line(GRAPH_MARGIN_SIZE,GRAPH_MARGIN_SIZE,CANVAS_WIDTH-GRAPH_MARGIN_SIZE,GRAPH_MARGIN_SIZE)
    canvas.create_line(GRAPH_MARGIN_SIZE,CANVAS_HEIGHT-GRAPH_MARGIN_SIZE,CANVAS_WIDTH-GRAPH_MARGIN_SIZE,CANVAS_HEIGHT-
                       GRAPH_MARGIN_SIZE)

    # to draw straight lines by the number of years
    for i in range(len(YEARS)):
        year=YEARS[i]
        x=get_x_coordinate(CANVAS_WIDTH,i)
        canvas.create_line(x,0,x,CANVAS_HEIGHT)
        canvas.create_text(x+TEXT_DX,CANVAS_HEIGHT-GRAPH_MARGIN_SIZE,text=str(year),anchor=tkinter.NW)


def draw_names(canvas, name_data, lookup_names):

    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)        # draw the fixed background grid

    # Write your code below this line
    #################################
    height=CANVAS_HEIGHT-GRAPH_MARGIN_SIZE*2  # the length is to calculate the y-coordinate

    for j in range(len(lookup_names)):  # to check every element of the name list
        color = j%len(COLORS) # tutors help me to make the colour changes by name
        name=lookup_names[j]
        year = name_data[name]  # year is key of name_data and is also a dictionary
        for i in range(len(YEARS)):  # to check the situation of a single name by years
            y_final = []  # a list to store y-coordinate to draw the line
            print_rank = []  # a list to store the ranking to print
            # year_wip is specific year e.g. 1900/2000
            x = int(get_x_coordinate(CANVAS_WIDTH, i))  # use function above to get the x-coordinate
            x1= int(get_x_coordinate(CANVAS_WIDTH, i+1))  # to point out the second x-coordinate for the line
            for each_year in YEARS:  # check a single name's ranking in every year
                if str(each_year) in year:  # if the year is in the dictionary {'year':'rank'}
                    y_wip = year[str(each_year)]
                    final = GRAPH_MARGIN_SIZE + int(y_wip) * height / 1000  # to modify y-coordinate by the proportion
                    y_final.append(final)
                    print_rank.append(year[str(each_year)])
                else:
                    y_final.append(CANVAS_HEIGHT - GRAPH_MARGIN_SIZE)
                    print_rank.append('**')

            # the text shows the name and ranking by years at appointed position
            canvas.create_text(x + TEXT_DX, y_final[i], text=name + str(' ' + print_rank[i]), anchor=tkinter.SW,
                               fill=COLORS[color])

            # stop drawing line in the last point
            if 0 <= i < len(YEARS)-1 :
                canvas.create_line(x, y_final[i], x1, y_final[i + 1], width=LINE_WIDTH,fill=COLORS[color])



# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
