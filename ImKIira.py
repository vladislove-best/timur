import pygame
pygame.init()
display_width = 1000
display_height = 700
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('SPAWN')
black = (0,0,0)
white = (255,255,255)

carImg = pygame.image.load('11.jpg')
ship = pygame.image.load("slam.png")
ship_top = gameDisplay.get_height() - ship.get_height()
ship_left = gameDisplay.get_width()/2 - ship.get_width()/2

gameDisplay.blit(ship, (ship_left,ship_top))

def car(x,y):
    gameDisplay.blit(carImg, (x,y))

x =  (display_width * 0.45)
y = (display_height * 0.8)	#1
x_change = 0
y_change = 0
#spawn = False
car_speed = 0

    ############################
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -5
            elif event.key == pygame.K_RIGHT:
                x_change = 5
            elif event.key == pygame.K_UP:
                y_change = -5
            elif event.key == pygame.K_DOWN:
                y_change = 5
            #elif ebent.key == pygame.K_SPACE:
            #    spawn = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_change = 0
            elif event.key == pygame.K_UP:
                y_change = 0
        ######################
        
clock = pygame.time.Clock()

crashed = False

while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
    pygame.display.update()
    clock.tick(60)



pygame.quit()
quit()