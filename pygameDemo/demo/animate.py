import pygame, sys
pygame.init()
screen = pygame.display.set_mode((500, 500))
image = pygame.image.load('./static/hero1.png')
image2 = pygame.image.load('./static/hero2.png')
clock = pygame.time.Clock()
counter = 0
while True:
    counter += 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    clock.tick(60)
    screen.fill((255, 255, 255))
    if counter % 5 == 0:
        screen.blit(image, (20, 20))
    else:
        print(counter)
        screen.blit(image2, (20, 20))
    pygame.display.flip()