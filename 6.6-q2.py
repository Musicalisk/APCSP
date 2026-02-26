import simplegui
def draw_handler(canvas):
    canvas.draw_circle([150,150],150,4,'green')
    canvas.draw_circle([450,150],150,4,'green')
    canvas.draw_circle([150,450],150,4,'green')
    canvas.draw_circle([450,450],150,4,'green')
frame = simplegui.create_frame('Testing', 600, 600)
frame.set_canvas_background("white")
frame.set_draw_handler(draw_handler)
frame.start()