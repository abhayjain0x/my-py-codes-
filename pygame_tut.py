import pygame 
pygame.init()
BACKGROUND = "black"
screen = pygame.display.set_mode((800, 600)) 
clock = pygame.time.Clock()
screen.fill(BACKGROUND)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            BACKGROUND = "white"

    screen.fill(BACKGROUND)
           
        
    pygame.display.update()
    clock.tick(60)

