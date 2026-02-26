import simplegui
def draw_handler(canvas):
    center=(300,300)
    canvas.draw_circle(center,250,1,'black','white')
    canvas.draw_circle(center,200,1,'black','blue')
    canvas.draw_circle(center,150,1,'black','red')
    canvas.draw_circle(center,100,1,'black','yellow')
frame = simplegui.create_frame('Testing', 600, 600)
frame.set_canvas_background("White")
frame.set_draw_handler(draw_handler)