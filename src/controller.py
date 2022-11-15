#I think we should code one minigame first, then see if we can add the rest, then if all goes well and we have time, implement the main idea
#I think running away from the bear, geometry-dash style or maybe like temple-run style would work the best as a standalone game
#(or we could change it to running away from bees or something, since we don't know about the bear)
#I'm outlining this as if we're going to do all of them, but I'm trying to keep our options open just in case
#I'm willing to do a lot of the work for this if we have the time
class Controller:
  
  def __init__(self):
    pygame.init()
    self.display=pygame.display.set_mode()
    self.dimensions=pygame.display.get_window_size()
    self.screen=#some value that is going to represent the mainmenu loop. the value of this changes for different screens
    #also, that^^ might be a bad way to do it. idk. will reevaluate later.
    
    self.mainmenubg
    self.maingamebg
    self.game1bg
    self.game2bg
    self.game3bg
    self.youdiedbg
    #backgrounds^^^

    
  def mainloop(self): #idk if this is how im supposed to write this, this might be wrong but it's just supposed to check which loop is supposed to be running so it's not super important
    running=True
    while running:
      mainmenuloop() if self.screen==#value that represents main menu
      maingameloop() if self.screen==#some value that represents main game
      game1loop() if self.screen==#some value that represents minigame 1
      game2loop() if self.screen==#value
      game3loop() if self.screen==#value
      gameoverloop() if self.screen==#value
      pickminigameloop() if self.screen==#value
      petloop() if self.screen==#value
  
  
  def mainmenuloop(self):
    while self.screen==#above value
      #EVENT LOOP
      if event.type==pygame.MOUSEBUTTONDOWN:
        clickpos=event.pos
        if startbutton.collidepoint(clickpos):
          self.screen=#some value that represents the main game
        elif minigame.collidepoint(clickpos):
          self.screen=#value that rep.s minigame selection menu
        elif instructions.collidepoint(clickpos):
          self.screen=#represents instructions menu
      
      #UPDATE DATA (no data? I think?)

      #REDRAW
      self.display.blit(self.mainmenubg,self.dimensions)
      self.display.blit(#stuff for start button)
      self.display.blit(#stuff for minigame selection button)
      self.display.blit(#stuff for instructions button)
      pygame.display.flip()


        
  def game1loop(self):
    gamehasstarted=False
    isjumping=False
    while self.screen==#some value:
      #EVENT LOOP
      if event.type==pygame.KEYDOWN:
        key=event.key
      elif event.type==pygame.MOUSEBUTTONDOWN:
        clickpos=event.pos
        if returntomenubutton.collidepoint(clickpos):
          self.screen==#main menu value
      
      if key==pygame.K_SPACE and not gamehasstarted: #using space to start game
        gamehasstarted=True
      elif key==pygame.K_SPACE and not isjumping: #using space to jump
        isjumping=True

      #update data -- dunno what to do here yet

      #REDRAW
      pygame.display.blit(game1bg,self.size)
      #must redraw character according to position
      #redraw foreground
      #if background is moving, redraw that too
      if not gamehasstarted:
        #display message "press space to start/jump"

  
  def gameoverloop(self):
      #event loop

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