import pygame
from Tile import *
from Interactions import tileIDs

silver = pygame.font.Font('Assets/Silver.ttf', 36)

class Inventory:
    
    def __init__(self):
        
        # inventory
        self.items = []
        self.color = (48, 164, 252)
        self.invRect = pygame.Rect(50, 50, 300, 450)
        
        # Visible Information
        self.itemNames = []
        self.itemQuantities = []
        
        # Logic
        self.page = 0
        self.selector = 0
        self.selectedItem = 0
        self.display = self.items[4*self.page: 4*self.page + 4]
        self.isOpen = False
        
        # Visual elements
        self.emptyTxt = silver.render('Empty', False, (0, 0, 0))
        self.pageNum = silver.render(f'{self.page + 1}', False, (0, 0, 0))
        
        # quantities of every possible item one can possess in a playthrough
        self.quantities = {
    
            #Grass
            1: 0,

            # Tree
            2: 0,

            # Border
            # ... Unobtainable

            # Stone
            4: 0,

            # Dirt
            5: 0,
            
            # Hole
            # ... Unobtainable
            
            # Shallow Water
            # ... Unobtainable
            
            # Deep Water
            # ... Unobtainable
            
            # Sand
            9: 0,
            
            # Clay
            10: 0,
            
            # Wood
            11: 0,
            
            # Wooden Spade
            12: 0,
            
            # Wooden Pickaxe
            13: 0,
            
            # Wooden Axe
            14: 0,
            
            # Stone Spade
            15: 0,
            
            # Stone Pickaxe
            16: 0,
            
            # Stone Axe
            17: 0

        }
        
        
    def draw(self, surf):
        
        # Held Item
        if self.selectedItem != 0:
            surf.blit(tileIDs(self.selectedItem).icon, (405, 405))
        
        # dont draw if it's closed
        if not self.isOpen:
            return
        
        # draw the inventory rectangle
        pygame.draw.rect(surf, self.color, self.invRect)
        
        if len(self.items) != 0:
            
            for y in range(len(self.display)):
            
                # Rectangle Background
                pygame.draw.rect(surf, (255, 255, 255), (75, y*100 + 75, 250, 50))
                
                # Item Icon
                surf.blit(tileIDs(self.display[y]).icon, (80, y*100 + 80))
                
                # Names
                surf.blit(self.itemNames[y], (135, y*100 + 85))
                
                # Quantities
                surf.blit(self.itemQuantities[y], (285, y*100 + 85))
            
            # Selector
            pygame.draw.rect(surf, (0, 0, 0), (75, self.selector*100 + 75, 250, 50), width=5)
            
            # Page Number
            surf.blit(self.pageNum, (325, 465))
            
        # The word 'Empty'
        else:
            surf.blit(self.emptyTxt, (175, 250))
        
    # refresh the visible elements
    def reload(self):
        
        self.display = self.items[4*self.page: 4*self.page + 4]
        self.itemNames = [silver.render(f'{tileIDs(itemID).name}', False, (0, 0, 0)) for itemID in self.display]
        self.itemQuantities = [silver.render(f'{self.quantities[itemID]}', False, (0, 0, 0)) for itemID in self.display]
        
    # add item to the inventory and/or quantites dictionary
    def addItem(self, blockID, quan):
        
        if self.quantities[blockID] == 0:
            self.items.append(blockID)
            
        self.quantities[blockID] += quan
        
        self.reload()
        
    # remove item from the inventory and/or from the quantities dictionary
    def removeItem(self, blockID, quan):
        
        self.quantities[blockID] -= quan
        
        if self.quantities[blockID] == 0:
            self.items.remove(blockID)
            self.selectedItem = 0
            self.scroll('up')
        self.reload()
        
    # open (or close) inventory
    def open(self):
        
        self.isOpen = not self.isOpen
        self.page = 0
        self.selector = 0
        self.pageNum = silver.render(f'{self.page + 1}', False, (0, 0, 0))
        self.reload()
        
    # scroll through the inventory, either up or down
    def scroll(self, direction):
        
        if direction == 'up' and not (self.page == 0 and self.selector == 0):
            
            self.selector -= 1
                
        elif direction == 'down' and self.page*4 + self.selector != len(self.items) - 1 and len(self.items) != 0:
            
            self.selector += 1
                
        # Change page if selector leaves bounds
        if self.selector == -1:
            
            self.selector = 3
            self.page -= 1
            self.pageNum = silver.render(f'{self.page + 1}', False, (0, 0, 0))
            self.reload()
            
        elif self.selector == 4:
            
            self.selector = 0
            self.page += 1
            self.pageNum = silver.render(f'{self.page + 1}', False, (0, 0, 0))
            self.reload()
                
        
    
    