import moderngl
import numpy as np


class Sprite:
    def __init__(self):
        self.ctx: moderngl.Context = moderngl.get_context()
        vertices = np.array([
            -1.0, 1.0,  0.0, # topleft
            1.0,  1.0,  0.0, # topright
            -1.0, -1.0, 0.0, # bottomleft
            1.0,  -1.0, 0.0, # bottomright
        ])

        self.vbo = self.ctx.buffer(vertices.astype('f4').tobytes())

    def vertex_array(self, program) -> moderngl.VertexArray:
        return self.ctx.vertex_array(program, [(self.vbo, '3f', 'vertex')])
