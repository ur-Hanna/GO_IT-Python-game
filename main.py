import random
import os
import pygame
from pygame.constants import QUIT, K_UP, K_RIGHT, K_DOWN, K_LEFT

pygame.init()

WIDTH = 1200
HEIGHT = 800
FONT = pygame.font.SysFont('Verdana', 32)
FPS = pygame.time.Clock()
WHITE_COLOR = (255, 255, 255)
BLACK_COLOR = (15, 15, 15)

mainDisplay = pygame.display.set_mode((WIDTH, HEIGHT))

bg = pygame.transform.scale(pygame.image.load('./img/background.png'), (WIDTH, HEIGHT))

bgX1 = 0
bgX2 = bg.get_width()
bgMove = 3

# гравець
IMAGE_PATH = "./img/goose"
PLAYER_IMAGES = os.listdir(IMAGE_PATH)

player = pygame.image.load('./img/player.png').convert_alpha()
playerSize = player.get_size()
playerRect = player.get_rect(center=(100, 400))
playerMoveUp = [0, -4]
playerMoveRight = [4, 0]
playerMoveDown = [0, 4]
playerMoveLeft = [-4, 0]

# супротивники
def createEnemy():
    enemy = pygame.image.load('./img/enemy.png').convert_alpha()
    enemySize = enemy.get_size()
    enemyRect = pygame.Rect(WIDTH, random.randint(100, 700), *enemySize)
    enemyMove = [random.randint(-8, -4), 0]
    return [enemy, enemyRect, enemyMove]

# бонуси
def createBonus():
    bonus = pygame.image.load('./img/bonus.png').convert_alpha()
    bonusSize = bonus.get_size()
    bonusRect = pygame.Rect(random.randint(100, 1100), 0, *bonusSize)
    bonusMove = [0, random.randint(4, 8)]
    return [bonus, bonusRect, bonusMove]

CREATE_ENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(CREATE_ENEMY, 2000)
CREATE_BONUS = pygame.USEREVENT + 2
pygame.time.set_timer(CREATE_BONUS, 2500)
CHANGE_IMAGE = pygame.USEREVENT + 3
pygame.time.set_timer(CHANGE_IMAGE, 500)

enemies = []
bonuses = []
score = 0

imgIndex = 0

playing = True

while playing:
    FPS.tick(180)

    for event in pygame.event.get():
        if event.type == QUIT:
            playing = False
        if event.type == CREATE_ENEMY:
            enemies.append(createEnemy())
        if event.type == CREATE_BONUS:
            bonuses.append(createBonus())
        if event.type == CHANGE_IMAGE:
            player = pygame.image.load(os.path.join(IMAGE_PATH, PLAYER_IMAGES[imgIndex]))
            imgIndex += 1
            if imgIndex >= len(PLAYER_IMAGES):
                imgIndex = 0

    bgX1 -= bgMove
    bgX2 -= bgMove

    if bgX1 < -bg.get_width():
        bgX1 = bg.get_width()

    if bgX2 < -bg.get_width():
        bgX2 = bg.get_width()

    mainDisplay.blit(bg, (bgX1, 0))
    mainDisplay.blit(bg, (bgX2, 0))

    keys = pygame.key.get_pressed()

    if keys[K_UP] and playerRect.top > 0:
        playerRect = playerRect.move(playerMoveUp)

    if keys[K_RIGHT] and playerRect.right < WIDTH:
        playerRect = playerRect.move(playerMoveRight)

    if keys[K_DOWN] and playerRect.bottom < HEIGHT:
        playerRect = playerRect.move(playerMoveDown)

    if keys[K_LEFT] and playerRect.left > 0:
        playerRect = playerRect.move(playerMoveLeft)

    for enemy in enemies:
        enemy[1] = enemy[1].move(enemy[2])
        mainDisplay.blit(enemy[0], enemy[1])

        if playerRect.colliderect(enemy[1]):
            playing = False

    for bonus in bonuses:
        bonus[1] = bonus[1].move(bonus[2])
        mainDisplay.blit(bonus[0], bonus[1])

        if playerRect.colliderect(bonus[1]):
            score += 1
            bonuses.pop(bonuses.index(bonus))

    mainDisplay.blit(FONT.render(str(score), True, BLACK_COLOR), (WIDTH-50, 20))

    mainDisplay.blit(player, playerRect)

    pygame.display.flip()

    for enemy in enemies:
        if enemy[1].left < 0:
            enemies.pop(enemies.index(enemy))

    for bonus in bonuses:
        if bonus[1].top > HEIGHT:
            bonuses.pop(bonuses.index(bonus))