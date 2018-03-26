__author__ = 'harsh'
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
def init():
    glClearColor(0.0,0,0,0)
    gluOrtho2D(-1.0, 1.0,-1.0, 1.0)

def plot():
    print('harsh')
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 0.0, 0.0)
    glLineWidth(5)

    glBegin(GL_LINES)
    #glBegin(GL_LINE_STRIP)        # the end points are joined of the lines
    #glBegin(GL_LINE_LOOP)          # the starting as well as ending points of the lines are joined
    glVertex2f(-1.0, 0.0)
    glVertex2f(1.0, 0.0)
    glVertex2f(0.0, -1.0)
    glVertex2f(0.0, 1.0)

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