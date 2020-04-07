import pygame

from pygameProject import constants
from pygameProject.game.bullet import Bullet


class Plane(pygame.sprite.Sprite):
    """飞机基类"""
    plane_images = []
    active = True
    bullets = pygame.sprite.Group()
    def __init__(self, screen, speed = None):
        super().__init__()
        self.screen = screen
        self.speed = speed or 10
        self.img_list = []  # 飞机图片静态资源列表
        self.load_src()
        self.rect = self.img_list[0].get_rect()  # 飞机位置
        self.plane_w, self.plane_h = self.img_list[0].get_size()  # 飞机宽高
        self.width, self.height = self.screen.get_size()  # 窗口宽高
        self.rect.left = int((self.width-self.plane_w)/2)  # 设置飞机初始化位置
        self.rect.top = int(self.height/2)

    def load_src(self):
        for img in self.plane_images:
            self.img_list.append(pygame.image.load(img))

    @property
    def image(self):
        return self.img_list[0]

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

    def shoot(self):
        bullet = Bullet(self.screen, self, 15)
        self.bullets.add(bullet)

class OurPlane(Plane):
    """我方飞机"""
    plane_images = [constants.OUR_PLANE_IMG_1, constants.OUR_PLANE_IMG_2]

    def update(self, frame):
        if frame % 5:
            self.screen.blit(self.img_list[0], self.rect)
        else:
            self.screen.blit(self.img_list[1], self.rect)

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
        if self.rect.left >= self.width -self.plane_w:
            self.rect.left = self.width -self.plane_w

