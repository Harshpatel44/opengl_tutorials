__author__ = 'harsh'
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math
import time
import sys
def init():
    glClearColor(1.0,1,1,1)
    gluOrtho2D(-2.0, 2.0,-2.0, 2.0)

def plot():

    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 0.0, 0.0)
    glLineWidth(0.01)
    glPointSize(5)
    global c
    c=0.1
    for t in range(0,63,1):    # these loop is for generating f(n)=x^2=y ... It loops from -15 to 15 x values

        t=float(t/10)+c
        c+=0.1
        #print(t)
        x=math.sin(t)
        y=math.cos(t)
        glBegin(GL_POINTS)
        glVertex2f(x,y)
        glEnd()
        glFlush()





def main():
    glutInit(sys.argv)
    glutInitDisplayMode( GLUT_SINGLE | GLUT_RGB )
    glutInitWindowSize( 500,500 )
    glutInitWindowPosition(50,50)
    glutCreateWindow('harsh')
    glutDisplayFunc(plot)
    #glutDisplayFunc(plot)
    init()
    glutMainLoop()

main()