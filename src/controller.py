import pygame
from src.player import Player
from src.block import Block

class Controller:
  
  def __init__(self):
    pygame.init()
    self.display=pygame.display.set_mode((750,300))
    self.displayx,self.displayy=pygame.display.get_window_size()
    self.screen=1 #I'm working on game 1 rn, so setting it to this
    
    #self.mainmenubg
    #self.maingamebg
    #self.game1bg
    #self.game2bg
    #self.game3bg
    #self.youdiedbg
    #backgrounds^^^

    
  def mainloop(self):
    running=True
    while running:
      if self.screen==0:
        self.mainmenuloop()
      elif self.screen==1:
        self.game1loop()
      #elif self.screen==2:
        #game2loop()
      #elif self.screen==3:
        #game3loop()
  #    elif self.screen==4:
  #      maingameloop()
  #    elif self.screen==5:
  #      gameoverloop()
  #    elif self.screen==6:
  #      pickminigameloop()
  #    elif self.screen==7:
  #      petloop()
      elif self.screen==8: #option to quit game will set self.screen to 8
        running=False
  
  
  def mainmenuloop(self):
    startbutton=pygame.rect(0,self.displayy/2,100,50)
    minigamebutton=pygame.rect(self.displayx-100,self.displayy/2,100,10)
    while self.screen==0:
      #EVENT LOOP
      for event in pygame.event.get():
        if event.type==pygame.MOUSEBUTTONDOWN:
          clickpos=event.pos
          if startbutton.collidepoint(clickpos):
            self.screen=4
          elif minigamebutton.collidepoint(clickpos):
            self.screen=7
        elif event.type==pygame.KEYDOWN:
          if event.key==pygame.K_q:
            self.screen=8

      
      #UPDATE DATA (no data? I think?)

      #REDRAW
      #self.display.blit(self.mainmenubg,self.dimensions)
      self.display.fill("white")
      pygame.draw.rect(self.display,(0,0,0),startbutton)
      pygame.draw.rect(self.display,(100,100,100),minigamebutton)
      #replace these later^^
      pygame.display.flip()


        
  def game1loop(self):
    xloc=75
    charwidth,charheight=(10,10)
    platformwidth,platformheight=(100,5)
    character=Player(xloc,self.displayy/2,charwidth,charheight)
    block1=Block(self.displayx,250,platformwidth,platformheight)
    block2=Block(self.displayx+100,200,platformwidth,platformheight)
    block3=Block(self.displayx+200,150,platformwidth,platformheight)
    block4=Block(self.displayx+300,100,platformwidth,platformheight)
    ground=Block(self.displayx,self.displayy-5,self.displayx,5)
    all_sprites=pygame.sprite.Group()
    all_blocks=pygame.sprite.Group()
    moveblocks=pygame.sprite.Group()
    all_sprites.add(character,block1,block2,block3,block4,ground)
    all_blocks.add(block1,block2,block3,block4,ground)
    moveblocks.add(block1,block2,block3,block4)
    #EVENT LOOP
    while self.screen==1:
      for event in pygame.event.get():
        if event.type==pygame.KEYDOWN:
          if event.key==pygame.K_SPACE:
            character.jump()
            print("jump!")
          elif event.key==pygame.K_q:
            self.screen=8

      #UPDATE DATA
      charloc=character.gety()
      block=pygame.sprite.spritecollideany(character,all_blocks)
      if block:
        blocky=block.getloc()[1]
        character.stopfall(blocky)
      else:
        character.fall()
      if charloc>self.displayy:
        character.override(xloc,self.displayy-charheight)
      block1.move(2)
      block2.move(2)
      block3.move(2)
      block4.move(2)

      #REDRAW
      self.display.fill("white")
      all_sprites.draw(self.display)
      character.update()
      pygame.display.flip()
      pygame.time.wait(10)

  
  def gameoverloop(self):
    while self.screen==5:
      #EVENT LOOP
      for event in pygame.event.get():
        if event.type==pygame.MOUSEBUTTONDOWN:
          clickpos=event.pos
          if returntomenu.collidepoint(clickpos):
            self.screen=0
          elif playagain.collidepoint(clickpos):
            self.screen=1

      #update data

      #redraw

#necessary^^^
#if we have time vvv
    
  #def maingameloop(self):
      #event loop

      #update data

      #redraw

  #def pickminigameloop(self):
      #event loop

      #update data

      #redraw
    
  #def game2loop(self):
      #event loop

      #update data

      #redraw
  
  #def game3loop(self):
      #event loop

      #update data

      #redraw
    
  #def petloop(self):
      #event loop

      #update data

      #redraw