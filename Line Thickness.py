import pygame
pygame.init()

window = pygame.display.set_mode([400, 400])
window.fill((255, 255, 255))

left = (0, 200)
right = (400, 200)
top = (200, 0)
bottom = (200, 400)

pygame.draw.line(window, (231, 154, 73), left, top, 1)
pygame.draw.line(window, (231, 154, 73), left, bottom, 2)
pygame.draw.line(window, (231, 154, 73), right, bottom, 4)
pygame.draw.line(window, (231, 154, 73), right, top, 8)

pygame.display.flip()
pygame.time.wait(5000)
