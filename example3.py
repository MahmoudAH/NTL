import turtle


def draw_square():
    ange = turtle.Screen()
    ange.bgcolor("green")

    brade = turtle.Turtle()
    brade.shape("turtle")
    brade.speed(5)
    for i in range(24):
        if i%2==0:
          brade.color("blue")

        else:
          brade.color("red")
        for j in range(4):
           brade.forward(100)
           brade.right(90)
        brade.right(15)
    ange.exitonclick()
draw_square()