from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forward():
    tim.forward(10)


def move_backward():
    tim.backward(10)


def turn_right():
    # new_heading = tim.heading() + 10
    # tim.setheading(new_heading)
    tim.right(10)


def turn_left():
    # new_heading = tim.heading() - 10
    # tim.setheading(new_heading)
    tim.left(10)


def clear():
    # tim.clear()
    # tim.penup()
    # tim.home()
    # tim.pendown()
    tim.reset()


screen.listen()
screen.onkey(fun=move_forward, key="w")
screen.onkey(fun=move_backward, key="s")
screen.onkey(fun=turn_left, key="a")
screen.onkey(fun=turn_right, key="d")
screen.onkey(fun=clear, key="c")

screen.exitonclick()
