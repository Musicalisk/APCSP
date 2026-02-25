import simplegui
from random import *
def draw_handler(canvas):
    color=['Red','Green','Blue']
    for i in range(1000):
        x=randrange(0,600)
        y=randrange(0,600)
        dotColor=choice(color)
        canvas.draw_point([x,y],dotColor)
frame = simplegui.create_frame('Testing', 600, 600)
frame.set_canvas_background("Black")
frame.set_draw_handler(draw_handler)
frame.start()