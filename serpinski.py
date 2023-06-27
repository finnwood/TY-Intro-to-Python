
import pygame

def sierpinski_triangle(x, y, size, depth, screen):
    if depth == 0:
        # Draw a triangle
        pygame.draw.polygon(screen, (255, 255, 255), [(x, y), (x + size, y), (x + size / 2, y + size)])
    else:
        # Recursively draw three smaller triangles
        sierpinski_triangle(x, y, size / 2, depth - 1, screen)
        sierpinski_triangle(x + size / 2, y, size / 2, depth - 1, screen)
        sierpinski_triangle(x + size / 4, y + size / 2, size / 2, depth - 1, screen)

# Example usage
pygame.init()
screen = pygame.display.set_mode((800, 600))
sierpinski_triangle(200, 100, 400, 5, screen)
pygame.display.flip()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
