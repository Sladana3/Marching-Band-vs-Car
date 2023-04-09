import pygame
from pygame.locals import *
import random
#The road
size = width, height = (1800, 1000)
road_w = int(width/1.6) 
roadmark_w = int(width/80)
right_lane = width/2 + road_w/4
left_lane = width/2 - road_w/4
speed = 1

pygame.init()
running = True
#size of window
screen = pygame.display.set_mode(size)
#Title
pygame.display.set_caption("Marching Band vs Car")
#background color
screen.fill((60, 200, 0))

pygame.display.update()
#Load MB
MB = pygame.image.load("MB.png")
MB_loc = MB.get_rect()
MB_loc.center = right_lane, height*0.8

#Load Car 
Car = pygame.image.load("Car.png")
Car_loc = MB.get_rect()
Car_loc.center = left_lane, height*0.2

text_font = pygame.font.SysFont("Arial", 30)
text_font2 = pygame.font.SysFont("italic", 30)

def text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))

lvl = 1
counter = 0
moveing = 0


#Game loop
while running:
    
    #Points
    counter += 1
    if counter == 8000 and speed > 0:
        speed += 0.5
        lvl += 1
        counter = 0
        screen.fill(pygame.Color(60, 200, 0), (0, 0, 350, 300))
    
    text("Level: {}".format(lvl), text_font, (0, 0, 0), 150, 150)
    
    #Enemy
    Car_loc[1] += speed
    if Car_loc[1] > height:
        Car_loc[1] = -200
        if random.randint(0,1) == 0:
            Car_loc.center = right_lane, -200
        else:
            Car_loc.center = left_lane, -200

    #End game
    if MB_loc[0] == Car_loc[0] and Car_loc[1] > MB_loc[1] -250:
        speed = 0


    #Event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == KEYDOWN and speed > 0:
            if event.key in [K_a, K_LEFT] and moveing == 0:
                MB_loc = MB_loc.move([-int(road_w/2), 0])
                moveing = 1
            if event.key in [K_d, K_RIGHT] and moveing == 1:
                MB_loc = MB_loc.move([int(road_w/2), 0])
                moveing = 0

    if speed == 0: 
        screen.fill(pygame.Color(0, 0, 0), (0, 0, width , height))
        text("RIP! No more music for this town", text_font2, (250, 0, 0), width/2.5, height/3.5)
        text("Your final level: {}".format(lvl), text_font2, (250, 0, 0), width/2.25, height/3.2)

    #Graphics
    if speed > 0:
        pygame.draw.rect(
            screen,
            (50, 50, 50), 
            (width/2-road_w/2, 0, road_w, height))

        pygame.draw.rect(
            screen,
            (255, 240, 60),
            (width/2-roadmark_w/2, 0, roadmark_w, height))

        pygame.draw.rect(
            screen,
            (255, 255, 255),
            (width/2 - road_w/2 + roadmark_w*2, 0, roadmark_w, height))

        pygame.draw.rect(
            screen,
            (255, 255, 255),
            (width/2 + road_w/2 - roadmark_w*3, 0, roadmark_w, height))

    screen.blit(MB, MB_loc)
    screen.blit(Car, Car_loc)
    pygame.display.update()

pygame.quit()
