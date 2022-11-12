import Inventory
import Player

class Display:
  def __init__(self, screen):
    self.pets = returnpets()
    self.screen = screen
    # the screen will be useful to show the pos of the pets
    self.image = returnimage()
  def displaypets(self):
    if len(self.pets) == 1:
      # Display image of the pet on the screen that is a reflection across the y-axis. Display  of pet will be at the lower right corner of the screen
    if len(self.pets) == 2:
      # Player will be at the center and one pet will be displayed ont he elft whle the other is on the right
    if len(self.pets) == 3:
      # One of the pet will be displayed on the left along with the player and the other two will be displayed on the right of the screen
  def displayplayer(self)
    # This will show the image of the player and over ride anything in the location of the player
  