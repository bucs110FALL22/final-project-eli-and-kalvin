import pygame

class Block(pygame.sprite.Sprite):
  def __init__(self,x,y,ground=False):
    super().__init__()
    if not ground:
      IMAGE=pygame.image.load('assets/block.png').convert_alpha()
      self.image=IMAGE
    else:
      IMAGE=pygame.image.load('assets/groundblock.png').convert_alpha()
      self.image=IMAGE
    self.rect=self.image.get_rect()
    self.rect.topright=[x,y]
  def getloc(self):
    return (self.rect.x,self.rect.y)
  def update(self):
    self.rect.x-=3