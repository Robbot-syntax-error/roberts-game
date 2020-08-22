import pygame
import sys
import random
import time
pygame.init()

BACKGROUND_COLOUR = (0,0,0)

clock = pygame.time.Clock()
MYFONT = pygame.font.SysFont("monospace", 35)
MYFONT2 = pygame.font.SysFont("monospace", 25)
# pygame.mixer.music.load('game music.mp3')

NEXTLEVEL = pygame.mixer.Sound('next level.WAV')
AMMOBRUH = [0, 40, 0]
game_over = False
level = 1
WIDTH = 1300
HEIGHT = 700
GAMEOVER = True
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
PINK = (255,0,255)
YELLOW = (255,255,0)
WHITE = (255,255,255)
COLOUR = BLUE
GEORGE = 0
GEORGE2 = 0
gravity = True
JUMP = False
JUMPIDY = False
BULLETFIRE = False
REFUEL = True
r = 0
HandH = 0
G = 40
YO = 0
A = []
MONSTERPOS = [500, 200]
ROCKETFUEL = 10
player1_pos = [0, 0]
player1_size = [50, 100]
PLAYER_MOVE = 10
Target = [player1_pos[0] + 350, player1_pos[1] + 25]
AMMO = 13
MONSTERSIZE = [0, 0]
H = random.randint(1, level)
BOSSTYPE = random.choices([0, 1])
def repeat_fun(times, f):
    for i in range(times): f()
playerpicture = pygame.image.load('shooter forward.png')
bulletpicture = pygame.image.load('TRANSPARENT.png')
floorpicture = pygame.image.load('floor.png')
spikepicture = pygame.image.load('SPIKE.png')
walkingpicture = pygame.image.load('walking monster.png')
grenadepicture1 = pygame.image.load('grenade.png')
grenadepicture2 = pygame.image.load('grenade.png')
leftpicture = pygame.image.load('LASER facing left.png')
uppicture = pygame.image.load('LASER facing upward.png')
flyingpicture = pygame.image.load('flying monster.png')

bigbosspicture = pygame.image.load('BIG BOSS.png')
flyingpicture = pygame.image.load('flying monster.png')
blasterbackwardpicture = pygame.image.load('fireball backward.png')
blasterforwardpicture = pygame.image.load('fireball forward.png')
blasterdownpicture = pygame.image.load('fireball down.png')

smallbosspicture = pygame.image.load('small boss.png')
ammopicture = pygame.image.load('ammo.png')
backgroundpicture = pygame.image.load('background.png')
startpicture = pygame.image.load('start.png')
FREEZE = pygame.image.load('DEHYDRATION2.png')

#-------------------------------------------------------------------------------
WE5 = 0
GUTHRIE = [1400, 800]
d = random.choices([0, 0, 0, 0, 1])

SPEEDY = 1
SPEn = 0
oh = 40
BLASTER = 0
n = 0
DROPPINGS = [random.randint(1, 4)*100, -100, 0]
LAZERPOS = [1400, 550, 1400, 2, 0, 0]
BOSSIFNO = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
JOEY = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
JOEY2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
m = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
HH_pos = [[800, 800], [800, 800], [800, 800], [800, 800], [800, 800], [800, 800], [800, 800], [800, 800], [800, 800], [800, 800], [800, 800], [800, 800], [800, 800], [800, 800], [800, 800], [800, 800], [800, 800], [800, 800], [800, 800], [800, 800], ]
H = 0
hun = 0
WE = 0
WE4 = 0
WE3 = 0
FORMY = 1
BOSSSTART = False
KK = random.randint(50, 1100)
KK2 = random.randint(4, 9)*50
BLASTER1_pos = 1400
BLASTER2_pos = [MONSTERPOS[0], MONSTERPOS[0] + 150, MONSTERPOS[1]] 
AMIALIVE = [True, True, True, True, True, True, True, True, True, True]
AMIALIVE2 = [True, True, True, True, True, True, True, True, True, True]
DAVEy = 0
FOGY = 0
longrange = False
gravityMONSTER = [True, True, True, True, True, True, True, True, True, True, ]
GE = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
b = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
WE2 = 0
PLAYERHEIGHT = 100
MAN = [1400, 1400, 1400, 1400, 1400, 1400, 1400, 1400, 1400, 1400]
GRENADE1POS = [MONSTERPOS[0] + 200, MONSTERPOS[1], MONSTERPOS[0], MONSTERPOS[1]]
GRENADE1SIZE = [50, 50, 50, 50]
DAVEYJONESLOCKER = [1, 1, 0, 0]
AMMOPACKET = [random.randint(0, WIDTH - 25), 0]
UHH2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
yy = [WIDTH, WIDTH, WIDTH, WIDTH, WIDTH, WIDTH, WIDTH, WIDTH, WIDTH, WIDTH, WIDTH, WIDTH, WIDTH, WIDTH, WIDTH, WIDTH, WIDTH, WIDTH, WIDTH, WIDTH]
yyy = [MONSTERPOS[0], MONSTERPOS[0] + 50, MONSTERPOS[0] + 25, MONSTERPOS[0] + 100, MONSTERPOS[0] + 75, MONSTERPOS[0] + 150, MONSTERPOS[0] + 125, MONSTERPOS[0] + 200]
#self = [500,random.randint(0, HEIGHT - 50), 500,random.randint(0, HEIGHT - 50), 500,random.randint(0, HEIGHT - 50), 500,random.randint(0, HEIGHT - 50), 500,random.randint(0, HEIGHT - 50), 500,random.randint(0, HEIGHT - 50), 500,random.randint(0, HEIGHT - 50), 500,random.randint(0, HEIGHT - 50), 500,random.randint(0, HEIGHT - 50), 500,random.randint(0, HEIGHT - 50), 500,random.randint(0, HEIGHT - 50), 500,random.randint(0, HEIGHT - 50), 500,random.randint(0, HEIGHT - 50), 500,random.randint(0, HEIGHT - 50), ]
BULLET0_pos = [player1_pos[0], player1_pos[0], player1_pos[0], player1_pos[0], player1_pos[0], player1_pos[0], player1_pos[0], player1_pos[0], player1_pos[0], player1_pos[0], player1_pos[0], player1_pos[0], player1_pos[0], player1_pos[0], player1_pos[0], player1_pos[0], player1_pos[0], player1_pos[0], player1_pos[0], player1_pos[0], player1_pos[0]]
BULLET1_pos = [player1_pos[0] + 40, player1_pos[0] + 40, player1_pos[0] + 40, player1_pos[0] + 40, player1_pos[0] + 40, player1_pos[0] + 40, player1_pos[0] + 40, player1_pos[0] + 40, player1_pos[0] + 40, player1_pos[0] + 40, player1_pos[0] + 40, player1_pos[0] + 40, player1_pos[0] + 40, player1_pos[0] + 40, player1_pos[0] + 40, player1_pos[0] + 40, player1_pos[0] + 40, player1_pos[0] + 40, player1_pos[0] + 40, player1_pos[0] + 40, player1_pos[0] + 40, player1_pos[0] + 40, player1_pos[0] + 40, player1_pos[0] + 40, player1_pos[0] + 40, player1_pos[0] + 40, player1_pos[0] + 40, player1_pos[0] + 40, player1_pos[0] + 40, player1_pos[0] + 40, player1_pos[0] + 40, player1_pos[0] + 40, player1_pos[0] + 40, player1_pos[0] + 40, player1_pos[0] + 40, player1_pos[0] + 40, player1_pos[0] + 40, player1_pos[0] + 40, player1_pos[0] + 40]
UH = [WIDTH, random.randint(0, HEIGHT - 50), random.randint(0, HEIGHT - 50), random.randint(0, HEIGHT - 50), random.randint(0, HEIGHT - 50), random.randint(0, HEIGHT - 50), random.randint(0, HEIGHT - 50), random.randint(0, HEIGHT - 50), random.randint(0, HEIGHT - 50), random.randint(0, HEIGHT - 50), random.randint(0, HEIGHT - 50), random.randint(0, HEIGHT - 50), random.randint(0, HEIGHT - 50), random.randint(0, HEIGHT - 50), random.randint(0, HEIGHT - 50), random.randint(0, HEIGHT - 50), random.randint(0, HEIGHT - 50), random.randint(0, HEIGHT - 50), random.randint(0, HEIGHT - 50), random.randint(0, HEIGHT - 50), random.randint(0, HEIGHT - 50), random.randint(0, HEIGHT - 50), random.randint(0, HEIGHT - 50), random.randint(0, HEIGHT - 50), random.randint(0, HEIGHT - 50), random.randint(0, HEIGHT - 50), random.randint(0, HEIGHT - 50), random.randint(0, HEIGHT - 50)]
UH2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
UH22 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
UH3 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
FML = [random.choices([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]), random.choices([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]), random.choices([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]), random.choices([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]), random.choices([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]), random.choices([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]), random.choices([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]), random.choices([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]), random.choices([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]), random.choices([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]), random.choices([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]), random.choices([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]), random.choices([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]), random.choices([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]), random.choices([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]), random.choices([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26])]
FML2 = [random.choices([9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]), random.choices([9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]), random.choices([9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]), random.choices([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]), random.choices([9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]), random.choices([9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]), random.choices([9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]), random.choices([9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]), random.choices([9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]), random.choices([9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]), random.choices([9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]), random.choices([9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]), random.choices([9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]), random.choices([9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]), random.choices([9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]), random.choices([9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26])]
FML3 = [random.choices([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]), random.choices([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]), random.choices([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]), random.choices([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]), random.choices([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]), random.choices([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]), random.choices([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]), random.choices([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]), random.choices([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]), random.choices([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]), random.choices([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]), random.choices([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]), random.choices([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]), random.choices([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]), random.choices([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]), random.choices([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26])]
FML4 = [random.choices([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]), random.choices([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]), random.choices([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]), random.choices([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]), random.choices([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]), random.choices([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]), random.choices([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]), random.choices([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]), random.choices([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]), random.choices([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]), random.choices([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]), random.choices([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]), random.choices([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]), random.choices([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]), random.choices([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]), random.choices([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26])]
#-------------------------------------------------------------------------------

