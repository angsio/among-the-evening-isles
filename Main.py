#-----------------------------------------------------------------------------
# Name:        Assignment Template (assignment.py)
# Purpose:
# This project will be a game developed using the pygame library.
# It will consist of a player traversing an open 2-dimensional world,
# aiming to survive by eating, drinking, and avoiding damage from enemies.
# The player will discover different levels of elevation within the world
# as they delve into caves to gain more items while facing more dangerous
# enemies. Eventually, the player can find a boss somewhere in the game
# and defeat them to win.
# 
#
# Author:      Mr. Brooks
# Created:     15-May-2023
# Updated:     6-June-2023
#-----------------------------------------------------------------------------
#I think this project deserves a level 4+ because ...
#
#Features Added:
#   Perlin Noise Map Generator
#   World Bounds
#   Player Movement
#   Tile Collision
#   Easily Extendable Code
#   Start Screen
#      Info Screen
#      Saves Screen
#   Saving and Loading System:
#      Seed
#      Manipulations
#      Inventory
#      Player Coordinates
#   Inventory System
#      Item Storage
#      Item Quantities
#      Selecting items
#   Crafting System
#      Requirements
#      Item Crafting
#   World Interactions:
#      Breaking Tiles
#      Placing Tiles
#      Realistic Interactions
#         Ex: Cannot get stone with hands, but can use a pickaxe
#   Appealing Visuals:
#      Inventory Icons
#      World Tile Images
#   
#-----------------------------------------------------------------------------

# https://pypi.org/project/perlin-noise/
# https://cupnooble.itch.io/sprout-lands-asset-pack
# tool icons credit to @EyEyMoses
# other icons credit at https://github.com/ThePotatoKing55/2D-block-texture-pack

from NoiseMap import NoiseMap
from StartScreen import StartScreen
from Player import Player
from Inventory import Inventory
from Crafting import Crafting
from Tile import *
from Interactions import *

import pygame
import ast

pygame.init()

running = True

surfaceSizeX = 850
surfaceSizeY = 850
state = 0

clock = pygame.time.Clock()
mainSurface = pygame.display.set_mode((surfaceSizeX, surfaceSizeY))

frame = 0

newMap = NoiseMap(50, 50, 5)
player = Player(newMap)
inventory = Inventory()
startScreen = StartScreen()
crafting = Crafting()

silver = pygame.font.Font('Assets/Silver.ttf', 72)
loadingTxt = silver.render('Loading...', False, (0, 0, 0))

def gameMove():
    keys = pygame.key.get_pressed()

    if keys[pygame.K_w]:
        player.move(newMap, 'up')
                
    elif keys[pygame.K_s]:
        player.move(newMap, 'down')
                
    if keys[pygame.K_d]:
        player.move(newMap, 'right')
                
    elif keys[pygame.K_a]:
        player.move(newMap, 'left')
        
    player.crossCalc()

# def tileOps():

def saveGame():
    
    with open(f'Saves/save{startScreen.saveLoad}.txt', 'w') as file:
        
        file.write(str(player.coords))
        file.write('\n\n')
        
        file.write(str(newMap.seed))
        file.write('\n\n')
        
        file.write(str(newMap.manips))
        file.write('\n\n')
            
        file.write(str(inventory.items))
        file.write('\n\n')
        
        file.write(str(inventory.quantities))
        file.write('\n\n')
        
def loadGame():
    
    # LOAD GAME HERE
    with open(f'Saves/save{startScreen.saveLoad}.txt', 'r') as file:
        
        coordsList = file.readline()
        coordsList = coordsList[1:-2].split(', ')
        coordsList[0], coordsList[1] = int(coordsList[0]), int(coordsList[1])
        player.coords = coordsList
        
        file.readline()
        
        newMap.__init__(300, 300, 15, int(file.readline()))
        
        file.readline()
        
        newMap.manips = ast.literal_eval(file.readline()[:-1])
        for coords in newMap.manips:
            newMap.nMap[coords[1]][coords[0]] = tileIDs(newMap.manips[coords])
        
        file.readline()
        
        itemsList = file.readline()[1:-2].split(', ')
        inventory.items = [int(item) for item in itemsList if item != '']
        
        file.readline()
        
        inventory.quantities = ast.literal_eval(file.readline())
        
        newMap.updateDisplay(player.coords)
        inventory.reload()

# STATES MEANINGS
# 0 = Start Screen
# 1 = Creation of a New World
# 2 = Loading of an old world
# 3 = The Game
# 4 = Saving of a world

