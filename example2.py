import  turtle
def draw_square():

    brade=turtle.Turtle()
    brade.shape("turtle")
    brade.speed(2)

    brade.forward(100)
    brade.right(50)
    brade.forward(100)
    brade.right(60)
    brade.forward(100)
    brade.right(70)
    brade.forward(100)
    brade.right(50)
  ## brade.right(50)
    brade.forward(100)
    brade.right(60)
    brade.forward(100)
    #brade.right(50)
def d_cir():
    cir=turtle.Turtle()
    cir.shape("arrow")
    cir.color("blue")
    cir.circle(100)
ange = turtle.Screen()
ange.bgcolor("green")

draw_square()
d_cir()

ange.exitonclick()
