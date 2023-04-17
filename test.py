import pygame
import time

pygame.init()

while True:
    # Create a window
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Window Example")

    # Display the window for 3 seconds
    pygame.display.flip()
    time.sleep(3)

    # Close the window
    pygame.display.quit()

    # Wait 1 second
    time.sleep(1)

