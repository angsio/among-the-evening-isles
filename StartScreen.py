import pygame

silver = pygame.font.Font('Assets/Silver.ttf', 48)
philosopher = pygame.font.Font('Assets/Philosopher.ttf', 72)
philoSmall = pygame.font.Font('Assets/Philosopher.ttf', 24)

background = pygame.transform.scale(pygame.image.load('Assets/StartScreen/Background.png'), (1200, 850))

class StartScreen:
    
    def __init__(self):
        
        self.buttons = (
            
            # MAIN
            (
                (
                    # BUTTON RECTS
                    pygame.Rect(300, 350, 250, 50), # New World
                    pygame.Rect(300, 450, 250, 50), # Saves
                    pygame.Rect(300, 550, 250, 50), # Info
                    pygame.Rect(300, 650, 250, 50)  # Quit
                ),
                
                (
                    # BUTTON TEXT
                    (silver.render('NEW WORLD', False, (0, 0, 0)), (310, 355)),
                    (silver.render('SAVES', False, (0, 0, 0)), (310, 455)),
                    (silver.render('INFO', False, (0, 0, 0)), (310, 555)),
                    (silver.render('QUIT', False, (0, 0, 0)), (310, 655)),
                    
                    # TITLE
                    (philoSmall.render('Among the', False, (213, 14, 235)), (240, 185)),
                    (philosopher.render('Evening Isles', False, (213, 14, 235)), (225, 205)),
                    
                    # ICONS
                    (pygame.transform.scale(pygame.image.load('Assets/StartScreen/Backpack.png'), (40, 40)), (505, 353)),
                    (pygame.transform.scale(pygame.image.load('Assets/StartScreen/Save.png'), (40, 40)), (506, 455)),
                    (pygame.transform.scale(pygame.image.load('Assets/StartScreen/Info.png'), (40, 40)), (506, 555)),
                    (pygame.transform.scale(pygame.image.load('Assets/StartScreen/Exit.png'), (40, 40)), (508, 656))
                    
                )
            ),
            
            # SAVES
            (
                (
                    # Save Buttons
                    pygame.Rect(300, 350, 200, 50), # Save 1
                    pygame.Rect(300, 450, 200, 50), # Save 2
                    pygame.Rect(300, 550, 200, 50), # Save 3
                
                    pygame.Rect(25, 775, 150, 50),  # BACK
                    
                    # Del Save Buttons
                    pygame.Rect(505, 350, 50, 50),  # Del Save 1
                    pygame.Rect(505, 450, 50, 50),  # Del Save 2
                    pygame.Rect(505, 550, 50, 50)   # Del Save 3
                    
                    
                ),
                
                (
                    # BUTTON TEXT
                    (silver.render('SAVE 1', False, (0, 0, 0)), (365, 355)),
                    (silver.render('SAVE 2', False, (0, 0, 0)), (365, 455)),
                    (silver.render('SAVE 3', False, (0, 0, 0)), (365, 555)),
                    (silver.render('BACK', False, (0, 0, 0)), (35, 780)),
                    
                    # ICONS
                    (pygame.transform.scale(pygame.image.load('Assets/StartScreen/Trashbin.png'), (40, 40)), (510, 353)),
                    (pygame.transform.scale(pygame.image.load('Assets/StartScreen/Trashbin.png'), (40, 40)), (510, 453)),
                    (pygame.transform.scale(pygame.image.load('Assets/StartScreen/Trashbin.png'), (40, 40)), (510, 553)),
                    (pygame.transform.scale(pygame.image.load('Assets/StartScreen/Restart.png'), (40, 40)), (130, 780)),
                ),
                
            ),
            
            # INFO SCREEN
            (
                (
                    pygame.Rect(25, 775, 150, 50),  # BACK
                    pygame.Rect(100, 100, 650, 585) # INFO BOX
                    
                ),
                
                (
                    # INFO
                    (silver.render('BACK', False, (0, 0, 0)), (35, 780)),
                    (philoSmall.render('LEFT CLICK on blocks to damage them and eventually', False, (0, 0, 0)), (105, 105)),
                    (philoSmall.render('break them. If it seems you aren\'t doing enough damage,', False, (0, 0, 0)), (105, 130)),
                    (philoSmall.render('press C to see what you need to make some rough tools.', False, (0, 0, 0)), (105, 155)),
                    
                    (philoSmall.render('Open your inventory with TAB and SCROLL through', False, (0, 0, 0)), (105, 205)),
                    (philoSmall.render('your items. Press Q to delete unwanted possessions.', False, (0, 0, 0)), (105, 230)),
                    (philoSmall.render('Press SPACE to select an item in your inventory, or to try', False, (0, 0, 0)), (105, 255)),
                    (philoSmall.render('making it in the crafting menu.', False, (0, 0, 0)), (105, 280)),
                    
                    (philoSmall.render('RIGHT CLICK in the world to place a selected block.', False, (0, 0, 0)), (105, 330)),
                    (philoSmall.render('Note that some things cannot be placed on others, and some', False, (0, 0, 0)), (105, 355)),
                    (philoSmall.render('things cannot be placed at all.', False, (0, 0, 0)), (105, 380)),
                    (philoSmall.render('Pressing ESCAPE also deselects an item.', False, (0, 0, 0)), (105, 405)),
                    
                    (philoSmall.render('Press P to save the game at any point. The save will be in', False, (0, 0, 0)), (105, 455)),
                    (philoSmall.render('the lowest open numbered save. Press the X in the window', False, (0, 0, 0)), (105, 480)),
                    (philoSmall.render('to quit at any time.', False, (0, 0, 0)), (105, 505)),
                    
                    (philoSmall.render('Enjoy your walk Among the Evening Isles...', False, (0, 0, 0)), (105, 555)),
                    
                    (philoSmall.render('DISCLAIMER: This game is NOT completed by the deadline,', False, (150, 0, 0)), (105, 630)),
                    (philoSmall.render('but it certainly carries potential...', False, (150, 0, 0)), (105, 655)),
                    
                    
                    # ICON
                    (pygame.transform.scale(pygame.image.load('Assets/StartScreen/Restart.png'), (40, 40)), (130, 780)),
     
                )         
            )     
        )
          
            
        # main = 0
        # saves = 1
        # info = 2
        self.state = 0
        
        self.saveLoad = 0 # None initially
        
    # DRAW CURRENT STATE SCREEN
    def draw(self, surf):
        
        drawSet = self.buttons[self.state]
        
        surf.blit(background, (0, 0))

        for button in drawSet[0]:
            
            pygame.draw.rect(surf, (255, 255, 255), button)
            
        for image in drawSet[1]:
            
            surf.blit(image[0], image[1])
            
    # DELETE GIVEN SAVE FILE
    def delSave(self, save):
        with open(f'Saves/save{save}.txt', 'w') as file:
            file.write('')
    
    # MANAGE BUTTON CLICKS AND FUNCTIONALITY
    def click(self, state, button):
        
        buttonSet = self.buttons[self.state][0]
        
        match self.state:
            
            # MAIN
            case 0:
                    
                if button == buttonSet[0]:
                    return 1
                
                elif button == buttonSet[1]:
                    self.state = 1
                    return state
                
                elif button == buttonSet[2]:
                    self.state = 2
                    return state
                
                elif button == buttonSet[3]:
                    return 10
                    
            # SAVES
            case 1:
                    
                # LOAD GAME
                
                # Save 1
                if button == buttonSet[0]:
                    self.saveLoad = 1
                    
                    with open('Saves/save1.txt', 'r') as test:
                        if test.readline() == '':
                            return state
                        
                    return 2
                      
                # Save 2
                elif button == buttonSet[1]:
                    self.saveLoad = 2
                    
                    with open('Saves/save2.txt', 'r') as test:
                        if test.readline() == '':
                            return state
                        
                    return 2
                
                # Save 3
                elif button == buttonSet[2]:
                    self.saveLoad = 3
                    
                    with open('Saves/save3.txt', 'r') as test:
                        if test.readline() == '':
                            return state
                        
                    return 2
                        
                # Back button
                elif button == buttonSet[3]:
                    self.state = 0
                    return state
                
                # delete buttons
                elif button == buttonSet[4]:
                    self.delSave(1)
                    return state
                
                elif button == buttonSet[5]:
                    self.delSave(2)
                    return state
                
                elif button == buttonSet[6]:
                    self.delSave(3)
                    return state
            
            # INFO
            case 2:
                
                if button == buttonSet[0]:
                    self.state = 0
                    return state
                
        return state