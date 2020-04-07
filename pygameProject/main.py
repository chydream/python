import sys

import pygame

from pygameProject import constants
from pygameProject.game.plane import OurPlane


def main():
    # 游戏初始化，定义屏幕宽高，标题及背景图片
    pygame.init()
    size = width, height = 480, 852
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('飞机大战')
    bg = pygame.image.load(constants.BG_IMG)
    # 加载游戏标题图片
    img_game_title = pygame.image.load(constants.IMG_GAME_TITLE)
    t_width, t_height = img_game_title.get_size()
    img_game_title_rect = img_game_title.get_rect()
    img_game_title_rect.topleft = (int((width - t_width)/2), int(height/2-t_height))
    # 加载游戏开始按钮
    btn_start = pygame.image.load(constants.IMG_GAME_START_BTN)
    btn_width, btn_height = btn_start.get_size()
    btn_start_rect = btn_start.get_rect()
    btn_start_rect.topleft = (int((width - btn_width)/2), int(height/2 + btn_height))
    # 加载游戏背景音乐
    pygame.mixer.music.load(constants.BG_MUSIC)
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.2)
    status = 0
    frame = 0
    our_plane = OurPlane(screen, 10)
    clock = pygame.time.Clock()
    while True:
        clock.tick(60)
        frame += 1
        if frame >= 60:
            frame = 0
        # 监听键盘事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if status == 0:
                    status = 1
            elif event.type == pygame.KEYDOWN:
                if status == 1:
                    if event.key == pygame.K_w or event.key == pygame.K_UP:
                        our_plane.move_up()
                    elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                        our_plane.move_down()
                    elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
                        our_plane.move_left()
                    elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                        our_plane.move_right()
                    elif event.key == pygame.K_SPACE:
                        our_plane.shoot()
        #监听status状态
        if status == 0:
            screen.blit(bg, bg.get_rect())
            screen.blit(img_game_title, img_game_title_rect)
            screen.blit(btn_start, btn_start_rect)
        elif status == 1:
            screen.blit(bg, bg.get_rect())
            our_plane.update(frame)
            our_plane.bullets.update()
        pygame.display.flip()

if __name__ == '__main__':
    main()