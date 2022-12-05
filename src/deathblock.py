import pygame

class Deathblock(pygame.sprite.Sprite):
  def __init__(self,x,y,width,height,type=0):
    '''
    Creates a sprite that will kill the player at a certain position. Depending on the type, assigns an appearance and rect to it. More than 10 lines of code to handle all types of "deathblocks," which occur throughout the game.
    args:
      self
      x: int
      y: int
      width: int
      height: int
      type: int
    returns: None
    '''
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
      self.image.fill((255,255,255))
      self.rect=self.image.get_rect()
      self.rect.topright=[x,y]
    self.type=type
    self.alternate=False
  def getloc(self):
    '''
    Returns the x and y location of the block as a tuple.
    args: self
    returns: 
      self.rect.x: int
      self.rect.y: int
    '''
    return (self.rect.x,self.rect.y)
  def die(self):
    '''
    Removes the sprite from all groups, and moves it off-screen so it cannot be interacted with.
    args: self
    returns: None
    '''
    self.rect.y+=100
    self.kill()
  def update(self):
    '''
    Depending on the type, updates the sprite in different ways.
    args: self
    returns: None
    '''
    if self.type<3:
      self.rect.x-=3
    elif self.type==3:
      if self.alternate:
        self.alternate=False
      else:
        self.rect.y+=1
        