import pygame
import random
from src.player import Player
from src.block import Block
from src.deathblock import Deathblock
from src.frog import Frog
from src.inputbox import InputBox
from src.audio import Audio

class Controller:

  def __init__(self):
    pygame.init()
    self.display = pygame.display.set_mode((500, 250))
    self.displayx, self.displayy= pygame.display.get_window_size()
    self.background_images = [
      "assets/backgroundImage1.png",
      "assets/backgroundImage2.png",
    ]

    self.font=pygame.font.Font(None,25)
    self.screen = 0
    self.game = 0

  def mainloop(self):
    running = True
    while running:
      Audio().audioplay()
      if self.screen == 0:
        self.mainmenuloop()
      elif self.screen == 1 and self.game == 1:
        self.game1loop()
      elif self.screen == 1 and self.game == 2:
        self.game2loop()
      elif self.screen == 1 and self.game == 3:
        self.game3loop()
      elif self.screen == 1 and self.game == 4:
        self.game=0
        self.screen=0
      elif self.screen == 2:
        self.maingameloop()
      elif self.screen == 3:
        self.gameoverloop()
      elif self.screen==4:
        self.pickminigameloop()
      elif self.screen == 8:
        running = False

  def mainmenuloop(self):
    minigamebutton = pygame.Rect(self.displayx / 2 - 50, self.displayy/2+10,100,50)
    startbutton = pygame.Rect(self.displayx / 2 - 50, self.displayy/2-55,100,50)
    while self.screen == 0:

      #EVENT LOOP
      for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
          clickpos = event.pos
          if startbutton.collidepoint(clickpos):
            self.screen = 2
          elif minigamebutton.collidepoint(clickpos):
            self.screen = 4
        elif event.type == pygame.KEYDOWN:
          if event.key == pygame.K_q:
            self.screen = 8

      #UPDATE DATA (n/a)

      #REDRAW
      self.background= pygame.image.load(self.background_images[1])
      self.display.blit(self.background, (0, 0))
      self.display.blit(pygame.image.load("assets/startbutton.png"),(self.displayx/2-50,self.displayy/2-55))
      self.display.blit(pygame.image.load("assets/minigamebutton.png"),(self.displayx/2-50,self.displayy/2+10))
      pygame.display.flip()

  def game1loop(self):
    xloc = 75  #location of character on screen
    platformwidth, platformheight = (100, 19)
    spawnheights = [210, 165, 120, 210, 165, 165, 165, 230]
    stumps=[(1250,165)]
    character = Player(xloc, self.displayy / 2)
    i = 0
    finsh = False
    blocks = []
    deathblocks = []
    for spawnheight in spawnheights:
      i += 1
      add = i * 125
      blocks.append(Block((self.displayx + add), spawnheight, platformwidth,platformheight))
      deathblocks.append(Deathblock(self.displayx + add-platformwidth,spawnheight+2,1,17))
    ground=Block(self.displayx,self.displayy-20, self.displayx,5,True)
    add=(i+3)*125
    finalblock=Block(self.displayx+add, self.displayy-20,self.displayx,5,True)
    water = Deathblock(self.displayx, self.displayy - 5, self.displayx, 5, 2)
    for stump in stumps:
      deathblocks.append(Deathblock(stump[0],stump[1],10,10,1))
    all_sprites = pygame.sprite.Group()
    surfaceblocks = pygame.sprite.Group()
    badblocks = pygame.sprite.Group()
    moveblocks = pygame.sprite.Group()
    lastblock = pygame.sprite.Group()
    for block in blocks:
      moveblocks.add(block)
      surfaceblocks.add(block)
      all_sprites.add(block)
    for deathblock in deathblocks:
      moveblocks.add(deathblock)
      badblocks.add(deathblock)
      all_sprites.add(deathblock)
    all_sprites.add(character, ground, water, finalblock)
    badblocks.add(water)
    surfaceblocks.add(ground, finalblock)
    moveblocks.add(ground)
    lastblock.add(finalblock)

    #EVENT LOOP
    while self.screen == 1 and self.game == 1:
      for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_SPACE or event.key == pygame.K_w or event.key == pygame.K_UP:
            character.jump()
          elif event.key == pygame.K_q:
            self.screen = 8

      #UPDATE DATA
      charloc = character.getloc()
      platform = pygame.sprite.spritecollideany(character, surfaceblocks)
      death = pygame.sprite.spritecollideany(character, badblocks)
      finish = pygame.sprite.spritecollideany(character, lastblock)
      if death:
        self.screen = 3
      elif platform:
        platformy = platform.getloc()[1]
        character.stopfall(platformy)
      else:
        character.fall()
      if finish:
        finsh = True
      if charloc[0] > self.displayx - 10:
        self.screen = 2
      elif charloc[0] < 0:
        character.override(charloc[0] + 5, charloc[1])
      if charloc[1] > self.displayy:
        character.override(charloc[0], 0)
      moveblocks.update()
      if finsh:
        msg=self.font.render("WIN!",False,(0,0,0))
        input_box1 = InputBox(100, 100, 140, 32)
        input_boxes = [input_box1]
      else:
        lastblock.update()
        msg=self.font.render("Don't fall into the water!",False,(0,0,0))
      character.update()

      #REDRAW
      self.background = pygame.image.load(self.background_images[0])
      self.background = pygame.transform.scale(self.background,                   (self.displayx, self.displayy))
      self.display.blit(self.background, (0, 0))
      self.display.blit(self.display,(0,0))
      self.display.blit(msg,(self.displayx/2-100,10))
      all_sprites.draw(self.display)
      if finsh:
        for box in input_boxes:
          box.handle_event(event)
          box.update()
          box.draw(self.display)
      pygame.display.flip()
      pygame.time.wait(15)
  
  def gameoverloop(self):
    replaybutton = pygame.Rect(self.displayx / 2 - 50, 50, 100, 50)
    menubutton = pygame.Rect(self.displayx / 2 - 50, 125, 100, 50)
    quitbutton = pygame.Rect(self.displayx / 2 - 50, 250, 100, 50)
    while self.screen == 3:

      #EVENT LOOP
      for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
          clickpos = event.pos
          if menubutton.collidepoint(clickpos):
            self.screen = 0
            self.game = 0
          elif replaybutton.collidepoint(clickpos):
            self.screen = 1
          elif quitbutton.collidepoint(clickpos):
            self.screen = 8
        elif event.type == pygame.KEYDOWN:
          if event.key == pygame.K_q:
            self.screen = 8

      #UPDATE DATA (n/a)

      #REDRAW
      self.background = pygame.image.load(self.background_images[0])
      self.background = pygame.transform.scale(self.background,                   (self.displayx, self.displayy))
      self.display.blit(self.background, (0, 0))
      self.display.blit(self.display,(0,0))
      pygame.draw.rect(self.display, (0, 0, 0), replaybutton)
      pygame.draw.rect(self.display, (100, 100, 100), menubutton)
      #replace these later^^
      pygame.display.flip()

  def game2loop(self):
    character = Player(self.displayx / 2, 50)
    ground = Block(self.displayx, self.displayy - 20, self.displayx, 5, True)
    i=0
    keyupallow=False
    all_sprites = pygame.sprite.Group()
    surfaceblocks = pygame.sprite.Group()
    acorns=pygame.sprite.Group()
    for slow in range(15):
      acornx=random.randint(1,self.displayx)
      i+=1
      adds=i*50
      slow=Deathblock(acornx,-adds,5,5,3)
      acorns.add(slow)
      all_sprites.add(slow)
    i=0
    for medium in range(25):
      acornx=random.randint(1,self.displayx)
      addm=adds+(i*15)
      i+=1
      medium=Deathblock(acornx,-addm,5,5,3)
      acorns.add(medium)
      all_sprites.add(medium)
    i=0
    for fast in range(25):
      acornx=random.randint(1,self.displayx)
      addf=addm+(i*5)
      i+=1
      fast=Deathblock(acornx,-addf,5,5,3)
      acorns.add(fast)
      all_sprites.add(fast)
    lastacorn=Deathblock(acornx,-addf,5,5,3)
    all_sprites.add(character,ground,lastacorn)
    surfaceblocks.add(ground)
    
    while self.screen==1 and self.game==2:
      #EVENT LOOP
      for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_a or event.key == pygame.K_LEFT:
            character.control(-2)
            keyupallow=True
          elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
            character.control(2)
            keyupallow=True
          elif event.key == pygame.K_SPACE or event.key == pygame.K_w or event.key == pygame.K_UP:
            character.jump()
          elif event.key == pygame.K_q:
            self.screen = 8
        elif event.type==pygame.KEYUP and keyupallow:
          if event.key == pygame.K_a or event.key == pygame.K_LEFT:
            character.control(2)
          elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
            character.control(-2)

      acorns.update()
      
      charloc=character.getloc()
      platform= pygame.sprite.spritecollideany(character, surfaceblocks)
      fallcollision=pygame.sprite.spritecollideany(ground, acorns)
      death=pygame.sprite.spritecollideany(character, acorns)
      end=pygame.sprite.spritecollideany(lastacorn, surfaceblocks)
      if not end:
        lastacorn.update()
      if fallcollision:
        fallcollision.die()
      if death:
        self.screen=3
      if platform:
        platformy = platform.getloc()[1]
        character.stopfall(platformy)
      else:
        character.fall()
      if not end:
        msg=self.font.render("Avoid acorns!",False,(0,0,0))
      else:
        msg=self.font.render("WIN!",False,(0,0,0))
        character.override(charloc[0]+5,charloc[1])
        if charloc[0] > self.displayx:
          self.screen=2
        
      if charloc[0]>self.displayx-10 and not end:
        character.override(charloc[0]-5, charloc[1])
      elif charloc[0] < 0:
        character.override(charloc[0]+5, charloc[1])
      if charloc[1] > self.displayy:
        character.override(charloc[0], 0)
      pygame.time.wait(10)

      self.background = pygame.image.load(self.background_images[0])
      self.background = pygame.transform.scale(self.background,(self.displayx, self.displayy))
      self.display.blit(self.background, (0, 0))
      self.display.blit(msg,(self.displayx/2-100,10))
      all_sprites.draw(self.display)
      character.update()
      pygame.display.flip()

  def pickminigameloop(self):
    game1button=pygame.Rect(self.displayx/2-50, self.displayy/2-20,100,30)
    game2button=pygame.Rect(self.displayx/2-50, self.displayy/2+20,100,30)
    game3button=pygame.Rect(self.displayx/2-50, self.displayy/2+60,100,30)
    while self.screen == 4:

      #EVENT LOOP
      for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
          clickpos = event.pos
          if game1button.collidepoint(clickpos):
            self.game=1
            self.screen = 1
          elif game2button.collidepoint(clickpos):
            self.game=2
            self.screen = 1
          elif game3button.collidepoint(clickpos):
            self.game=3
            self.screen = 1
        elif event.type == pygame.KEYDOWN:
          if event.key == pygame.K_q:
            self.screen = 8

      #UPDATE DATA (n/a)

      #REDRAW
      self.background= pygame.image.load(self.background_images[1])
      self.display.blit(self.background, (0, 0))
      pygame.draw.rect(self.display,(0,0,0),game1button)
      pygame.draw.rect(self.display,(0,0,0),game2button)
      pygame.draw.rect(self.display,(0,0,0),game3button)
      pygame.display.flip()

  
  def maingameloop(self):
    character = Player(self.displayx / 2, 50)
    ground = Block(self.displayx, self.displayy - 20, self.displayx, 5, True)
    all_sprites = pygame.sprite.Group()
    surfaceblocks = pygame.sprite.Group()
    all_sprites.add(character, ground)
    surfaceblocks.add(ground)
    keyupallow=False
    while self.screen == 2:
      #EVENT LOOP
      for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
          keyupallow=True
          if event.key == pygame.K_a or event.key == pygame.K_LEFT:
            character.control(-2)
          elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
            character.control(2)
          elif event.key == pygame.K_SPACE or event.key == pygame.K_w or event.key == pygame.K_UP:
            character.jump()
          elif event.key == pygame.K_q:
            self.screen = 8
        elif event.type==pygame.KEYUP and keyupallow:
          if event.key == pygame.K_a or event.key == pygame.K_LEFT:
            character.control(2)
          elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
            character.control(-2)

      charloc = character.getloc()
      platform = pygame.sprite.spritecollideany(character, surfaceblocks)
      if platform:
        platformy = platform.getloc()[1]
        character.stopfall(platformy)
      else:
        character.fall()
      if charloc[0] > self.displayx - 10:  #"-10" to account for player width
        self.game += 1
        self.screen = 1
      elif charloc[0] < 0:
        character.override(charloc[0] + 5, charloc[1])
      if charloc[1] > self.displayy:
        character.override(charloc[0], 0)
      #^^if there's a glitch and the character's outside the screen, reset location

      self.background = pygame.image.load(self.background_images[0])
      self.background = pygame.transform.scale(self.background,
                                             (self.displayx, self.displayy))

      self.display.blit(self.background, (0, 0))
      all_sprites.draw(self.display)
      character.update()
      pygame.display.flip()
      pygame.time.wait(10)
      
  def game3loop(self):
    character = Player(self.displayx / 2, 50)
    ground = Block(self.displayx, self.displayy - 20, self.displayx, 5, True)
    all_sprites = pygame.sprite.Group()
    surfaceblocks = pygame.sprite.Group()
    playergroup=pygame.sprite.Group()
    frogs=pygame.sprite.Group()
    froglist=[]
    count=0
    keyupallow=False
    for frog in range(9):
      startx=random.randint(1,self.displayx)
      frog=Frog(startx,self.displayy/2)
      all_sprites.add(frog)
      frogs.add(frog)
      froglist.append(frog)
    all_sprites.add(character,ground)
    playergroup.add(character)
    surfaceblocks.add(ground)
    while self.screen==1 and self.game==3:
      #EVENT LOOP
      for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
          keyupallow=True
          if event.key == pygame.K_a or event.key == pygame.K_LEFT:
            character.control(-2)
          elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
            character.control(2)
          elif event.key == pygame.K_SPACE or event.key == pygame.K_w or event.key == pygame.K_UP:
            character.jump()
          elif event.key == pygame.K_q:
            self.screen = 8
          elif event.key == pygame.K_r:
            self.game=2
            self.screen=2
        elif event.type==pygame.KEYUP and keyupallow:
          if event.key == pygame.K_a or event.key == pygame.K_LEFT:
            character.control(2)
          elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
            character.control(-2)

      for f in froglist:
        randommove=random.randrange(0,50)
        f.rmove(randommove)
        if pygame.sprite.spritecollideany(f,surfaceblocks):
          groundy=ground.getloc()[1]
          f.stopfall(groundy)
        else:
          f.fall()
        if pygame.sprite.spritecollideany( f,playergroup):
          count+=1
          print(count)
          f.die()

      charloc = character.getloc()
      platform = pygame.sprite.spritecollideany(character, surfaceblocks)
      if platform:
        platformy = platform.getloc()[1]
        character.stopfall(platformy)
      else:
        character.fall()

      if charloc[0]>self.displayx-10 and count<6:
        character.override(charloc[0]-5,charloc[1])
      elif charloc[0] < 0:
        character.override(charloc[0]+5,charloc[1])
      if charloc[1] > self.displayy:
        character.override(charloc[0], 0)
      frogs.update()

      if count>5:
        msg=self.font.render("WIN!",False,(0,0,0))
        character.override(charloc[0]+5,charloc[1])
        if charloc[0] > self.displayx:
          self.screen=2
      else:
        msg=self.font.render("Catch the frogs! (R to restart)",False,(0,0,0))
      
      self.background = pygame.image.load(self.background_images[0])
      self.background = pygame.transform.scale(self.background,        (self.displayx, self.displayy))
      self.display.blit(self.background, (0, 0))
      self.display.blit(msg,(self.displayx/2-100,10))
      all_sprites.draw(self.display)
      character.update()
      pygame.display.flip()
      pygame.time.wait(10)

  #def petloop(self):
  # i did some of this in the pokemon model. all that model does is it gets a sprite from the api. thanks
  #event loop

  #update data

  #redraw

  # def petloop(self):
  #   clock = pygame.time.Clock()
  #   input_box1 = InputBox(100, 100, 140, 32)
  #   input_boxes = [input_box1]
  #   done = False
  #   while not done:
  #     self.display.blit(self.background, (0, 0))
  #     for event in pygame.event.get():
  #       if event.type == pygame.QUIT:
  #         done = True
  #       for box in input_boxes:
  #         box.handle_event(event)
  #     for box in input_boxes:
  #       box.update()
  #     for box in input_boxes:
  #       box.draw(self.display)
  #     pygame.display.flip()
  #     clock.tick(30)
