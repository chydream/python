import random

import pygame
from pygameDemo import constants
from pygameDemo.game.bullet import Bullet


class Plane(pygame.sprite.Sprite):
    plane_images = []
    destroy_images = []
    down_sound_src = None
    active = True # 飞机的状态 True活False死
    bullets = pygame.sprite.Group() # 子弹精灵组
    def __init__(self, screen, speed = None):
        super().__init__()
        self.img_list = []
        self._destroy_img_list = []
        self.down_sound = None
        self.load_src()
        self.speed = speed or 10
        self.screen = screen
        self.rect = self.img_list[0].get_rect()
        self.width, self.height = self.screen.get_size()
        self.plane_w, self.plane_h = self.img_list[0].get_size()
        self.rect.left = int((self.width - self.plane_w)/2)
        self.rect.top = int(self.height / 2)
    def load_src(self):
        for img in self.plane_images:
            self.img_list.append(pygame.image.load(img))

        for img in self.destroy_images:
            self._destroy_img_list.append(pygame.image.load(img))

        if self.down_sound_src:
            self.down_sound = pygame.mixer.Sound(self.down_sound_src)

    @property
    def image(self):
        return  self.img_list[0]

    def blit_me(self):
        self.screen.blit(self.image, self.rect)

    def move_up(self):
        self.rect.top -= self.speed

    def move_down(self):
        self.rect.top += self.speed

    def move_left(self):
        self.rect.left -= self.speed

    def move_right(self):
        self.rect.left += self.speed

    def broken_down(self):
        if self.down_sound:
            self.down_sound.play()
        for img in self._destroy_img_list:
            self.screen.blit(img, self.rect)
        self.active = False

    def shoot(self):
        bullet = Bullet(self.screen, self, 15)
        self.bullets.add(bullet)


class OurPlane(Plane):
    plane_images = constants.OUR_PLANE_IMG_LIST
    destroy_images = constants.OUR_DESTROY_IMG_LIST
    down_sound_src = None

    def update(self, war):
        self.move(war.key_down)
        if war.frame % 5:
            self.screen.blit(self.img_list[0], self.rect)
        else:
            self.screen.blit(self.img_list[1], self.rect)
        rest = pygame.sprite.spritecollide(self, war.enemies, False)
        if rest:
            war.status = war.OVER
            war.enemies.empty()
            war.small_enemies.empty()
            self.broken_down()

    def move(self, key):
        if key == pygame.K_w or key == pygame.K_UP:
            self.move_up()
        elif key == pygame.K_s or key == pygame.K_DOWN:
            self.move_down()
        elif key == pygame.K_a or key == pygame.K_LEFT:
            self.move_left()
        elif key == pygame.K_d or key == pygame.K_RIGHT:
            self.move_right()

    def move_up(self):
        super().move_up()
        if self.rect.top <= 0:
            self.rect.top = 0

    def move_down(self):
        super().move_down()
        if self.rect.top >= self.height - self.plane_h:
            self.rect.top = self.height - self.plane_h

    def move_left(self):
        super().move_left()
        if self.rect.left <= 0:
            self.rect.left = 0

    def move_right(self):
        super().move_right()
        if self.rect.left >= self.width-self.plane_w:
            self.rect.left = self.width-self.plane_w


class SmallEnemyPlane(Plane):
    plane_images = constants.SMALL_ENEMY_PLANE_IMG_LIST
    destroy_images = constants.SMALL_ENEMY_DESTROY_IMG_LIST
    down_sound_src = constants.SMALL_ENEMY_PLANE_DOWN_SOUND

    def __init__(self, screen, speed):
        super().__init__(screen, speed)
        self.init_pos()

    def init_pos(self):
        self.rect.left = random.randint(0, self.width - self.plane_w)
        self.rect.top = random.randint(-5 * self.plane_h, -self.plane_h)

    def update(self, *args):
        super().move_down()
        self.blit_me()
        if self.rect.top >= self.height:
            # self.kill()
            self.reset()

    def reset(self):
        self.active = True
        self.init_pos()

    def broken_down(self):
        super().broken_down()
        self.reset()