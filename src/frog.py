import pygame

class Frog(pygame.sprite.Sprite):
  def __init__(self,xpos,ypos):
    super().__init__()
    self.image=pygame.Surface([3,3])
    self.image.fill((0,255,0))
    self.rect=self.image.get_rect()
    self.jumpmotion=-15
    self.fallmotion=0
    self.rect.center=[xpos,ypos]
    self.jumping=False
    self.falling=True
    self.xmotion=0
  def fall(self):
    if not self.falling and not self.jumping:
      self.falling=True
  def stopfall(self,y):
    self.falling=False
    self.fallmotion=0
    self.platform=y+1
  def die(self):
    self.rect.y+=100
    self.kill()
  def getloc(self):
    return self.rect
  def override(self,x,y):
    self.rect.x=x
    self.rect.y=y
  def rmove(self,movement,xlimit=500):
    if self.rect.x>xlimit:
      self.xmotion=-3
    elif self.rect.x<0:
      self.xmotion+3
    elif movement<2:
      self.xmotion=3
    elif movement<4:
      self.xmotion=-3
    elif movement==4 and not self.jumping and not self.falling:
      self.jumping=True
  def update(self):
    if self.jumping:
      self.rect.y+=self.jumpmotion
      if self.jumpmotion<0:
        self.jumpmotion+=1
      else:
        self.jumpmotion=-15
        self.jumping=False
    elif self.falling:
      self.rect.y+=self.fallmotion
      if self.fallmotion<15:
        self.fallmotion+=1
    else:
      self.rect.midbottom=[self.rect.center[0],self.platform]
    self.rect.x+=self.xmotion
    if self.rect.y>240:
      self.rect.y=240