import pygame
""" class player:
    def __init__(self,hp):
        self.hp = hp
    def enemy_touch(self,dist):
        if dist <63:
            self.hp -= 1 """
class Unit():
    def __init__(self):
        self.last = pygame.time.get_ticks()
        self.cooldown = 3

    def fire(self):
        # fire gun, only if cooldown has been 0.3 seconds since last
        now = pygame.time.get_ticks()
        if now - self.last >= self.cooldown:
            self.last = now
            print("Hello World")
            
            
Unit().fire()