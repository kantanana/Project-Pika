import pygame
import math
import os
import random
from time import time
from pygame import mixer
pygame.init()
#   functions
num_of_enemies = 100
score = 0
sTime = None


def stage1():
    global score
    global num_of_enemies
    over_font = pygame.font.Font("Pokemon Solid.ttf", 40)
    font =  pygame.font.Font("Pokemon Solid.ttf", 38)
    def game_over_text():
        over_text = over_font.render("YOU LOSE!!! SCROLL UP TO RESTART", True, (255, 255, 255))
        screen.blit(over_text, (230, 250))
        
    def move_on():
        over_text = font.render("Scroll up to continue Scroll down to quit", True, (255, 255, 255))
        screen.blit(over_text, (230, 400))

    def stage_clear():
        over_text = font.render("Stage Clear", True, (255, 255, 255))
        screen.blit(over_text, (230, 250))

    def background(x,y):
        screen.blit(background1, (0, 0))
    #Initialize

    #exec(open('displaying.py').read())
    #Functions
    def player(pX,pY):
        screen.blit(playerimg,(pX,pY))

    def enemy(x, y, i):
        screen.blit(enemyImg[i], (x, y))


    # Enemy
    enemyImg = []
    enemyX = []
    enemyY = []
    enemyX_change = []
    enemyY_change = []
    
    for item in range(num_of_enemies):
        enemyImg.append(pygame.image.load('circle.png'))
        enemyX.append(random.randint(0, 1136))
        enemyY.append(random.randint(0, 736))
        enemyX_change.append(1)
        enemyY_change.append(1)

    check = num_of_enemies

    enemies = {}

    for i in range(num_of_enemies):
        enemies["enemy{}".format(i)] = [enemyX[i],enemyY[i]]
    print(enemy)




    background1 = pygame.image.load('background.png')
    bulletImg = pygame.image.load('PIKA.png')
    bulletchangeX = 15
    bulletchangeY = 15
    bulletstate = 'ready'
    def fire_bullet(x, y):
        global bullet_state
        bullet_state = "fire"
        screen.blit(bulletImg, (x + 16, y + 10))

    def bull(x,y):
        screen.blit(bulletImg,(x,y) )
        
    def collide(x1,y1,x2,y2):
        if ((x1-x2)**2 + (y1-y2)**2)**0.5 <= 63:
            return True

    #Values
    clock = pygame.time.Clock()
    #Create screen
    screen = pygame.display.set_mode((1200,800))
    #display  
    playerimg = pygame.image.load('square.png')
    playX = 370
    playY = 400
    pchangex = 0
    pchangey = 0
    playHP = 5
    invincible_time = 3
    #Game loop

    bulletX = 1000
    bulletY = 1000
    angle = 0
    running = True
    while running:
        temp = num_of_enemies
        
        screen.fill((0,0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    pchangex -= 5
                if event.key == pygame.K_RIGHT:
                    pchangex += 5
                if event.key == pygame.K_UP:
                    pchangey -= 5
                if event.key == pygame.K_DOWN:
                    pchangey += 5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    pchangex = 0
                    pchangey = 0
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouseposi = pygame.mouse.get_pos()
                mouseX =  mouseposi[0]
                mouseY = mouseposi[1]
                if event.button == 1:
                    bullet_sound = mixer.Sound('Pikachu.wav')
                    bullet_sound.play()
                    
                    if bulletstate == "ready":
                        
                        bulletX = playX
                        bulletY = playY
                        diffX = mouseX - bulletX
                        diffY = mouseY - bulletY
                        
                        angle = math.atan2(diffY,diffX)
                        fire_bullet(bulletX, bulletY)

        
        playX += pchangex
        playY += pchangey
        bulletX += math.cos(angle)*bulletchangeX
        bulletY += math.sin(angle)*bulletchangeY
        
        if playX < 0:
            playX = 0
        elif playX > 1136:
            playX = 1136
        
        elif playY < 0:
            playY = 0
        elif playY > 736:
            playY = 736
        
        for x in range(num_of_enemies):
            if enemies["enemy"+str(x)] == None:
                continue
            if enemies["enemy"+str(x)][0] > playX:
                enemyX_change[x] = -1
            elif enemies["enemy"+str(x)][0] < playX:
                enemyX_change[x] = 1
            elif enemies["enemy"+str(x)][1] > playY:
                enemyY_change[x] = -1
            elif enemies["enemy"+str(x)][1] < playY:
                enemyY_change[x] = 1

    
        for i in range(num_of_enemies):
            if enemies["enemy"+str(i)] == None:
                continue
            enemies["enemy"+str(i)][0] += enemyX_change[i]
            enemies["enemy"+str(i)][1] += enemyY_change[i]
            if enemies["enemy"+str(i)][0] > 1136:
                enemies["enemy"+str(i)][0] = 1136
            elif enemies["enemy"+str(i)][0]< 0:
                enemies["enemy"+str(i)][0]= 0
            elif enemies["enemy"+str(i)][1] > 736:
                enemies["enemy"+str(i)][1] = 736
            elif enemies["enemy"+str(i)][1]< 0:
                enemies["enemy"+str(i)][1]= 0
            
            
            enemy(enemies["enemy"+str(i)][0], enemies["enemy"+str(i)][1], i)
        player(playX,playY)
        for it in range(num_of_enemies):
            if enemies["enemy"+str(it)] == None:
                continue
            if it + 1 > num_of_enemies - 1:
                break
            if enemies["enemy"+str(it)] == enemies["enemy"+str(it+1)]:
                enemies["enemy"+str(it+1)][0] += 64
                enemies["enemy"+str(it+1)][1] += 64





        sTime = None      
        for j in range(num_of_enemies):
            if enemies["enemy"+str(j)] == None:
                continue
            dist = math.sqrt(((playY-enemies["enemy"+str(j)][1])**2)+((playX-enemies["enemy"+str(j)][0])**2))
            if dist < 63:
           
                playHP = 0
                print(playHP)
           
        
        enemyX_temp = enemyX
     
        
        bull(bulletX, bulletY)
        
        for item in range(num_of_enemies):
            if enemies["enemy"+str(item)] == None:
                continue
            if collide(bulletX,bulletY,enemies["enemy"+str(item)][0],enemies["enemy"+str(item)][1]):
                enemies["enemy"+str(item)] = None
                score += 1
                check -= 1
        if playHP == 0:
            
            game_over_text()
            background(0,0)
            
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    
                    if event.button == 4:
                        
                        stage1()

        if check == 0:
            
            
            stage_clear()
            move_on()
            bullet_state = 'ready'
            print(score)
            
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    
                    if event.button == 4:
                        num_of_enemies += 1
                        
                        stage1()
                    elif event.button == 5:
                        quit()  


                        
        
        clock.tick(200)
        pygame.display.update() 
stage1()