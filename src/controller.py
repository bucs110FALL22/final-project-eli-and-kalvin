import pygame
from src.player import Player
from src.block import Block
from src.deathblock import Deathblock

class Controller:
  
  def __init__(self):
    pygame.init()
    #self.display=pygame.display.set_mode((500,250))
    self.display = pygame.display.set_mode()
    self.displayx,self.displayy=pygame.display.get_window_size() #replaced "size" with 2 variables for x-length and y-length bc I was using these variables elsewhere
    self.background_images = [
            "assets/backgroundImage1.png",
        ]
    self.background = pygame.image.load(self.background_images[0])
    self.background = pygame.transform.scale(self.background, (self.displayx,self.displayy))
    
    self.display.blit(self.background,(0,0))
    pygame.display.update()


    #self.screen=1 #self.screen keeps track of which screen/part of game is playing


    
  def mainloop(self):
    running=True
    while running:
      pass
      #if self.screen==0:
        #self.mainmenuloop()
      #elif self.screen==1:
        #self.game1loop()
  #    elif self.screen==2:
  #      game2loop()
  #    elif self.screen==3:
  #      game3loop()
  #    elif self.screen==4:
  #      maingameloop()
  #    elif self.screen==5:
  #      gameoverloop()
  #    elif self.screen==6:
  #      pickminigameloop()
  #    elif self.screen==7:
  #      petloop()
      #elif self.screen==8: #option to quit game will set self.screen to 8
        #running=False
  
  
  def mainmenuloop(self):
    startbutton=pygame.Rect(0,self.displayy/2,100,50)
    minigamebutton=pygame.Rect(self.displayx-100,self.displayy/2,100,10)
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
    xloc=75 #location of character on screen
    platformwidth,platformheight=(100,19)
    spawnheights=[210,165,120,210,165,165,165,230]
    stumps=[(1000,210),(1250,165)]
    character=Player(xloc,self.displayy/2)
    i=0
    blocks=[]
    deathblocks=[] #"deathblocks" meaning anything that ends the game when the player collides w/ it
    for spawnheight in spawnheights:
      i+=1
      add=i*125
      blocks.append(Block((self.displayx+add),spawnheight,platformwidth,platformheight))
      deathblocks.append(Deathblock(self.displayx+add-platformwidth,spawnheight+2,1,17))
    ground=Block(self.displayx,self.displayy-20,self.displayx,5,True)
    water=Deathblock(self.displayx,self.displayy-5,self.displayx,5,2)
    for stump in stumps:
      deathblocks.append(Deathblock(stump[0],stump[1],10,10,1))
    all_sprites=pygame.sprite.Group()
    surfaceblocks=pygame.sprite.Group() #blocks the player can stand on
    badblocks=pygame.sprite.Group() #deathblocks
    moveblocks=pygame.sprite.Group() #blocks that move
    for block in blocks:
      moveblocks.add(block)
      surfaceblocks.add(block)
      all_sprites.add(block)
    for deathblock in deathblocks:
      moveblocks.add(deathblock)
      badblocks.add(deathblock)
      all_sprites.add(deathblock)
    all_sprites.add(character,ground,water)
    badblocks.add(water)
    surfaceblocks.add(ground)
    moveblocks.add(ground)
    
    #EVENT LOOP
    while self.screen==1:
      for event in pygame.event.get():
        if event.type==pygame.KEYDOWN:
          if event.key==pygame.K_SPACE or event.key==pygame.K_w:
            character.jump()
          elif event.key==pygame.K_q: #press Q to quit
            self.screen=8

      #UPDATE DATA
      charloc=character.gety()
      platform=pygame.sprite.spritecollideany(character,surfaceblocks)
      death=pygame.sprite.spritecollideany(character,badblocks)
      if death:
        self.screen=8
      elif platform:
        platformy=platform.getloc()[1]
        character.stopfall(platformy)
      else:
        character.fall()
      if charloc>self.displayy: #if there's a glitch and the character's outside the screen, reset location
        character.override(xloc,self.displayy-charheight)
      moveblocks.update()

      #REDRAW
      self.display.blit(self.background,(0,0))
      all_sprites.draw(self.display)
      character.update()
      pygame.display.flip()
      pygame.time.wait(20) #this makes the jumping a lot smoother

  
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