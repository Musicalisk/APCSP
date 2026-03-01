import simplegui
x=25
y=5
def draw_handler(canvas):
    global x
    global y
    x=x+y
    canvas.draw_polygon([(125,200),(275,200),(200,150)],1,'black','black')
    for i in range(1):
        canvas.draw_circle((x,150), 50, 1, 'Black', 'Yellow')
        canvas.draw_circle((x+22,125),5,1,'black','black')
        canvas.draw_circle((x-22,125),5,1,'black','black')
        canvas.draw_line((x-22,150),(x+22,150),2,'black')
        canvas.draw_line((x-22,150),(x+22,150),2,'black')
    if x==275:
        y=-5
    for i in range(1):
        canvas.draw_circle((x,150), 50, 1, 'Black', 'Yellow')
        canvas.draw_circle((x+22,125),5,1,'black','black')
        canvas.draw_circle((x-22,125),5,1,'black','black')
        canvas.draw_line((x-22,150),(x+22,150),2,'black')
        canvas.draw_line((x-22,150),(x+22,150),2,'black')
    if x==25:
        y=5
frame = simplegui.create_frame('Animation', 300, 300)
frame.set_canvas_background("Black")
frame.set_draw_handler(draw_handler)
frame.start()