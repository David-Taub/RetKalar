import moderngl
import numpy as np


class Sprite:
    def __init__(self, program):
        self.ctx = moderngl.get_context()
        # vertices = np.array([
        #     -1.0, 1.0, 0.0, 0.0,  # topleft
        #     1.0, 1.0, 1.0, 0.0,  # topright
        #     -1.0, -1.0, 0.0, 1.0,  # bottomleft
        #     1.0, -1.0, 1.0, 1.0,  # bottomright
        # ])
        vertices = np.array([
            -1.0, 1.0,   # topleft
            1.0, 1.0,    # topright
            -1.0, -1.0,  # bottomleft
            1.0, -1.0,   # bottomright
        ])

        self.vbo = self.ctx.buffer(vertices.astype('f4').tobytes())
        self.vao = self.ctx.vertex_array(program, [(self.vbo, '2f', 'in_vertex')])

    def render(self, position, color, scale):
        self.vao.program['position'] = position
        self.vao.program['color'] = color
        self.vao.program['scale'] = scale
        self.vao.render(moderngl.TRIANGLE_STRIP)
