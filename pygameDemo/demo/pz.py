# 精灵 图形对象，精灵组 容器
# 两个精灵之间的矩形碰撞检测
# pygame.sprite.collide_rect(sprite_1, sprite_2)
# pygame.sprite.collide_rect_ratio(0.5)(sprite_1, sprite_2)
import pygame, sys
pygame.init()
screen = pygame.display.set_mode((500, 500))


class Block(pygame.sprite.Sprite):
    def __init__(self, color, width, height, init_pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.topleft = init_pos


sprite_1 = Block(pygame.Color(255,0,0), 50, 50, (110, 110)) # 实例化精灵对象
sprite_2 = Block(pygame.Color(0,255,0), 50, 50, (150, 150)) # 实例化精灵对象

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.blit(sprite_1.image, sprite_1.rect)
    screen.blit(sprite_2.image, sprite_2.rect)

    rest = pygame.sprite.collide_rect(sprite_1, sprite_2)
    rest2 = pygame.sprite.collide_rect_ratio(1)(sprite_1, sprite_2)
    print(rest)
    print('rest2', rest2)
    pygame.display.flip()