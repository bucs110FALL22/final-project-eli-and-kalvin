import Player
import requests
import random
class Inventory:
  def __init__(self):
    self.inventory = returninventory()
    self.coin = self.inventory[0,0]
    self.points = self.inventory[1,0]
    self.score = self.inventory[2,0]
    self.pets =[]
  def rewards():
    # based on the points/coins/score some pokemon pets will be displayed
    response = requests.get("https://github.com/PokeAPI/sprites/tree/master/sprites/pokemon")
    randomnum = random.randrange(10000, 10200)
    if self.coins > 90:
      self.pets(append)
      # append png image from the file request into self.pets and later display the images
    if self.points > 150:
    self.pets(append)
    # append png image from the file request into self.pets and later display the images
    if self.score > 250:
      self.pets(append)
      # append png image from the file request into self.pets and later display the images
    def returnpets(self):
      return self.pets
    