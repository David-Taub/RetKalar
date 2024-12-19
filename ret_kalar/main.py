import sys
from array import array

import numpy as np
import pygame
import moderngl

from ret_kalar.scene import Scene
# import math
import os
import sys
import pygame



def main():
    os.environ['SDL_WINDOWS_DPI_AWARENESS'] = 'permonitorv2'

    pygame.init()
    pygame.display.set_mode((800, 800), flags=pygame.OPENGL | pygame.DOUBLEBUF, vsync=True)
    scene = Scene()

    clock = pygame.time.Clock()
    t = 0
    while True:
        t += 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        scene.render()
        scene.program["time"] = t
        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    main()
