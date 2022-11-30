import pygame

class Deathblock(pygame.sprite.Sprite):
  def __init__(self,x,y,width,height,type=0):
    super().__init__()
    if type==0:
      self.image=pygame.Surface([width,height])
      self.image.fill((122,84,68))
      self.rect=self.image.get_rect()
      self.rect.topright=[x,y]
    elif type==1:
      IMAGE=pygame.image.load('assets/game1images/stump.png').convert_alpha()
      self.image=IMAGE
      self.rect=self.image.get_rect()
      self.rect.bottomright=[x,y]
    elif type==2:
      self.image=pygame.Surface([width,height])
      self.image.fill((75,75,150))
      self.rect=self.image.get_rect()
      self.rect.topright=[x,y]
  def getloc(self):
    return (self.rect.x,self.rect.y)
  def update(self):
    self.rect.x-=3