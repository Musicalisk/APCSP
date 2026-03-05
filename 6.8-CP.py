import simplegui
x=5
def draw_handler(canvas):
    global x
    x=x+5
    canvas.draw_circle((x,150), 50, 1, 'Black', 'Yellow')
    canvas.draw_circle((x+22,125),5,1,'black','black')
    canvas.draw_circle((x-22,125),5,1,'black','black')
    canvas.draw_line((x-22,150),(x+22,150),2,'black')
    canvas.draw_line((x-22,150),(x+22,150),2,'black')
frame = simplegui.create_frame('Testing', 600, 300)
frame.set_canvas_background("Black")
frame.set_draw_handler(draw_handler)
frame.start()