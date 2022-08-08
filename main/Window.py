import time

from OpenGL.GL import *
from OpenGL.GLUT import *

from Classes.Parents.Map import Map


RESOLUTION = 500
GUI_SCALE = 10
zoom = 5  # How many lines of squares of screen will be visible


class Window:

    def __init__(self, w: int, h: int, ma: Map):
        glutInit()
        self.player_x = 10
        self.player_y = 10
        self.visible_chunks = [ma.cells[i][self.player_y - zoom: self.player_y + zoom] for i in range(self.player_x - zoom, self.player_x + zoom)]

        self.window_width = w
        self.window_height = h
        glutInitContextProfile(GLUT_CORE_PROFILE)
        glutInitContextFlags(GLUT_FORWARD_COMPATIBLE)
        glutSetOption(GLUT_MULTISAMPLE, 16)
        glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH | GLUT_MULTISAMPLE)
        glutInitWindowSize(w, h)
        glutCreateWindow('Test')
        glutReshapeFunc(self.reshape)
        glutDisplayFunc(self.display)
        glutIdleFunc(self.idle_func)
        self.keys = {chr(i): False for i in range(256)}

        self.start_time = time.time()
        self.num_frames = 0

    def render(self):
        pass

    def display(self):

        glutSwapBuffers()
        self.num_frames += 1

        t = time.time() - self.start_time
        if t >= 1:
            glutSetWindowTitle(f"Fps: {self.num_frames}")
            self.start_time = time.time()
            self.num_frames = 0

    def run(self):
        glutMainLoop()

    def idle_func(self):
        glutPostRedisplay()

    def reshape(self, w, h):
        glViewport(0, 0, w, h)
        self.window_width = w
        self.window_height = h


if __name__ == '__main__':
    m = Map(1, "Hello")
    w = Window(500, 500, m)
    w.run()
