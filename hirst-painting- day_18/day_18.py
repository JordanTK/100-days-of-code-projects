# Extrcting the colors in the painting as tuples
import colorgram, turtle
from random import choice
turtle.screensize(5000,5000)
rgb_colors = [color.rgb for color in colorgram.extract('image.jpg', 30)]
turtle.colormode(255)
# Drawing columns of rows
for _ in range(10):
    tp = turtle.position()
    # Drawing a row of circles
    for _ in range(10):
        turtle.dot(40,choice(rgb_colors))
        turtle.up()
        turtle.fd(50)
        turtle.down()
    turtle.up()
    turtle.setposition(tp+(0, 90))
    turtle.down()

turtle.exitonclick()