def repeat_fun(times, f):
    for i in range(times): f(times)
class Floor:
    def __init__(self, position):
        self.pos = position
        if self.pos[1] > HEIGHT - 25:
            self.pos[1] = HEIGHT + 1
        if self.pos[1] >= HEIGHT - 25:
            self.use = 0
        if self.pos[1] < HEIGHT - 25:
            self.use = 1


def myfun(s,i=[0]):    
    i[0]+=1 # mutable variable get evaluated ONCE
    return i[0]

class FLYINGMONSTERS:
    def __init__(self, position):
#        problem is that with every loop the position goes back to [500, 200], so add a run once function
        
        global UH
        global AMIALIVE
        global GAMEOVER
        global BULLET_pos
        global WE
        global yy
        global n
        global AMMOBRUH
        global oh
        x = position
        if AMIALIVE[x] == True:
            H = True
            self.pos = [yy[x], UH[x]]
            screen.blit(flyingpicture, (self.pos[0], self.pos[1]))

            one = player1_pos[0] - yy[x]
            two = player1_pos[1] - UH[x]
            six = player1_pos[1] + 50 - UH[x]
            three = BULLET_pos[0] - yy[x]
            four = BULLET_pos[1] - UH[x]
            if one <= 50 and one >= -50 and two <= 50 and two >= -100:
                GAMEOVER = True
                 

            if BULLETFIRE == True:
                if three <= 25 and three >= -50 and four <= 25 and four >= -50:
                    n = 0
                    oh = 40
                    AMMOBRUH[0] = 0
                    AMIALIVE[x] = False

            moveleftandright3 = round(one/40)
            moveupanddown3 = round(six/40)
            yy[x] += moveleftandright3*SPEEDY
            UH[x] += moveupanddown3*SPEEDY
def BULLET():
    global bulletpicture
    global AMMOBRUH
    global n
    global oh
    global AMMO
    if AMMOBRUH[2] == 0:
        AMMOBRUH[1] = G
        AMMOBRUH[2] = 1
    if AMMOBRUH[0] == 1:
        if AMMOBRUH[1] == 40:
            n += (10 - HandH)
            n += (10 - HandH)
            oh = 40

        if AMMOBRUH[1] == -40:
            n -= (10 - HandH)
            n -= (10 - HandH)
            oh = 40

        if AMMOBRUH[1] == 0:
            oh += 10
            oh += 10
    if (Target[0] - BULLET_pos[0]) <= 25 and (Target[0] - BULLET_pos[0]) >= -100 and (Target[1] - BULLET_pos[1]) < 20:
        AMMOBRUH[0] = 0
        n = 0
        oh = 40
        AMMO -= 1

    
def FLYINGMONSTER(u):
    global UH
    global hun
    x = 0
    y = 1
    for k in range(u):
        exec(f'G_{k} = FLYINGMONSTERS(k)')

def FLYINGMONSTER2(u):
    global UH
    global hun
    x = 0
    y = 1
    for k in range(u):
        exec(f'MAN_{k} = FLYINGMONSTERS2(k)')
def FLYINGMONSTER3(u):
    global UH
    global hun
    x = 0
    y = 1
    for k in range(u):
        exec(f'G_{k} = FLYINGMONSTERS3(k)')
Floor1 = Floor([0, random.randint(200, HEIGHT - 200)])
Floor2 = Floor([50, random.randint(Floor1.pos[1] - 100 , HEIGHT + 50)])
Floor3 = Floor([100, random.randint(Floor2.pos[1] - 100, HEIGHT + 50)])
Floor4 = Floor([150, random.randint(Floor3.pos[1] - 100, HEIGHT + 50)])
Floor5 = Floor([200, random.randint(Floor4.pos[1] - 100, HEIGHT + 50)])
Floor6 = Floor([250, random.randint(Floor5.pos[1] - 100, HEIGHT + 50)])
Floor7 = Floor([300, random.randint(Floor6.pos[1] - 100, HEIGHT + 50)])
Floor8 = Floor([350, random.randint(Floor7.pos[1] - 100, HEIGHT + 50)])
Floor9 = Floor([400, random.randint(Floor8.pos[1] - 100, HEIGHT + 50)])
Floor10 = Floor([450, random.randint(Floor9.pos[1] - 100, HEIGHT + 50)])
Floor11 = Floor([500, random.randint(Floor10.pos[1] - 100, HEIGHT + 50)])
Floor12 = Floor([550, random.randint(Floor11.pos[1] - 100, HEIGHT + 50)])
Floor13 = Floor([600, random.randint(Floor12.pos[1] - 100, HEIGHT + 50)])
Floor14 = Floor([650, random.randint(Floor13.pos[1] - 100, HEIGHT + 50)])
Floor15 = Floor([700, random.randint(Floor14.pos[1] - 100, HEIGHT + 50)])
Floor16 = Floor([750, random.randint(Floor15.pos[1] - 100, HEIGHT + 50)])
Floor17 = Floor([800, random.randint(Floor16.pos[1] - 100, HEIGHT + 50)])
Floor18 = Floor([850, random.randint(Floor17.pos[1] - 100, HEIGHT + 50)])
Floor19 = Floor([900, random.randint(Floor18.pos[1] - 100, HEIGHT + 50)])
Floor20 = Floor([950, random.randint(Floor19.pos[1] - 100, HEIGHT + 50)])
Floor21 = Floor([1000, random.randint(Floor20.pos[1] - 100, HEIGHT + 50)])
Floor22 = Floor([1050, random.randint(Floor21.pos[1] - 100, HEIGHT + 50)])
Floor23 = Floor([1100, random.randint(Floor22.pos[1] - 100, HEIGHT + 50)])
Floor24 = Floor([1150, random.randint(Floor23.pos[1] - 100, HEIGHT + 50)])
Floor25 = Floor([1200, random.randint(Floor24.pos[1] - 100, HEIGHT + 50)])
Floor26 = Floor([1250, random.randint(Floor25.pos[1] - 100, HEIGHT + 50)])
screen = pygame.display.set_mode((WIDTH, HEIGHT))
#-------------------------------------------------------------------------------
BRUH = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

floorss = [Floor1.pos, Floor2.pos, Floor3.pos, Floor4.pos, Floor5.pos, Floor6.pos, Floor7.pos, Floor8.pos, Floor9.pos, Floor10.pos, Floor11.pos, Floor12.pos, Floor13.pos, Floor14.pos, Floor15.pos, Floor16.pos, Floor17.pos, Floor18.pos, Floor19.pos, Floor20.pos, Floor21.pos, Floor22.pos, Floor23.pos, Floor24.pos, Floor25.pos, Floor26.pos]
flor = [0, Floor1.use, Floor2.use, Floor3.use, Floor4.use, Floor5.use, Floor6.use, Floor7.use, Floor8.use, Floor9.use, Floor10.use, Floor11.use, Floor12.use, Floor13.use, Floor14.use, Floor15.use, Floor16.use, Floor17.use, Floor18.use, Floor19.use, Floor20.use, Floor21.use, Floor22.use, Floor23.use, Floor24.use, Floor25.use, Floor26.use]
def FIND_USEFUL_FLOORS(columns):
    ranges = [[i+1, v] for i,v in enumerate(columns[1:]) if columns[i] != columns[i+1]]
    ranges.append([len(columns),0]) # special case for last element
    global A
    for i,v in enumerate(ranges[:-1]):
        if v[1] != columns[0]:
            A.append([v[0]+1, ranges[i+1][0], v[1]])
FIND_USEFUL_FLOORS(flor)
WOWY = random.randint(1, level)

#-------------------------------------------------------------------------------

