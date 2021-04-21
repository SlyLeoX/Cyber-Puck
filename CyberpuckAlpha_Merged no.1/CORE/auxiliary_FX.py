import pygame


def side_sounds(self):
    effect = pygame.mixer.Sound(r'CORE\ressources\sfx\mechanical-clonk-1.wav')
    effect.set_volume(0.1)
    effect.play()


def collide_sounds(self):
    effect = pygame.mixer.Sound(r'CORE\ressources\sfx\gun-gunshot-01.wav')
    effect.set_volume(0.1)
    effect.play()


def side_animations(self, entity, i):
    self.side_sounds()

    return_angle = {"bottom": 0, "right": 90, "top": 180, "left": 270}
    sprite = pygame.transform.rotate(self.sideimpact_effect, return_angle[i])
    sprite_rect = sprite.get_rect()
    sprite_rect.centerx, sprite_rect.centery = entity.rect.centerx, entity.rect.centery
    self.screen.blit(sprite, sprite_rect)


def collide_animations(self, i):
    self.collide_sounds()

    self.screen.blit(self.centerimpact_effect, i)