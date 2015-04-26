from RaspiRobotBoard import *

_robot = RaspiRobot()

def alias(*aliases):
  """
  A function to"""
  def wrap(f):
    import sys
    module = sys.modules[__name__]
    for alias in aliases:
      setattr(module, alias, f)
    return f
  return wrap

def tortuga():
  return _robot

@alias('register_shape', 'addshape')
def addshape(name, shape=None):
  #Alias register_shape | addshape
  pass

@alias('backward', 'bk')
def back(distance):
  #Alias back | backward | bk
  pass

def begin_fill():
  # Will not be implementing.
  print("Sorry this isn't implemented")

def begin_poly():
  # Already implemented
  pass  

def bye():
  # Will not be implementing.
  print("Sorry this isn't implemented")

def circle(radius, extent=None, steps=None):
  pass

def clear():
  # Will not be implementing.
  print("Sorry this isn't implemented")

def clearstamp(stampid):
  # Will not be implementing.
  print("Sorry this isn't implemented")

def clearstamps(n=None):
  # Will not be implementing.
  print("Sorry this isn't implemented")
  
def clone():
  # Will not be implementing.
  print("Sorry this isn't implemented")

def color(*args):
  # Will not be implementing.
  print("Sorry this isn't implemented")

def colormode(cmode=None):
  pass

def currentLine():
  # Will not be implementing.
  print("Sorry this isn't implemented")

def currentLineItem():
  # Will not be implementing.
  print("Sorry this isn't implemented")

def degrees(fullcircle=360.0):
  pass

def distance(x, y=None):
  # Will not be implementing.
  print("Sorry this isn't implemented")

@alias('mainloop')
def done():
  #Alias mainloop | done
  pass

def dot(size=None, *color):
  # Will not be implementing.
  print("Sorry this isn't implemented")

def end_fill():
  # Will not be implementing.
  print("Sorry this isn't implemented")

def end_poly():
  # Already implemented
  pass

def exitonclick():
  # Will not be implementing.
  print("Sorry this isn't implemented")

def forward(distance):
  #Alias forward | fd
  pass

def fill(flag):
  #Will not be implementing.
  print("Sorry this isn't implemented.")

def fillcolor(*args):
  # Will not be implementing.
  print("Sorry this isn't implemented.")

def Filling():
  # Will not be implementing.
  print("Sorry this isn't implemented.")

def get_poly():
  # Already implemented
  pass

def get_shapepoly():
  # Already implmented
  pass

def getcanvas():
  pass

@alias('getturtle')
def getpen():
  # Already implemented
  #Alias getturtle | getpen
  pass

def getscreen():
  # Will not be implementing.
  print("Sorry this isn't implemented.")

def getshapes():
  pass

@alias('setpo', 'setposition')
def goto(x, y=None):
  # Will not be implementing.
  #Alias goto | setpos | setposition
  print("Sorry this isn't implemented.")

def heading():
  # Already implemented
  pass

@alias('ht')
def hideturtle():
  # Will not be implementing.
  #Alias hideturtle | ht
  print("Sorry this isn't implemented.")

def home():
  # Will not be implementing.
  print("Sorry this isn't implemented.")

def isdown():
  # Already implemented
  pass

def isvisible():
  # Will not be implementing.
  print("Sorry this isn't implemented")

@alias("lt")
def left(angle):
  #Alias left | lt
  pass

def listen(xdummy=None, ydummy=None):
  pass

def mode(mode=None):
  pass

@alias("onscreenclick")
def onclick(fun, btn=1, add=None):
  # Will not be implementing.
  #Alias onclick | onscreenclick
  print("Sorry this isn't implemented.")

def ondrag(fun, btn=1, add=None):
  # Will not be implementing.
  print("Sorry this isn't implemented.")

def onkey(fun, key):
  pass

def onrelease(fun, btn=1, add=None):
  # Will not be implementing.
  print("Sorry this isn't implemented.")

def ontimer(fun, t=0):
  pass

def pen(pen=None, **pendict):
  # Will not be implementing.
  print("Sorry this isn't implemented.")

def pencolor(*args):
  # Will not be implementing.
  print("Sorry this isn't implemented.")

@alias("pd", "down")
def pendown():
  #Alias pendown | pd | down
  pass

@alias("pu", "up")
def penup():
  #Alias penup | pu | up
  pass

def pos():
  # Will not be implementing.
  #Alias position | pos
  print("Sorry this isn't implemented.")

def radians():
  pass

def reset():
  # Will not be implementing.
  print("Sorry this isn't implemented.")

def resizemode(rmode=None):
  # Will not be implementing.
  print("Sorry this isn't implemented.")

@alias("rt")
def right(angle):
  #Alias right | rt
  pass

def screen():
  # Will not be implementing.
  print("Sorry this isn't implemented.")

def seth(to_angle):
  #Alias setheading | seth
  pass

def settiltangle(angle):
  pass

def setundobuffer(size):
  pass

def setup(width=_CFG["width"], height=_CFG["height"], startx=_CFG["leftright"], starty=_CFG["topbottom"]):
  pass

def setx(x):
  # Will not be implementing.
  print("Sorry this isn't implemented.")

def sety(y):
  # Will not be implementing.
  print("Sorry this isn't implemented.")

def shape(name=None):
  pass

@alias("turtlesize")
def shapesize(stretch_wid=None, stretch_len=None, outline=None):
  #Alias shapesize | turtlesize
  pass

def shapetransform():
  pass

def shearfactor():
  pass

def speed(speed=None):
  # Will not be implementing.
  print("Sorry this isn't implemented.")

@alias("showturtle")
def st():
  # Will not be implementing.
  #Alias showturtle | st()
  print("Sorry this isn't implemented.")

def stamp():
  pass

def tilt(angle):
  pass

def tiltangle():
  pass

def title(titlestring):
  pass

def towards(x, y=None):
  # Will not be implementing.
  print("Sorry this isn't implemented.")

def tracer(flag=None, delay=None):
  pass

def turtle():
  return _robot

def turtles():
  return _robot

def undo():
  # Will not be implementing.
  print("Sorry this isn't implemented.")

def undobuffer():
  pass

def undobufferentries():
  pass

def update():
  pass

@alias("pensize", "width")
def width(width=None):
  # Will not be implementing.
  #Alias pensize | width
  print("Sorry this isn't implemented.")

def window_height():
  pass

def window_width():
  pass

def write(arg, move=False, align="left", font=("Arial", 8, "normal")):
  pass

def xcor():
  # Will not be implementing.
  print("Sorry this isn't implemented.")

def ycor():
  # Will not be implementing.
  print("Sorry this isn't implemented.")