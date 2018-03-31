from OpenGL import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

def init():
    glClearColor(0,0,0,0)
    gluOrtho2D(-2,2,-2,2)
def function():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0,0.0,0.0)
    glPointSize(2)
    a=1.0          #initial value of a (1,2)
    r=1
    g=0
    b=0
    while a<2.0:
        a+=0.1       #incrementing each time to create another cubic but at diffrent position

        r+=0.2
        g+=0.1
        b+=0.1
        t=-4.4      #initial value of t (-4.4,4,4)
        #raw_input()
        while t<4.4:

            t+=0.003          #increased each time to plot a dot to another place
            glColor3f(r,g,b)  #color changed for every cubic
            x=0.3*a*(t*t-3)   # x and y equations to produce tschirnhausen cubic
            y=0.1*a*t*(t*t-3)

            glBegin(GL_POINTS)
            glVertex2f(x,y)     #plotting the points
            glEnd()
            glFlush()




def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500,500)
    glutInitWindowPosition(20,20)
    glutCreateWindow("Tschirnhausens Cubic")
    glutDisplayFunc(function)
    init()
    glutMainLoop()
main()

