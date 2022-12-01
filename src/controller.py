import pygame
from src.player import Player
from src.block import Block
from src.deathblock import Deathblock
from src.inputbox import InputBox


class Controller:

  def __init__(self):
    pygame.init()
    self.display = pygame.display.set_mode((500, 250))
    #self.display = pygame.display.set_mode()
    self.displayx, self.displayy = pygame.display.get_window_size(
    )  #replaced "size" with 2 variables for x-length and y-length bc I was using these variables elsewhere
    self.background_images = [
      "assets/backgroundImage1.png",
    ]
    self.background = pygame.image.load(self.background_images[0])
    self.background = pygame.transform.scale(self.background,
                                             (self.displayx, self.displayy))

    self.display.blit(self.background, (0, 0))
    pygame.display.update()

    self.screen = 0  #self.screen keeps track of which screen/part of game is playing (screen 1 is any game;self.game selects which game)
    self.game = 0

  def mainloop(self):
    running = True
    while running:
      if self.screen == 0:
        self.mainmenuloop()
      elif self.screen == 1 and self.game == 1:
        self.game1loop()
        self.petloop()
      elif self.screen == 1 and self.game == 2:
        self.game2loop()
      elif self.screen == 1 and self.game == 3:
        self.game3loop()
      elif self.screen == 2:
        self.maingameloop()
      elif self.screen == 3:
        self.gameoverloop()

  #    elif self.screen==4:
  #      pickminigameloop()
  #    elif self.screen==5:
  #      petloop()

      elif self.screen == 8:  #option to quit game will set self.screen to 8
        running = False

  def mainmenuloop(self):
    minigamebutton = pygame.Rect(self.displayx / 2 - 50, self.displayy / 2,
                                 100, 50)
    startbutton = pygame.Rect(self.displayx / 2 - 50, self.displayy / 2 - 75,
                              100, 50)
    while self.screen == 0:

      #EVENT LOOP
      for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
          clickpos = event.pos
          print("click")
          if startbutton.collidepoint(clickpos):
            self.screen = 2
          elif minigamebutton.collidepoint(clickpos):
            self.screen = 7
        elif event.type == pygame.KEYDOWN:
          if event.key == pygame.K_q:
            self.screen = 8

      #UPDATE DATA (n/a)

      #REDRAW
      pygame.draw.rect(self.display, (0, 0, 0), startbutton)
      pygame.draw.rect(self.display, (100, 100, 100), minigamebutton)
      #replace these later^^
      pygame.display.flip()

  def game1loop(self):
    xloc = 75  #location of character on screen
    platformwidth, platformheight = (100, 19)
    spawnheights = [210, 165, 120, 210, 165, 165, 165, 230]
    #stumps=[(1000,210),(1250,165)]
    character = Player(xloc, self.displayy / 2)
    i = 0
    finsh = False  #see "finalblock" for context
    blocks = []
    deathblocks = [
    ]  #"deathblocks" meaning anything that ends the game when the player collides w/ it
    for spawnheight in spawnheights:
      i += 1
      add = i * 125
      blocks.append(
        Block((self.displayx + add), spawnheight, platformwidth,
              platformheight))
      deathblocks.append(
        Deathblock(self.displayx + add - platformwidth, spawnheight + 2, 1,
                   17))
    ground = Block(self.displayx, self.displayy - 20, self.displayx, 5, True)
    add = (i + 3) * 125
    finalblock = Block(self.displayx + add, self.displayy - 20, self.displayx,
                       5, True)
    water = Deathblock(self.displayx, self.displayy - 5, self.displayx, 5, 2)
    #for stump in stumps:
    #deathblocks.append(Deathblock(stump[0],stump[1],10,10,1))
    all_sprites = pygame.sprite.Group()
    surfaceblocks = pygame.sprite.Group()  #blocks the player can stand on
    badblocks = pygame.sprite.Group()  #deathblocks
    moveblocks = pygame.sprite.Group()  #blocks that move
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
          elif event.key == pygame.K_q:  #press Q to quit
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
      if charloc[0] > self.displayx - 10:  #"-10" to account for player width
        self.screen = 2
      elif charloc[0] < 0:
        character.override(charloc[0] + 5, charloc[1])
      if charloc[1] > self.displayy:
        character.override(charloc[0], 0)
      #^^if there's a glitch and the character's outside the screen, reset location
      moveblocks.update()
      if finsh:
        character.control(2)
      else:
        lastblock.update()

      #REDRAW
      self.display.blit(self.background, (0, 0))
      all_sprites.draw(self.display)
      character.update()
      pygame.display.flip()
      pygame.time.wait(20)  #this makes the jumping a lot smoother

  def gameoverloop(self):
    while self.screen == 3:
      replaybutton = pygame.Rect(self.displayx / 2 - 50, 50, 100, 50)
      menubutton = pygame.Rect(self.displayx / 2 - 50, 125, 100, 50)
      quitbutton = pygame.Rect(self.displayx / 2 - 50, 250, 100, 50)
    while self.screen == 0:

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
      pygame.display.fill("white")
      pygame.draw.rect(self.display, (0, 0, 0), startbutton)
      pygame.draw.rect(self.display, (100, 100, 100), minigamebutton)
      #replace these later^^
      pygame.display.flip()

  def game2loop(self):
    print("game 2wooo")
    self.screen = 2
    #event loop

    #update data

    #redraw

  #def pickminigameloop(self):
  #event loop

  #update data

  #redraw

  def maingameloop(self):
    character = Player(self.displayx / 2, 50)
    ground = Block(self.displayx, self.displayy - 20, self.displayx, 5, True)
    all_sprites = pygame.sprite.Group()
    surfaceblocks = pygame.sprite.Group()
    all_sprites.add(character, ground)
    surfaceblocks.add(ground)
    while self.screen == 2:
      #EVENT LOOP
      for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_a or event.key == pygame.K_LEFT:
            character.control(-2)
          elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
            character.control(2)
          elif event.key == pygame.K_SPACE or event.key == pygame.K_w or event.key == pygame.K_UP:
            character.jump()
          elif event.key == pygame.K_q:
            self.screen = 8
        elif event.type == pygame.KEYUP:
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

      self.display.blit(self.background, (0, 0))
      all_sprites.draw(self.display)
      character.update()
      pygame.display.flip()
      pygame.time.wait(20)

  #def game3loop(self):
  #event loop

  #update data

  #redraw

  #def petloop(self):
  # i did some of this in the pokemon model. all that model does is it gets a sprite from the api.
  #event loop

  #update data

  #redraw
  def petloop(self):
    clock = pygame.time.Clock()
    input_box1 = InputBox(100, 100, 140, 32)
    input_box2 = InputBox(100, 300, 140, 32)
    input_boxes = [input_box1, input_box2]
    done = False
    while not done:
      self.display.blit(self.background, (0, 0))
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          done = True
        for box in input_boxes:
          box.handle_event(event)
      for box in input_boxes:
        box.update()
      # self.display.fill((30, 30, 30))
      for box in input_boxes:
        box.draw(self.display)
      pygame.display.flip()
      clock.tick(30)
