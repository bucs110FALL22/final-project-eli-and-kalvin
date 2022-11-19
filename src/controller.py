#I think we should code one minigame first, then see if we can add the rest, then if all goes well and we have time, implement the main idea
#I think running away from the bear, geometry-dash style or maybe like temple-run style would work the best as a standalone game
#(or we could change it to running away from bees or something, since we don't know about the bear)
#I'm outlining this as if we're going to do all of them, but I'm trying to keep our options open just in case
#I'm willing to do a lot of the work for this if we have the time

import pygame
from player import Player
from button import Button

class Controller:
  
  def __init__(self):
    pygame.init()
    self.display=pygame.display.set_mode()
    self.dimensions=pygame.display.get_window_size()
    self.screen=0
    
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
        mainmenuloop()
      elif self.screen==1:
        game1loop()
      elif self.screen==2:
        game2loop()
      elif self.screen==3:
        game3loop()
      elif self.screen==4:
        maingameloop()
      elif self.screen==5:
        gameoverloop()
      elif self.screen==6:
        pickminigameloop()
      elif self.screen==7:
        petloop()
      elif self.screen==8: #option to quit game will set self.screen to 8
        running=False
  
  
  def mainmenuloop(self):
    startbutton=Button(100,50,100,10)
    minigamebutton=Button(100,100,100,10)
    buttons=pygame.sprite.Group()
    buttons.add(startbutton,minigamebutton)
    while self.screen==0:
      #EVENT LOOP
      for event in pygame.event.get():
        if event.type==pygame.MOUSEBUTTONDOWN:
          clickpos=event.pos
          if startbutton.collidepoint(clickpos):
            pygame.sprite.Group.empty(buttons)
            self.screen=4
          elif minigamebutton.collidepoint(clickpos):
            pygame.sprite.Group.empty(buttons)
            self.screen=7
        elif event.type==pygame.KEYDOWN:
          if event.key==pygame.K_q:
            self.screen=8

      
      #UPDATE DATA (no data? I think?)

      #REDRAW
      #self.display.blit(self.mainmenubg,self.dimensions)
      buttons.draw(self.display)
      pygame.display.flip()


        
  def game1loop(self):
    gamehasstarted=False
    isjumping=False
    while self.screen==1:
      for event in pygame.event.get():
        if event.type==pygame.KEYDOWN:
          if 
        elif event.type==pygame.MOUSEBUTTONDOWN:
          clickpos=event.pos
          if returntomenubutton.collidepoint(clickpos):
            self.screen==0

      #update data -- dunno what to do here yet

      #REDRAW
      pygame.display.blit(game1bg,self.size)
      player_group.update()#redraw character
      #redraw foreground
      #if background is moving, redraw that too
      if not gamehasstarted:
        #display message "press space to start/jump"

  
  def gameoverloop(self):
    while self.screen==#some value:
      #EVENT LOOP
      for event in pygame.event.get():
        if event.type==pygame.MOUSEBUTTONDOWN:
          clickpos=event.pos
          if returntomenu.collidepoint(clickpos):
            self.screen=#mainmenu value
          elif playagain.collidepoint(clickpos):
            self.screen=#minigame 1 value

      #update data

      #redraw

#necessary^^^
#if we have time vvv
    
  def maingameloop(self):
      #event loop

      #update data

      #redraw

  def pickminigameloop(self):
      #event loop

      #update data

      #redraw
    
  def game2loop(self):
      #event loop

      #update data

      #redraw
  
  def game3loop(self):
      #event loop

      #update data

      #redraw
    
  def petloop(self):
      #event loop

      #update data

      #redraw