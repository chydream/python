import pygame
from pygameDemo import constants

class Bullet(pygame.sprite.Sprite):
    active = True
    def __init__(self, screen, plane, speed=None):
        super().__init__()
        self.speed = speed or 10
        self.plane = plane
        self.screen = screen
        self.image = pygame.image.load(constants.BULLET_IMG)
        self.rect = self.image.get_rect()
        self.rect.centerx = plane.rect.centerx
        self.rect.top = plane.rect.top
        self.shoot_sound = pygame.mixer.Sound(constants.BULLET_SHOOT_SOUND)
        self.shoot_sound.set_volume(0.3)
        self.shoot_sound.play()

    def update(self, war):
        self.rect.top -= self.speed
        if self.rect.top < 0:
            self.remove(self.plane.bullets)
        self.screen.blit(self.image, self.rect)
        rest = pygame.sprite.spritecollide(self, war.enemies, False)
        for r in rest:
            self.kill()
            r.broken_down()
            war.rest.score += constants.SCORE_SHOOT_SMALL
            war.rest.set_history()
