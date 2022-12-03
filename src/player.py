import pygame

class Player(pygame.sprite.Sprite):
  def __init__(self,xpos,ypos):
    super().__init__()
    self.runframes=[]
    self.image=pygame.image.load('assets/charedit.png').convert_alpha()
    self.rect=self.image.get_rect()
    self.jumpmotion=-10
    self.fallmotion=0
    self.rect.center=[xpos,ypos]
    self.jumping=False
    self.falling=True
    self.running=False
    self.frame=0
    self.xmotion=0
  def control(self,x):
    # Controls movement  left and right of the screen(or on the x-axis)
    self.xmotion+=x
  def jump(self):
    # Moves the player down in y-axis  or up in screento mimick jumping
    if not self.jumping and not self.falling:
      self.jumping=True
  def fall(self):
    # Moves the user up in y-axis or down the screen
    if not self.falling and not self.jumping:
      self.falling=True
  def stopfall(self,y):
    # Ends the movement on the y-axis or stop  the falling actions
    self.falling=False
    self.fallmotion=0
    self.platform=y+1
  def override(self,x,y,type=0):
    # Places the player infront
    if type==0:
      self.rect.x=x
      self.rect.y=y
    elif type==1:
      self.xmotion=x
  def getloc(self):
    # Returns the location
    return self.rect
  def update(self):
    # Updates the player 
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
    self.rect.x+=self.xmotion
    if self.running:
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