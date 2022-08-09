import time
from math import floor

from OpenGL.GL import *
from OpenGL.GL import shaders
from OpenGL.GLUT import *

from Classes.Parents.Map import Map
from Classes.Parents.Game import Game

RESOLUTION = 500
GUI_SCALE = 10
zoom = 10  # How many lines of squares of screen will be visible

VERTEX_SHADER = """

#version 330

    in vec4 position;
    void main() {
    gl_Position = position;

}


"""

FRAGMENT_SHADER = """
#version 330
    uniform vec3 my_color;
    void main() {
    gl_FragColor.rgb = my_color;
    gl_FragColor.a = 1; // the alpha component
    }

"""


class Window:

    def __init__(self, w: int, h: int, ma: Map):
        glutInit()
        self.shaderProgram = None
        self.player_x = 10
        self.player_y = 10
        self.map = ma.cells
        self.visible_chunks = [ma.cells[i][self.player_y - zoom: self.player_y + zoom] for i in range(self.player_x - zoom, self.player_x + zoom)]

        self.window_width = w
        self.window_height = h

        glutInitContextProfile(GLUT_CORE_PROFILE)
        glutInitContextFlags(GLUT_FORWARD_COMPATIBLE)
        glutSetOption(GLUT_MULTISAMPLE, 16)
        glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH | GLUT_MULTISAMPLE)
        glutInitWindowSize(w, h)
        glutCreateWindow('Test')
        glutMouseFunc(self.mouseControl)
        glutReshapeFunc(self.reshape)
        glutDisplayFunc(self.display)
        glutIdleFunc(self.idle_func)
        self.keys = {chr(i): False for i in range(256)}

        self.start_time = time.time()
        self.num_frames = 0

    def draw_rect(self, color: tuple, x0: float, y0: float, x1: float, y1: float) -> None:
        color_location = glGetUniformLocation(self.shaderProgram, "my_color")
        glUniform3fv(color_location, 1, color)
        glBegin(GL_QUADS)
        glVertex2f(x0, y0)
        glVertex2f(x0, y1)
        glVertex2f(x1, y1)
        glVertex2f(x1, y0)
        glEnd()

    def mouseControl(self, button, state, mx, my):
        if button == GLUT_LEFT_BUTTON:
            if state == GLUT_DOWN:
                x = floor(mx / self.window_width * len(self.visible_chunks))
                y = floor(my / self.window_height * len(self.visible_chunks))
                self.visible_chunks[-(y + 1)][x].get_terrain().color = (1, 1, 1)

    def rect(self, is_drawing: bool):
        temp1 = 1
        temp2 = 3
        temp = 2 / len(self.visible_chunks)
        for ykey, yvalue in enumerate(self.visible_chunks):
            for xkey, xvalue in enumerate(yvalue):
                x0 = round(temp * xkey - temp1, temp2)
                x1 = round(temp * (xkey + 1) - temp1, temp2)
                y0 = round(temp * ykey - temp1, temp2)
                y1 = round(temp * (ykey + 1) - temp1, temp2)
                if is_drawing:
                    self.draw_rect(xvalue.get_terrain().color, x0, y0, x1, y1)
                else:
                    print(x0, x1, y0, y1)

    def render(self) -> None:
        glClearColor(0, 0, 0, 1)  # Background color
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        glUseProgram(self.shaderProgram)
        self.rect(True)
        glUseProgram(0)
        self.display()

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

        VBO = glGenBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER, VBO)

        position = glGetAttribLocation(self.shaderProgram, 'position')
        glVertexAttribPointer(position, 3, GL_FLOAT, GL_FALSE, 0, None)
        glEnableVertexAttribArray(position)


if __name__ == '__main__':
    game = Game(Map(1, "Hello"))
    win = Window(500, 500, game.map)
    win.run()
