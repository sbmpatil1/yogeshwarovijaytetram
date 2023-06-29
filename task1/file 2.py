import turtle

def draw_rainbow(colors):
  t = turtle.Turtle()
  t.penup()
  t.setposition(0, -200)
  t.pendown()
  for i in range(7):
    t.pencolor(colors[i])
    t.forward(200)
    t.right(60)

colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
draw_rainbow(colors)

turtle.done()
 