import random, pygame, math, sys
# pygame.display.update() / pygame.display.flip() gameDisplay.fill() keys = pygame.key.get_pressed() pygame.draw.line(gameDisplay, color, start_position, end_position, width)

#def draw(self):
#self.screen.fill(self.color)# clear screen
#self.draw(self.screen)# draw updated screen

pygame.init()

white = (255,255,255)
white_o = (255,255,255)
black = (0,0,0)
red = ( 255,0,0)
green = ( 0,255,0)
blue = (0,0,255)
brown = (150,75,0)
gray = (112.95,112.95,112.95)
yellow = (255,255,0)

display_width, display_height = 1200, 800
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("Counter Strike Global Blocks")

menu = True

fps = pygame.time.Clock()

font = pygame.font.Font("IBMPlexSans-Regular.ttf", 40)
fontGameEnd = pygame.font.Font("IBMPlexSans-Regular.ttf", 200)

def title(msg, color):
    screen_text = font.render(msg, True, color)
    gameDisplay.blit(screen_text, [1, 10])
def bluescore(msg, color):
    screen_text = font.render(msg, True, color)
    gameDisplay.blit(screen_text, [1035, 10])
def redscore(msg, color):
    screen_text = font.render(msg, True, color)
    gameDisplay.blit(screen_text, [1115, 10])
def GameOver(msg, color):
    screen_text = fontGameEnd.render(msg, True, color)
    gameDisplay.blit(screen_text, [150, 200])
def mainMenu():
    while menu:
        #[x, y], [1, 0, 0]
        gameDisplay.fill(brown)
        pygame.draw.line(gameDisplay, gray, (0, 0), (0, 800), 200)
        pygame.draw.circle(gameDisplay, white_o, (50, 150), 30)
        pygame.draw.polygon(gameDisplay, gray, [(37,137), (37,163), (70,150)], 0)
        title("CSGB", black)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        
        pygame.display.update()
        pos, pressed = pygame.mouse.get_pos(), pygame.mouse.get_pressed()
        if 20 <= pos[0] <= 80 and 120 <= pos[1] <= 180 and pressed[0] == 1:
             gameSystem()

    fps.tick(120)
    pygame.display.update()

