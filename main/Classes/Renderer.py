from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


RESOLUTION = 500
GUI_SCALE = 10
zoom = 10  # How many lines of squares of screen will be visible


def vertical_lines():
    for x in range(zoom):
        glVertex2f(RESOLUTION / zoom * x, RESOLUTION - (RESOLUTION / zoom * (zoom - 2)))
        glVertex2f(RESOLUTION / zoom * x, RESOLUTION)


def horizontal_lines():
    for x in range(3, zoom):
        glVertex2f(0, RESOLUTION / zoom * x)
        glVertex2f(RESOLUTION, RESOLUTION / zoom * x)


def menu_lines():
    for x in range(1, 3):
        glVertex2f(0, RESOLUTION / GUI_SCALE * x)
        glVertex2f(RESOLUTION, RESOLUTION / GUI_SCALE * x)
    for x in range(GUI_SCALE):
        glVertex2f(RESOLUTION / zoom * x, RESOLUTION - (RESOLUTION / GUI_SCALE * (GUI_SCALE - 2)))
        glVertex2f(RESOLUTION / zoom * x, 0)


def mesh():
    glBegin(GL_LINES)
    glColor3f(3.0, 3.0, 3.0)
    horizontal_lines()
    vertical_lines()
    glColor3f(0.0, 3.0, 1.0)
    menu_lines()
    glEnd()


def iterate():
    glViewport(0, 0, RESOLUTION, RESOLUTION)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, RESOLUTION, 0.0, RESOLUTION, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    mesh()
    glutSwapBuffers()


def main():
    glutInit()
    glutInitDisplayMode(GLUT_RGBA)
    glutInitWindowSize(RESOLUTION, RESOLUTION)
    glutInitWindowPosition(0, 0)
    window = glutCreateWindow("OpenGL Coding Practice")
    glutDisplayFunc(showScreen)
    glutIdleFunc(showScreen)
    glutMainLoop()


if __name__ == '__main__':
    main()
