import pygame
import random
import math
import os

#path setup
BASE_DIR = os.path.dirname(__file__)
def load_image(filename):
    return pygame.image.load(os.path.join(BASE_DIR,filename))

#variables
screen_width = 800
screen_height = 500
player_start_x = 370
player_start_y = 380
enemy_start_y_min = 50
enemy_start_y_max = 150
enemy_speed_x = 4
enemy_speed_y = 40
bullet_speed_y = 10
collision_distance = 27

#initialize the game
pygame.init()

#creating the screen
screen = pygame.display.set_mode((screen_width,screen_height))

#background image
background = load_image("bgspace.jpg")

#caption and icon
pygame.display.set_caption("Space invaders")
icon = load_image("ufo.png")
pygame.display.set_icon(icon)

#player
player_img = load_image("player.png")
player_x = player_start_x
player_y = player_start_y
player_x_change = 0

#enemy
enemy_img = []
enemy_x = []
enemy_y = []
enemy_x_change = []
enemy_y_change = []
num_of_enemies = 6

for _i in range(num_of_enemies):
    enemy_img.append(load_image("en.png"))
    enemy_x.append(random.randint(0,screen_width-64))
    enemy_x.append(random.randint(enemy_start_y_min,enemy_start_y_max))
    enemy_x_change.append(enemy_speed_x)
    enemy_y_change.append(enemy_speed_y)

#bullet
bullet_img = load_image("bul.png")
bullet_x = 0
bullet_y = player_start_y
bullet_x_change = 0
bullet_y_change = bullet_speed_y
bullet_state = "ready"

#score
score_value = 0
font = pygame.font.Font("Times New Roman",32)
text_x = 10
text_y = 10

#game Over text
over_font = pygame.font.Font("Times New Roman",64)

def show_score(x,y):
    score = font.render("Score: "+str(score_value),True,(255,255,255))
    screen.blit(score(x,y))

def game_over_text():
    over_text = over_font.render("Game Over",True,(255,255,255))
    screen.blit(over_text(250,250))

def player(x,y):
    screen.blit(player_img(x,y))

def enemy(x,y,i):
    screen.blit(enemy_img[i],(x,y))

def fire_bullet(x,y):
    global bullet_state
    bullet_state = "Fire"
    screen.blit(bullet_img,(x+16,y+10))

def isCollision(enemy_x,enemy_y,bullet_x,bullet_y):
    distance = math.sqrt((enemy_x-bullet_x)**2+(enemy_y-bullet_y)**2)
    return distance < collision_distance