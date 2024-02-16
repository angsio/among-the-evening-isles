import pygame
from Tile import *
from Interactions import tileIDs

silver = pygame.font.Font('Assets/Silver.ttf', 36)

silverSmall = pygame.font.Font('Assets/Silver.ttf', 24)

class Crafting:
    def __init__(self):
        self.craftingRect = pygame.Rect(450, 50, 350, 450)
        self.color = (48, 164, 252)
        self.isOpen = False
        
        self.selector = 0
        self.page = 0
        self.display = []
        
        self.recipeNames = []
        self.pageNum = silver.render(f'{self.page + 1}', False, (0, 0, 0))
        
        # Key: Recipe #
        # Value: (Name, ((Req 1, Quan 1), (Req 2, Quan 2), ...), (Crafted Item, Quantity))
        self.recipes = {
            
            0: (
                    # Name
                    'Wood x2',
                
                # Requirements:
                [
                    # Need 4 tree
                    (2, 1)
                ],
                    # Give 3 wood
                    (11, 2)
            ),
            
            1: (
                    # Name
                    'Wood Shovel',
                
                # Requirements:
                [
                    # 10 Wood
                    (11, 10)
                ],
                
                    # Give 1 wood shovel
                    (12, 1)
            ),
            
            2: (
                    
                    # Name
                    'Wood Pick',
                    
                # Requirements
                [
                    # 12 Wood
                    (11, 12)  
                ],      
                    # Give 1 wood pickaxe
                    (13, 1)
            ),
            
            3: (
                    # Name
                    'Wood Axe',
                    
                # Requirements
                [    
                    # 10 Wood
                    (11, 10)
                ],
                    # Give 1 wood pickaxe
                    (14, 1)
                
                
            ),
            
            4: (
                    # Name
                    'Stone Shovel',
                    
                # Requirements
                [
                    # 6 Wood
                    (11, 6),
                    # 10 Stone
                    (4, 10)  
                ],  
                    # Give 1 wood pickaxe
                    (15, 1)
            ),
            
            5: (
                    # Name
                    'Stone Pick',
                    
                # Requirements
                [
                    # 6 Wood
                    (11, 6),
                    # 10 Stone
                    (4, 10)
                ],
                    # Give 1 stone pickaxe
                    (16, 1)
            ),
            
            6: (
                    # Name
                    'Stone Axe',
                    
                # Requirements
                [
                    
                    # 6 Wood
                    (11, 6),
                    # 10 Stone
                    (4, 10)
                    
                    
                ],
                    # Give 1 stone pickaxe
                    (17, 1)
            )
        }
        
        # Requirements visible element
        self.reqDisplay = pygame.Surface((125, 350))
        self.reqDisplay.set_colorkey((0, 0, 0))
        
        self.reload()
    
    # check if player meets requirements, process craft if they do
    def craft(self, inventory):
        
        selRecipe = self.recipes[self.page*4 + self.selector]
        
        for requirement in selRecipe[1]:
            
            if inventory.quantities[requirement[0]] < requirement[1]:
                return
        
        for requirement in selRecipe[1]:
            inventory.removeItem(requirement[0], requirement[1])
            
        inventory.addItem(selRecipe[2][0], selRecipe[2][1])
    
    # draw the menu
    def draw(self, surf):
        
        if not self.isOpen:
            return
        
        # Blue menu outline
        pygame.draw.rect(surf, self.color, self.craftingRect)
        
        # For each recipe on the current page
        for y in range(len(self.display)):
            
            # Draw the recipe rectangle
            pygame.draw.rect(surf, (255, 255, 255), (475, y*100 + 75, 200, 50))
            
            # The item to craft
            surf.blit(tileIDs(self.display[y][2][0]).icon, (480, y*100 + 80))
            
            # Names of the recipes
            surf.blit(self.recipeNames[y], (530, y*100 + 85))
        
        # Page num
        surf.blit(self.pageNum, (775, 465))
        
        # Selector
        pygame.draw.rect(surf, (0, 0, 0), (475, self.selector*100 + 75, 200, 50), width=5)
        
        # Requirement Display
        surf.blit(self.reqDisplay, (680, 80))
        
    # refresh elements
    def reload(self):
        
        # set display
        self.display.clear()
        for i in range(4):
            if self.recipes.get(self.page*4 + i) != None:
                
                # append a tuple containing the recipe number, the crafted item in tile form, and the name of the recipe
                self.display.append( self.recipes[self.page*4 + i] )
                
        self.recipeNames = [silver.render(self.display[i][0], False, (0, 0, 0)) for i in range(len(self.display))]
        self.pageNum = silver.render(f'{self.page + 1}', False, (0, 0, 0))
        
    # separately update the visible element of resource requirements
    def updateReqs(self, inventory):
        
        self.reqDisplay.fill((0, 0, 0))
        requirementTxts = [silver.render(f'{tileIDs(requirement[0]).name} {inventory.quantities[requirement[0]]}/{requirement[1]}', False, (0, 0, 1)) for requirement in self.display[self.selector][1]]
        
        for y in range(len(requirementTxts)):
            self.reqDisplay.blit(requirementTxts[y], (0, y*75))
    
    # open (or close) menu
    def open(self):
        
        self.isOpen = not self.isOpen
        self.selector = 0
        self.page = 0
        self.reload()
        
    # scroll through the menu
    def scroll(self, direction):
        
        if direction == 'up' and not (self.page == 0 and self.selector == 0):
            
            self.selector -= 1
                
        elif direction == 'down' and self.page*4 + self.selector != len(self.recipes) - 1:
            
            self.selector += 1
                
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
        
        
        
    