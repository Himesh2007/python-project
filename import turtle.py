import turtle
wn = turtle.Screen()
wn.title("Turtle Square")
wn.bgcolor("lightblue")
t = turtle.Turtle()
t.color("black")
t.speed(2)
for _ in range(4):
    t.forward(100)
    t.left(90)
wn.mainloop()