import pygame

pygame.init()

# Defining Window
win = pygame.display.set_mode((500, 500))

# Title for the Window
pygame.display.set_caption("First Game")

screenWidth = 500

x = 50
y = 425
width = 40
height = 60
vel = 5

isJump = False
jumpCount = 10

run = True

while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > vel:
        x -= vel

    if keys[pygame.K_RIGHT] and x < screenWidth - width - vel:
        x += vel

    if not(isJump):
        if keys[pygame.K_UP] and y > vel:
            y -= vel

        if keys[pygame.K_DOWN] and y < screenWidth - height - vel:
            y += vel

        if keys[pygame.K_SPACE]:
            isJump = True

    else:
        if jumpCount >= -10:
            neg = 1
            if jumpCount < 0:
                neg = -1

            y -= (jumpCount ** 2) * .5 * neg
            jumpCount -= 1

        else:
            isJump = False
            jumpCount = 10

    win.fill((0, 0, 0))
    pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))
    pygame.display.update()
pygame.quit()
