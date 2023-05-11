from pygame.locals import *
import pygame
 
class Jugador:
    x = [0]
    y = [0]
    pasos = 44
    direccion = 0
    longitud = 3
 
    updateCuentaMax = 2
    updateCuenta = 0
 
    def __init__(self, longitud):
       self.longitud = longitud
       for i in range(0,2000):
           self.x.append(-100)
           self.y.append(-100)
 
       # posicion inicial sin colisiones
       self.x[1] = 1*44
       self.x[2] = 2*44
 
    def update(self):
 
        self.updateCuenta = self.updateCuenta + 1
        if self.updateCuenta > self.updateCuentaMax:
 
            # actualiza posiciones anteriores
            for i in range(self.longitud-1,0,-1):
                self.x[i] = self.x[i-1]
                self.y[i] = self.y[i-1]
 
            # actualiza la posicion de la cabeza de la serpiente
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