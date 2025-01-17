import pygame.image
from Mesh3D import *

class Cube(Mesh3D):
    def __init__(self):

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

        self.traingles = [0, 2, 3, 0, 3, 1, 8, 4, 5,
                          8, 5, 9, 10, 6, 7, 10, 7, 11,
                          12, 13, 14, 12, 14, 15, 16, 17, 18,
                          16, 18, 19, 20, 21, 22, 20, 22, 23]

