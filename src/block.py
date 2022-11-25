import pygame

class Block(pygame.sprite.Sprite):
  def __init__(self,x,y,width,height):
    super().__init__()
    self.image=pygame.Surface([width,height])
    self.image.fill((0,0,255))
    self.rect=self.image.get_rect()
    self.rect.topright=[x,y]
  def move(self,x):
    self.rect.x-=x
  def getloc(self):
    return (self.rect.x,self.rect.y)