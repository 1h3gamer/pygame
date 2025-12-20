import pygame
import random

pygame.init()

sprite_color_change_event=pygame.USEREVENT + 1
bg_color_change_event=pygame.USEREVENT + 2

blue=pygame.Color('blue')
lightblue=pygame.Color('lightblue')
darkblue=pygame.Color('darkblue')

yellow=pygame.Color('yellow')
magenta=pygame.Color('magenta')
orange=pygame.Color('orange')
white=pygame.Color('white')

class Sprite(pygame.sprite.Sprite):
    def __init__(self,color,height,width):
        super().__init__()
        self.image=pygame.Surface((width,height))
        self.image.fill(color)
        self.rect=self.image.get_rect()
        self.velocity=[random.choice([-1,1]), random.choice([-1,1])]

    def update(self):
        self.rect.move_ip(self.velocity)
        boundary_hit= False
        if self.rect.left <=0 or self.rect.right >=500:
            self.velocity[0] = -self.velocity[0]
            boundary_hit= True
        if self.rect.top <=0 or self.rect.bottom >=400:
            self.velocity[1] = -self.velocity[1]
            boundary_hit= True
        if boundary_hit:
            pygame.event.post(pygame.event.Event(sprite_color_change_event))
            pygame.event.post(pygame.event.Event(bg_color_change_event))

    def change_color(self):
        self.image.fill(random.choice([yellow,magenta,orange,yellow]))

    def change_bg_color(self):
        global bg_color
        bg_color=random.choice([blue,lightblue,darkblue])


all_sprites_list=pygame.sprite.Group()
sp1 = Sprite(white,20,30)
sp1.rect.x=random.randint(0,480)
sp1.rect.y=random.randint(0,370)
all_sprites_list.add(sp1)
    
screen = pygame.display.set_mode((500,400))
pygame.display.set_caption("colourful bounce")
bg_color=blue
screen.fill(bg_color)
exit=False
clock=pygame.time.Clock()

while not exit:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit=True
        elif event.type==sprite_color_change_event:
            sp1.change_color()
        elif event.type==bg_color_change_event:
            bg_color
    all_sprites_list.update()
    screen.fill(bg_color)
    all_sprites_list.draw(screen)

    pygame.display.flip()
    clock.tick(240)

pygame.quit()