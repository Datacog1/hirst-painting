# import colorgram

# rgb_colors = []
# colors = colorgram.extract('image.jpg', 9)


# for c in colors:
#     r = c.rgb.r
#     g = c.rgb.g
#     b = c.rgb.b
#     new_color = (r,g,b)
#     rgb_colors.append(new_color)
    

# print(rgb_colors)
 
#-------------------------------------------------------


from this import d
import turtle
import random


turtle.colormode(255)
my_turtle = turtle.Turtle()
my_turtle.speed("fastest")
my_turtle.penup()
my_turtle.hideturtle()

color_list = [(247, 247, 247), (154, 42, 114), (165, 84, 71), (118, 29, 83), (223, 122, 183), (123, 180, 206), (5, 147, 193), (7, 18, 45), (244, 235, 241)]
my_turtle.setheading(225)
my_turtle.forward(300)
my_turtle.setheading(0)
dots_number = 100

for d_count in range(1,dots_number+1):
    my_turtle.dot(20,random.choice(color_list))
    my_turtle.forward(50)
    
    if d_count % 10 == 0:
        my_turtle.setheading(90)
        my_turtle.fd(50)
        my_turtle.setheading(180)
        my_turtle.forward(500)
        my_turtle.setheading(0)






my_screen = turtle.Screen()
my_screen.exitonclick()