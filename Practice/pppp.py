import pygame
 
pygame.init() #Initialize
 
#==============================INITIALIZING==============================
 
screen = pygame.display.set_mode((600,500)) # (x, y)
 
#=============================== (R,G,B) ================================
 
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
black = (0,0,0)
white = (255,255,255)
yellow = (255,255,0)
grey = (128,128,128)
 
x = 290
y = 400
width = 20
height = 20
vel = 10
 
 
 
 
  
# ========================================Game Loop=============================
while True:
    pygame.time.delay(100)
     
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
         
         
 
    keys = pygame.key.get_pressed()
 
    if keys[pygame.K_LEFT]:
        x -= vel
 
    if keys[pygame.K_RIGHT]:
        x += vel
 
    if keys[pygame.K_UP]:
        y -= vel
 
    if keys[pygame.K_DOWN]:
        y += vel
 
# player stops at the sidewalls and top and bottom walls
    if x <= 30:
        x = 30
    if x >= 550:
        x = 550
    if y <= 31:
        y = 31
    if x <= 250 and y >= 450:
        y = 450
    if x >= 350 and y >= 450:
        y = 450
 
# player stops at castle walls
 
    if x >= 140 and y <= 260:
        x = 140
     
     
     
             
 
 
 
 
    screen.fill(grey)
    pygame.draw.rect(screen,yellow,[0,0,30,500])
    pygame.draw.rect(screen,yellow,[570,0,30,500])
    pygame.draw.rect(screen,yellow,[0,470,250,30])
    pygame.draw.rect(screen,yellow,[350,470,250,30])
    pygame.draw.rect(screen,yellow,[0,0,200,30])
    pygame.draw.rect(screen,yellow,[400,0,200,30])
    pygame.draw.rect(screen,yellow,[210,0,10,30])
    pygame.draw.rect(screen,yellow,[230,0,10,30])
    pygame.draw.rect(screen,yellow,[250,0,10,30])
    pygame.draw.rect(screen,yellow,[380,0,10,30])
    pygame.draw.rect(screen,yellow,[360,0,10,30])
    pygame.draw.rect(screen,yellow,[340,0,10,30])
    pygame.draw.rect(screen,yellow,[160,30,100,200])
    pygame.draw.rect(screen,yellow,[340,30,100,240])
    pygame.draw.rect(screen,yellow,[160,130,200,140])
    pygame.draw.rect(screen,yellow,[180,130,100,240])
    pygame.draw.rect(screen,yellow,[320,130,100,240])
    pygame.draw.rect(screen,yellow,[x,y,20,20])
 
    pygame.display.update()