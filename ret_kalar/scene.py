import moderngl
import numpy as np

from ret_kalar.sprite import Sprite


class VisObject:
    def __init__(self, sprite: Sprite, position, color, scale):
        self.sprite = sprite
        self.position = position
        self.color = color
        self.scale = scale
    def render(self):
        self.sprite.render(position=self.position, color=self.color, scale=self.scale)


class Scene:
    def __init__(self):
        self.ctx = moderngl.create_context()
        self.ctx.enable(moderngl.BLEND)
        with open("shader.vert", "r") as f:
            vertex_shader = f.read()
        with open("shader.frag", "r") as f:
            fragment_shader = f.read()
        self.program = self.ctx.program(vertex_shader=vertex_shader, fragment_shader=fragment_shader)

        sprite = Sprite(self.program)
        N = 10
        self.vis_objects = [
            VisObject(sprite, position=(i / N, i / N), color=(np.sin(i), np.cos(i), np.tan(i)), scale=1 / (2 * N)) for i
            in range(N)]

    def render(self):
        self.ctx.clear()
        self.ctx.enable(self.ctx.DEPTH_TEST)
        for vis_object in self.vis_objects:
            vis_object.render()
