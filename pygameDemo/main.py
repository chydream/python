import sys
import  pygame
from pygameDemo import constants
from pygameDemo.game.plane import Plane, OurPlane


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
    pygame.mixer.music.load(constants.BG_MUSIC)
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.2)
    status = 0 # 0 准备中 1 游戏中 2 游戏结束
    our_plane = OurPlane(screen)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if status == 0:
                    status = 1
                elif status == 2:
                    status = 0

        if status == 0:
            screen.blit(bg, bg.get_rect())
            screen.blit(img_game_title, img_game_title_rect)
            screen.blit(btn_start, btn_start_rect)
        elif status == 1:
            screen.blit(bg, bg.get_rect())
            our_plane.blit_me()


        pygame.display.flip()

if __name__ == '__main__':
    main()