class SPIKE:
    def __init__(self, position):        
        global floorss
        global FML4
        global GAMEOVER
        global b
        x = position
        if FML3[x] == [1]:
            FML3[x] = 3
        if FML3[x] == [2]:
            FML3[x] = 3
        if FML3[x] == [3]:
            FML3[x] = 3
        if FML3[x] == [4]:
            FML3[x] = 4
        if FML3[x] == [5]:
            FML3[x] = 5
        if FML3[x] == [6]:
            FML3[x] = 6
        if FML3[x] == [7]:
            FML3[x] = 7
        if FML3[x] == [8]:
            FML3[x] = 8
        if FML3[x] == [9]:
            FML3[x] = 9
        if FML3[x] == [10]:
            FML3[x] = 10
        if FML3[x] == [11]:
            FML3[x] = 11
        if FML3[x] == [12]:
            FML3[x] = 12
        if FML3[x] == [13]:
            FML3[x] = 13
        if FML3[x] == [14]:
            FML3[x] = 14
        if FML3[x] == [15]:
            FML3[x] = 15
        if FML3[x] == [16]:
            FML3[x] = 16
        if FML3[x] == [17]:
            FML3[x] = 17
        if FML3[x] == [18]:
            FML3[x] = 18
        if FML3[x] == [19]:
            FML3[x] = 19
        if FML3[x] == [20]:
            FML3[x] = 1
        if FML3[x] == [21]:
            FML3[x] = 21
        if FML3[x] == [22]:
            FML3[x] = 22
        if FML3[x] == [23]:
            FML3[x] =23
        if FML3[x] == [24]:
            FML3[x] = 24
        if FML3[x] == [25]:
            FML3[x] = 25
        if FML3[x] == [26]:
            FML3[x] = 25
        y = FML3[x]
        self.pos = [floorss[y + b[x]][0], floorss[y + b[x]][1] - 25]
        if floorss[y][1] >= 675 and y != 25:
            b[x] = 1
        if floorss[y][1] >= 675 and y == 25:
            b[x] = -1
        if floorss[y][1] < 675:
            b[x] = 0

        one = player1_pos[0] - self.pos[0]
        two = player1_pos[1] - self.pos[1]
        if one <= 52 and one >= -48 and two <= 25 and two >= -100:
            GAMEOVER = True
             

        screen.blit(spikepicture, (self.pos[0], self.pos[1]))

class ICEMONSTERS:
    def __init__(self, position):
        
        global PLAYER_MOVE
        global floorss
        global FML3
        global JOEY
        x = position
        if FML3[x] == [1]:
            FML3[x] = 3
        if FML3[x] == [2]:
            FML3[x] = 3
        if FML3[x] == [3]:
            FML3[x] = 3
        if FML3[x] == [4]:
            FML3[x] = 4
        if FML3[x] == [5]:
            FML3[x] = 5
        if FML3[x] == [6]:
            FML3[x] = 6
        if FML3[x] == [7]:
            FML3[x] = 7
        if FML3[x] == [8]:
            FML3[x] = 8
        if FML3[x] == [9]:
            FML3[x] = 9
        if FML3[x] == [10]:
            FML3[x] = 10
        if FML3[x] == [11]:
            FML3[x] = 11
        if FML3[x] == [12]:
            FML3[x] = 12
        if FML3[x] == [13]:
            FML3[x] = 13
        if FML3[x] == [14]:
            FML3[x] = 14
        if FML3[x] == [15]:
            FML3[x] = 15
        if FML3[x] == [16]:
            FML3[x] = 16
        if FML3[x] == [17]:
            FML3[x] = 17
        if FML3[x] == [18]:
            FML3[x] = 18
        if FML3[x] == [19]:
            FML3[x] = 19
        if FML3[x] == [20]:
            FML3[x] = 1
        if FML3[x] == [21]:
            FML3[x] = 21
        if FML3[x] == [22]:
            FML3[x] = 22
        if FML3[x] == [23]:
            FML3[x] =23
        if FML3[x] == [24]:
            FML3[x] = 24
        if FML3[x] == [25]:
            FML3[x] = 25
        if FML3[x] == [26]:
            FML3[x] = 25
        y = FML3[x]
        self.pos = [floorss[y][0], floorss[y][1] - 350]
        one = player1_pos[0] - self.pos[0]
        two = player1_pos[1] - self.pos[1]
        if one <= 250 and one >= -50 and two <= 150 and two >= -100 and JOEY[x] < 100:
            PLAYER_MOVE = 0
            screen.blit(FREEZE, (0, 0))

            JOEY[x] += 1
            BACKGROUND_COLOUR = PINK
        if JOEY[x] >= 100:
            PLAYER_MOVE = 10
class FIREMONSTERS:
    def __init__(self, position):
#        problem is that with every loop the position goes back to [500, 200], so add a run once function
        global UH3
        global player1_pos
        global GAMEOVER
        global GE
        global HH_pos
        global FML2
        x = position
        if FML3[x] == [6]:
            FML3[x] = 9
        if FML3[x] == [8]:
            FML3[x] = 9
        if FML2[x] == [9]:
            FML2[x] = 9
        if FML2[x] == [10]:
            FML2[x] = 10
        if FML2[x] == [11]:
            FML2[x] = 11
        if FML2[x] == [12]:
            FML2[x] = 12
        if FML2[x] == [13]:
            FML2[x] = 13
        if FML2[x] == [14]:
            FML2[x] = 14
        if FML2[x] == [15]:
            FML2[x] = 15
        if FML2[x] == [16]:
            FML2[x] = 16
        if FML2[x] == [17]:
            FML2[x] = 17
        if FML2[x] == [18]:
            FML2[x] = 18
        if FML2[x] == [19]:
            FML2[x] = 19
        if FML2[x] == [20]:
            FML2[x] = 1
        if FML2[x] == [21]:
            FML2[x] = 21
        if FML2[x] == [22]:
            FML2[x] = 22
        if FML2[x] == [23]:
            FML2[x] =23
        if FML2[x] == [24]:
            FML2[x] = 24
        if FML2[x] == [25]:
            FML2[x] = 25
        if FML2[x] == [26]:
            FML2[x] = 25
        PLACEMARK1 = False
        y = FML2[x]
        self.pos = [FML2[x]*50, floorss[y][1] - 50]
        GE[x] += 1
        if GE[x] >= 25:
            BOLT = True
        if GE[x] < 25 or GE[x] >= 50:
            BOLT = False
        if GE[x] >= 50:
            GE[x] = 0
        if BOLT == True:
            HH_pos[x] = [self.pos[0], 0]
        if BOLT == False:
            HH_pos[x] = [self.pos[0], 800]
        screen.blit(uppicture, (self.pos[0], self.pos[1]))
        pygame.draw.rect(screen, RED, (HH_pos[x][0], HH_pos[x][1], 50, self.pos[1]))
        
        one = player1_pos[0] - HH_pos[x][0]
        two = player1_pos[1] - HH_pos[x][1]
        if one <= 50 and one >= -50 and two <= self.pos[1] and two >= -100:
            GAMEOVER = True
             

        three = player1_pos[0] - self.pos[0]
        four = player1_pos[1] - self.pos[1]
        if three <= 50 and three >= -50 and four <= 50 and four >= -100:
            player1_pos[0] -= 5
            player1_pos[1] -= 10
def get_min_max(numbers):
    sorted_list = sorted(numbers)
    minValue = sorted_list[0]
    maxValue = sorted_list[-1]

    return maxValue
def A_FILTER():
    global A
    x = len(A)
    if A[0][0] == A[0][1]:
        A[0] = None
    if A[1][0] == A[1][1]:
        A[1] = None
    if 2 < x:    
        if A[2][0] == A[2][1]:
            A[2] = None
            if 3 < x:    
                if A[3][0] == A[3][1]:
                    A[3] = None
                    if 4 < x:    
                        if A[4][0] == A[4][1]:
                            A[4] = None
                            if 5 < x:    
                                if A[5][0] == A[5][1]:
                                    A[5] = None
                                    if 6 < x:    
                                        if A[6][0] == A[6][1]:
                                           A[6] = None
                                           if 7 < x:    
                                                if A[7][0] == A[7][1]:
                                                    A[7] = None
                                                    if 8 < x:    
                                                        if A[8][0] == A[8][1]:
                                                            A[8] = None
                                                            if 9 < x:    
                                                                if A[9][0] == A[9][1]:
                                                                    A[9] = None
                                                                    if 10 < x + 1:    
                                                                        if A[10][0] == A[10][1]:
                                                                            A[10] = None
                                                                            if 11 < x:    
                                                                                if A[11][0] == A[11][1]:
                                                                                    A[11] = None
