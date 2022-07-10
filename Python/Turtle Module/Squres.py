import turtle

turtle.bgcolor("black")


box = turtle.Turtle("circle")
box.speed(12)
box.pensize(5)
kk = 0
for k in range(4):
    i = 300
    colors = ['orange','white','red','blue','green','black']
    box.color(colors[kk])
    while i >= 0:
        box.penup()
        box.goto(-i,i)
        box.pendown()
        for j in range(4):
            box.forward(i*2+20)
            box.right(90)
        i -= 20
        print(i)
    kk += 1
    box.color(colors[kk])
    while i < 320:
        box.penup()
        box.goto(-i,i)
        box.pendown()
        for j in range(4):
            box.forward(i*2+20)
            box.right(90)
        i += 20
        print(i)
    kk += 1

input()