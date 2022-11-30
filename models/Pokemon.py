import Player
import io
import pygame
import requests
import random
from urllib.request import urlopen

class Pokemon:
  def __init__(self):
    pygame.init()
    self.window = pygame.display.set_mode()
    # self.inventory = returninventory()
    # self.coin = self.inventory[0,0]
    # self.points = self.inventory[1,0]
    # self.score = self.inventory[2,0]
    # self.pets =[]
  def pokemonsprite(self, pokemonname='ditto'):
    link= f"https://pokeapi.co/api/v2/pokemon/{pokemonname.lower()}"
    r = requests.get(link)
    while r.status_code != 200:
      print("failed")
    else:
      rjson = r.json()
      sprite= rjson['sprites']['front_default']
    image_url = sprite
    image_str = urlopen(image_url).read()
    image_file = io.BytesIO(image_str)
    image = pygame.image.load(image_file)
    self.window.blit(image, (20, 20))
    pygame.display.update()
  # def randomname(self):
  #   int = random.randint(0,999)
  #   link = "https://pokeapi.co/api/v2/pokemon?limit=1000&offset=0"
  #   r = requests.get(link)
  #   rjson = r.json
    
  #   name = rjson[int]['name']
  #   return name
    