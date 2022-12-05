import pygame

class Player(pygame.sprite.Sprite):
  def __init__(self,xpos,ypos):
    '''
    Creates a player sprite, its appearnance, its rect, and the variables to control its movement
    args:
      self
      xpos: int
      ypos: int
    returns: None
    '''
    super().__init__()
    self.image=pygame.image.load('assets/charedit.png').convert_alpha()
    self.rect=self.image.get_rect()
    self.jumpmotion=-10
    self.fallmotion=0
    self.rect.center=[xpos,ypos]
    self.jumping=False
    self.falling=True
    self.frame=0
    self.xmotion=0
  def control(self,x):
    '''
    Moves the player.
    args:
      self
      x: int
    returns: None
    '''
    self.xmotion+=x
  def jump(self):
    '''
    If the player is not falling and not already jumping, starts its jump movement.
    args: self
    returns: None
    '''
    if not self.jumping and not self.falling:
      self.jumping=True
  def fall(self):
    '''
    Begins the player's descent, as long as the player is not already jumpig or falling.
    args: self
    returns: None
    '''
    if not self.falling and not self.jumping:
      self.falling=True
  def stopfall(self,y):
    '''
    Ends the player's descent, and keeps track of what platform it has landed on using its y-coordinate.
    args:
      self
      y: int
    returns: None
    '''
    self.falling=False
    self.fallmotion=0
    self.platform=y+1
  def override(self,x,y,type=0):
    '''
    Sets the player to a different location, or stops its movement.
    args:
      self
      x: int
      y: int
      type: int
    returns: None
    '''
    if type==0:
      self.rect.x=x
      self.rect.y=y
    elif type==1:
      self.xmotion=x
  def getloc(self):
    '''
    Returns the character's location as a tuple.
    args: self
    returns:
      self.rect: tuple (int,int)
    '''
    return self.rect
  def update(self):
    '''
    Updates the player's position based on its movement. Must be more than 10 lines of code to keep track of all movements, not only including falling, jumping, and moving left or right, but also the speed at which the falling and jumping occurs.
    args: self
    returns: None
    ''' 
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