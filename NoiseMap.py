from perlin_noise import PerlinNoise

from Tile import *
from Interactions import *

import random
import pygame

pygame.init()

silver = pygame.font.Font('Assets/Silver.ttf', 36)

class NoiseMap:
    
    def __init__(self, sizeX, sizeY, octs, seed = random.randint(0, 999999)):
        
        self.seed = seed
        
        
        # take noise values and make them tiles
        def sort(i, j, x, y):
    
            n = self.noise([j/x, i/y])
            
            if n < -0.3:
                return DeepWater() # 0.2 opening
            
            elif n < -0.12:
                return ShallowWater() # 0.18 opening
            
            elif n < -0.05:
                return Sand() # 0.07 opening
            
            elif n < 0.21:
                return Grass() # 0.26 opening
            
            elif n < 0.28:
                return Tree() # 0.07 opening
            
            else:
                return Stone() # 0.22 opening

        # Logic
        self.sizeX, self.sizeY = sizeX, sizeY
        self.noise = PerlinNoise(octaves=octs, seed = self.seed)
        self.nMap = [[sort(i, j, sizeX, sizeY) for j in range(sizeX)] for i in range(sizeY)]
        self.manips = {}
        
        self.surface = pygame.Surface((850, 850))
        self.damageDisplayFrames = 0
        self.damage = 0
        self.damageTxtPos = (0, 0)
        
        # create world borders
        for y in range(8):
            
            for x in range(len(self.nMap[y])):
                
                self.nMap[y][x] = Border()
                self.nMap[y + self.sizeY - 8][x] = Border()
                
        for y in range(8, self.sizeY - 8):
            
            for x in range(8):
                
                self.nMap[y][x] = Border()
                self.nMap[y][x + self.sizeX - 8] = Border()
    
    # draw
    def draw(self, surf):
        
        surf.blit(self.surface, (0, 0))
        
    # damage/destroy tile in world
    def destroy(self, player, inventory):
        
        # The block the crosshair lies on
        selBlock = self.nMap[player.crossCoords[1]][player.crossCoords[0]]
        
        # Player cannot destroy the tile they stand on.
        if player.crossCoords == player.coords:
            return
        
        # Don't even bother doing calculations if the block is not breakable
        if not selBlock.breakable:
            return
        
        # Determine the value of the held item
        heldItem = inventory.selectedItem
        
        # get the information of the interaction from dict, if not found, use the default interaction for that block.
        interaction = breaks.get((selBlock.tileID, heldItem), breaks[(selBlock.tileID, 0)])
        
        # determine damage to do to block
        self.damage = random.randint(interaction[2][0], interaction[2][1])
        
        # do damage to the block
        self.nMap[player.crossCoords[1]][player.crossCoords[0]].health -= self.damage
        
        # if the block's health is 0 or below...
        if self.nMap[player.crossCoords[1]][player.crossCoords[0]].health <= 0:
            
            # give player proper item unless no drop is specified
            if interaction[1] != None:
                inventory.addItem(interaction[1], 1)
                
            # replace block in world and update the screen
            self.nMap[player.crossCoords[1]][player.crossCoords[0]] = tileIDs(interaction[0])
            
            # update map
            self.updateDisplay(player.coords)
            
            # add the break to the list of manipulations
            self.manips[tuple(player.crossCoords)] = interaction[0]
            
        # display damage
        self.damageDisplayFrames = 20
        self.damageTxtPos = (random.randint(player.crosshair.left, player.crosshair.right - 10), random.randint(player.crosshair.top, player.crosshair.bottom - 10))

    # Calculations for placing a tile
    def placeTile(self, player, inventory):
        
        # The block the crosshair lies on
        selBlock = self.nMap[player.crossCoords[1]][player.crossCoords[0]]
        
        # Player cannot place on their own tile
        if player.crossCoords == player.coords:
            return
        
        # Determine the value of the held item, if not holding anything then stop the function.
        if inventory.selectedItem != 0:
            heldItem = inventory.selectedItem
        else:
            return
        
        # Don't bother if the item is not placeable
        if not tileIDs(heldItem).placeable:
            return
        
        replacement = places.get((heldItem, selBlock.tileID))
        
        # if not found, it was not meant to be
        if replacement == None:
            return

        # remove the item from inventory
        inventory.removeItem(heldItem, 1)
        
        # change the block in the world
        self.nMap[player.crossCoords[1]][player.crossCoords[0]] = tileIDs(replacement)
        
        #update map
        self.updateDisplay(player.coords)
        
        self.manips[tuple(player.crossCoords)] = heldItem
        

    # draw damage
    def drawDamage(self, surf):
        
        if self.damageDisplayFrames != 0:
            damageTxt = silver.render(f'{self.damage}', False, (0, 0, 0))
            surf.blit(damageTxt, self.damageTxtPos)
            self.damageDisplayFrames -= 1
        
    
    # redraw the map
    def updateDisplay(self, coords):
            
        for y in range(17):
            
            for x in range(17):
                
                pygame.draw.rect(self.surface, self.nMap[coords[1] - 8 + y][coords[0] - 8 + x].color, (x*50, y*50, 50, 50))
                self.surface.blit(self.nMap[coords[1] - 8 + y][coords[0] - 8 + x].tileSurf, (x*50, y*50))