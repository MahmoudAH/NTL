import turtle


def draw_square():

    brade = turtle.Turtle()
    brade.shape("turtle")
    brade.color("yellow")
    brade.speed(3)
    #turtle.resizemode(2)
    brade.width(30)


    for i in range(8):
        brade.forward(100)
        brade.right(90)
def cir():
    noga=turtle.Turtle()
    noga.shape("arrow")
    noga.color("red")
    noga.width(40)
    noga.circle(100)

def tri():
    tom = turtle.Turtle()
    tom.shape("turtle")
    tom.color("blue")
    tom.width(20)
    tom.backward(100)
    tom.right(120)
    tom.backward(100)
    tom.right(120)
    tom.backward(100)

windows=turtle.Screen()
windows.bgcolor("green")
draw_square()
cir()
tri()

windows.exitonclick()