A_FILTER()
class WALKINGMONSTERS:
    def __init__(self, position):
        global UH22
        global GAMEOVER
        global UHH2
        global n
        global oh
        global AMMOBRUH
        global AMIALIVE2
        global BRUH
        global UH2
        global floorss
        global flor
        global gravityMONSTER
        global WE3
        global AMMO
        x = position
        r = len(A)

        if A[x] == None or A[x] == 1:
            x += 1
        if r > 1:
            if A[x] == None:
                x += 1
        if r > 2:
            if A[x] == None:
                x += 1
        if r > 3:
            if A[x] == None:
                x += 1
        if r > 4:
            if A[x] == None:
                x += 1
        if AMIALIVE2[x] == True:
            y = A[x][0] - 2
            y2 = A[x][1]  - 2
            p = round(UH2[x]/50) 
            self.pos = [UH2[x], UHH2[x]]
            target1 = [y*50 + UH22[x], floorss[y][1] - 100]
            target2 = [1250, floorss[25][1] - 100]
            if BRUH[x]== 0:
                UH2[x] = target1[0]
                BRUH[x]= 1
            if UH2[x] <= target1[0]:
                BRUH[x]= 1
            if UH2[x] >= target2[0] - 50:
                BRUH[x]= 2
            if BRUH[x]== 1:
                UH2[x] += 1*SPEEDY


            if BRUH[x]== 2:
                UH2[x] -= 1*SPEEDY

            if UH2[x] <= 50:
                UH2[x] += 50
                BRUH[x] = 1
            if gravityMONSTER[x] == True:
                UHH2[x] = floorss[p][1] - 100

            if target1[0] == 0:
                UH22[x] = 50
            if target1[0] == target2[0] - 50:
                UH2[x] = target2[0] - 50
                BRUH[x]= 3 
#             pygame.draw.rect(screen, YELLOW, (target1[0], target1[1], 50, 100))
#             pygame.draw.rect(screen, YELLOW, (target2[0], target2[1], 50, 100))
            screen.blit(walkingpicture, (self.pos[0], self.pos[1]))

            one = player1_pos[0] - UH2[x]
            two = player1_pos[1] - UHH2[x]
            three = BULLET_pos[0] - UH2[x]
            four = BULLET_pos[1] - UHH2[x]

            if floorss[y - 1][0] >= 700:
                WALKING_MONSTER_DIRECTION = 1        
            if one <= 48 and one >= -50 and two <= 50 and two >= -100:
                GAMEOVER = True
                 

            if BULLETFIRE == True:
                if three <= 25 and three >= -50 and four <= 100 and four >= -25:
                    n = 0
                    oh = 40
                    AMMOBRUH[0] = 0
                    AMMO -= 1
                    AMIALIVE2[x] = False

def WALKINGMONSTER(u):
    for k in range(u):
        exec(f'HJ_{k} = WALKINGMONSTERS(k)')
def ICEMONSTER(u):
    for k in range(u):
        exec(f'GJ_{k} = ICEMONSTERS(k)')
def FIREMONSTER(u):
    for k in range(u):
        exec(f'GO_{k} = FIREMONSTERS(k)')
def HE(u):
    for k in range(u):
        exec(f'HONEY_{k} = SPIKE(k)')
def shooterprint(u):
    for k in range(u):
        exec(f'hhhh{k} = SHOOTERS(k)')
def flyingmonsterprint(n):
    x = random.choice([0, 1])
    if x == 0:
        repeat_fun(n, WALKINGMONSTER)
    if x == 1:
        repeat_fun(n, ICEMONSTER)
def constrained_sum_sample_pos(n, total):
    dividers = sorted(random.sample(range(1, total), n - 1))
    return [a - b for a, b in zip(dividers + [total], [0] + dividers)]
class blaster1:
    def __init__(self, x, T):
        global BLASTER1_pos
        global KK2
        global GAMEOVER
        if BLASTER1_pos >= 100:
            BLASTER1_pos -= 10*x
        if BLASTER1_pos <= 100 or BLASTER1_pos == 1400:
            if T < 3 or T > 10:
                KK2 =  random.randint(6, 8)*50
            else:
                KK2 =  random.randint(6, 12)*50

            BLASTER1_pos = 1100
        GUTHRIE = [BLASTER1_pos, KK2]

        one = player1_pos[0] - BLASTER1_pos
        two = player1_pos[1] - KK2
        if one <= 50 and one >= -50 and two <= 50 and two >= -PLAYERHEIGHT:
            GAMEOVER = True
             

class blaster2:
    def __init__(self, x, T):
        global BLASTER2_pos

        global GAMEOVER
        if BLASTER2_pos[0] >= 0:
            BLASTER2_pos[0] -= 5*x - 1*x
        if BLASTER2_pos[0] <= 0:
            BLASTER2_pos[0] = MONSTERPOS[0]
        if BLASTER2_pos[1] < 1300:
            BLASTER2_pos[1] += 5*x - 1*x
        if BLASTER2_pos[1] >= 1300:
            BLASTER2_pos[1] = MONSTERPOS[0]
        if BLASTER2_pos[2] < 700:
            BLASTER2_pos[2] += 5*x - 1*x
        if BLASTER2_pos[2] >= 700:
            BLASTER2_pos[2] = MONSTERPOS[0]
        one = player1_pos[0] - BLASTER2_pos[0]
        two = player1_pos[1] - 200
        if one <= 50 and one >= -50 and two <= 50 and two >= -PLAYERHEIGHT:
            GAMEOVER = True
             

        three = player1_pos[0] - BLASTER2_pos[1]
        four = player1_pos[1] - 200
        if three <= 50 and three >= -50 and four <= 50 and four >= -PLAYERHEIGHT:
            GAMEOVER = True
             

        five = player1_pos[0] - MONSTERPOS[0]
        six = player1_pos[1] - BLASTER2_pos[2]
        if five <= 50 and five >= -50 and six <= 50 and six >= -PLAYERHEIGHT:
            GAMEOVER = True
             

class grenade2:
    def __init__(self, x, T):
        global GRENADE1POS
        global DAVEYJONESLOCKER
        global GAMEOVER
        global GRENADE1SIZE
        global grenadepicture1
        global grenadepicture2

        DAVEYJONESLOCKER
        if GRENADE1POS[0] < 1300:
            TARGET = MONSTERPOS[0] + 100 - 1*x
            GRENADE1POS[0] += 1*x
            if DAVEYJONESLOCKER[0] == 1:
                GRENADE1POS[1] -= 2*x
            if GRENADE1POS[1] <= 50:
                DAVEYJONESLOCKER[0] = 2
        if DAVEYJONESLOCKER[0] == 2:
            GRENADE1POS[1] += 2*x
        if GRENADE1POS[1] >= 700:
            GRENADE1POS[0] = MONSTERPOS[0] + 150
            GRENADE1POS[1] = MONSTERPOS[1]
            DAVEYJONESLOCKER[0] = 1
        if DAVEYJONESLOCKER[1] == 1:
            GRENADE1POS[3] -= 2*x
        if GRENADE1POS[3] <= 50:
            DAVEYJONESLOCKER[1] = 2
        if DAVEYJONESLOCKER[1] == 2:
            GRENADE1POS[3] += 2*x
        one = player1_pos[0] - GRENADE1POS[0]
        two = player1_pos[1] - GRENADE1POS[1]
        if one <= 50 and one >= -50 and two <= 50 and two >= -PLAYERHEIGHT:
            GAMEOVER = True
             

        three = player1_pos[0] - GRENADE1POS[2]
        four = player1_pos[1] - GRENADE1POS[3]
        if three <= 50 and three >= -50 and four <= 50 and four >= -PLAYERHEIGHT:
            GAMEOVER = True
             

        if T > 3:
            if GRENADE1POS[1] >= 650:
                if DAVEYJONESLOCKER[2] == 0:
                    GRENADE1POS[0] -= 50 
                    GRENADE1POS[1] -= 25
                    grenadepicture1 = pygame.image.load('explosion.png')
                    
                DAVEYJONESLOCKER[2] += 1
                
                if one <= 100 and one >= -50 and two <= 100 and two >= -PLAYERHEIGHT:
                    GAMEOVER = True
                     
                if DAVEYJONESLOCKER[2] == 2:
                    GRENADE1POS[0] = MONSTERPOS[0]
                    GRENADE1POS[1] = MONSTERPOS[1]
                    DAVEYJONESLOCKER[0] = 1
                    grenadepicture1 = pygame.image.load('explosion.png')
                    DAVEYJONESLOCKER[2] = 0
            if GRENADE1POS[3] >= 650:
                if DAVEYJONESLOCKER[3] == 0:
                    GRENADE1POS[2] -= 50 
                    GRENADE1POS[3] -= 25
                    grenadepicture2 = pygame.image.load('explosion.png')

                DAVEYJONESLOCKER[3] += 1
                if three <= 100 and three >= -50 and four <= 100 and four >= -PLAYERHEIGHT:
                    GAMEOVER = True
                     
                if DAVEYJONESLOCKER[3] == 2:
                    GRENADE1POS[2] = MONSTERPOS[0]
                    GRENADE1POS[3] = MONSTERPOS[1]
                    DAVEYJONESLOCKER[1] = 1
                    grenadepicture2 = pygame.image.load('grenade.png')

                    DAVEYJONESLOCKER[3] = 0

        if T < 3:
            if GRENADE1POS[1] >= 450:
                if DAVEYJONESLOCKER[2] == 0:
                    GRENADE1POS[0] -= 50 
                    GRENADE1POS[1] -= 25
                    grenadepicture1 = pygame.image.load('explosion.png')

                DAVEYJONESLOCKER[2] += 1
                
                if one <= 100 and one >= -50 and two <= 100 and two >= -PLAYERHEIGHT:
                    GAMEOVER = True
                     
                if DAVEYJONESLOCKER[2] == 2:
                    GRENADE1POS[0] = MONSTERPOS[0]
                    GRENADE1POS[1] = MONSTERPOS[1]
                    DAVEYJONESLOCKER[0] = 1
                    grenadepicture1 = pygame.image.load('grenade.png')

                    DAVEYJONESLOCKER[2] = 0
            if GRENADE1POS[3] >= 450:
                if DAVEYJONESLOCKER[3] == 0:
                    GRENADE1POS[2] -= 50 
                    GRENADE1POS[3] -= 25
                    grenadepicture2 = pygame.image.load('explosion.png')

                DAVEYJONESLOCKER[3] += 1
                if three <= 100 and three >= -50 and four <= 100 and four >= -PLAYERHEIGHT:
                    GAMEOVER = True
                     
                if DAVEYJONESLOCKER[3] == 2:
                    GRENADE1POS[2] = MONSTERPOS[0]
                    GRENADE1POS[3] = MONSTERPOS[1]
                    DAVEYJONESLOCKER[1] = 1
                    grenadepicture2 = pygame.image.load('grenade.png')

                    DAVEYJONESLOCKER[3] = 0
