#Python. Code should be:
#This tricks is for spiral 
import colorsys
import turtle

t = turtle.Turtle()
s = turtle.Screen()

s.bgcolor('black')
t.speed(0)  # Maximum drawing speed

n = 36
h = 0

for i in range(460):
    c = colorsys.hsv_to_rgb(h, 1, 0.8)
    h += 1 / n
    t.color(c)
    t.left(145)

    for j in range(5):
        t.forward(100)
        t.left(150)