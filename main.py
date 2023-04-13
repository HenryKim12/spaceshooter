import pygame
import random
import math

pygame.init()

screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption("Space Shooter")
icon = pygame.image.load("icon.png")
pygame.display.set_icon(icon)

aliens = []
alienX = []
alienY = []
alienSpeedX = []
alienSpeedY = []

num_aliens = 6

for i in range(num_aliens):
    aliens.append(pygame.image.load("alien.png"))
    alienX.append(random.randint(0, 736))
    alienY.append(random.randint(30, 150))
    alienSpeedX.append(-3)
    alienSpeedY.append(40)


background = pygame.image.load("bg.png")
spaceship = pygame.image.load("spaceship1.png")
bullet = pygame.image.load("bullet.png")

# alienX = random.randint(0, 736)
# alienY = random.randint(30, 150)
# alienSpeedX = 3
# alienSpeedY = 40

spaceshipX = 370
spaceshipY = 480
changeX = 0

check = False
bulletX = 386
bulletY = 490

score = 0

running = True

font = pygame.font.SysFont("Arial", 32, "bold")


def score_board():
    score_img = font.render(f"SCORE:{score}", True, "white")
    screen.blit(score_img, (10, 10))


font_gameover = pygame.font.SysFont("Arial", 64, "bold")


def gameover():
    gameoverImg = font_gameover.render("GAME OVER", True, "white")
    screen.blit(gameoverImg, (250, 250))


def collision():
    # distance formula between bullet, alien
    distance = math.sqrt(math.pow(bulletX - alienX, 2) + math.pow(bulletY - alienY, 2))
    if distance < 35:
        return True


while running:
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:  # key is pressed
            if event.key == pygame.K_LEFT:
                changeX = -4
            if event.key == pygame.K_RIGHT:
                changeX = 4
            if event.key == pygame.K_SPACE:
                if check is False:
                    check = True
                    bulletX = spaceshipX + 16

        if event.type == pygame.KEYUP:  # key is released
            changeX = 0

    spaceshipX += changeX

    if spaceshipX <= 0:
        spaceshipX = 0
    elif spaceshipX >= 736:
        spaceshipX = 736

    for i in range(num_aliens):
        if alienY[i] > 420:
            for j in range(num_aliens):
                alienY[j] = 2000
            gameover()
            break

        alienX[i] += alienSpeedX[i]
        if alienX[i] <= 0:
            alienSpeedX[i] = 3
            alienY[i] += alienSpeedY[i]
        elif alienX[i] >= 736:
            alienSpeedX[i] = -3
            alienY[i] += alienSpeedY[i]

        distance = math.sqrt(math.pow(bulletX - alienX[i], 2) + math.pow(bulletY - alienY[i], 2))
        if distance < 35:
            bulletY = 480
            check = False
            alienX[i] = random.randint(0, 736)
            alienY[i] = random.randint(30, 150)
            score += 1
        screen.blit(aliens[i], (alienX[i], alienY[i]))


    if bulletY <= 0:
        bulletY = 490
        check = False
    if check:
        screen.blit(bullet, (bulletX, bulletY))
        bulletY -= 8

    screen.blit(spaceship, (spaceshipX, spaceshipY))
    score_board()
    pygame.display.update()
