import pygame

class Player(pygame.sprite.Sprite):
  def __init__(self,xpos,ypos,width,height):
    super().__init__()
    self.image=pygame.Surface([width,height]) 
    self.image.fill((255,0,0))
    self.rect=self.image.get_rect()
    self.xmotion=0
    self.ymotion=-10
    self.rect.center=[xpos,ypos]
    self.jumping=False
  def control(self,x):
    self.xmotion+=x
  def jump(self):
    if not self.jumping:
      self.jumping=True
  def update(self):
    pygame.time.wait(10)
    self.rect.x+=self.xmotion
    if self.jumping:
      self.rect.y+=self.ymotion
      if self.ymotion<10:
        self.ymotion+=1
      else:
        self.ymotion=-10
        self.jumping=False