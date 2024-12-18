import sys
from array import array

import numpy as np
import pygame
import moderngl

vert_shader = '''
'''

frag_shader = '''
'''


def surf_to_texture(surf, ctx):
    tex = ctx.texture(surf.get_size(), 4)
    tex.filter = (moderngl.NEAREST, moderngl.NEAREST)
    tex.swizzle = 'BGRA'
    tex.write(surf.get_view('0'))
    return tex


def gen_quad_buffer(ctx):
    return ctx.buffer(data=array('f', [
        # position (x, y), uv coords (x, y)
        -1.0, 1.0,  0.0, 0.0,  # topleft
        1.0, 1.0,   1.0, 0.0,  # topright
        -1.0, -1.0, 0.0, 1.0,  # bottomleft
        1.0, -1.0,  1.0, 1.0,  # bottomright
    ]))


def main():
    pygame.init()

    pygame.display.set_mode((800, 600), pygame.OPENGL | pygame.DOUBLEBUF)
    display = pygame.surfarray.make_surface(np.random.rand(800,600,3)*255)
    ctx = moderngl.create_context()

    program = ctx.program(vertex_shader=vert_shader, fragment_shader=frag_shader)
    render_object = ctx.vertex_array(program, [(gen_quad_buffer(ctx), '2f 2f', 'vert', 'texcoord')])

    clock = pygame.time.Clock()
    t = 0
    while True:

        t += 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        frame_tex = surf_to_texture(display, ctx)
        frame_tex.use(0)
        program['tex'] = 0
        program['time'] = t
        render_object.render(mode=moderngl.TRIANGLE_STRIP)
        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    main()
