import turtle

def draw_shape(shape, speed, color, corners, lenght):
    brad = turtle.Turtle()
    brad.shape("classic")
    brad.color(color)
    turtle.showturtle()
    brad.speed(speed)

    if corners > 0 :
        angle = 360/corners
        while corners > 0:
            brad.forward(lenght)
            brad.right(angle)
            corners -=1
    else:
        brad.circle(lenght)



window = turtle.Screen()
window.bgcolor("black")

draw_shape("turtle",3,"yellow",4,100)
draw_shape("arrow",4,"white",0,100)
draw_shape("classic",5,"orange",3,100)
draw_shape("arrow",8,"green",8,100)
window.exitonclick()