class DROPPY:
    def __init__(self):
        global DROPPINGS
        if DROPPINGS[1] >= 700:
            DROPPINGS[0] = random.randint(7, 10)*100
            DROPPINGS[1] = -5*SPEEDY
        one = player1_pos[0] - DROPPINGS[0]
        two = player1_pos[1] - DROPPINGS[1]
        if one <= 100 and one >= -50 and two <= 100 and two >= -PLAYERHEIGHT:
            GAMEOVER = True
             
            
class LAZER:
    def __init__(self):
        global LAZERPOS        
        global GAMEOVER
        if LAZERPOS[5] == 0:
            LAZERPOS[0] = 1050
            LAZERPOS[3] = 1050
            LAZERPOS[5] = 1
        LAZERPOS[4] += 1
        if LAZERPOS[4] <= 50 - SPEEDY:
            LAZERPOS[2] = 1100
            if LAZERPOS[1] <= 300:
                LAZERPOS[3] = 1
            if LAZERPOS[3] == 1:
                LAZERPOS[1] += 5
            if LAZERPOS[1] >= 500:
                LAZERPOS[3] = 2
            if LAZERPOS[3] == 2:
                LAZERPOS[1] -= 5
        if LAZERPOS[4] > 50 - SPEEDY:
            LAZERPOS[2] = 0
            if player1_pos[1] - LAZERPOS[1] <= 50 and player1_pos[1] - LAZERPOS[1] >= -PLAYERHEIGHT:
                GAMEOVER = True
                 

            LAZERPOS[4] = 0

#=============================================================================================================================
class BOSS:
    def __init__(self, HEALTH, SPEED, BLASTER, TERRAIN, FORMS, CHARGE_NUMBER, SIZE, POS, GUN, SPEEDY):
        global COLOUR
        global MONSTERPOS
        global KK
        global player1_pos
        global MONSTERSIZE
        global BLASTER2_pos
        global GAMEOVER
        global DAVEy
        global n
        global oh
        global FOGY
        global GRENADE1POS
        global BOSSTYPE
        global FORMY
        global AMMOBRUH
        global AMMO
        global BLASTER1_pos
        if DAVEy == 0:
            FOGY = HEALTH*2
            player1_pos = [0, 390]
            DAVEy = 1
            
        if SPEED < 10:
            H = SPEED
        if SPEED >= 10:
            H = 10
         #determines the speed the boss moves
        if BLASTER <= 5:
            if BOSSTYPE == [0]:
                GUT = blaster1(SPEED, TERRAIN)
                BLASTER2_pos = [1400, 1400, 1400]
                GRENADE1POS = [1400, 1400, 1400, 1400]
            if BOSSTYPE == [1]:
                GUTH = grenade2(SPEED, TERRAIN)
                BLASTER2_pos = [1400, 1400, 1400]
                BLASTER1_pos
        if BLASTER > 6:
            if BOSSTYPE == [0]:
                ROLLY = DROPPY
                GRENADE1POS = [1400, 1400, 1400, 1400]
                BLASTER2_pos = [1400, 1400, 1400]
            if BOSSTYPE == [1]:
                if BLASTER < 15:
                    repeat_fun(round(BLASTER/5), FLYINGMONSTER3)
                    GRENADE1POS = [1400, 1400, 1400, 1400]
                    BLASTER2_pos = [1400, 1400, 1400]
                    BLASTER1_pos
                if BLASTER >= 15:
                    GUTHRIE = blaster2(SPEED, TERRAIN)
                    GRENADE1POS = [1400, 1400, 1400, 1400]
                    BLASTER1_pos

        if BOSSTYPE == [0]:
            MONSTERPOS = [1100, 0]
            MONSTERSIZE = [300, 760]
        if BOSSTYPE == [1]:
            MONSTERSIZE = [200, 100]


            if MONSTERPOS == [0, 0]:
                MONSTERPOS = [550, 0]

            if MONSTERPOS[0] - KK >= -50 and MONSTERPOS[0] - KK <= 50:
                KK = random.randint(50, 1100)
            if MONSTERPOS[0] - KK < -50:
                MONSTERPOS[0] += 1*SPEED
            if MONSTERPOS[0] - KK > 50:
                MONSTERPOS[0] -= 1*SPEED
        if TERRAIN <= 3:
            Floor1.pos[1] = 500
            Floor2.pos[1] = 500
            Floor3.pos[1] = 500
            Floor4.pos[1] = 500
            Floor5.pos[1] = 500
            Floor6.pos[1] = 500
            Floor7.pos[1] = 500
            Floor8.pos[1] = 500
            Floor9.pos[1] = 500
            Floor10.pos[1] = 500
            Floor11.pos[1] = 500
            Floor12.pos[1] = 500
            Floor13.pos[1] = 500
            Floor14.pos[1] = 500
            Floor15.pos[1] = 500
            Floor16.pos[1] = 500
            Floor17.pos[1] = 500
            Floor18.pos[1] = 500
            Floor19.pos[1] = 500
            Floor20.pos[1] = 500
            Floor21.pos[1] = 500
            Floor22.pos[1] = 500
            Floor23.pos[1] = 500
            Floor24.pos[1] = 500
            Floor25.pos[1] = 500
            Floor26.pos[1] = 500

        if TERRAIN > 10:
            Floor1.pos[1] = 500
            Floor2.pos[1] = 00
            Floor3.pos[1] = 00
            Floor4.pos[1] = 00
            Floor5.pos[1] = 00
            Floor6.pos[1] = 00
            Floor7.pos[1] = 00
            Floor8.pos[1] = 00
            Floor9.pos[1] = 00
            Floor10.pos[1] = 00
            Floor11.pos[1] = 500
            Floor12.pos[1] = 500
            Floor13.pos[1] = 00
            Floor14.pos[1] = 00
            Floor15.pos[1] = 00
            Floor16.pos[1] = 00
            Floor17.pos[1] = 00
            Floor18.pos[1] = 00
            Floor19.pos[1] = 00
            Floor20.pos[1] = 00
            Floor21.pos[1] = 00
            Floor22.pos[1] = 00
            Floor23.pos[1] = 00
            Floor24.pos[1] = 00
            Floor25.pos[1] = 500
            Floor26.pos[1] = 500
        if GUN >= 6:
            COLOUR = PINK

        one = player1_pos[0] - MONSTERPOS[0]
        two = player1_pos[1] - MONSTERPOS[1]
        if BOSSTYPE == [1]:
            if one <= 200 and one >= -50 and two <= 100 and two >= -PLAYERHEIGHT:
                GAMEOVER = True
                 

        if BOSSTYPE == [0]:
            if player1_pos[0] >= 1050:
                GAMEOVER = True
                 

        if BOSSTYPE == [1]:
            three = BULLET_pos[0] - MONSTERPOS[0]
            four = BULLET_pos[1] - MONSTERPOS[1]
            if three <= 200 and three >= -25 and four <= 100 and four >= -25:
                    FOGY -= 1
                    AMMOBRUH[0] = 0
                    AMMO -= 1
                    n = 0
                    oh = 40
        if BOSSTYPE == [0]:
            if BULLET_pos[0] >= 1100:
                    FOGY -= 1
                    AMMOBRUH[0] = 0
                    AMMO -= 1
                    n = 0
                    oh = 40
        if FOGY <= 0:
            FORMY -= 1
            if BOSSTYPE == [0]:
                BOSSTYPE = [1]
            if BOSSTYPE == [1]:
                BOSSTYPE = [0]
            FOGY += HEALTH
        if FORMY <= 0: 
            player1_pos[0] = 1300
        if BOSSTYPE == [0] and level >= 10:
            HOG = LAZER()
