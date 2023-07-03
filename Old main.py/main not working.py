import sys
import pygame

pygame.init()

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

# cursorImg = pygame.transform.scale(pygame.image.load("art/PNG/cursor.png"), (25,25))
# cursorImgRect = cursorImg.get_rect()

cursorSurface = pygame.Surface(screen.get_size()).convert_alpha()
cursorSurface.fill((255, 255, 255, 0))

pygame.mouse.set_visible(False)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(cursorSurface, (0, 0))

    # cursorImgRect.center = pygame.mouse.get_pos()
    # cursorSurface.blit(cursorImg, cursorImgRect)
    # screen.blit(cursorSurface, (0,0))

    pygame.display.flip()
 