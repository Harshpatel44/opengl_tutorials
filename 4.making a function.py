__author__ = 'harsh'
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math
import time
import sys
def init():
    glClearColor(1.0,1,1,1)
    gluOrtho2D(-100.0, 100.0,-40.0, 200.0)

def plot():

    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 0.0, 0.0)
    glLineWidth(0.01)
    glPointSize(5)
    for x in range(-15,15):    # these loop is for generating f(n)=x^2=y ... It loops from -15 to 15 x values
        y=x*x                  # y is calculted and stored

        #things you can try
        #y=math.sin(x)
        #y=math.cos(x)
        #y=math.sin(3*x)

        glBegin(GL_POINTS)
        glVertex2f(x,y)        # point is plotted
        glEnd()
        glFlush()

        glBegin(GL_LINES)      # these part is for rendering the coordinate x and y axis
        glVertex2f(-100.0,0)   # these 4 points make x axis and y axis
        glVertex2f(100.0,0)
        glVertex2f(0.0,-40)
        glVertex2f(0,200)
        glEnd()
        glFlush()



def main():
    glutInit(sys.argv)
    glutInitDisplayMode( GLUT_SINGLE | GLUT_RGB )
    glutInitWindowSize( 500,500 )
    glutInitWindowPosition(50,50)
    glutCreateWindow'Making a Function')
    glutDisplayFunc(plot)
    #glutDisplayFunc(plot)
    init()
    glutMainLoop()

main()
