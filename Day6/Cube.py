from Mesh3D import *

class Cube(Mesh3D):
    def __init__(self, draw_type, filename):
        self.vertices = [(0.5, -0.5, 0.5),
                        (-0.5, -0.5, 0.5),
                        (0.5, 0.5, 0.5),
                        (-0.5, 0.5, 0.5),
                        (0.5, 0.5, -0.5),
                        (-0.5, 0.5, -0.5),
                        (0.5, -0.5, -0.5),
                        (-0.5, -0.5, -0.5),
                        (0.5, 0.5, 0.5),
                        (-0.5, 0.5, 0.5),
                        (0.5, 0.5, -0.5),
                        (-0.5, 0.5, -0.5),
                        (0.5, -0.5, -0.5),
                        (0.5, -0.5, 0.5),
                        (-0.5, -0.5, 0.5),
                        (-0.5, -0.5, -0.5),
                        (-0.5, -0.5, 0.5),
                        (-0.5, 0.5, 0.5),
                        (-0.5, 0.5, -0.5),
                        (-0.5, -0.5, -0.5),
                        (0.5, -0.5, -0.5),
                        (0.5, 0.5, -0.5),
                        (0.5, 0.5, 0.5),
                        (0.5, -0.5, 0.5)]

        self.triangles = [0, 2, 3, 0, 3, 1, 8, 4, 5,
                          8, 5, 9, 10, 6, 7, 10, 7, 11,
                          12, 13, 14, 12, 14, 15, 16, 17, 18,
                          16, 18, 19, 20, 21, 22, 20, 22, 23]

        self.uvs = [(0.0, 0.0),
                   (1.0, 0.0),
                   (0.0, 1.0),
                   (1.0, 1.0),
                   (0.0, 1.0),
                   (1.0, 1.0),
                   (0.0, 1.0),
                   (1.0, 1.0),
                   (0.0, 0.0),
                   (1.0, 0.0),
                   (0.0, 0.0),
                   (1.0, 0.0),
                   (0.0, 0.0),
                   (0.0, 1.0),
                   (1.0, 1.0),
                   (1.0, 0.0),
                   (0.0, 0.0),
                   (0.0, 1.0),
                   (1.0, 1.0),
                   (1.0, 0.0),
                   (0.0, 0.0),
                   (0.0, 1.0),
                   (1.0, 1.0),
                   (1.0, 0.0)]

        Mesh3D.draw_type = draw_type
        Mesh3D.texture = pygame.image.load(filename)
        Mesh3D.int_texture(self)
