import turtle
loadWindow = turtle.Screen()
turtle.colormode(255)

turtle.speed(2)

for i in range(100):
    turtle.circle(5*i)
    turtle.circle(-5*i)
    turtle.left(i)

turtle.exitonclick()

# This program draws an image in Python Shell
#February 17, 2020
# Dayna Madourie 
        
