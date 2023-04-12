import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption("Space Shooter")
icon = pygame.image.load("icon.png")
pygame.display.set_icon(icon)

background = pygame.image.load("bg.png")
spaceship = pygame.image.load("spaceship1.png")

spaceshipX = 370
spaceshipY = 480
changeX = 0

running = True
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
        if event.type == pygame.KEYUP:  # key is released
            changeX = 0
    spaceshipX += changeX

    if spaceshipX <= 0:
        spaceshipX = 0
    elif spaceshipX >= 736:
        spaceshipX = 736

    screen.blit(spaceship, (spaceshipX, spaceshipY))
    pygame.display.update()
