import pygame
import numpy as np
import math

class Transform:
    def __init__(self, position=None, rotation=None, scale=None):
        self.position = position or pygame.Vector3(0, 0, 0)
        self.rotation = rotation or pygame.Vector3(0, 0, 0)
        self.scale = scale or pygame.Vector3(1, 1, 1)

    def move(self, x, y, z):
        """
        Moves the object by the given offsets.
        """
        self.position += pygame.Vector3(x, y, z)

    def rotate(self, x, y, z):
        """
        Rotates the object by the given angles (in degrees) on each axis.
        """
        self.rotation += pygame.Vector3(x, y, z)