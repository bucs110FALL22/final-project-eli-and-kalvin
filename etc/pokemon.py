import pygame
import requests
from urllib.request import urlopen

class Pokemon:
  def __init__(self):
    pygame.init()
    self.window = pygame.display.set_mode()
    self.pokemonfile = []
  def pokemonsprite(self, pokemonname='ditto'):
    # Search the name of the pokemon through the api and returns the sprite url
    link= f"https://pokeapi.co/api/v2/pokemon/{pokemonname.lower()}"
    r = requests.get(link)
    if r.status_code != 200:
      print("failed")
      return None
    else:
      rjson = r.json()
      sprite= rjson['sprites']['front_default']
      image_url = sprite
      image_str = urlopen(image_url).read()
      return image_str