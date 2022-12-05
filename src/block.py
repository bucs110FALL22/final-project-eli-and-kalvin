import pygame

class Block(pygame.sprite.Sprite):
  def __init__(self,x,y,ground=False):
    '''
    Creates a block sprite at a certain position. Depending on the type of block, assigns an appearance and rect to it.
    args: 
      self
      x: int
      y: int
      ground: boolean
    returns: None
    '''
    super().__init__()
    if not ground:
      IMAGE=pygame.image.load('assets/block.png').convert_alpha()
      self.image=IMAGE
    else:
      IMAGE=pygame.image.load('assets/groundblock.png').convert_alpha()
      self.image=IMAGE
    self.rect=self.image.get_rect()
    self.rect.topright=[x,y]
  def getloc(self):
    '''
    Returns the x and y location of the block as a tuple.
    args: self
    returns: 
      self.rect.x: int
      self.rect.y: int
    '''
    return (self.rect.x,self.rect.y)
  def update(self):
    '''
    Moves the block.
    args: self
    returns: None
    '''
    self.rect.x-=3