def translator():
    global level
    global WE
    global WE2
    global WE3
    global WE4
    global WE5
    global BOSSSTART
    global BLASTER
    global FORMY
    global BOSSINFO
    x = constrained_sum_sample_pos(WOWY, level)
    SPEEDY = sum(i > 5 for i in x) + 1
    r = len(x)
    if SPEEDY - 1  == r:
        WE4 = 9
        WE2 = level - 9
    if float(level/5).is_integer() == True:
        if BOSSTYPE == [0]:
            HEALTH = level*2
            SPEED = level/5
            if x.count(1) < 5:
                BLASTER = x.count(1)
            if x.count(1) >= 5:
                BLASTER = 5
            TERRAIN = x.count(2)
            FORMY += x.count(3) #and that's what the library of forms is
            CHARGE_NUMBER = x.count(5)
            GUN = x.count(5)
            SIZE = [200, 700]
            POS = [1100, 0]
        if BOSSTYPE == [1]:
            SPEED = level
            HEALTH = level
            if x.count(1) < 5:
                BLASTER = x.count(1)
            if x.count(1) >= 5:
                BLASTER = 5
            TERRAIN = x.count(2)
            FORMY += x.count(3) #and that's what the library of forms is
            CHARGE_NUMBER = x.count(5)
            GUN = x.count(5)
            SIZE = [150, 100]
            POS = 0
        BOSSSTART = True
        BOSSINFO = [HEALTH, SPEED, BLASTER, TERRAIN, 6, CHARGE_NUMBER, SIZE, POS, GUN, SPEEDY]
    if float(level/5).is_integer() == False:
        if x.count(1) > 9:
            WE4 = 9
        if x.count(1) <= 9:
            WE4 = x.count(1) #WHEN THIS IS REAL ADD SPEEDY SO WE KNOW HOW FAST EVERYTHING GOES
        WE = x.count(2)
        WE2 = x.count(3)
        WE3 = x.count(4)
        WE5 = x.count(5)
translator()
# pygame.mixer.music.play(-1)

while not game_over:
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    Target = [player1_pos[0] + 350, player1_pos[1] + 25]
    JOE_pos = [Target[0] - 450, Target[1]]
    BULLET_pos = [player1_pos[0] + n, player1_pos[1] + oh]

    if event.type == pygame.KEYDOWN:
##
        H = HandH

        x = player1_pos[0]
        y = player1_pos[1]
        x2 = JOE_pos[0]
        y2 = JOE_pos[1]
        AUK = AMMOBRUH

        if event.key == pygame.K_a:
            x -= PLAYER_MOVE
            H -= PLAYER_MOVE
            x2 -= PLAYER_MOVE
            G = -40

        if event.key == pygame.K_d:
            x += PLAYER_MOVE
            x2 += PLAYER_MOVE
            H += PLAYER_MOVE
            G = 40
        if PLAYER_MOVE == 10:
            if ROCKETFUEL >= 1:
                if JUMPIDY == True:
                    if event.key == pygame.K_w:
                        oh = 40
                        if COLOUR == BLUE:
                            ROCKETFUEL -= 2
                        y -= PLAYER_MOVE*30
                        y2 -= PLAYER_MOVE*30
                        GEORGE2 = 0
                        JUMPIDY = False
        if AMMO >= 1:
            if event.key == pygame.K_e:
                n = 0
                oh = 40
                YO = 0
                AUK[0] = 1
                AUK[2] = 0
                BULLETFIRE = True

        if event.key == pygame.K_SPACE and GAMEOVER == True:
            level = 0
            x = 1400
            GAMEOVER = False
        if event.key == pygame.K_s:
            if float(level/5).is_integer() == False:
                G = 0
            if float(level/5).is_integer() == True:
                PLAYERHEIGHT = 50
                y += 50
        if event.key != pygame.K_s:
            if float(level/5).is_integer() == True:
                PLAYERHEIGHT = 100
        H = HandH                 
        player1_pos[0] = x
        player1_pos[1] = y
        x2 = JOE_pos[0]
        y2 = JOE_pos[1]
        AUK = AMMOBRUH
    if GAMEOVER == True:
        level = 0
        AMM0 = 13
        ROCKETFUEL = 6
    if REFUEL == True:
        ROCKETFUEL += 0.015
        if ROCKETFUEL >= 6:
            REFUEL = False
            ROCKETFUEL = 6
    if ROCKETFUEL < 6:
        REFUEL = True
    if longrange == False:
        if G == -40:
            Target = [player1_pos[0] - 400, player1_pos[1] + 25]
            if PLAYERHEIGHT == 100:
                playerpicture = pygame.image.load('shooter backwards.png')
            else:
                playerpicture = pygame.image.load('player crouch backward.png')

        if G == 40:
            Target = [player1_pos[0] + 350, player1_pos[1] + 25]
            if PLAYERHEIGHT == 100:
                playerpicture = pygame.image.load('shooter forward.png')
            else:
                playerpicture = pygame.image.load('player crouch forward.png')

        if G == 0:
            Target = [player1_pos[0], player1_pos[1] + 450]
            playerpicture = pygame.image.load('shooter down.png')
    if longrange == True:
        pass
    if player1_pos[0] <= 0:
        player1_pos[0] = 0
#         pygame.time.Clock().tick(60)

