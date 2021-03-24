import turtle
kalem = turtle.Turtle()
kalem.speed(3)
sc = turtle.Screen()
sc.setup(1500,700)

kalem.penup()
kalem.goto(-600,300)
kalem.pendown()
kalem.color("#00b5e2", "#00b5e2")
kalem.begin_fill()
for x in range(2):
    kalem.forward(1200)
    kalem.right(90)
    kalem.forward(200)
    kalem.right(90)
kalem.end_fill()

kalem.penup()
kalem.goto(-600,100)
kalem.pendown()
kalem.color("#ef3340", "#ef3340")
kalem.begin_fill()
for x in range(2):
    kalem.forward(1200)
    kalem.right(90)
    kalem.forward(200)
    kalem.right(90)
kalem.end_fill()


kalem.penup()
kalem.goto(-600,-100)
kalem.pendown()
kalem.color("#509e2f", "#509e2f")
kalem.begin_fill()
for x in range(2):
    kalem.forward(1200)
    kalem.right(90)
    kalem.forward(200)
    kalem.right(90)
kalem.end_fill()


kalem.penup()
kalem.goto(-30,0)
kalem.pendown()
kalem.color("white","white")
kalem.begin_fill()
kalem.dot(180)


kalem.penup()
kalem.goto(-10,0)
kalem.pendown()
kalem.color("#ef3340","#ef3340")
kalem.begin_fill()
kalem.dot(150)
kalem.end_fill()

kalem.penup()
kalem.goto(30,30)
kalem.pendown()
kalem.color("white", "white")
kalem.right(20)
kalem.begin_fill()
for x in range(8):
    kalem.forward(80)
    kalem.right(135)
kalem.end_fill()


kalem.penup()
kalem.goto(-10,0)
kalem.pendown()
kalem.color("#ef3340","#ef3340")
kalem.begin_fill()
kalem.end_fill()



turtle.mainloop()