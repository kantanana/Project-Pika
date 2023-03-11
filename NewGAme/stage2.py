import pygame

#   functions
def EmptyGrid(x,y):
    grid = []
    for i in range(y):
        grid.append([0]*x)
    return grid


#   Dataclasses
class Vector2:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __add__(self,other):
        return Vector2(self.x+other.x,self.y+other.y)
    def __sub__(self,other):
        return Vector2(self.x-other.x,self.y-other.y)


class Object:
    def __init__(self,position,size):
        self.pos = Vector2(position[0],position[1])
        self.size = Vector2(size[0],size[1])
        self.fillColor = (255,255,255)
        self.objectListIndex = 0
        self.active = True

    def CheckUp(self,collisionLayer):
        for i in range(self.pos.x,self.pos.x+self.size.x):
            if collisionLayer[self.pos.y-1][i]:
                return collisionLayer[self.pos.y+self.size.y][i]
        return 0

    def CheckDown(self,collisionLayer):
        for i in range(self.pos.x,self.pos.x+self.size.x):
            if collisionLayer[self.pos.y+self.size.y][i]:
                return collisionLayer[self.pos.y+self.size.y][i]
        return 0

    def CheckLeft(self,collisionLayer):
        for i in range(self.pos.y,self.pos.y+self.size.y):
            if collisionLayer[i][self.pos.x-1]:
                return collisionLayer[self.pos.y+self.size.y][i]
        return 0
    
    def CheckRight(self,collisionLayer):
        for i in range(self.pos.y,self.pos.y+self.size.y):
            if collisionLayer[i][self.pos.x+self.size.x]:
                return collisionLayer[self.pos.y+self.size.y][i]
        return 0

class PhysicsObj(Object):
    def __init__(self,position,size):
        super().__init__(position,size)
        self.Velocity = Vector2(0,0)
        self.dynamic = True
        self.contacts = []

        self.gravityActive = 0 #0 for off, 1 for on, -1 for system(do not use)
        self.gravity = 0

        self.bounce = 0
        self.friction = 0

class ComplexObj(PhysicsObj):
    def __init__(self,position,size):
        super().__init__(position,size)
        self.collider = EmptyGrid(size,size)
        self.sprite = ''

#Specific Variants
class Player(PhysicsObj):
    def __init__(self,position,size):
        super().__init__(position,size)



