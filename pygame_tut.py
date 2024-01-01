import pygame 

pygame.init() #initializing the pygame module

screen = pygame.display.set_mode((800,400)) #setting the screen size
pygame.display.set_caption("My first game") #setting the caption of the game window

# test_surface = pygame.Surface((200,200)) 
# test_surface.fill((255,0,0)) #filling the surface with red color
SNAIL_POS = 600

sky_img = pygame.image.load("graphics\Sky.png").convert_alpha() #loading the image
ground_img = pygame.image.load("graphics\ground.png").convert_alpha() #loading the image
text_font = pygame.font.Font("font\Pixeltype.ttf", 50) #loading the font
snail = pygame.image.load("graphics\snail\snail2.png").convert_alpha() #loading the image
text = text_font.render("My first game", False, 'Black') #rendering the text
Game_is_on = True #setting the game loop to true
FPS = 60 
clock = pygame.time.Clock() #setting the clock
while Game_is_on:
    clock.tick(FPS) #setting the FPS
    SNAIL_POS -= 4

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Game_is_on = False
    screen.blit(sky_img, (0,0)) #bliting the image on the screen
    screen.blit(ground_img, (0,300)) #bliting the image on the screen
    screen.blit(text, (300,80)) #bliting the text on the screen
    if SNAIL_POS < -100:
        SNAIL_POS = 800
    screen.blit(snail, (SNAIL_POS, 260)) #bliting the image on the screen

    

    pygame.display.update() #updating the screen

pygame.quit() #quiting the pygame module
