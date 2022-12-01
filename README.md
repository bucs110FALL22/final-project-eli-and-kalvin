:warning: Everything between << >> needs to be replaced (remove << >> after replacing)
# CS110 Project Proposal
# << Project Title >>
## CS 110 Final Project
### Fall 2022
### [Assignment Description](https://docs.google.com/document/d/1H4R6yLL7som1lglyXWZ04RvTp_RvRFCCBn6sqv-82ps/edit?usp=sharing)

https://replit.com/join/wbpdwumwzr-kalvinweng1)

<< [link to demo presentation slides](#) >>

### Team: [blank]
#### Eli and Kalvin

***

## Project Description

Survive the walk through the nature preserve! While walking through the nature preserve, the player will have to play a series of minigames to survive. At the end of the game, there will be a surprise for the user!

***    

## User Interface Design

- **Initial Concept**
  - << A wireframe or drawing of the user interface concept along with a short description of the interface. You should have one for each screen in your program. For example, if your program has a start screen, game screen, and game over screen, you should include a wireframe / screenshot / drawing of each one and a short description of the components. >>
    
    
- **Final GUI**
  - << You should also have a screenshot of each screen for your final GUI >>

***        

## Program Design

* Non-Standard libraries
    * << You should have a list of any additional libraries or modules used (pygame, request) beyond non-standard python. 
         For each additional module you should include
         - url for the module documentation
         - a short description of the module >>
=============================================================
import requests
  -https://www.dataquest.io/blog/python-api-tutorial/
  - used to import files or datas from the web to help aid in like adding picutres to the game
import random, pygame, math
  - class notes
  - really depends on situation but generally speaking to help with a random selection for import random; pygame to run the whole thing; and math to some math problems with the pos of certain objects
  - not really sure if I need the math module but maybe
============================
* Class Interface Design
    * << A simple drawing that shows the class relationships in your code (see below for an example). This does not need to be overly detailed, but should show how your code fits into the Model/View/Controller paradigm. >>
        * ![class diagram](assets/class_diagram.jpg)
================================================
https://jamboard.google.com/d/1FnbirFeLqDNUrMsNV_nTlI8YGqxwCTqWraLUG-juG9c/viewer?f=0
========================================
* Classes
    * << You should have a list of each of your classes with a description. >>
    * ===============================================
* Player-the basic information about the player and the items they have
* Inventory- the value of the items and a function to help decide the rewards
* Display-- change the screen when enter neew game and the winning screen at the end of the game
## Project Structure and File List

The Project is broken down into the following file structure:

* main.py
* src
    * << all of your python files should go here >>
* assets
    * << all of your media, i.e. images, font files, etc, should go here) >>
* etc
    * << This is a catch all folder for things that are not part of your project, but you want to keep with your project >>

***

## Tasks and Responsibilities 

   * Outline the team member roles and who was responsible for each class/method, both individual and collaborative.

## Testing

* << Describe your testing strategy for your project. >>

## ATP

| Step                 |Procedure             |Expected Results                   |
|----------------------|:--------------------:|----------------------------------:|
|  1                   | Run Counter Program  |GUI window appears with count = 0  |
|  2                   | click count button   | display changes to count = 1      |
etc...
