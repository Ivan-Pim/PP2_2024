import pygame
import copy
import random, time

import snake_table

pygame.init()

FPSoptions = [5, 10, 15]
FramePerSec = pygame.time.Clock()

#Creating colors
BLUE  = pygame.Color(0, 0, 255)
RED   = pygame.Color(255, 0, 0)
GREEN = pygame.Color(0, 255, 0)
YELLOW = pygame.Color(255, 255, 0)
BLACK = pygame.Color(0, 0, 0)
GRAY = pygame.Color(128, 128, 128)
WHITE = pygame.Color(255, 255, 255)


#Other Variables for use in the program
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCORE = 0
EXP = 0
LVL = 1

#Setting up Fonts
font = pygame.font.SysFont("rubikbold", 60)
font_small = pygame.font.SysFont("rubikbold", 20)
game_over = font.render("Game Over", True, GREEN)

#Create a white screen 
screen = pygame.display.set_mode((800,600))
screen.fill(BLACK)
pygame.display.set_caption("Game")
working = True
paused = True

#"""
class Food(pygame.Rect):
    def __init__(self):
        # just setting the initial size, will be moved later
        super().__init__(0, 0, 15, 15)
        self.move(P1.pieces, walls)
    # choosing which if its rare food to spawn
    def get_type(self):
        # choose which coin to spawn
        id = random.randint(0, 9)
        # set type and time to stay in one spot
        if id == 9:
            self.worth = 10
            self.wait = random.randint(4000, 7000)
            self.color = YELLOW
        else:
            self.worth = 1
            self.wait = random.randint(7000, 10000)
            self.color = RED
        pygame.time.set_timer(MOVE_APPLE, self.wait, 1)
    def move(self, snake, walls):
        self.get_type()
        # while intersecting with something choose another position
        ok = False
        while not ok:
            ok = True
            position = (random.randint(1, (SCREEN_WIDTH // 20) - 1), random.randint(1, (SCREEN_HEIGHT // 20) - 1))
            self.center = (10 + 20 * position[0], 10 + 20 * position[1])
            # checks for collision with any of the rects in snake or walls
            if self.collidelist(snake) != -1 or self.collidelist(walls) != -1:
                ok = False

class Piece(pygame.Rect):
    def __init__(self, left, top, width, height, direction):
        super().__init__(left, top, width, height)
        self.dir = direction

class Player():
    def __init__(self):
        self.last_step = "right"
        self.growth = False
        # create a head
        self.Head = Piece(400, 300, 20, 20, "right")
        # create a list of all segments, including the head
        self.pieces = [self.Head, Piece(381, 301, 18, 18, "right"), Piece(361, 301, 18, 18, "right")]
       
    def move(self):
        # on turns where we grow, just duplicate the last piece
        grew = 0
        if self.growth:
            new = copy.copy(self.pieces[-1])
            self.pieces.append(new)
            grew = 1
            self.growth = False
        # move each piece into the next piece's position
        for id in range(len(self.pieces) - 1 - grew, 0, -1):
            self.pieces[id].center = self.pieces[id - 1].center
            self.pieces[id].dir = self.pieces[id - 1].dir
        # move head into new position
        if self.Head.dir == "right":
            self.Head.centerx += 20
        elif self.Head.dir == "left":
            self.Head.centerx -= 20
        elif self.Head.dir == "up":
            self.Head.centery -= 20
        elif self.Head.dir == "down":
            self.Head.centery += 20
        self.last_step = self.Head.dir

    
    def collide(self, objects, type):
        if type == "snake":
            for el_id in range(len(self.pieces)):
                for block_id in range(el_id, len(objects)):
                    if el_id != block_id:
                        if self.pieces[el_id].colliderect(objects[block_id]):
                            print(el_id, block_id)
                            print(self.pieces[el_id], objects[block_id])
                            return True
        else:
            for el in self.pieces:
                if el.collidelist(objects) != -1:
                    return True

#Adding a new User event 
LVL_UP = pygame.USEREVENT + 1
MOVE_APPLE = pygame.USEREVENT + 2

# initialize all objects
base_walls = [pygame.Rect(0, 0, 780, 20), pygame.Rect(780, 0, 20, 580), pygame.Rect(0, 20, 20, 580), pygame.Rect(20, 580, 780, 20)]
walls1 = [pygame.Rect(20, 260, 80, 80), pygame.Rect(700, 260, 80, 80), pygame.Rect(360, 20, 80, 80), pygame.Rect(360, 500, 80, 80)]
walls2 = [pygame.Rect(120, 140, 40, 320), pygame.Rect(660, 140, 40, 320), pygame.Rect(200, 120, 400, 20), pygame.Rect(200, 480, 400, 20)]
walls3 = [pygame.Rect(20, 200, 400, 20), pygame.Rect(380, 400, 400, 20), pygame.Rect(140, 220, 20, 200), pygame.Rect(480, 400, 20, 100), pygame.Rect(600, 20, 20, 200)]
all_walls = [walls1, walls2, walls3]

snake_table.create_table()

## that was all defintions, now we begin the setup

username = input("Please input your username: \n")

snake_table.insert_user(username, 1, 0, 0)
personal, multi = snake_table.query_data(username)


ascencion = personal[0] - 1
walls = all_walls[ascencion] + base_walls
FPS = FPSoptions[ascencion]

P1 = Player()
F1 = Food()


all_objects = [P1, F1, walls]

#Game Loop
while working:
      
    #Cycles through all events occuring  
    for event in pygame.event.get():
        if event.type == MOVE_APPLE:
            if not paused:
                F1.move(P1.pieces, walls)
            else:
                pygame.time.set_timer(MOVE_APPLE, F1.wait, 1)
        if event.type == LVL_UP:
            LVL += 1
            FPS = min(60, FPS + 1)
        if event.type == pygame.QUIT:
            working = False

        if event.type == pygame.KEYDOWN:
            if (event.key == pygame.K_RIGHT or event.key == pygame.K_d) and P1.last_step != "left":
                P1.Head.dir = "right"
            elif (event.key == pygame.K_DOWN or event.key == pygame.K_s) and P1.last_step != "up":
                P1.Head.dir = "down"
            elif (event.key == pygame.K_LEFT or event.key == pygame.K_a) and P1.last_step != "right":
                P1.Head.dir = "left"
            elif (event.key == pygame.K_UP or event.key == pygame.K_w) and P1.last_step != "down":
                P1.Head.dir = "up"
            elif event.key == pygame.K_p:
                paused = not paused

    screen.fill(BLACK)

    #Moves and Re-draws all Sprites
    if not paused:
        P1.move()

    #when eating an apple grow, gain points, exp and move it
    if P1.Head.colliderect(F1):
        # grow
        P1.growth = True
        # add score
        SCORE += F1.worth 
        # move apple to a new position
        if not paused:
            F1.move(P1.pieces, walls)

        EXP += 1
        # at 5 exp level up
        if EXP >= max(4, LVL // 4):
            pygame.event.post(pygame.event.Event(LVL_UP))
            EXP = 0


    #To be run if collision occurs between Player and Enemy
    if P1.collide(P1.pieces, "snake") or P1.collide(walls, "walls"):
        high_score = max(multi[0], SCORE)
        exp = personal[1] + (SCORE // 5)
        level = personal[0]
        if (level < 3):
            if exp >= (5 * level):
                exp -= (5 * level)
                level += 1
        
        snake_table.update(username, level, exp, high_score)
        
        time.sleep(1)
                
        screen.fill(BLUE)
        screen.blit(game_over, (30,250))
        
        pygame.display.update()
        time.sleep(2)
        working = False

    for el in P1.pieces:
        pygame.draw.rect(screen, GREEN, el)
    pygame.draw.rect(screen, F1.color, F1)
    for w in walls:
        pygame.draw.rect(screen, GRAY, w)

    #blit score
    scores = font_small.render(str(SCORE), True, GREEN)
    screen.blit(scores, (10,10))
    lvl = font_small.render(str(LVL), True, YELLOW)
    screen.blit(lvl, (770, 10))

    pygame.display.update()
    FramePerSec.tick(FPS)

pygame.quit()