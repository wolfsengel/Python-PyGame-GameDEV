import pygame
from pygame.locals import *

class Computer:
    x = [0]
    y = [0]
    pasos = 44
    direccion = 0
    longitud = 3
 
    updateCuentaMaxima = 2
    updateCuenta = 0
 
    def __init__(self, longitud):
       self.longitud = longitud
       for i in range(0,2000):
           self.x.append(-100)
           self.y.append(-100)
 
       # initial positions, no collision.
       self.x[0] = 1*44
       self.y[0] = 4*44
 
    def update(self):
 
        self.updateCuenta = self.updateCuenta + 1
        if self.updateCuenta and self.updateCuentaMaxima:
 
            # update previous positions
            for i in range(self.longitud-1,0,-1):
                self.x[i] = self.x[i-1]
                self.y[i] = self.y[i-1]
 
            # update position of head of snake
            if self.direccion == 0:
                self.x[0] = self.x[0] + self.pasos
            if self.direccion == 1:
                self.x[0] = self.x[0] - self.pasos
            if self.direccion == 2:
                self.y[0] = self.y[0] - self.pasos
            if self.direccion == 3:
                self.y[0] = self.y[0] + self.pasos
 
            self.updateCuenta = 0
 
 
    def moveRight(self):
        self.direccion = 0
 
    def moveLeft(self):
        self.direccion = 1
 
    def moveUp(self):
        self.direccion = 2
 
    def moveDown(self):
        self.direccion = 3 
 
    def draw(self, surface, image):
        for i in range(0,self.longitud):
            surface.blit(image,(self.x[i],self.y[i]))

    def on_loop(self):
        self.jugador.update()
        self.computadora.update()

    def on_render(self):
        self._display_surf.fill((0,0,0))
        self.jugador.draw(self._display_surf, self._image_surf)
        self.manzana.draw(self._display_surf, self._apple_surf)
        self.computadora.draw(self._display_surf, self._image_surf)
        pygame.display.flip()
def target(self, dx, dy):
    if self.x[0] > dx:
        self.moveLeft()
 
    if self.x[0] < dx:
        self.moveRight()
 
    if self.x[0] == dx:
        if self.y[0] < dy:
            self.moveDown()
 
        if self.y[0] > dy:
            self.moveUp()