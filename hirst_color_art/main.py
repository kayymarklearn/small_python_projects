from random import choice
from turtle import Turtle, Screen

# import colorgram
# colors = colorgram.extract('Hirst.Jpeg', 5)

# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)

# print(rgb_colors)

tom = Turtle()
tom.shape("triangle")
tom.speed("fastest")
tom.hideturtle()
screen = Screen()
screen.colormode(255)
colors_list = [(47, 79, 79), (102, 51, 153), (184, 134, 11), (85, 107, 47), (205, 92, 92), (72, 61, 139), (139, 69, 19), (95, 158, 160), (154, 205, 50), (188, 143, 143), (123, 104, 238), (176, 196, 222), (46, 139, 87), (160, 82, 45), (112, 128, 144)]

tom.penup()
tom.setheading(225)
tom.forward(300)
tom.setheading(0)



for _ in range(10):
    for _ in range(10):
        tom.dot(20, choice(colors_list))
        tom.penup()
        tom.forward(50)
    tom.penup()
    tom.backward(500)
    tom.left(90)
    tom.forward(50)
    tom.right(90)


screen.exitonclick()