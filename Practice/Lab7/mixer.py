import os
import pygame

def make_font(fonts, size):
    available = pygame.font.get_fonts()
    # get_fonts() returns a list of lowercase spaceless font names
    choices = map(lambda x:x.lower().replace(' ', ''), fonts)
    for choice in choices:
        if choice in available:
            return pygame.font.SysFont(choice, size)
    return pygame.font.Font(None, size)

_cached_fonts = {}
def get_font(font_preferences, size):
    global _cached_fonts
    key = str(font_preferences) + '|' + str(size)
    font = _cached_fonts.get(key, None)
    if font == None:
        font = make_font(font_preferences, size)
        _cached_fonts[key] = font
    return font

_cached_text = {}
def create_text(text, fonts, size, color):
    global _cached_text
    key = '|'.join(map(str, (fonts, size, color, text)))
    image = _cached_text.get(key, None)
    if image == None:
        font = get_font(fonts, size)
        image = font.render(text, True, color)
        _cached_text[key] = image
    return image

## load the songlist
def Ready(path):
    lst = os.listdir(path)
    global songlist
    songlist = ['music/' + x for x in lst if os.path.isfile(path + '/' + x)]

## run or stop the current song
def Run(id):
    global PauseState
    global text
    if PauseState:
        pygame.mixer.music.load(songlist[id])
        pygame.mixer.music.play(0)
    else:
        pygame.mixer.music.stop()
    PauseState = not PauseState
    text = create_text(songlist[id][6:], font_preferences, 48, (128, 128, 128))

## pause the current song
def Pause():
    global PauseState
    if PauseState:
        pygame.mixer.music.unpause()
    else:
        pygame.mixer.music.pause()
    PauseState = not PauseState

## new song starts paused
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


font_preferences = ["They definitely dont have this installed Gothic", 'msgothic', 'rubikbold',"Comic Sans MS"]
text = create_text(songlist[0][6:], font_preferences, 48, (128, 128, 128))

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
    screen.blit(text, (300 - text.get_width() // 2, 125 - text.get_height() // 2))
    pygame.display.flip()

    clock.tick(60)