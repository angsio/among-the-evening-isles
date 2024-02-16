import pygame

from Tile import *


# from Interactions import Places

class Player:
    
    def __init__(self, nMap):
        
        # coords and hitbox rect
        self.coords = [int(nMap.sizeX / 2) - 1, int(nMap.sizeY / 2) - 1]
        self.hitbox = pygame.Rect(400, 400, 50, 50)
        
        # crosshair
        self.crossOrient = [1, 0]
        self.crosshair = pygame.Rect(400 + self.crossOrient[0]*50, 400 + self.crossOrient[1]*50, 50, 50)
        self.crossCoords = [self.coords[0] + self.crossOrient[0], self.coords[1] - self.coords[1]]
        
    # movement function that matches the inputted direction and updates coordinates dutifully
    def move(self, nMap, direction):
        
        match direction:
            
            case 'right':
                
                if nMap.nMap[self.coords[1]][self.coords[0] + 1].passable:
                    
                    self.coords[0] += 1
            
            case 'left':
                
                if nMap.nMap[self.coords[1]][self.coords[0] - 1].passable:
                    self.coords[0] -= 1
                
            case 'up':
                
                if nMap.nMap[self.coords[1] - 1][self.coords[0]].passable:
                    self.coords[1] -= 1
                
            case 'down':
                
                if nMap.nMap[self.coords[1] + 1][self.coords[0]].passable:
                    self.coords[1] += 1
                
        nMap.updateDisplay(self.coords)
                
    # draw player and crosshair
    def draw(self, surf):
        
        pygame.draw.rect(surf, (0, 0, 150), self.hitbox)
        pygame.draw.rect(surf, (200, 20, 20), self.crosshair, width=5)
        
    # Calculate crosshair position based on mouse position
    def crossCalc(self):
        
        mosPos = pygame.mouse.get_pos()       
        mosPos = (mosPos[0] - 425, abs(mosPos[1] - 850) - 425)
        
        
        if (abs(mosPos[0]) + 25) // 50 < 3:
        
            self.crossOrient[0] = ((mosPos[0]+25) // 50)
        
        else:
            self.crossOrient[0] = 3 * (mosPos[0]//abs(mosPos[0]))
        
        
        if (abs(mosPos[1]) + 25) // 50 < 3:
            
            self.crossOrient[1] = ((mosPos[1]+25) // 50)
            
        else:
            self.crossOrient[1] = 3 * (mosPos[1]//abs(mosPos[1]))
            
            
        self.crosshair.left = 400 + self.crossOrient[0]*50
        self.crosshair.top = 400 - self.crossOrient[1]*50
        
        self.crossCoords = [self.coords[0] + self.crossOrient[0], self.coords[1] - self.crossOrient[1]]