while running:

    events = pygame.event.get()

    # START SCREEN
    if state == 0:
        
        startScreen.draw(mainSurface)
        
        for event in events:
            
            # if the event is not a click, we are not interested.
            if event.type != pygame.MOUSEBUTTONDOWN:
                continue
                
            # checks for button clicks possibly changes the state depending what button was clicked
            for button in startScreen.buttons[startScreen.state][0]:
                if button.collidepoint(pygame.mouse.get_pos()):
                    state = startScreen.click(state, button)
                    
    # CREATE NEW WORLD
    elif state == 1:
        
        # loading text
        mainSurface.fill((255, 255, 255))
        mainSurface.blit(loadingTxt, (325, 415))
        pygame.display.flip()
        
        # create world objects
        newMap = NoiseMap(300, 300, 15)
        player = Player(newMap)
        inventory = Inventory()
        
        for i in range(1, 4):
            
            with open(f'Saves/save{i}.txt', 'r') as testFile:
                
                if testFile.readline() == '':
                    
                    startScreen.saveLoad = i
                    break
                
            startScreen.saveLoad = 0
            
        if startScreen.saveLoad != 0:
            
            saveGame()
            newMap.updateDisplay(player.coords)
            state = 3
            
        else:
            
            print('all save files full.')
            state = 0
        
    elif state == 2:
        
        mainSurface.fill((255, 255, 255))
        mainSurface.blit(loadingTxt, (325, 415))
        pygame.display.flip()
        
        loadGame()
            
        state = 3            

    # GAME
    elif state == 3:

        # Handle controls
        for event in events:
            
            if event.type == pygame.QUIT:
                running = False
                
            elif event.type == pygame.KEYDOWN:
                
                # Inventory opening
                if event.key == pygame.K_TAB:
                    inventory.open()
                    if inventory.isOpen:
                        crafting.isOpen = False
                    
                # Crafting menu opening
                elif event.key == pygame.K_c:
                    crafting.open()
                    crafting.updateReqs(inventory)
                    if crafting.isOpen:
                        inventory.isOpen = False
                    
                # Saving
                elif event.key == pygame.K_p:
                    state = 4
                    
                # Deselecting item
                elif event.key == pygame.K_ESCAPE:
                    inventory.selectedItem = 0
                    
                # Selecting/Crafting item
                elif event.key == pygame.K_SPACE:
                    
                    if inventory.isOpen and len(inventory.items) != 0:
                        inventory.selectedItem = inventory.display[inventory.selector]
                    
                    elif crafting.isOpen:
                        crafting.craft(inventory)
                        crafting.updateReqs(inventory)
                
                # Remove item from inventory if player chooses to do so
                elif event.key == pygame.K_q:
                    
                    if inventory.isOpen and len(inventory.items) != 0:
                        inventory.removeItem(inventory.display[inventory.selector], 1)
                    
            # Placing/Destroying tiles
            elif event.type == pygame.MOUSEBUTTONDOWN:
                
                if pygame.mouse.get_pressed()[0]:
                    newMap.destroy(player, inventory)
                    
                elif pygame.mouse.get_pressed()[2]:
                    newMap.placeTile(player, inventory)
                    
                crafting.updateReqs(inventory)
                
            # Scrolling through menus
            elif event.type == pygame.MOUSEWHEEL:
                
                if event.y > 0:
                    
                    if inventory.isOpen:
                        inventory.scroll('up')
                        
                    elif crafting.isOpen:
                        crafting.scroll('up')
                        crafting.updateReqs(inventory)
                        
                elif event.y < 0:
                    
                    if inventory.isOpen:
                        inventory.scroll('down')

                    elif crafting.isOpen:
                        crafting.scroll('down')
                        crafting.updateReqs(inventory)
            
            # update crosshair coords again
            elif event.type == pygame.MOUSEMOTION:
                
                player.crossCalc()
        
        # movement
        if frame % 8 == 0:
            gameMove()

        # drawing everything
        newMap.draw(mainSurface)
        player.draw(mainSurface)
        inventory.draw(mainSurface)
        crafting.draw(mainSurface)
        newMap.drawDamage(mainSurface)
        
        frame += 1
        
        if frame == 60:
            frame = 0
            
    # saving
    elif state == 4:
        
        saveGame()
        state = 3
        
    else:
        running = False
        
    pygame.display.flip()
                
    clock.tick(60)
    
pygame.quit()