import turtle
 
t = turtle.Turtle()
t.fillcolor('#FFA500')
t.begin_fill()
for i in range(4):
  t.forward(150)
  t.right(-120)
t.end_fill()
