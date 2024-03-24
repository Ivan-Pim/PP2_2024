import os
import pygame

def Ready(path):
    lst = os.listdir(path)
    global songlist
    songlist = ['music/' + x for x in lst if os.path.isfile(path + '/' + x)]

def Run(id):
    global PauseState
    if PauseState:
        pygame.mixer.music.load(songlist[id])
        pygame.mixer.music.play(0)
    else:
        pygame.mixer.music.stop()
    PauseState = not PauseState
    pygame.display.set_caption(songlist[id][6:])

def Pause():
    global PauseState
    if PauseState:
        pygame.mixer.music.unpause()
    else:
        pygame.mixer.music.pause()
    PauseState = not PauseState

def ChangeStop():
    global PauseState
    pygame.mixer.music.stop()
    PauseState = True

pygame.init()
screen = pygame.display.set_mode((600, 450))
clock = pygame.time.Clock()

done = False
PauseState = True
songlist = []
Ready(os.curdir + '/music')
current = 0

color = (255, 32, 32)
w, h = screen.get_width(), screen.get_height() * 2 /3
h1, h2, h3 = h - 30, h + 30, h

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                Pause()
            if event.key == pygame.K_SPACE:
                Run(current)
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                ChangeStop()
                current -= 1
                current %= len(songlist)
                Run(current)
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                ChangeStop()
                current += 1
                current %= len(songlist)
                Run(current)        
    
    if PauseState:
        color = (255, 32, 32)
    else:
        color = (32, 32, 255)

    screen.fill((0, 0, 0))

    pygame.draw.circle(screen, color, (screen.get_width() / 2, screen.get_height() * 2 / 3), 30)
    pygame.draw.polygon(screen, (32, 32, 255), (((w / 2 + 60, h1), (w / 2 + 60 , h2), (w / 2 + 105, h3))))
    pygame.draw.polygon(screen, (32, 32, 255), (((w / 2 - 60, h1), (w / 2 - 60 , h2), (w / 2 - 105, h3))))
    pygame.display.flip()
    clock.tick(60)