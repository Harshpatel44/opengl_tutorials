__author__ = 'harsh'
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

def draw():
    glutSolidTeapot(0.5)     #making of teapot of size 0.5
    #glutWireSphere(0.5,10,10
    glFlush()
glutInit(sys.argv)         #initialises glut
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)      #sets display mode that is single window and rgb color
glutCreateWindow("My First OGL Program")         #sets the title of the window
glutDisplayFunc(draw)                            #calls the function draw to render
glutMainLoop()                                   #iterates to create graphics realtime

glutInitWindowSize(250,250)
glutInitWindowPosition(100,100)