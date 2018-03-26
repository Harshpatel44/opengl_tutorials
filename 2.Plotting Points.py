from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

def init():
    glClearColor(0.0, 0.0, 0.0, 0.0)   # to give screen background a color (R,G,B,opacity)  Black here
    gluOrtho2D(-1.0, 1.0, -1.0, 1.0)   # selects a range of the coordinate system of 2d

def plotpoints():
    glClear(GL_COLOR_BUFFER_BIT)       # clears the color so that each time black color background can be filled up
    glColor3f(1.0, 0.0, 0.0)           # sets the color of the point that we are going to plot (Red here)
    glPointSize(10)                    # sets point size that we are going to plot

    glBegin(GL_POINTS)                 # tells opengl that we are going to plot points now
    glVertex2f(0.0, 0.5)               # plotting of point at (0,0) [2f indicates 2 floating numbers as arguements]
    glVertex2f(0.0, 0.0)
    glVertex2f(0.0, -0.5)
    glVertex2f(0.5, 0.0)
    glVertex2f(-0.5, 0.0)
    glEnd()                            # end of plotting

    glFlush()                          # flushing drawing to the screen

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)   # single window and rgb mode
    glutInitWindowSize(500,500)                 # window size
    glutInitWindowPosition(50,50)               # window position in screen
    glutCreateWindow('harsh')                   # title of window
    glutDisplayFunc(plotpoints)                 # running the function
    init()                                      # running init function
    glutMainLoop()                              # mainloop iterates to render graphics
main()