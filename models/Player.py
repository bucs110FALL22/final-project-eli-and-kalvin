class Player:
  def __init__(self, name, hp, pos, image):
    self.name = name
    self.hp = hp
    self.pos = pos
    self.image = image
    self.inventory = [
      ["coin", ""],
      ["points", ""],
      ["score", ""] 
    ]
  def updatehp(self, damage):
    # if the player loses a game their hp will decrease
    self.hp -= damage
    return self.hp
  def updateinventory(self, item, value):
    # once the player wins a game, they will gain some items which will be added into their inventory
    self.inventory.replace(item, value)
    return self.inventory
  def returninventory(self)
  # to be used in other models
    return self.inventory
  def updatepos(self, pos):
    # to be used in other models
    self.pos = pos
  def returnplayer(self)
# to be used in other models
    return self.image
  
    
    
  