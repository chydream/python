import pygame

from pygameProject import constants


class Bullet(pygame.sprite.Sprite):
    """子弹类"""
    active = True

    def __init__(self, screen, plane, speed=None):
        super().__init__()
        self.screen = screen
        self.speed = speed or 10
        self.plane = plane
        self.image = pygame.image.load(constants.BULLET_IMG)  #  子弹图片静态资源列表
        self.rect = self.image.get_rect()   #  子弹位置
        self.rect.centerx = plane.rect.centerx #  子弹中心点位置
        self.rect.top = plane.rect.top  #  子弹中心点位置
        #  子弹音效
        self.shoot_sound = pygame.mixer.Sound(constants.BULLET_SHOOT_SOUND)
        self.shoot_sound.set_volume(0.3)
        self.shoot_sound.play()

    def update(self, *args):
        self.rect.top -= self.speed
        if self.rect.top < 0:
            self.remove(self.plane.bullets)
        self.screen.blit(self.image, self.rect)
