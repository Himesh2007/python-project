import pygame  # Import the pygame module
import sys     # Import the sys module to handle system exit

pygame.init()  # Initialize all imported pygame modules

# Set up the display window with a width of 800 pixels and a height of 600 pixels
screen = pygame.display.set_mode((800, 600))

# Set the title of the display window
pygame.display.set_caption("Pygame Example")

# Set the variable 'running' to True to keep the main loop running
running = True

# Start the main loop to keep the window open
while running:
    # Check for events in the event queue
    for event in pygame.event.get():
        # If the event type is QUIT, set 'running' to False to exit the loop
        if event.type == pygame.QUIT:
            running = False
    
    # Fill the screen with white color (RGB: 255, 255, 255)
    screen.fill((255, 255, 255))
    
    # Draw a red circle (RGB: 255, 0, 0) with a radius of 30 pixels at the position (400, 300)
    pygame.draw.circle(screen, (255, 0, 0), (400, 300), 30)
    
    # Update the full display Surface to the screen
    pygame.display.flip()

# Quit pygame
pygame.quit()

# Exit the system safely
sys.exit()