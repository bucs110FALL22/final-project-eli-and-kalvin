# Final Project Milestone II

*Place this document in your final project repo folder `/etc`. *

***

Come up with interfaces for 3 possible classes you think you may need for your project. Again, brainstorm a little. Nothing is *wrong*.

## Class Interface 1

class Player:
  attributes:
    x
    y
    image
    health
    inventory
  methods:
    left()
    right()
    jump()
    update_inventory()
    takedamage()
    gethealth()
    attack()
(kalvin--feel free to change anything, i'm just brainstorming here because we don't have anything yet :))

## Class Interface 2

class Bear:
  attributes:
    x
    y
    health
  methods:
    left()
    right()
    takedamage()
    attack()

## Class Interface 3

class Loot:
  attributes:
    x
    y
    image
    type
  methods:
    getcollected()
