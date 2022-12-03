:warning: Everything between << >> needs to be replaced (remove << >> after replacing)
# CS110 Project Proposal
# Survive the Woods
## CS 110 Final Project
### Fall 2022
### [Assignment Description](https://docs.google.com/document/d/1H4R6yLL7som1lglyXWZ04RvTp_RvRFCCBn6sqv-82ps/edit?usp=sharing)
https://replit.com/join/wbpdwumwzr-kalvinweng1)


https://jamboard.google.com/d/1FnbirFeLqDNUrMsNV_nTlI8YGqxwCTqWraLUG-juG9c/viewer?f=0

### Team: Eli and Kalvin

***

## Project Description

Survive the walk through the nature preserve! While walking through the nature preserve, the player will have to play a series of minigames to survive. At the end of each game, there will be a surprise for the user!

***    

## User Interface Design

- **Initial Concept**
  - << A wireframe or drawing of the user interface concept along with a short description of the interface. You should have one for each screen in your program. For example, if your program has a start screen, game screen, and game over screen, you should include a wireframe / screenshot / drawing of each one and a short description of the components. >>
    
    
- **Final GUI**
  - https://jamboard.google.com/d/1IyVr-l5mJ83mSrQFYeI-ECPdgcos6e9rRZtgsrfTwkY/edit?usp=sharing

***        

## Program Design

* Non-Standard libraries
- import requests
  -https://www.dataquest.io/blog/python-api-tutorial/
  - used to import files or datas from the web to help aid in adding pictures to the game
- import pygame -https://www.pygame.org/docs/
  - Allows the cration of sprites and other functions that are helpful to create a game.
  
============================
* Class Interface Design
    * << A simple drawing that shows the class relationships in your code (see below for an example). This does not need to be overly detailed, but should show how your code fits into the Model/View/Controller paradigm. >>
        * ![class diagram](assets/class_diagram.jpg)
================================================
========================================
* Classes
  * Player - this class creates the main playable character using an x-position and a y-position. The player can jump, fall, and move. There are two additional methods to get the player's location, and to allow the program rather than the user to control the player's location.
  * Block - this class is used to create surfaces the player can stand on, using x and y position. The block can move or return its location.
  * Deathblock - these sprites end the game when the player collides with them. They behave differently depending on type, and can fall, move, die, or return location
  * Frog - these sprites move around the screen much like the Player sprite does, and can also jump, fall, die, and return location.
## Project Structure and File List

The Project is broken down into the following file structure:

* main.py
* src
    * audio.py
    * block.py
    * controller.py
    * deathblock.py
    * frog.py
    * inputbox.py
    * player.py
    * pokemon.py
* assets
    * backgroundImage0.png
    * backgroundImage1.png
    * backgroundImage2.png
    * backgroundImage3.png
    * block.png
    * charedit.png
    * class_diagram.jpg
    * foldercontents.txt
    * game1button.png
    * game2button.png
    * game3button.png
    * groundblock.png
    * mainmenubutton.png
    * minigamebutton.png
    * quitbutton.png
    * replaybutton.png
    * song.mp3
    * startbutton.png
    * stump.png
* etc
    * chat.txt

***

## Tasks and Responsibilities 

   * Kalvin - worked on pokemon pets, added music
   * Eli - worked on art/visual components
   * Most of the game was made collaboratively

## Testing

* Tested each game, then added the next one.

## ATP

| Step                 |Procedure             |Expected Results                   |
|----------------------|:--------------------:|----------------------------------:|
|  1                   | Click on Shell and enter "python3 main.py"  |Pygame window opens and program begins to run. |
|  2                   | click "start" button   | The screen changes to a new background, and a character and the ground appears.      |
|  3                   | push the 'd' key continuously  | The character moves to the right, and once it hits the right side of the screen, a message appears saying, "Avoid acorns!".      |
|  4                   | push the 'w', 'a', or 'd' keys | The character moves or jumps around the screen. When colliding with one of the brown blocks, a screen will appear with three buttons reading "Replay," "Main Menu," and "Quit."     |
|  5                   | click the "Main Menu" button   | The screen changes to a new background, with two buttons reading "Start" and "Select Minigame"      |
|  6                   | click the "Select Minigame" button   | The buttons change to three buttons reading "1," "2," and "3."      |
|  7                   | click the "2" button   | The screen changes to a new background, and a character and the ground appears.      |
|  8                   | push the 'd' key continuously  | The character moves to the right, and once it hits the right side of the screen, a message appears saying, "Catch the frogs!".      |
|  9                   | push the 'w', 'a', or 'd' keys until the character has collided with all of the green blocks | The character moves or jumps around the screen. When all of the "frogs" have been caught, the text changes to "WIN!" and the character moves to the right. The screen then changes to a new background without text    |
|  10                   | push the 'd' key continuously  | The character moves to the right, and once it hits the right side of the screen, a message appears saying, "Don't fall in the water!".      |
|  11                   | press the 'w' key when the character is near the edge of one of the grassy platforms  | The character jumps. If the character collides with the side of one of the blocks, a screen will appear with three buttons reading "Replay," "Main Menu," and "Quit." When the character makes it to the end of the game, the text will change to "WIN!" and a text box will appear   |