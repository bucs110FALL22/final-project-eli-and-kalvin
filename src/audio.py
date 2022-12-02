import pygame

class Audio():
  def __init__(self):
    self.file = 'assets/song.mp3'
  def audioplay(self):
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(self.file)
    pygame.mixer.music.play(loops=2, start=100.3)
    pygame.event.wait()
