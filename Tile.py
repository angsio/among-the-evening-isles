import random
import pygame

itemIcons1 = pygame.image.load('Assets/Game/GameIcons1.png')
itemIcons1.set_colorkey((51, 48, 61))

class Tile:
    def __init__(self, passable, placeable, breakable, tileID, color, name, health):
        
        # set passed variables
        self.passable = passable
        self.placeable = placeable
        self.breakable = breakable
        self.tileID = tileID
        self.color = color
        self.name = name
        self.health = health
        
        # Icon for when in inventory
        self.icon = pygame.Surface((60, 60))
        self.icon.set_colorkey((0, 0, 0))
        
        # texture when shown in world
        self.tileSurf = pygame.Surface((16, 16))
        self.tileSurf.set_colorkey((0, 0, 0))

# all the following classes are children of the Tile parent class

class Empty(Tile):
    def __init__(self):
        super().__init__(False, False, False, 0, (0, 0, 0), 'The Hand', 10000)
        
class Grass(Tile):
    def __init__(self): 
        super().__init__(True, True, True, 1,  (42, 232, 73), 'Grass', 30)
        
        self.icon = pygame.image.load('Assets/Game/MoreIcons/grass.png')
        self.icon = pygame.transform.scale(self.icon, (40, 40))
        
        self.tileSurf.blit(pygame.image.load('Assets/Game/Tiles/Grass.png'), (0, 0), area=(random.randint(0, 2)*16, random.randint(5, 6)*16, 16, 16))
        self.tileSurf = pygame.transform.scale(self.tileSurf, (50, 50))
        
class Tree(Tile):
    def __init__(self):
        super().__init__(False, True, True, 2, (192, 212, 112), 'Tree', 60)
        
        self.icon = pygame.image.load('Assets/Game/MoreIcons/tree.png')
        self.icon = pygame.transform.scale(self.icon, (40, 40))
        
        tree = pygame.transform.scale(pygame.image.load('Assets/Game/Tiles/Tree.png'), (16, 16))
        tree.set_colorkey((255, 255, 255))
        self.tileSurf.blit(tree, (0, 0))
        self.tileSurf = pygame.transform.scale(self.tileSurf, (50, 50))

        
class Border(Tile):
    def __init__(self):
        super().__init__(False, False, False, 3, (52, 60, 66), 'Border', 1000)
        
        
class Stone(Tile):
    def __init__(self):
        super().__init__(False, True, True, 4, (134, 147, 158), 'Stone', 100)

        self.icon = pygame.image.load('Assets/Game/MoreIcons/stone.png')
        
        self.icon = pygame.transform.scale(self.icon, (40, 40))

        
class Dirt(Tile):
    def __init__(self):
        super().__init__(True, True, True, 5, (112, 50, 28), 'Dirt', 30)
        
        self.icon = pygame.image.load('Assets/Game/MoreIcons/dirt.png')
        self.icon = pygame.transform.scale(self.icon, (40, 40))
        
        self.tileSurf.blit(pygame.image.load('Assets/Game/Tiles/Dirt.png'), (0, 0), area=(random.randint(0, 2)*16, random.randint(0, 1)*16, 16, 16))
        self.tileSurf = pygame.transform.scale(self.tileSurf, (50, 50))
        
    def regenGrass(self):
        
        regenRoll = random.randint(1, 1000)
        if regenRoll == 1:
            return True
        else:
            return False
        
class Hole(Tile):
    def __init__(self):
        super().__init__(False, False, False, 6, (84, 76, 75), 'Hole', 1000)
        
class ShallowWater(Tile):
    def __init__(self):
        super().__init__(True, False, True, 7, (16, 171, 227), 'S-Water', 25)
        
        self.tileSurf.blit(pygame.image.load('Assets/Game/Tiles/SWater.png'), (0, 0), area=(random.randint(0, 3)*16, 0, 16, 16))
        self.tileSurf = pygame.transform.scale(self.tileSurf, (50, 50))
        
class DeepWater(Tile):
    def __init__(self):
        super().__init__(False, False, False, 8, (9, 92, 217), 'D-Water', 1000)
        
        self.tileSurf.blit(pygame.image.load('Assets/Game/Tiles/DWater.png'), (0, 0), area=(random.randint(0, 3)*16, 0, 16, 16))
        self.tileSurf = pygame.transform.scale(self.tileSurf, (50, 50))
        
class Sand(Tile):
    def __init__(self):
        super().__init__(True, True, True, 9, (248, 250, 165), 'Sand', 30)
        
        self.icon = pygame.image.load('Assets/Game/MoreIcons/sand.png')
        self.icon = pygame.transform.scale(self.icon, (40, 40))
        
class Clay(Tile):
    def __init__(self):
        super().__init__(False, True, True, 10, (149, 180, 184), 'Clay', 35)
        
        self.icon = pygame.image.load('Assets/Game/MoreIcons/clay.png')
        self.icon = pygame.transform.scale(self.icon, (40, 40))
        
# ITEMS

class Wood(Tile):
    def __init__(self):
        super().__init__(False, True, True, 11, (214, 181, 15), 'Wood', 55)
        
        self.icon = pygame.image.load('Assets/Game/MoreIcons/wood.png')
        self.icon = pygame.transform.scale(self.icon, (40, 40))
        
class WoodSpade(Tile):
    def __init__(self):
        super().__init__(False, False, False, 12, (237, 224, 36), 'Wood Shovel', 1)
        
        self.icon.blit(itemIcons1, (0, 0), area=(546, 418, 57, 58))
        self.icon = pygame.transform.scale(self.icon, (40, 40))
        
class WoodPick(Tile):
    def __init__(self):
        super().__init__(False, False, False, 13, (237, 224, 36), 'Wood Pick', 1)
        
        self.icon.blit(itemIcons1, (0, 0), area=(427, 418, 53, 58))
        self.icon = pygame.transform.scale(self.icon, (40, 40))
        
class WoodAxe(Tile):
    def __init__(self):
        super().__init__(False, False, False, 14, (237, 224, 36), 'Wood Axe', 1)
        
        self.icon.blit(itemIcons1, (0, 0), area=(487, 418, 53, 58))
        self.icon = pygame.transform.scale(self.icon, (40, 40))
        
class StoneSpade(Tile):
    def __init__(self):
        super().__init__(False, False, False, 15, (237, 224, 36), 'Stone Shovel', 1)
        
        self.icon.blit(itemIcons1, (0, 0), area=(546, 478, 58, 58))
        self.icon = pygame.transform.scale(self.icon, (40, 40))
        
class StonePick(Tile):
    def __init__(self):
        super().__init__(False, False, False, 16, (237, 224, 36), 'Stone Pick', 1)
        
        self.icon.blit(itemIcons1, (0, 0), area=(427, 478, 58, 58))
        self.icon = pygame.transform.scale(self.icon, (40, 40))
        
class StoneAxe(Tile):
    def __init__(self):
        super().__init__(False, False, False, 17, (237, 224, 36), 'Stone Axe', 1)
        
        self.icon.blit(itemIcons1, (0, 0), area=(487, 478, 58, 58))
        self.icon = pygame.transform.scale(self.icon, (40, 40))
        
