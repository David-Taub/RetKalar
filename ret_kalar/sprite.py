import moderngl
import numpy as np
from pygame.transform import scale


class Sprite:
    def __init__(self, center_position, scale, rotation):
        self.ctx: moderngl.Context = moderngl.get_context()
        # position (x, y), uv coords (x, y)
        quad_vertices = np.array([
            -1.0, 1.0, 0.0, 0.0,  # topleft
            1.0, 1.0, 1.0, 0.0,  # topright
            -1.0, -1.0, 0.0, 1.0,  # bottomleft
            1.0, -1.0, 1.0, 1.0,  # bottomright
        ])
        self.center_position = center_position,
        self.scale = scale,
        self.rotation = rotation
        self.texture = self.ctx.texture(size=(2,2), components=3, data=)
        self.quad_vertex_buffer = self.ctx.buffer(quad_vertices.astype('f4').tobytes())

    def render(self, program):
        self.texture.use()
        program["center_position"] = self.center_position
        program["scale"] = self.scale
        program["rotation"] = self.rotation
        vao = self.ctx.vertex_array(program, [(self.quad_vertex_buffer, '2f 2f', 'in_pos in_uv')])
        vao.render()
