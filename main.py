import pygame

pygame.init()
screen = pygame.display.set_mode((640,480))
pygame.display.set_caption("MY FIRST GAME SCREEN")

done = False
while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            quit
    pygame.draw.rect(screen,(0,225,225),pygame.Rect(30,30,200,200))
    pygame.display.flip()