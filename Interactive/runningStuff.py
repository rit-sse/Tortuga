#!/usr/bin/env python
 
# Adapted from David Llewellyn-Jones's code
# http://www.flypig.co.uk/?page=list&list_id=363&list=blog
# By Aaron Brady
# http://insom.me.uk/
 
import turtle as t
import sys
import tty
import termios
 
 
def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch
 
ch = ' '
print "Ready"
while ch != 'q':
    ch = getch()
 
    if ch == 'w':
        t.forward(10)
    elif ch == 's':
        t.backward(10)
    elif ch == 'a':
        t.left(10)
    elif ch == 'd':
        t.right(10)
