import turtle
t = turtle.Turtle()
f = open("Turtle.txt",'w')
have = []
for func in dir(t):
    doc = eval("t." + func + ".__doc__")
    if (doc in have) | (func[0] == "_") | (func.upper() == func):
        pass
    else:
        have.append(doc)
        f.write("##" + func + "\n\n\n")