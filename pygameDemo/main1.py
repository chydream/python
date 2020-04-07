import sys
import  pygame
from pygameDemo import constants
from pygameDemo.game.plane import Plane, OurPlane, SmallEnemyPlane


def main():
    pygame.init()
    size = width, height = 480, 852
    screen = pygame.display.set_mode(size)
    bg = pygame.image.load(constants.BG_IMG)

    img_game_title = pygame.image.load(constants.IMG_GAME_TITLE)
    img_game_title_rect = img_game_title.get_rect()
    t_width, t_height = img_game_title.get_size()
    img_game_title_rect.topleft = (int((width-t_width)/2), int(height/2 - t_height))

    btn_start = pygame.image.load(constants.IMG_GAME_START)
    btn_start_rect = btn_start.get_rect()
    btn_width, btn_height = btn_start.get_size()
    btn_start_rect.topleft = (int((width - btn_width) / 2), int(height / 2 + btn_height))

    pygame.display.set_caption('飞机大战')
    # pygame.mixer.music.load(constants.BG_MUSIC)
    # pygame.mixer.music.play(-1)
    # pygame.mixer.music.set_volume(0.2)
    status = 0 # 0 准备中 1 游戏中 2 游戏结束
    our_plane = OurPlane(screen)
    frame = 0
    clock = pygame.time.Clock()

    small_enemies = pygame.sprite.Group()
    enemies = pygame.sprite.Group()
    for i in range(6):
        plane = SmallEnemyPlane(screen, 2)
        plane.add(small_enemies, enemies)

    while True:
        clock.tick(60)
        frame += 1
        if frame >= 60:
            frame = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if status == 0:
                    status = 1
                elif status == 2:
                    status = 0
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


        if status == 0:
            screen.blit(bg, bg.get_rect())
            screen.blit(img_game_title, img_game_title_rect)
            screen.blit(btn_start, btn_start_rect)
        elif status == 1:
            screen.blit(bg, bg.get_rect())
            our_plane.update(frame)
            our_plane.bullets.update()
            small_enemies.update()
        pygame.display.flip()

if __name__ == '__main__':
    main()