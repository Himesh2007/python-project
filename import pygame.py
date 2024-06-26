import pygame
import sys
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Pygame Example")
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, (255, 0, 0), (400, 300), 30)
    pygame.display.flip()
pygame.quit()
sys.exit()