__author__ = 'harsh'
__author__ = 'harsh'
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math
import time
import sys
def init():
    glClearColor(0,0,0,0)
    gluOrtho2D(-2.0, 2.0,-2.0, 2.0)

def plot():

    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 0.0, 0.0)
    glLineWidth(0.01)
    glPointSize(3)

    t=0.00
    while(t<6.28):               # these loop is for generating f(n)=x^2=y ... It loops from -15 to 15 x values
        time.sleep(0.001)        # these is delay for 0.001 seconds , to show transition
        global t
        t=t+0.01                 # increasing value of t by 0.01 each time
        x=math.sin(t)            # putting x value
        y=math.cos(t)            # putting y value
        glBegin(GL_POINTS)       # pointing points
        glVertex2f(x,y)

        glEnd()
        glFlush()

        # decentralised applications
        # internet of things , machine learning
        # delfii ide
        # unity engine





def main():
    glutInit(sys.argv)
    glutInitDisplayMode( GLUT_SINGLE | GLUT_RGB )
    glutInitWindowSize( 500,500 )
    glutInitWindowPosition(50,50)
    glutCreateWindow('Circle Animation')
    glutDisplayFunc(plot)
    #glutDisplayFunc(plot)
    init()
    glutMainLoop()

main()