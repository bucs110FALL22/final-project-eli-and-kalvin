import io
import pygame
import requests
from urllib.request import urlopen

class Pokemon:
  def __init__(self):
    pygame.init()
    self.window = pygame.display.set_mode()
    self.pokemonfile = []
    self.distancecounter = 100
  def pokemonsprite(self, pokemonname='ditto'): 
    # Gets the sprite for the pokemon by using the api
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
      image_file = io.BytesIO(image_str)
      image = pygame.image.load(image_file)
      self.window.blit(image, (200, 200))
      pygame.display.update()

  
  # def randomname(self):
      # This originall was suppose to be a button and get a few random pokemon, but we are running out of time so I'm trashing this idea.
  #   int = random.randint(0,999)
  #   link = "https://pokeapi.co/api/v2/pokemon?limit=1000&offset=0"
  #   r = requests.get(link)
  #   rjson = r.json
    
  #   name = rjson[int]['name']
  #   return name
    