import simplegui
def draw_handler(canvas):
    center=(300,300)
    maxSize=560
    for i in range(4,0,-1):
        size = maxSize*(i/4)
        halfSize=size/2
        point1=(center[0],center[1]-halfSize)
        point2=(center[0]+halfSize,center[1])
        point3=(center[0],center[1]+halfSize)
        point4=(center[0]-halfSize,center[1])
        points=[point1,point2,point3,point4]
        color='White'
        canvas.draw_polygon(points,2,color,color)
frame = simplegui.create_frame('Testing', 600, 600)
frame.set_canvas_background("Black")
frame.set_draw_handler(draw_handler)
frame.start()