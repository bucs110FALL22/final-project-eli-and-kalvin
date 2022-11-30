import pygame

class Player(pygame.sprite.Sprite):
  def __init__(self,xpos,ypos):
    super().__init__()
    self.runframes=[]
    for i in range (1,4):
      self.runframes.append(pygame.image.load('assets/game1images/character_run'+str(i)+'.png').convert_alpha())
    self.image=self.runframes[1]
    self.rect=self.image.get_rect()
    self.jumpmotion=-10
    self.fallmotion=0
    self.rect.center=[xpos,ypos]
    self.jumping=False
    self.falling=False
    self.frame=0
  def jump(self):
    if not self.jumping and not self.falling:
      self.jumping=True
  def fall(self):
    if not self.falling and not self.jumping:
      self.falling=True
  def stopfall(self,y):
    self.falling=False
    self.fallmotion=0
    self.platform=y+1
  def override(self,x,y):
    self.rect.x=x
    self.rect.y=y
  def gety(self):
    return self.rect.y
  def update(self):
    if self.jumping:
      self.rect.y+=self.jumpmotion
      if self.jumpmotion<0:
        self.jumpmotion+=1
      else:
        self.jumpmotion=-10
        self.jumping=False
    elif self.falling:
      self.rect.y+=self.fallmotion
      if self.fallmotion<10:
        self.fallmotion+=1
    else:
      self.rect.midbottom=[self.rect.center[0],self.platform]
    if self.frame==30:
      self.frame=0
    if self.frame==0:
      self.image=self.runframes[1]
    elif self.frame==5:
      self.image=self.runframes[0]
    elif self.frame==15:
      self.image=self.runframes[1]
    elif self.frame==20:
      self.image=self.runframes[2]
    self.frame+=1