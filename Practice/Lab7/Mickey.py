import pygame
import datetime

def blit_rotate(surf, image, pos, originPos, angle):
    # offset from pivot to center
    image_rect = image.get_rect(topleft = (pos[0] - originPos[0], pos[1]-originPos[1]))
    offset_center_to_pivot = pygame.math.Vector2(pos) - image_rect.center
    
    # roatated offset from pivot to center
    rotated_offset = offset_center_to_pivot.rotate(-angle)

    # roatetd image center
    rotated_image_center = (pos[0] - rotated_offset.x, pos[1] - rotated_offset.y)

    # get a rotated image
    rotated_image = pygame.transform.rotate(image, angle)
    rotated_image_rect = rotated_image.get_rect(center = rotated_image_center)

    # rotate and blit the image
    surf.blit(rotated_image, rotated_image_rect)

done = False
time = datetime.datetime.now()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((1000, 800))

mickey = pygame.image.load('mickeyclock.jpeg')
hour = pygame.image.load('mickey_hour.png')
minute = pygame.image.load('mickey_minute.png')
mickey = pygame.transform.smoothscale(mickey, (1000, 800))
start_hour = 130 - (time.hour * 3600 + time.minute * 60 + time.second) / 240
start_minute = 124 - (time.minute * 60 + time.second) / 10
angle = 0
w, h = mickey.get_size()
pos = [400, 300]
box = [pygame.math.Vector2(p) for p in [(0, 0), (w, 0), (w, -h), (0, -h)]]

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    screen.fill((0, 0, 0))

    pos = (screen.get_width()/2, screen.get_height()/2)

    screen.blit(mickey, (0, 0))
    blit_rotate(screen, minute, pos, (0, 0), start_minute + angle / 300)
    blit_rotate(screen, hour, pos, (0, 0), start_hour + angle / 18000)

    angle -= 1
    

    pygame.display.flip()
    clock.tick(30)
