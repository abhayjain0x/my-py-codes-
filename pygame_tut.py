import pygame 

pygame.init() #initializing the pygame module

screen = pygame.display.set_mode((800,600)) #setting the screen size
pygame.display.set_caption("My first game") #setting the caption of the game window


Game_is_on = True #setting the game loop to true

while Game_is_on:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Game_is_on = False

    pygame.display.update() #updating the screen

pygame.quit() #quiting the pygame module