#        if event.type == pygame.KEYDOWN:
##            
#            x = player1_pos[0]
#            x2 = player1_pos[1]
#            y = bullet_pos[0]
#            y2 = bullet_pos[1]
#
#            if event.key == pygame.K_a:
#    
#            player1_pos[0] = x
#            player1_pos[1] = x2
#            bullet_pos[0] = y
#            bullet_pos[1] = y2
    if n == 0 and oh == 40:
        bulletpicture = pygame.image.load('TRANSPARENT.png')
    else:
        bulletpicture = pygame.image.load('bullet.png')
    def FLOORCOLLISION(self, position):
        self.pos = position
        global n
        global oh
        global AMMOBRUH
        global AMMO
        one = player1_pos[0] - self.pos[0]
        two = player1_pos[1] - self.pos[1]
        if one <= 48 and one >= -48 and two <= 0 and two >= -PLAYERHEIGHT:
            player1_pos[1] = self.pos[1] - (PLAYERHEIGHT + 10)
        if one <= 50 and one >= -50 and two >= 0 and PLAYERHEIGHT == 100:
            player1_pos[0] += (50 - one)
        three = BULLET_pos[0] - self.pos[0]
        if three <= 51 and three >= -49 and BULLET_pos[1] >= self.pos[1] and AMMOBRUH[0] == 1:
            AMMOBRUH[0] =  0
            n = 0
            AMMO -= 1
            oh = 40
    if player1_pos[1] >= HEIGHT - 100:
        GAMEOVER = True
         

    AMMOPACKET[1] += 10
    if AMMOPACKET[1] >= HEIGHT:
        AMMOPACKET = [random.randint(0, WIDTH - 25), 0]
    def COLLISION(position, punishment, size):
        global GAMEOVER
        global AMMO
        global AMMOPACKET
        one = player1_pos[0] - position[0]
        two = player1_pos[1] - position[1]

        if one <= size[0] and one >= -50 and two <= -size[1] and two >= -PLAYERHEIGHT:
            if punishment == 1:
                GAMEOVER = True
                 
            if punishment == 2:
                AMMO = 13
                AMMOPACKET = [random.randint(0, WIDTH - 25), 0]
    COLLISION(AMMOPACKET, 2, [25, 25])
    FLOORCOLLISION(Floor1, Floor1.pos)
    FLOORCOLLISION(Floor2, Floor2.pos)
    FLOORCOLLISION(Floor3, Floor3.pos)
    FLOORCOLLISION(Floor4, Floor4.pos)
    FLOORCOLLISION(Floor5, Floor5.pos)
    FLOORCOLLISION(Floor6, Floor6.pos)
    FLOORCOLLISION(Floor7, Floor7.pos)
    FLOORCOLLISION(Floor8, Floor8.pos)
    FLOORCOLLISION(Floor9, Floor9.pos)
    FLOORCOLLISION(Floor10, Floor10.pos)
    FLOORCOLLISION(Floor11, Floor11.pos)
    FLOORCOLLISION(Floor12, Floor12.pos)
    FLOORCOLLISION(Floor13, Floor13.pos)
    FLOORCOLLISION(Floor14, Floor14.pos)
    FLOORCOLLISION(Floor15, Floor15.pos)
    FLOORCOLLISION(Floor16, Floor16.pos)
    FLOORCOLLISION(Floor17, Floor17.pos)
    FLOORCOLLISION(Floor18, Floor18.pos)
    FLOORCOLLISION(Floor19, Floor19.pos)
    FLOORCOLLISION(Floor20, Floor20.pos)
    FLOORCOLLISION(Floor21, Floor21.pos)
    FLOORCOLLISION(Floor22, Floor22.pos)
    FLOORCOLLISION(Floor23, Floor23.pos)
    FLOORCOLLISION(Floor24, Floor24.pos)
    FLOORCOLLISION(Floor25, Floor25.pos)
    FLOORCOLLISION(Floor26, Floor26.pos)
    if player1_pos[0] >= WIDTH - 50:
        level += 1
        NEXTLEVEL.play()
        PLAYER_MOVE = 10
        Floor1 = Floor([0, random.randint(200, HEIGHT - 200)])
        Floor2 = Floor([50, random.randint(Floor1.pos[1] - 100 , HEIGHT + 50)])
        Floor3 = Floor([100, random.randint(Floor2.pos[1] - 100, HEIGHT + 50)])
        Floor4 = Floor([150, random.randint(Floor3.pos[1] - 100, HEIGHT + 50)])
        Floor5 = Floor([200, random.randint(Floor4.pos[1] - 100, HEIGHT + 50)])
        Floor6 = Floor([250, random.randint(Floor5.pos[1] - 100, HEIGHT + 50)])
        Floor7 = Floor([300, random.randint(Floor6.pos[1] - 100, HEIGHT + 50)])
        Floor8 = Floor([350, random.randint(Floor7.pos[1] - 100, HEIGHT + 50)])
        Floor9 = Floor([400, random.randint(Floor8.pos[1] - 100, HEIGHT + 50)])
        Floor10 = Floor([450, random.randint(Floor9.pos[1] - 100, HEIGHT + 50)])
        Floor11 = Floor([500, random.randint(Floor10.pos[1] - 100, HEIGHT + 50)])
        Floor12 = Floor([550, random.randint(Floor11.pos[1] - 100, HEIGHT + 50)])
        Floor13 = Floor([600, random.randint(Floor12.pos[1] - 100, HEIGHT + 50)])
        Floor14 = Floor([650, random.randint(Floor13.pos[1] - 100, HEIGHT + 50)])
        Floor15 = Floor([700, random.randint(Floor14.pos[1] - 100, HEIGHT + 50)])
        Floor16 = Floor([750, random.randint(Floor15.pos[1] - 100, HEIGHT + 50)])
        Floor17 = Floor([800, random.randint(Floor16.pos[1] - 100, HEIGHT + 50)])
        Floor18 = Floor([850, random.randint(Floor17.pos[1] - 100, HEIGHT + 50)])
        Floor19 = Floor([900, random.randint(Floor18.pos[1] - 100, HEIGHT + 50)])
        Floor20 = Floor([950, random.randint(Floor19.pos[1] - 100, HEIGHT + 50)])
        Floor21 = Floor([1000, random.randint(Floor20.pos[1] - 100, HEIGHT + 50)])
        Floor22 = Floor([1050, random.randint(Floor21.pos[1] - 100, HEIGHT + 50)])
        Floor23 = Floor([1100, random.randint(Floor22.pos[1] - 100, HEIGHT + 50)])
        Floor24 = Floor([1150, random.randint(Floor23.pos[1] - 100, HEIGHT + 50)])
        Floor25 = Floor([1200, random.randint(Floor24.pos[1] - 100, HEIGHT + 50)])
        Floor26 = Floor([1250, random.randint(Floor25.pos[1] - 100, HEIGHT + 50)])
        LAZERPOS = [1400, 550, 1400, 2, 0, 0]
        GUTHRIE = [1400, 800]
        COLOUR = BLUE
        BLASTER = 0
        PLAYERHEIGHT = 100
        BOSSTYPE = random.choices([0, 1])
        KK = random.randint(50, 1100)
        KK2 =  random.randint(4, 11)*50
        GRENADE1POS = [MONSTERPOS[0] + 150, MONSTERPOS[1], MONSTERPOS[0], MONSTERPOS[1]]
        DAVEYJONESLOCKER = [1, 1, 0, 0]
        GRENADE1SIZE = [50, 50, 50, 50]
        BLASTER1_pos = 1400
        BLASTER2_pos = [1400, 1400, 1400]
        BOSSIFNO = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        MONSTERSIZE = [0, 0]
        MONSTERPOS = [500, 200]
        FORMY = 1
        JOEY = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        JOEY2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        m = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        HH_pos = [[800, 800], [800, 800], [800, 800], [800, 800], [800, 800], [800, 800], [800, 800], [800, 800], [800, 800], [800, 800], [800, 800], [800, 800], [800, 800], [800, 800], [800, 800], [800, 800], [800, 800], [800, 800], [800, 800], [800, 800], ]
        H = 0
        hun = 0
        WE = 0
        WE4 = 0
        WE3 = 0
        DAVEy = 0
        FOGY = 0
        
        BOSSSTART = False
        AMIALIVE = [True, True, True, True, True, True, True, True, True, True]
        AMIALIVE2 = [True, True, True, True, True, True, True, True, True, True]

        gravityMONSTER = [True, True, True, True, True, True, True, True, True, True, ]
        GE = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        b = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        WE2 = 0
        WE5= 0
        AMMOPACKET = [random.randint(0, WIDTH - 25), 0]
        UHH2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        yy = [WIDTH, WIDTH, WIDTH, WIDTH, WIDTH, WIDTH, WIDTH, WIDTH, WIDTH, WIDTH, WIDTH, WIDTH, WIDTH, WIDTH, WIDTH, WIDTH, WIDTH, WIDTH, WIDTH, WIDTH]
