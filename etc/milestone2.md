# Final Project Milestone II

*Place this document in your final project repo folder `/etc`. *

***

Come up with interfaces for 3 possible classes you think you may need for your project. Again, brainstorm a little. Nothing is *wrong*.

## Game Context
Survivie the walk through the nature perserve! While walking through the nature perserve, player will have to play a series of minigame to survive. At the end of the game, there will be a suprise for the user!

## Class Interface 1

class Player:
  attributes:
    (x, y)
    image
    health
    inventory
    name
  methods:
    positionchange() ##left,right,forward
    update_inventory()
    damage()
    gethealth()
    attack()

    jump()  ---For a 3D, definitely but for a 2D game, jump won't be helpful
(kalvin--feel free to change anything, i'm just brainstorming here because we don't have anything yet :))

## Class Interface 2
class GameOneBear:
### I want to use what you said about like cataching frog. We could use the first game as catching bears and player must xx amount of bears

  attributes:
    (x, y)
    timeleft
    bearnumber
    points
    image
    
  methods:
    boxclick()
    addpoints()
    time()
    display()
    gameresult()

## Class Interface 3
### For loot we can do something like a puzzle. Player's choice in loot determine what kind of suprise they get at the end of the game. Feel free to change my idea.
class Loot:
  attributes:
    image
    type
  methods:
    boxclick()
    addlootitem()
### Game 2 is IDK.

## Class Interface 4
## GameThreePokemonBattle. Essentially players choose a pokemon to battle. 
  attributes
    player_one_pokemon_card
    computer_pokemon_card
    pokemon_one_hp
    pokemon_one_ability_one
    pokemon_one_ability_two
    pokemon_two_hp
    pokemon_two_ability_one
    pokemon_two_ability_two
  methods:
    abilitydamage()
    turn()
    pokemonsearch()
    gameover()
    

    
    
    
    