'''
    in this udacity project , we weill use turtle module to draw different shapes
    draws circles out of squares and triangles
'''

import turtle
import Tkinter

def draw_square():
    sq = turtle.Turtle()
    sq.color("red")
    sq.shape("turtle")
    sq.speed(10)
    sq.fillcolor("yellow")
    sq.screen.bgcolor("skyblue")
    i = 0
    while i < 36:
        for _ in range(0,4):
            sq.forward(200)
            sq.right(90)

        sq.right(10)
        i += 1

def draw_triangle():
    tr = turtle.Turtle(shape="turtle")
    i = 0
    while i < 36:
        for _ in range(0,3):
            tr.forward(200)
            tr.left(120)
        tr.left(10)
        i += 1



draw = turtle.Turtle()
draw.onclick(draw_square())
#draw.onclick(draw_triangle())
#draw_square()
#draw_triangle()


