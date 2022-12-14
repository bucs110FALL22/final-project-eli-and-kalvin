import pygame
import random
from src.player import Player
from src.block import Block
from src.deathblock import Deathblock
from src.frog import Frog
from src.audio import Audio
from src.pokemon import Pokemon
import io

class Controller:

  def __init__(self):
    '''
    Initializes pygame, stores background png files, creates font, and creates self.game and self.screen variables to store what game is being played.
    args: self
    returns: None
    '''
    pygame.init()
    self.display = pygame.display.set_mode((500, 250))
    self.displayx, self.displayy= pygame.display.get_window_size()
    self.background_images = [
      "assets/backgroundImage0.png",
      "assets/backgroundImage1.png",
      "assets/backgroundImage2.png",
      "assets/backgroundImage3.png",
    ]
    self.font=pygame.font.Font(None,25)
    self.screen = 0
    self.game = 0

  def mainloop(self):
    '''
    Keeps track of what game is being played, and whether the program is running.
    args: self
    returns: None
    '''
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
      elif self.screen==5:
        self.petloop()
      elif self.screen == 8:
        running = False

  def mainmenuloop(self):
    '''
    Main title screen where the user is allowed to choose between running the game chronologically or choosing a minigame to start from. It must contain more than 10 lines of code, in order to respond to events.
    args: self
    returns: None
    '''
    
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

      #REDRAW
      self.background= pygame.image.load(self.background_images[0])
      self.display.blit(self.background, (0, 0))
      self.display.blit(pygame.image.load("assets/startbutton.png"),(self.displayx/2-50,self.displayy/2-55))
      self.display.blit(pygame.image.load("assets/minigamebutton.png"),(self.displayx/2-50,self.displayy/2+10))
      pygame.display.flip()

  def game3loop(self):
    '''
    The third game, where the player must avoid crashing into blocks or falling into the water. It must contain more than 10 lines of code, since it creates several sprites and has to keep track of all collisions and interactions between them.
    args: self
    returns: None
    '''
    xloc = 75
    platformwidth=100
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
      blocks.append(Block((self.displayx + add), spawnheight))
      deathblocks.append(Deathblock(self.displayx + add-platformwidth,spawnheight+2,1,17))
    ground=Block(self.displayx,self.displayy-20,True)
    add=(i+3)*125
    finalblock=Block(self.displayx+add, self.displayy-20,True)
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
    while self.screen == 1 and self.game == 3:
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
        self.game=0
        self.screen = 5
        
      elif charloc[0] < 0:
        character.override(charloc[0] + 5, charloc[1])
      if charloc[1] > self.displayy:
        character.override(charloc[0], 0)
      moveblocks.update()
      if finsh:
        character.override(charloc[0]+5,charloc[1])
        msg=self.font.render("WIN!",False,(0,0,0))
      else:
        lastblock.update()
        msg=self.font.render("Don't fall into the water!",False,(0,0,0))
      character.update()

      #REDRAW
      self.background = pygame.image.load(self.background_images[3])
      self.background = pygame.transform.scale(self.background,                   (self.displayx, self.displayy))
      self.display.blit(self.background, (0, 0))
      self.display.blit(self.display,(0,0))
      self.display.blit(msg,(self.displayx/2-100,10))
      all_sprites.draw(self.display)
      pygame.display.flip()
      pygame.time.wait(15)
  
  def gameoverloop(self):
    '''
    A screen that is displayed when the user dies, giving the option to quit the game, restart it, or return to the main menu. It must contain more than 10 lines of code, in order to respond to events.
    args: self
    returns: None
    '''
    replaybutton=pygame.Rect(self.displayx/2-50, self.displayy/2-40,100,30)
    menubutton=pygame.Rect(self.displayx/2-50, self.displayy/2,100,30)
    quitbutton=pygame.Rect(self.displayx/2-50, self.displayy/2+40,100,30)
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

      #REDRAW
      if self.game==1:
        self.background = pygame.image.load(self.background_images[1])
      elif self.game==2:
        self.background = pygame.image.load(self.background_images[2])
      elif self.game==3:
        self.background = pygame.image.load(self.background_images[3])
        self.background = pygame.transform.scale(self.background,                   (self.displayx, self.displayy))
      self.display.blit(self.background, (0, 0))
      self.display.blit(self.display,(0,0))
      self.display.blit(self.display,(0,0))
      self.display.blit(pygame.image.load("assets/replaybutton.png"),(self.displayx/2-50,self.displayy/2-40))
      self.display.blit(pygame.image.load("assets/mainmenubutton.png"),(self.displayx/2-50,self.displayy/2))
      self.display.blit(pygame.image.load("assets/quitbutton.png"),(self.displayx/2-50,self.displayy/2+40))
      pygame.display.flip()

  def game1loop(self):
    '''
    The first game, where the player must avoid acorns. It must contain more than 10 lines of code, since it creates several sprites and has to keep track of all collisions and interactions between them.
    args: self
    returns: None
    '''
    character = Player(self.displayx / 2, 50)
    ground = Block(self.displayx, self.displayy - 20,True)
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
    
    while self.screen==1 and self.game==1:
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
        msg=self.font.render("Avoid acorns!",False,(255,255,255))
      else:
        msg=self.font.render("WIN!",False,(255,255,255))
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

      self.background = pygame.image.load(self.background_images[1])
      self.background = pygame.transform.scale(self.background,(self.displayx, self.displayy))
      self.display.blit(self.background, (0, 0))
      self.display.blit(msg,(self.displayx/2-100,10))
      all_sprites.draw(self.display)
      character.update()
      pygame.display.flip()

  def pickminigameloop(self):
    '''
    A screen that displays three buttons, giving the user the options of playing game 1, 2, or 3. It must contain more than 10 lines of code, in order to respond to events.
    args: self
    returns: None
    '''
    game1button=pygame.Rect(self.displayx/2-50, self.displayy/2-40,100,30)
    game2button=pygame.Rect(self.displayx/2-50, self.displayy/2,100,30)
    game3button=pygame.Rect(self.displayx/2-50, self.displayy/2+40,100,30)
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
      self.background= pygame.image.load(self.background_images[0])
      self.display.blit(self.background, (0, 0))
      self.display.blit(pygame.image.load( "assets/game1button.png"),(self.displayx/2-50,self.displayy/2-40))
      self.display.blit(pygame.image.load( "assets/game2button.png"),(self.displayx/2-50,self.displayy/2))
      self.display.blit(pygame.image.load( "assets/game3button.png"),(self.displayx/2-50,self.displayy/2+40))
      pygame.display.flip()

  
  def maingameloop(self):
    '''
    A screen that is displayed between games, when the character is walking through the woods. It must contain more than 10 lines of code, in order to respond to events and control the player sprite.
    args: self
    returns: None
    '''
    character = Player(self.displayx / 2, 50)
    ground = Block(self.displayx, self.displayy - 20, True)
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

      if self.game==0:
        self.background = pygame.image.load(self.background_images[1])
      elif self.game==1:
        self.background = pygame.image.load(self.background_images[2])
      else:
        self.background = pygame.image.load(self.background_images[3])
        self.background = pygame.transform.scale(self.background,
                                             (self.displayx, self.displayy))

      self.display.blit(self.background, (0, 0))
      all_sprites.draw(self.display)
      character.update()
      pygame.display.flip()
      pygame.time.wait(100)
      
  def game2loop(self):
    '''
    The second game, where the player must catch all of the frogs before they disappear. It must contain more than 10 lines of code, since it creates several sprites and has to keep track of all collisions and interactions between them.
    args: self
    returns: None
    '''
    character = Player(self.displayx / 2, 50)
    ground = Block(self.displayx, self.displayy - 20, True)
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
    while self.screen==1 and self.game==2:
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
            self.game=1
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
        msg=self.font.render("WIN!",False,(255,255,255))
        character.override(charloc[0]+5,charloc[1])
        if charloc[0] > self.displayx:
          self.screen=2
      else:
        msg=self.font.render("Catch the frogs! (R to restart)",False,(255,255,255))
      
      self.background = pygame.image.load(self.background_images[2])
      self.display.blit(self.background, (0, 0))
      self.display.blit(msg,(50,10))
      all_sprites.draw(self.display)
      character.update()
      pygame.display.flip()
      pygame.time.wait(10)

  def petloop(self):
    '''
    Screen where the user types in the name of a pokemon and they will appear on the screen. Input box will switch color when clicked. It contains then 10 lines of code because the method is managing both the pokemon and input box.
    args: self
    returns: None
    '''
    clock = pygame.time.Clock()
    input_box1 = (100, 100, 140, 32)
    done = False
    self.display.blit(self.background, (0,0))
    colorOff = pygame.Color('lightskyblue3')
    colorOn = pygame.Color('dodgerblue2')
    font = pygame.font.Font(None, 32)
    color = colorOff
    text = ''
    txt_surface = font.render(text, True, 'black')
    active = False
    image_str = []
    appear = False
    while self.screen==5:
      # Loop for both the textbox and the api
      displacement = 0
      while not done:
          rect = pygame.Rect(input_box1)
          pygame.draw.rect(self.display, color, rect) 
          for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
              if rect.collidepoint(event.pos):
                  active = not active
              else:
                  active = False
              color = colorOn if active else colorOff
            if event.type == pygame.KEYDOWN:
                if active: 
                    if event.key == pygame.K_RETURN:
                        if Pokemon().pokemonsprite(pokemonname=text) == None:
                          text= ''
                          self.display.blit(self.background, (0,0))
                          active = False
                          done = True
                          appear = True
                        else:
                          image_str.append(Pokemon().pokemonsprite(pokemonname=text))
                          text =''
                          txt_surface = font.render(text, True, color) 
                          active = False
                          done = True
                          appear = True
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode
            txt_surface = font.render(text, True, 'black')
            self.display.blit(txt_surface, (rect.x+5, rect.y+5))
            width = max(200, txt_surface.get_width()+10)
            rect.w = width
            pygame.display.flip()
            clock.tick(60)
      print(displacement)
      self.display.blit(self.background, (0,0))
      while appear:
        for i in image_str:
          image_file = io.BytesIO(i)
          image = pygame.image.load(image_file)
          self.display.blit(image, (displacement,self.displayy-25))
          print(displacement, self.displayy-25)
          pygame.display.update()
          displacement += 100
          done = False
          active = True
          appear = False
        if displacement >= self.displayx:
          self.screen=0
    