import pygame

class Player(pygame.sprite.Sprite):
  def __init__(self,x,y,width,height,moveamount,color=(255,0,0)):
    super().__init()
    self.image=pygame.Surface([width,height])
    self.image.fill(color)#making the player a blank square first,will change later
    self.rect=self.image.getrect()
    self.moveamount=moveamount
    self.movex=0
    self.frame=0
  def control(self):
    self.movex+=moveamount
  def update(self):
    ??