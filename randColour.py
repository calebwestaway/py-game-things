import sys
import pygame
import time
import random

pygame.init()

screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
# pygame.FULLSCREEN (480, 360)

pygame.mouse.set_visible(False)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    time.sleep(0.5)
    randInt = random.randrange(1,5)

    if randInt == 1:
        screen.fill("green")
    elif randInt == 2:
        screen.fill("blue")
    elif randInt == 3:
        screen.fill("yellow")
    elif randInt == 4:
        screen.fill("purple")
    elif randInt == 5:
        screen.fill("orange")

    pygame.display.flip()
