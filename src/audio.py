import pygame

class Audio():
  def __init__(self):
    '''
    Stores the audio file in self.file.
    args: self
    returns: None
    '''
    self.file = 'assets/song.mp3'
  def audioplay(self):
    '''
    Initializes pygame, and plays the audio file.
    args: self
    returns: None
    '''
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(self.file)
    pygame.mixer.music.play(loops=2, start=100.3)
    pygame.event.wait()
