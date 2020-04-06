import pygame
from pygameDemo import constants

class Plane(pygame.sprite.Sprite):
    plane_images = []
    destroy_images = []
    down_sound_src = None
    active = True # 飞机的状态 True活False死
    bullets = pygame.sprite.Group() # 子弹精灵组
    def __init__(self, screen, speed = None):
        super().__init__()
        self._img_list = []
        self._destroy_img_list = []
        self.down_sound = None
        self.load_src()
        self.speed = speed or 10
        self.screen = screen
        self.rect = self._img_list[0].get_rect()

    def load_src(self):
        for img in self.plane_images:
            self._img_list.append(pygame.image.load(img))

        for img in self.destroy_images:
            self._destroy_img_list.append(pygame.image.load(img))

        if self.down_sound_src:
            self.down_sound = pygame.mixer.Sound(self.down_sound_src)

    @property
    def image(self):
        return  self._img_list[0]

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


class OurPlane(Plane):
    plane_images = constants.OUR_PLANE_IMG_LIST
    destroy_images = constants.OUR_DESTROY_IMG_LIST
    down_sound_src = None
