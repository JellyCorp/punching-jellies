import pygame

class Player:

    def __init__(self, pos, front):
        self.hit_points = 100
        self.stamina = 10
        self.pos = pos
        self.history = []
        self.front = front
