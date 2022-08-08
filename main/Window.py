import time

import numpy as np
from OpenGL.GL import *
from OpenGL.GL import shaders
from OpenGL.GLUT import *

from Classes.Parents.Map import Map

RESOLUTION = 500
GUI_SCALE = 10
zoom = 5  # How many lines of squares of screen will be visible

VERTEX_SHADER = """

#version 330

    in vec4 position;
    void main() {
    gl_Position = position;

}


"""

FRAGMENT_SHADER = """
#version 330

    void main() {

    gl_FragColor = 

    vec4(1.0f, 0.0f,0.0f,1.0f);

    }

"""


class Window:

    def __init__(self, w: int, h: int, ma: Map):
        glutInit()
        self.shaderProgram = None
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
        glClearColor(0, 0, 0, 1)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        glUseProgram(self.shaderProgram)

        glDrawArrays(GL_TRIANGLES, 0, 3)

        glUseProgram(0)
        glutSwapBuffers()

    def display(self):

        glutSwapBuffers()
        self.num_frames += 1

        t = time.time() - self.start_time
        if t >= 1:
            glutSetWindowTitle(f"Fps: {self.num_frames}")
            self.start_time = time.time()
            self.num_frames = 0

    def run(self):
        self.initliaze()
        glutDisplayFunc(self.render)
        glutMainLoop()

    def idle_func(self):
        glutPostRedisplay()

    def reshape(self, w, h):
        glViewport(0, 0, w, h)
        self.window_width = w
        self.window_height = h

    def initliaze(self):

        self.vertexshader = shaders.compileShader(VERTEX_SHADER, GL_VERTEX_SHADER)
        self.fragmentshader = shaders.compileShader(FRAGMENT_SHADER, GL_FRAGMENT_SHADER)

        self.shaderProgram = shaders.compileProgram(self.vertexshader, self.fragmentshader)

        triangles = [-0.5, -0.5, 0.0,
                     0.5, -0.5, 0.0,
                     0.0, 0.5, 0.0]

        triangles = np.array(triangles, dtype=np.float32)

        VBO = glGenBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER, VBO)
        glBufferData(GL_ARRAY_BUFFER, triangles.nbytes, triangles, GL_STATIC_DRAW)

        position = glGetAttribLocation(self.shaderProgram, 'position')
        glVertexAttribPointer(position, 3, GL_FLOAT, GL_FALSE, 0, None)
        glEnableVertexAttribArray(position)


if __name__ == '__main__':
    m = Map(1, "Hello")
    win = Window(500, 500, m)
    win.run()
