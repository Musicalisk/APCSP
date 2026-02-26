import simplegui
def draw_handler(canvas):
    canvas.draw_polygon([(0,300),(400,300),(400,400),(0,400)],1,'black','green')
    canvas.draw_polygon([(150,200),(250,200),(250,350),(150,350)],1,'black','yellow')
    canvas.draw_polygon([(125,200),(275,200),(200,150)],1,'black','brown')
    canvas.draw_circle([50,50],25,1,'black','yellow')
frame = simplegui.create_frame('Testing', 400, 400)
frame.set_canvas_background("lightblue")
frame.set_draw_handler(draw_handler)
frame.start()