#self = [500,random.randint(0, HEIGHT - 50), 500,random.randint(0, HEIGHT - 50), 500,random.randint(0, HEIGHT - 50), 500,random.randint(0, HEIGHT - 50), 500,random.randint(0, HEIGHT - 50), 500,random.randint(0, HEIGHT - 50), 500,random.randint(0, HEIGHT - 50), 500,random.randint(0, HEIGHT - 50), 500,random.randint(0, HEIGHT - 50), 500,random.randint(0, HEIGHT - 50), 500,random.randint(0, HEIGHT - 50), 500,random.randint(0, HEIGHT - 50), 500,random.randint(0, HEIGHT - 50), 500,random.randint(0, HEIGHT - 50), ]
        BULLET_pos = [player1_pos[0] + n, player1_pos[1] + 40]
        UH = [WIDTH, random.randint(0, HEIGHT - 50), random.randint(0, HEIGHT - 50), random.randint(0, HEIGHT - 50), random.randint(0, HEIGHT - 50), random.randint(0, HEIGHT - 50), random.randint(0, HEIGHT - 50), random.randint(0, HEIGHT - 50), random.randint(0, HEIGHT - 50), random.randint(0, HEIGHT - 50), random.randint(0, HEIGHT - 50), random.randint(0, HEIGHT - 50), random.randint(0, HEIGHT - 50), random.randint(0, HEIGHT - 50), random.randint(0, HEIGHT - 50), random.randint(0, HEIGHT - 50), random.randint(0, HEIGHT - 50), random.randint(0, HEIGHT - 50), random.randint(0, HEIGHT - 50), random.randint(0, HEIGHT - 50), random.randint(0, HEIGHT - 50), random.randint(0, HEIGHT - 50), random.randint(0, HEIGHT - 50), random.randint(0, HEIGHT - 50), random.randint(0, HEIGHT - 50), random.randint(0, HEIGHT - 50), random.randint(0, HEIGHT - 50), random.randint(0, HEIGHT - 50)]
        UH2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        UH22 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        UH3 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        FML = [random.choices([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]), random.choices([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]), random.choices([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]), random.choices([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]), random.choices([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]), random.choices([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]), random.choices([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]), random.choices([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]), random.choices([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]), random.choices([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]), random.choices([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]), random.choices([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]), random.choices([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]), random.choices([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]), random.choices([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]), random.choices([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26])]
        FML2 = [random.choices([9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]), random.choices([9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]), random.choices([9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]), random.choices([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]), random.choices([9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]), random.choices([9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]), random.choices([9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]), random.choices([9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]), random.choices([9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]), random.choices([9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]), random.choices([9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]), random.choices([9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]), random.choices([9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]), random.choices([9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]), random.choices([9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]), random.choices([9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26])]
        FML3 = [random.choices([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]), random.choices([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]), random.choices([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]), random.choices([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]), random.choices([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]), random.choices([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]), random.choices([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]), random.choices([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]), random.choices([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]), random.choices([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]), random.choices([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]), random.choices([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]), random.choices([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]), random.choices([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]), random.choices([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]), random.choices([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26])]
        FML4 = [random.choices([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]), random.choices([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]), random.choices([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]), random.choices([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]), random.choices([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]), random.choices([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]), random.choices([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]), random.choices([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]), random.choices([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]), random.choices([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]), random.choices([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]), random.choices([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]), random.choices([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]), random.choices([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]), random.choices([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]), random.choices([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26])]
        BRUH = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        startpicture = pygame.image.load('you died.png')

        floorss = [Floor1.pos, Floor2.pos, Floor3.pos, Floor4.pos, Floor5.pos, Floor6.pos, Floor7.pos, Floor8.pos, Floor9.pos, Floor10.pos, Floor11.pos, Floor12.pos, Floor13.pos, Floor14.pos, Floor15.pos, Floor16.pos, Floor17.pos, Floor18.pos, Floor19.pos, Floor20.pos, Floor21.pos, Floor22.pos, Floor23.pos, Floor24.pos, Floor25.pos, Floor26.pos]
        flor = [0, Floor1.use, Floor2.use, Floor3.use, Floor4.use, Floor5.use, Floor6.use, Floor7.use, Floor8.use, Floor9.use, Floor10.use, Floor11.use, Floor12.use, Floor13.use, Floor14.use, Floor15.use, Floor16.use, Floor17.use, Floor18.use, Floor19.use, Floor20.use, Floor21.use, Floor22.use, Floor23.use, Floor24.use, Floor25.use, Floor26.use]

        FIND_USEFUL_FLOORS(flor)
        WOWY = random.randint(1, level)
        translator()
        
        player1_pos = [0, 0]
    if BOSSSTART == True:
        BOSSYBOSSMCBOSS = BOSS(BOSSINFO[0], BOSSINFO[1], BOSSINFO[2], BOSSINFO[3], BOSSINFO[4], BOSSINFO[5], BOSSINFO[6], BOSSINFO[7], BOSSINFO[8], BOSSINFO[9])
        
    if gravity == True:
        player1_pos[1] += PLAYER_MOVE
        JOE_pos[1] += PLAYER_MOVE
    if JUMPIDY == False:
        GEORGE2 += 1
        if GEORGE2 >= 20:
            JUMPIDY = True
    if BULLETFIRE == True:
        BULLET()
        YO += 1
        if YO >= 17:
            BULLETFIRE = False
    if BULLETFIRE == False:
        n = 0
        oh = 40
    def r():
        screen.fill(BACKGROUND_COLOUR)


        screen.blit(backgroundpicture, (0, 0))

        screen.blit(floorpicture, (Floor1.pos[0], Floor1.pos[1]))
        screen.blit(floorpicture, (Floor2.pos[0], Floor2.pos[1]))
        screen.blit(floorpicture, (Floor3.pos[0], Floor3.pos[1]))
        screen.blit(floorpicture, (Floor4.pos[0], Floor4.pos[1]))
        screen.blit(floorpicture, (Floor5.pos[0], Floor5.pos[1]))
        screen.blit(floorpicture, (Floor6.pos[0], Floor6.pos[1]))
        screen.blit(floorpicture, (Floor7.pos[0], Floor7.pos[1]))
        screen.blit(floorpicture, (Floor8.pos[0], Floor8.pos[1]))
        screen.blit(floorpicture, (Floor9.pos[0], Floor9.pos[1]))
        screen.blit(floorpicture, (Floor10.pos[0], Floor10.pos[1]))
        screen.blit(floorpicture, (Floor11.pos[0], Floor11.pos[1]))
        screen.blit(floorpicture, (Floor12.pos[0], Floor12.pos[1]))
        screen.blit(floorpicture, (Floor13.pos[0], Floor13.pos[1]))
        screen.blit(floorpicture, (Floor14.pos[0], Floor14.pos[1]))
        screen.blit(floorpicture, (Floor15.pos[0], Floor15.pos[1]))
        screen.blit(floorpicture, (Floor16.pos[0], Floor16.pos[1]))
        screen.blit(floorpicture, (Floor17.pos[0], Floor17.pos[1]))
        screen.blit(floorpicture, (Floor18.pos[0], Floor18.pos[1]))
        screen.blit(floorpicture, (Floor19.pos[0], Floor19.pos[1]))
        screen.blit(floorpicture, (Floor20.pos[0], Floor20.pos[1]))
        screen.blit(floorpicture, (Floor21.pos[0], Floor21.pos[1]))
        screen.blit(floorpicture, (Floor22.pos[0], Floor22.pos[1]))
        screen.blit(floorpicture, (Floor23.pos[0], Floor23.pos[1]))
        screen.blit(floorpicture, (Floor24.pos[0], Floor24.pos[1]))
        screen.blit(floorpicture, (Floor25.pos[0], Floor25.pos[1]))
        screen.blit(floorpicture, (Floor26.pos[0], Floor26.pos[1]))
       
#        pygame.draw.rect(screen, BLUE, (player1_pos[0], player1_pos[1], 50, PLAYERHEIGHT))
        screen.blit(playerpicture, (player1_pos[0], player1_pos[1]))

#        pygame.draw.rect(screen, BLUE, (player1_pos[0] + G, player1_pos[1] + 25, 50, 25))
#        pygame.draw.rect(screen, BLUE, (BULLET_pos[0], BULLET_pos[1], 25, 25))
#        pygame.draw.rect(screen, BLUE, (BULLET_pos[0], BULLET_pos[1], 25, 25))
        screen.blit(bulletpicture, (BULLET_pos[0], BULLET_pos[1]))

        screen.blit(ammopicture, (AMMOPACKET[0], AMMOPACKET[1]))



#    screen.fill(BACKGROUND_COLOUR
    r()
    repeat_fun(WE, flyingmonsterprint)
    repeat_fun(WE2, FLYINGMONSTER)
    repeat_fun(WE4, HE)
    repeat_fun(WE5 + WE3, FIREMONSTER)

    pygame.draw.rect(screen, BLUE, (0, HEIGHT - 25, 160, 25))
    pygame.draw.rect(screen, COLOUR, (0, 0, ROCKETFUEL*100, 25))

    if float(level/5).is_integer() == True:
#         pygame.draw.rect(screen, WHITE, (BLASTER2_pos[0], 200, 50, 50))
        screen.blit(blasterforwardpicture, (BLASTER2_pos[0], 200))
        screen.blit(blasterbackwardpicture, (BLASTER2_pos[1], 200))

        pygame.draw.rect(screen, WHITE, (BLASTER2_pos[1], 200, 50, 50))

        pygame.draw.rect(screen, WHITE, (GUTHRIE[0], GUTHRIE[1], 50, 50))


#        pygame.draw.rect(screen, WHITE, (GRENADE1POS[2], GRENADE1POS[3], GRENADE1SIZE[2], GRENADE1SIZE[3]))
        screen.blit(grenadepicture2, (GRENADE1POS[2], GRENADE1POS[3]))
        screen.blit(grenadepicture1, (GRENADE1POS[0], GRENADE1POS[1]))
        screen.blit(blasterforwardpicture, (BLASTER1_pos, KK2))
        label8 = MYFONT.render("BOSS BATTLE", 1, (0, 0, 0))

        pygame.draw.rect(screen, RED, (500, 25, 250, 40))
        screen.blit(label8, (509, 25))

        pygame.draw.rect(screen, RED, (0, 650, FOGY*50, 25))
        text2 = "BOSS HP"
        label2 = MYFONT2.render(text2, 1, WHITE)
        screen.blit(label2, (0, 650))

        pygame.draw.rect(screen, RED, (LAZERPOS[2], LAZERPOS[1], 1300, 50))
        screen.blit(leftpicture, (LAZERPOS[0], LAZERPOS[1]))

        pygame.draw.rect(screen, WHITE, (MONSTERPOS[0] + 75, BLASTER2_pos[2], 50, 50))
        pygame.draw.rect(screen, YELLOW, (DROPPINGS[0], DROPPINGS[1], 100, 100))
        if MONSTERSIZE[1] == 760:
            screen.blit(bigbosspicture, (MONSTERPOS[0], MONSTERPOS[1]))
        else:
            screen.blit(smallbosspicture, (MONSTERPOS[0], MONSTERPOS[1]))
    pygame.draw.rect(screen, YELLOW, (WIDTH - 200, 25, 200, 40))

    text = "LEVEL  " + str(level)
    text2 = "AMMO:" + str(AMMO) + "/13"
    label = MYFONT.render(text, 1, (0, 0, 0))
    label2 = MYFONT2.render(text2, 1, WHITE)
    label3 = MYFONT2.render("ROCKETFUEL", 1, WHITE)

    screen.blit(label, (WIDTH - 200, 25))
    screen.blit(label3, (0, 0))
    screen.blit(label2, (0, HEIGHT - 25))
    if GAMEOVER == True:
        AMMO = 13
        screen.blit(startpicture, (0, 0))


    pygame.display.update()
    clock.tick(60)
