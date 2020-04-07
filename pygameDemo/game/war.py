import sys
import  pygame
from pygameDemo import constants
from pygameDemo.game.plane import Plane, OurPlane, SmallEnemyPlane
from pygameDemo.store.result import PlayRest


class PlaneWar(object):
    READY = 0
    PLAYING = 1
    OVER = 2
    status = READY  # 0 准备中 1 游戏中 2 游戏结束
    our_plane = None
    frame = 0
    small_enemies = pygame.sprite.Group()
    enemies = pygame.sprite.Group()
    rest = PlayRest()

    def __init__(self):
        pygame.init()
        self.width, self.height = 480, 852
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.bg = pygame.image.load(constants.BG_IMG)
        self.bg_over = pygame.image.load(constants.BG_IMG_OVER)

        self.img_game_title = pygame.image.load(constants.IMG_GAME_TITLE)
        self.img_game_title_rect = self.img_game_title.get_rect()
        t_width, t_height = self.img_game_title.get_size()
        self.img_game_title_rect.topleft = (int((self.width - t_width) / 2), int(self.height / 2 - t_height))

        self.btn_start = pygame.image.load(constants.IMG_GAME_START)
        self.btn_start_rect = self.btn_start.get_rect()
        btn_width, btn_height = self.btn_start.get_size()
        self.btn_start_rect.topleft = (int((self.width - btn_width) / 2), int(self.height / 2 + btn_height))

        pygame.display.set_caption('飞机大战')


        self.score_font = pygame.font.SysFont('kaiti', 32)
        # pygame.mixer.music.load(constants.BG_MUSIC)
        # pygame.mixer.music.play(-1)
        # pygame.mixer.music.set_volume(0.2)
        self.our_plane = OurPlane(self.screen)
        self.clock = pygame.time.Clock()
        self.key_down = None

    def bind_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.status == self.READY:
                    self.status = self.PLAYING
                elif self.status == self.OVER:
                    self.status = self.READY
                    self.add_small_enemies(6)
            elif event.type == pygame.KEYDOWN:
                self.key_down = event.key
                if self.status == self.PLAYING:
                    if event.key == pygame.K_w or event.key == pygame.K_UP:
                        self.our_plane.move_up()
                    elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                        self.our_plane.move_down()
                    elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
                        self.our_plane.move_left()
                    elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                        self.our_plane.move_right()
                    elif event.key == pygame.K_SPACE:
                        self.our_plane.shoot()

    def add_small_enemies(self, num):
        for i in range(num):
            plane = SmallEnemyPlane(self.screen, 2)
            plane.add(self.small_enemies, self.enemies)

    def run_game(self):
        while True:
            self.clock.tick(60)
            self.frame += 1
            if self.frame >= 60:
                frame = 0
            self.bind_event()

            if self.status == self.READY:
                self.screen.blit(self.bg, self.bg.get_rect())
                self.screen.blit(self.img_game_title, self.img_game_title_rect)
                self.screen.blit(self.btn_start, self.btn_start_rect)
                self.key_down = None
            elif self.status == self.PLAYING:
                self.screen.blit(self.bg, self.bg.get_rect())
                self.our_plane.update(self)
                self.our_plane.bullets.update(self)
                self.small_enemies.update()
                score_text = self.score_font.render('得分：{0}'.format(self.rest.score),False,constants.TEXT_SOCRE_COLOR)
                self.screen.blit(score_text,score_text.get_rect())
            elif self.status == self.OVER:
                self.screen.blit(self.bg_over, self.bg_over.get_rect())
                score_text = self.score_font.render('{0}'.format(self.rest.score), False, constants.TEXT_SOCRE_COLOR)
                score_text_rect = score_text.get_rect()
                text_w, text_h = score_text.get_size()
                score_text_rect.topleft = (
                    int((self.width-text_h)/2),
                    int(self.height/2)
                )
                self.screen.blit(score_text, score_text_rect)
                score_his = self.score_font.render(
                    '{0}'.format(self.rest.get_max_core()), False, constants.TEXT_SOCRE_COLOR
                )
                self.screen.blit(score_his, (150, 40))
            pygame.display.flip()