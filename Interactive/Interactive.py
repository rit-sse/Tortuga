import turtle
wn = turtle.Screen()
t = turtle.Turtle()

can = turtle.Canvas()

def moveUp():
	t.fd(100)

def moveDown():
	t.bk(100)

def turnRight():
	t.rt(90)

def turnLeft():
	t.lt(90)
	# print(event.char)

wn.onkey(moveUp, "Up")
wn.onkey(moveDown, "Down")
wn.onkey(turnRight, "Right")
wn.onkey(turnLeft, "Left")

wn.listen()
wn.mainloop()