def gameSystem():
    lead_x = 12.5
    lead_y = 410
    lead_x_change = 0
    lead_y_change = 0
    lead_x2 = 968.25
    lead_y2 = 390
    lead_x2_change = 0
    lead_y2_change = 0
    redBullet_counter = 0
    redBullet_x = 0
    redBullet_y = -10
    redBullet_x2 = 0
    redBullet_y2 = -10
    redBullet_x3 = 0
    redBullet_y3 = -10
    redBullet_x4 = 0
    redBullet_y4 = -10
    redBullet_x5 = 0
    redBullet_y5 = -10
    blueBullet_counter = 0
    blueBullet_x = 0
    blueBullet_y = -19
    blueBullet_x2 = 0
    blueBullet_y2 = -19
    blueBullet_x3 = 0
    blueBullet_y3 = -19
    blueBullet_x4 = 0
    blueBullet_y4 = -19
    blueBullet_x5 = 0
    blueBullet_y5 = -19
    blueScore = 0
    redScore = 0
    rePlay_x = 200
    rePlay_y = 600
    endGame_x = 850
    endGame_y = 600
    menuButton_x = 525
    menuButton_y = 600
    gameOn = True

    while gameOn:
        gameDisplay.fill(black)
        bluescore(str(blueScore), blue)
        redscore(str(redScore), red)
        pygame.draw.line(gameDisplay, green, (1002.5,0), (1002.5, 800), 5)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    lead_x2_change = 0
                if event.key == pygame.K_RIGHT:
                    lead_x2_change = 0
                if event.key == pygame.K_UP:
                    lead_y2_change = 0
                if event.key == pygame.K_DOWN:
                    lead_y2_change = 0
                if event.key == pygame.K_a:
                    lead_x_change = 0
                if event.key == pygame.K_d:
                    lead_x_change = 0
                if event.key == pygame.K_w:
                    lead_y_change = 0
                if event.key == pygame.K_s:
                    lead_y_change = 0
                if event.key == pygame.K_SLASH: 
                   if redBullet_counter == 0:
                       redBullet_x = lead_x2 - 15
                       redBullet_y = lead_y2 + 8
                       redBullet_counter += 1
                   elif redBullet_counter == 1:
                       redBullet_x2 = lead_x2 - 15
                       redBullet_y2 = lead_y2 + 8
                       redBullet_counter += 1
                   elif redBullet_counter == 2:
                       redBullet_x3 = lead_x2  - 15
                       redBullet_y3 = lead_y2 + 8
                       redBullet_counter += 1
                   elif redBullet_counter == 3:
                       redBullet_x4 = lead_x2 - 15
                       redBullet_y4 = lead_y2 + 8
                       redBullet_counter += 1
                   elif redBullet_counter == 4:
                       redBullet_x5 = lead_x2 - 15
                       redBullet_y5 = lead_y2 + 8
                       redBullet_counter = 0
                if event.key == pygame.K_e:
                   if blueBullet_counter == 0:
                       blueBullet_x = lead_x + 25
                       blueBullet_y = lead_y + 8
                       blueBullet_counter += 1
                   elif blueBullet_counter == 1:
                       blueBullet_x2 = lead_x + 25
                       blueBullet_y2 = lead_y + 8
                       blueBullet_counter += 1
                   elif blueBullet_counter == 2:
                       blueBullet_x3 = lead_x + 25
                       blueBullet_y3 = lead_y + 8
                       blueBullet_counter += 1
                   elif blueBullet_counter == 3:
                       blueBullet_x4 = lead_x + 25
                       blueBullet_y4 = lead_y + 8
                       blueBullet_counter += 1
                   elif blueBullet_counter == 4:
                       blueBullet_x5 = lead_x + 25
                       blueBullet_y5 = lead_y + 8
                       blueBullet_counter = 0
                       
        blueBullet_x = blueBullet_x + 20
        blueBullet_x2 = blueBullet_x2 + 20
        blueBullet_x3 = blueBullet_x3 + 20
        blueBullet_x4 = blueBullet_x4 + 20
        blueBullet_x5 = blueBullet_x5 + 20
        
        redBullet_x = redBullet_x - 20
        redBullet_x2 = redBullet_x2 - 20
        redBullet_x3 = redBullet_x3 - 20
        redBullet_x4 = redBullet_x4 - 20
        redBullet_x5 = redBullet_x5 - 20
        
        if (redBullet_x >= lead_x - 4 and redBullet_x <= lead_x + 24 and redBullet_y >= lead_y - 4 and redBullet_y <= lead_y + 24 or redBullet_x2 >= lead_x - 4 and redBullet_x2 <= lead_x + 24 and redBullet_y2 >= lead_y - 4 and redBullet_y2 <= lead_y + 24 or
            redBullet_x3 >= lead_x - 4 and redBullet_x3 <= lead_x + 24 and redBullet_y3 >= lead_y - 4 and redBullet_y3 <= lead_y + 24 or redBullet_x4 >= lead_x - 4 and redBullet_x4 <= lead_x + 24 and redBullet_y4 >= lead_y - 4 and redBullet_y4 <= lead_y + 24 or
            redBullet_x5 >= lead_x - 4 and redBullet_x5 <= lead_x + 24 and redBullet_y5 >= lead_y - 4 and redBullet_y5 <= lead_y + 24):
            redScore += 1
            lead_x = 12.5
            lead_y = 410
            lead_x2 = 968.25
            lead_y2 = 390
        if (blueBullet_x >= lead_x2 - 4 and blueBullet_x <= lead_x2 + 24 and blueBullet_y >= lead_y2 - 4 and blueBullet_y <= lead_y2 + 24 or blueBullet_x2 >= lead_x2 - 4 and blueBullet_x2 <= lead_x2 + 24 and blueBullet_y2 >= lead_y2 - 4 and blueBullet_y2 <= lead_y2 + 24
        or blueBullet_x3 >= lead_x2 - 4 and blueBullet_x3 <= lead_x2 + 24 and blueBullet_y3 >= lead_y2 - 4 and blueBullet_y3 <= lead_y2 + 24 or blueBullet_x4 >= lead_x2 - 4 and blueBullet_x4 <= lead_x2 + 24 and blueBullet_y4 >= lead_y2 - 4 and blueBullet_y4 <= lead_y2 + 24
            or blueBullet_x5 >= lead_x2 - 4 and blueBullet_x5 <= lead_x2 + 24 and blueBullet_y5 >= lead_y2 - 4 and blueBullet_y5 <= lead_y2 + 24):
            blueScore += 1
            lead_x = 12.5
            lead_y = 410
            lead_x2 = 968.25
            lead_y2 = 390
        if redScore == 20:
            gameDisplay.fill(black)
            GameOver("Red Wins", red)
            gameOn = False
        if blueScore == 20:
            gameDisplay.fill(black)
            GameOver("Blue Wins", blue)
            gameOn = False
            
            
                   
        key = pygame.key.get_pressed()
        if key[ord('a')]:
            lead_x_change = -13
        if key[ord('d')]:
            lead_x_change = 13
        if key[ord('w')]:
            lead_y_change = -9
        if key[ord('s')]:
            lead_y_change = 9
        if key[pygame.K_LEFT]:
            lead_x2_change = -13
        if key[pygame.K_RIGHT]:
            lead_x2_change = 13
        if key[pygame.K_UP]:
            lead_y2_change = -9
        if key[pygame.K_DOWN]:
            lead_y2_change = 9

                
        if lead_y <= 0:
            lead_y = 800
        elif lead_y >= 800:
            lead_y = 0
        if lead_y2 <= 0:
            lead_y2 = 800
        elif lead_y2 >= 800:
            lead_y2 = 0
        if lead_x <= 0:
            lead_x = 0
        if lead_x2 >= 980:
            lead_x2 = 980
        if lead_x >= 500:
            lead_x = 500
        if lead_x2 <= 500:
            lead_x2 = 500
            
            
        lead_x += lead_x_change
        lead_y += lead_y_change
        lead_x2 += lead_x2_change
        lead_y2 += lead_y2_change
        
        
        fps.tick(120)
        
     
        pygame.draw.rect(gameDisplay, blue, [ lead_x, lead_y, 20, 20])
        pygame.draw.rect(gameDisplay, red, [ lead_x2, lead_y2, 20, 20])
        for bullet in [(redBullet_x, redBullet_y), (redBullet_x2, redBullet_y2), (redBullet_x3, redBullet_y3), (redBullet_x4, redBullet_y4), (redBullet_x5, redBullet_y5),
                        (blueBullet_x, blueBullet_y), (blueBullet_x2, blueBullet_y2), (blueBullet_x3, blueBullet_y3), (blueBullet_x4, blueBullet_y4), (blueBullet_x5, blueBullet_y5)]:   
            pygame.draw.rect(gameDisplay, yellow, [bullet[0], bullet[1], 10, 5])
        pygame.display.update()
    while gameOn == False:   
        if gameOn == False:
            pygame.draw.rect(gameDisplay, green, [rePlay_x, rePlay_y, 100, 50])
            pygame.draw.rect(gameDisplay, red, [endGame_x, endGame_y, 100, 50])
            pygame.draw.rect(gameDisplay, yellow, [menuButton_x, menuButton_y, 100, 50])
            pos, pressed = pygame.mouse.get_pos(), pygame.mouse.get_pressed()
            if endGame_x <= pos[0] <= endGame_x + 100 and endGame_y <= pos[1] <= endGame_y + 50 and pressed[0] == 1:
                pygame.quit()
                sys.exit()
            if rePlay_x <= pos[0] <= rePlay_x + 100 and rePlay_y <= pos[1] <= rePlay_y + 50 and pressed[0] == 1:
                gameSystem()
            if menuButton_x <= pos[0] <= menuButton_x + 100 and menuButton_y <= pos[1] <= menuButton_y + 50 and pressed[0] == 1:
                mainMenu()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            pygame.display.update() 


mainMenu()
