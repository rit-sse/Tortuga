#Turtle Parallel Functionallity

###This Document
This document describes the feasibility of each turtle-python function 

###Legend
✔ - Doable, Code should/can be created in Parallel System  
○ - Already Implemented, Code that exists doesn't need to be re-implemented  
✘ - Not-Doable, Hardware limitations prevent a parallel implementation  


##✔ back
Basic Movement.

##✘ begin_fill
Requires virtual space.

##○ begin_poly
Start recording the vertices of a polygon. Doesnt change canvas.

##✔ circle
Basic Movement.

##✘ clear
Clears the canvas (Can't Erase)

##✘ clearstamp
Removes a previous stamp by ID (Can't Erase)

##✘ clearstamps
Removes all previous stamps (Can't Erase)

##✘ clone
Makes another instance (Only have one robot per instance)

##✘ color
Changes pen color (can change manually)

##✘ currentLine
Returns the current line absolute positions (Only doing relative)

##✘ currentLineItem
Returns a variable (Not needed)

##✔ degrees
Changes the number of degrees in a full rotation

##✘ distance
Measures between the turtle and another location (Only doing relative)

##✘ dot
Filled in circle (Not doing fill)

##✔ down
Pen down

##✘ end_fill
Ends a fill (Not doing fill)

##○ end_poly
Ends a poly definition

##✔ fd
Basic Movement

##✘ fillcolor
not doing fill

##✘ filling
Not doing fill

##○ get_poly
Poly Stuff

##○ get_shapepoly
Poly Stuff

##○ getpen
Returns the turtle instance (Could be useful when you you dont want a clone).

##✘ getscreen
No canvas instance

##✘ goto
Only doing relative

##○ heading
Returns current heading

##✘ hideturtle
Can't hide the Pi

##✘ home
Only doing relative

##○ isdown
Returns pen state

##✘ isvisible
Not Hiding (Always return true)

##✔ left
Basic Movement

##✘ onclick
Requires screen

##✘ ondrag
Requires screen

##✘ onrelease
Requires Screen

##✘ pen
Not changing the pen


##✘ pencolor
Not changing the pen

##✘ pensize
Not changing the pen

##✔ penup
Lifts pen

##✘ pos
Only relative

##✔ radians
Changes angles to radians

##✘ reset
Can't erase and only relative

##✘ resizemode


##✔ right
Basic Movement

##✘ screen
No Screen

##? seth
?

##? settiltangle
?

##? setundobuffer
?

##✘ setx
Only Relative

##✘ sety 
Only Relative

##? shape 
?

##? shapesize
?

##? shapetransform
?

##? shearfactor
?

##✘ showturtle
Not hiding so it is always shown

##✔ speed
Changes the turtle speed

##✔ stamp
Marks where the current turtle is.

##? tilt
?

##? tiltangle
?

##✘ towards 
Only doing relative

##? turtle
?

##✘ undo 
Can't erase

##? undobuffer
?

##? undobufferentries 
?

##? write
Writes a given string

##✘ xcor 
Only doing Relative

##✘ ycor 
Only doing Relative
