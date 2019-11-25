import pygame
pygame.init()

window = pygame.display.set_mode((500, 500))

pygame.display.set_caption("first game")

screenwidth = 500

x = 10
y = 450
width = 20
height = 20
vel = 20

run = True
while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > vel:
        x -= vel
    if keys[pygame.K_RIGHT] and x < 500 - width - vel:
        x += vel
    if keys[pygame.K_UP]and y > vel:
        y -= vel
    if keys[pygame.K_DOWN]and y < 500 - width - vel:
        y += vel

    
    window.fill((0, 0, 0))
    pygame.draw.rect(window, (200, 23, 255), (x, y, width, height))
    pygame.draw.rect(window, (200, 0, 0), (30, 400, width, height))
    pygame.display.update()   

pygame.quit()         

