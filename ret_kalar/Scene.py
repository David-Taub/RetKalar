import moderngl


class Scene:
    def __init__(self):
        self.ctx = moderngl.get_context()
        with open("shader.vert", "r") as f:
            vertex_shader = f.read()
        with open("shader.frag", "r") as f:
            fragment_shader = f.read()
        self.program = self.ctx.program(vertex_shader=vertex_shader, fragment_shader=fragment_shader)

        self.triangle_geometry = TriangleGeometry()
        self.triangle = Mesh(self.program, self.triangle_geometry)

    def camera_matrix(self):
        now = pygame.time.get_ticks() / 1000.0
        eye = (math.cos(now), math.sin(now), 0.5)
        proj = glm.perspective(45.0, 1.0, 0.1, 1000.0)
        look = glm.lookAt(eye, (0.0, 0.0, 0.0), (0.0, 0.0, 1.0))
        return proj * look

    def render(self):
        camera = self.camera_matrix()

        self.ctx.clear()
        self.ctx.enable(self.ctx.DEPTH_TEST)

        self.program['camera'].write(camera)

        self.triangle.render((-0.2, 0.0, 0.0), (1.0, 0.0, 0.0), 0.2)
        self.triangle.render((0.0, 0.0, 0.0), (0.0, 1.0, 0.0), 0.2)
        self.triangle.render((0.2, 0.0, 0.0), (0.0, 0.0, 1.0), 0.2)
