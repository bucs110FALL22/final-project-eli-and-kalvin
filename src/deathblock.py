import pygame

class Deathblock(pygame.sprite.Sprite):
  def __init__(self,x,y,width,height,type=0):
    super().__init__()
    if type==0:
      self.image=pygame.Surface([width,height])
      self.image.fill((122,84,68))
      self.rect=self.image.get_rect()
      self.rect.topright=[x,y]
    elif type==1: #stump
      IMAGE=pygame.image.load('assets/stump.png').convert_alpha()
      self.image=IMAGE
      self.rect=self.image.get_rect()
      self.rect.bottomright=[x,y]
    elif type==2: #water
      self.image=pygame.Surface([width,height])
      self.image.fill((75,75,150))
      self.rect=self.image.get_rect()
      self.rect.topright=[x,y]
    elif type==3: #acorn
      self.image=pygame.Surface([width,height])
      # I changed the color to white. Easier to see. feel free to change it back
      # self.image.fill((122,84,68))
      self.image.fill((255,255,255))
      self.rect=self.image.get_rect()
      self.rect.topright=[x,y]
    self.type=type
    self.alternate=False
  def getloc(self):
    return (self.rect.x,self.rect.y)
  def die(self):
    self.rect.y+=100
    self.kill()
  def update(self):
    if self.type<3:
      self.rect.x-=3
    elif self.type==3:
      if self.alternate:
        self.alternate=False
      else:
        self.rect.y+=1
        