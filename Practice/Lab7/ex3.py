import pygame

pygame.init()
screen = pygame.display.set_mode((600, 450))
done = False
color = (255, 32, 32)

x, y = 30, 30
r = 25
step = 20

clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]:
        if y - r - step > 0:
            y -= step
    if pressed[pygame.K_RIGHT]:
        if x + r + step < screen.get_width():
            x += step
    if pressed[pygame.K_DOWN]:
        if y + r + step < screen.get_height():
            y += step
    if pressed[pygame.K_LEFT]:
        if x - r - step > 0:
            x -= step

    screen.fill((255, 255, 255 ))
    pygame.draw.circle(screen, color, (x, y), r)

    pygame.display.flip()
    clock.tick(60)