# import colorgram
import turtle as t
import random

t.colormode(255)
michael = t.Turtle()
michael.speed("fastest")
michael.penup()
michael.hideturtle()

color_list = [(198, 162, 101), (63, 90, 126), (139, 170, 191), (136, 91, 50), (132, 28, 53), (219, 205, 120),
              (29, 40, 65), (78, 16, 35), (149, 62, 85), (162, 155, 53), (184, 141, 158), (132, 182, 145), (48, 56, 99),
              (180, 97, 107), (56, 35, 22), (68, 130, 106), (98, 118, 166), (82, 148, 159), (221, 175, 187),
              (169, 206, 166), (90, 151, 96), (185, 97, 80), (163, 200, 213), (179, 188, 211), (80, 70, 39),
              (131, 37, 27)]

michael.setheading(225)
michael.forward(300)
michael.setheading(0)

number_of_dots = 101
for dot_count in range(1, number_of_dots):
    michael.dot(20, random.choice(color_list))
    michael.forward(50)

    if dot_count % 10 == 0:
        michael.setheading(90)
        michael.forward(50)
        michael.setheading(180)
        michael.forward(500)
        michael.setheading(0)

screen = t.Screen()
screen.exitonclick()