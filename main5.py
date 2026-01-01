import pygame
import random

surf_color = (0,142,204)
color = (0,0,0)

class Sprite(pygame.sprite.Sprite):
    def __init__(self,color,height,width):
        super().__init__()
        self.image = pygame.Surface([width,height])
        self.image.fill(surf_color)
        pygame.draw.rect(self.image,color,pygame.Rect(0,0,width,height))
        self.rect = self.image.get_rect()

pygame.init()
screen = pygame.display.set_mode((500,400))
pygame.display.set_caption("Creating Sprite")

all_sprites_list = pygame.sprite.Group()
sp1 = Sprite(color,20,30)
sp1.rect.x = random.randint(0,480)
sp1.rect.y = random.randint(0,370)
all_sprites_list.add(sp1)

exit = True

clock = pygame.time.Clock()


while exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = False
# Update Sprite Group
    all_sprites_list.update()
# Screen Set up
    screen.fill(surf_color)
# Displaying Sprites
    all_sprites_list.draw(screen)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()