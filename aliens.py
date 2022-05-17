import pygame

pygame.init()
win = pygame.display.set_mode((500, 500))

pygame.display.set_caption("Aliens coming")

x = 50
y = 50
widht = 40
height = 60
speed = 5

run = true
while run:
    pygame.time.delay(100)

    for event in pygame.exent.get():
        if event.type == pygame.QUIT:
            run = False
        
    pygame.draw.rect(win, (153, 0, 0,), (x, y, width, height))
    pygame.display.update()

pygame.quit()