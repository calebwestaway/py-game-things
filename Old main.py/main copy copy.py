import pygame
import sys

pygame.init()

windowDimensions = (640,360)

clock = pygame.time.Clock()

# Set up the display
screen = pygame.display.set_mode(windowDimensions, pygame.FULLSCREEN)
pygame.display.set_caption("Pygame thingy")

# Load the image
closeIcon = pygame.transform.scale(pygame.image.load('art/PNG/close.png'), (50,50))
closeIcon_rect = closeIcon.get_rect()

# Custom Cursor
cursorSurface = pygame.Surface(windowDimensions)
cursorSurface.fill('blue')

pygame.mouse.set_visible(False)

cursor_img = pygame.transform.scale(pygame.image.load("art/PNG/cursor.png"), (25,25))
cursor_img_rect = cursor_img.get_rect()

# Draw the close image on the screen
screen.blit(closeIcon, closeIcon_rect)

# Update the display
pygame.display.flip()

# Set up the timer event
CUSTOM_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(CUSTOM_EVENT, 1000)

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Check if the mouse click was on the image
            if closeIcon_rect.collidepoint(event.pos):
                # Quit the program if the image was clicked
                pygame.quit()
                sys.exit()
    cursorSurface.fill('blue')
    # Cursor-y bits
    # Update the position every frame and blit the image
    cursor_img_rect.center = pygame.mouse.get_pos()
    cursorSurface.blit(cursor_img, cursor_img_rect)
    screen.blit(cursorSurface, (0,0))

    # Update the display
    pygame.display.update()