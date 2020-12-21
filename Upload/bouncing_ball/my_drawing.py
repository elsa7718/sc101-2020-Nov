"""
File: My_drawing.py
Name:Elsa
----------------------
TODO:
"""

from campy.graphics.gobjects import GOval, GRect
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect,GPolygon,GLabel
from campy.graphics.gwindow import GWindow

def main():
    """
    TODO:
    This figure uses campy module to demonstrate personality.
    A lot of faiths hold by people, just like the shape of circles or triangles,
    while eventually others can only see the polygon.
    """
    window=GWindow(600,600)

    # color of background
    rect=GRect(800,800)
    rect.filled=True
    rect.fill_color='lightgrey'
    window.add(rect)

    # polygon, circle ,rect and triangle with different colors
    polygon1=GPolygon()
    polygon1.add_vertex((550, 590))
    polygon1.add_vertex((570, 360))
    polygon1.add_vertex((100, 60))
    polygon1.filled=True
    polygon1.fill_color='greenyellow'
    window.add(polygon1)

    rect1=GRect(335,335,x=135,y=150)
    rect1.filled=True
    rect1.fill_color='sage'
    rect2=GRect(370,370,x=120,y=135)
    rect2.filled=True
    rect2.fill_color='magenta'
    rect3=GRect(400,400,x=105,y=120)
    rect3.filled=True
    rect3.fill_color='purple'
    rect4=GRect(440,440,x=85,y=100)
    rect4.filled=True
    rect4.fill_color='peachpuff'
    window.add(rect4)
    window.add(rect3)
    window.add(rect2)
    window.add(rect1)

    circle5=GOval(265,265,x=170,y=185)
    circle5.filled=True
    circle5.fill_color='lightsage'
    circle6=GOval(285,285,x=160,y=175)
    circle6.filled=True
    circle6.fill_color='tan'
    circle7=GOval(305,305,x=150,y=165)
    circle7.filled=True
    circle7.fill_color='midnightblue'
    circle8=GOval(325,325,x=140,y=155)
    circle8.filled=True
    circle8.fill_color='powderblue'
    window.add(circle8)
    window.add(circle7)
    window.add(circle6)
    window.add(circle5)

    triangle1=GPolygon()
    triangle1.add_vertex((300,230))
    triangle1.add_vertex((225,340))
    triangle1.add_vertex((375,340))
    triangle2=GPolygon()
    triangle2.add_vertex((300,215))
    triangle2.add_vertex((210,350))
    triangle2.add_vertex((390,350))
    triangle1.filled=True
    triangle1.fill_color='pink'
    triangle2.filled=True
    triangle2.fill_color='lightgrey'
    triangle3=GPolygon()
    triangle3.add_vertex((300,200))
    triangle3.add_vertex((195,360))
    triangle3.add_vertex((405,360))
    triangle4=GPolygon()
    triangle4.add_vertex((300,185))
    triangle4.add_vertex((180,370))
    triangle4.add_vertex((420,370))
    triangle3.filled=True
    triangle3.fill_color='linen'
    triangle4.filled=True
    triangle4.fill_color='yellow'
    window.add(triangle4)
    window.add(triangle3)
    window.add(triangle2)
    window.add(triangle1)

    circle1=GOval(20,20,x=290,y=290)
    circle1.filled=True
    circle1.fill_color='aquamarine'
    circle2=GOval(40,40,x=280,y=280)
    circle2.filled=True
    circle2.fill_color='aqua'
    circle3=GOval(60,60,x=270,y=270)
    circle3.filled=True
    circle3.fill_color='darkblue'
    circle4=GOval(80,80,x=260,y=260)
    circle4.filled=True
    circle4.fill_color='blueviolet'
    window.add(circle4)
    window.add(circle3)
    window.add(circle2)
    window.add(circle1)

    polygon=GPolygon()
    polygon.add_vertex((100, 60))
    polygon.add_vertex((50,100))
    polygon.add_vertex((40,180))
    polygon.add_vertex((20,400))
    polygon.add_vertex((30,550))
    polygon.add_vertex((180,580))
    polygon.add_vertex((400, 550))
    polygon.add_vertex((550, 590))
    polygon.filled=True
    polygon.fill_color='salmon'
    window.add(polygon)

    # logo
    sc101=GLabel('SC101-2020.Nov')
    sc101.font='Courier-15-bold-italic'
    window.add(sc101,0,window.height-sc101.height+20)


if __name__ == '__main__':
    main()
