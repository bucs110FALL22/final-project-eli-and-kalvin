import pygame

class Frog(pygame.sprite.Sprite):
  def __init__(self,xpos,ypos):
    '''
    Creates a frog sprite, its appearnance, its rect, and the variables to control its movement.
    args:
      self
      xpos: int
      ypos: int
    returns: None
    '''
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
    '''
    Begins the frog's descent, as long as the frog is not already jumping or falling.
    args: self
    returns: None
    '''
    if not self.falling and not self.jumping:
      self.falling=True
  def stopfall(self,y):
    '''
    Ends the frog's descent, and keeps track of what platform it has landed on using its y-coordinate.
    args:
      self
      y: int
    returns: None
    '''
    self.falling=False
    self.fallmotion=0
    self.platform=y+1
  def die(self):
    '''
    Removes the sprite from all groups, and moves it off-screen so it cannot be interacted with.
    args: self
    returns: None
    '''
    self.rect.y+=100
    self.kill()
  def getloc(self):
    '''
    Returns the x and y location of the block as a tuple.
    args: self
    returns: 
      self.rect: tuple (int,int)
    '''
    return self.rect
  def override(self,x,y):
    '''
    Sets the frog to a different location.
    args:
      self
      x: int
      y: int
    returns: None
    '''
    self.rect.x=x
    self.rect.y=y
  def rmove(self,movement,xlimit=500):
    '''
    Randomly moves the frog, either based on the number given in movement or by moving it away from the edge of the screen.
    args:
      self
      movement: int
      xlimit: int
    returns: 
      None
    '''
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
    '''
    Updates the frog's position based on its movement. Must be more than 10 lines of code to keep track of all movements, not only including falling, jumping, and moving left or right, but also the speed at which the falling and jumping occurs.
    args: self
    returns: None
    '''
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