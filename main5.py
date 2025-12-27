import pygame

pygame.init()
window = pygame.display.set_mode((400,400))

window.fill((255,255,255))

green = (0,255,0)
sprite1=pygame.draw.rect(window,green,(34,30),60)
sprite2=pygame.draw.rect(window,green,(100,40),40,50)

pygame.display.update()

running = True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running = False

while sprite1 == False:
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_LEFT]: x-= 3
        if pressed[pygame.K_RIGHT]: x+= 3
        if pressed[pygame.K_UP]: y-= 3
        if pressed[pygame.K_DOWN]: y+= 3

pygame.quit()