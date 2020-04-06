import pygame, sys
pygame.init()
screen = pygame.display.set_mode((400,400))
screen.fill((0, 0, 0))
# 加载图片
ball = pygame.image.load('./static/intro_ball.gif')
#颜色
red = pygame.Color(255, 0, 0)
white = pygame.Color(255, 255, 255)
#文字
font = pygame.font.SysFont('kaiti', 32)
# font = pygame.font.Font('./simher.ttf', 40)
# 画字
text = font.render('得分：0', True, red, white)
# 加载背景音乐
ms = pygame.mixer.music.load('./static/bg_music.mp3')
pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.play(-1)
print(pygame.font.get_fonts())
# ballrect = ball.get_rect()
# screen.blit(ball, ballrect)
# screen.blit(ball, (100, 100))
# pygame.display.flip()

#动画切换


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    #画线
    pygame.draw.line(screen, red, (1, 1), (50, 50), 6)
    #矩形
    pygame.draw.rect(screen, red, (50, 50, 100, 100), 6)
    #画圆
    pygame.draw.circle(screen, red, (10, 10), 50, 6)
    #绘制
    screen.blit(ball, (100, 100))
    screen.blit(text, text.get_rect())
    pygame.display.flip()