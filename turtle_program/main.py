# import the Turtle Module from Python internal Library
import turtle


def turtle_stairs(steps, size):
    for i in range(0, steps):  # de 0 a 5 faça o seguinte:
        t.fd(size)  # frente 30
        t.left(90)  # cursor virar 90º esquerda
        t.fd(size)  # frente 30
        t.right(90)  # cursor virar 90º direita
    t.fd(size)  # avance mais 30


def turtle_square(size):
    for i in range(0, 4):
        t.fd(size)
        t.left(90)


def turtle_squares(starting_size, squares):
    for i in range(0, squares):
        size = (i + 1) * starting_size
        turtle_square(size)


# t = turtle Object - This creates and start a Turtle Object.
t = turtle.Turtle()

# stairs = turtle_stairs(1, 60)
turtle_squares(10, 10)

# this ends the turtle module
turtle.done()
