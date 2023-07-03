# Example file showing a basic pygame "game loop"
import pygame
from sys import exit

# Photo by <a href="https://unsplash.com/@color0911?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Charles Chen</a> on <a href="https://unsplash.com/s/photos/bread?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>
  
windowWidth = 800
windowHeight = 400

# pygame setup
pygame.init()

# screen = pygame.display.set_mode((windowWidth, windowHeight))
screen = pygame.display.set_mode((800, 600), pygame.FULLSCREEN)
pygame.display.set_caption('Bread')
pygame.display.set_icon(pygame.image.load('bread.png'))

clock = pygame.time.Clock()
running = True

windowWidth = 800

closeIcon = pygame.image.load('art/PNG/close.png')
closeIcon = pygame.transform.scale(closeIcon, (50, 50))

screen.blit(closeIcon,(0,0))

pygame.display.update()

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("quitEventTriggered")
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    # RENDER YOUR GAME HERE
    

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60) # limits FPS to 60
    print(clock.get_fps())

pygame.quit()
exit()
