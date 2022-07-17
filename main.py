from turtle import *

screen = Screen()
screen.setup(width=800, height=800)

speed(0)
bgcolor('black')
color('red')
hideturtle()

n = 1
p = True

while True:
    circle(n)
    if p:
        n = n - 2
    else:
        n = n + 2

    if n == 0 or n == 50:
        p = not p

    left(2)
    forward(4)

done()