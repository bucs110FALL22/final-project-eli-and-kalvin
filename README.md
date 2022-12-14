:warning: Everything between << >> needs to be replaced (remove << >> after replacing)
# CS110 Project Proposal
# Survive the Woods
## CS 110 Final Project
### Fall 2022
### [Assignment Description](https://docs.google.com/document/d/1H4R6yLL7som1lglyXWZ04RvTp_RvRFCCBn6sqv-82ps/edit?usp=sharing)
https://replit.com/join/wbpdwumwzr-kalvinweng1)

Demo slides:
https://docs.google.com/presentation/d/1WJYbhtsORL1l6su9HFzyQSwPmBSQxTK-biLVMRnVhiU/edit#slide=id.g4dfce81f19_0_45


### Team: Eli and Kalvin

***

## Project Description

Survive the walk through the nature preserve! While walking through the nature preserve, the player will have to play a series of minigames to survive. At the end, the user wins a prize.

***    

## User Interface Design

- **Initial Concept**
  - https://jamboard.google.com/d/1FnbirFeLqDNUrMsNV_nTlI8YGqxwCTqWraLUG-juG9c/viewer?f=0
    
    
- **Final GUI**
  - https://jamboard.google.com/d/1IyVr-l5mJ83mSrQFYeI-ECPdgcos6e9rRZtgsrfTwkY/edit?usp=sharing

***        

## Program Design

* Non-Standard libraries
- requests
  -https://www.dataquest.io/blog/python-api-tutorial/
  - used to import files or datas from the web to help aid in adding pictures to the game
- pygame -https://www.pygame.org/docs/
  - Allows the creation of sprites and other functions that are helpful to create a game.
- io -(https://docs.python.org/3/library/io.html)
  - converts png link to sprites
- urlopen -https://docs.python.org/3/library/urllib.request.html
  - opens the file to be read and used
  
============================
* Class Interface Design
        * ![class diagram](etc/ClassDiagram.png)
================================================
========================================
* Classes
  * Player - this class creates the main playable character using an x-position and a y-position. The player can jump, fall, and move. There are two additional methods to get the player's location, and to allow the program rather than the user to control the player's location.
  * Block - this class is used to create surfaces the player can stand on, using x and y position. The block can move or return its location.
  * Deathblock - these sprites end the game when the player collides with them. They behave differently depending on type, and can fall, move, die, or return location
  * Frog - these sprites move around the screen much like the Player sprite does, and can also jump, fall, die, and return location.
  * Audio - helps retrieve the audio file and play the audio file
  * Pokemon - retrieves the sprite of the pokemon to be displayed on screen
## Project Structure and File List

The Project is broken down into the following file structure:

* main.py
* src
    * audio.py
    * block.py
    * controller.py
    * deathblock.py
    * frog.py
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
   * Eli - worked on art/visual components, and the games
   * Most of the game was made collaboratively

## Testing

* Tested each game, then added the next one.
* Debugg the codes first and then added new game into the controller.

## ATP

| Step                 |Procedure             |Expected Results                   |
|----------------------|:--------------------:|----------------------------------:|
|  1                   | Click on Shell and enter "python3 main.py"  |Pygame window opens and program begins to run. |
|  2                   | click "start" button   | The screen changes to a new background, and a character and the ground appears.      |
|  3                   | push the 'd' key continuously  | The character moves to the right, and once it hits the right side of the screen, a message appears saying, "Avoid acorns!".      |
|  4                   | push the 'w', 'a', or 'd' keys or the arrow keys | The character moves or jumps around the screen. When colliding with one of the brown blocks, a screen will appear with three buttons reading "Replay," "Main Menu," and "Quit."     |
|  5                   | click the "Main Menu" button   | The screen changes to a new background, with two buttons reading "Start" and "Select Minigame"      |
|  6                   | click the "Select Minigame" button   | The buttons change to three buttons reading "1," "2," and "3."      |
|  7                   | click the "2" button   | The screen changes to a new background, and a character and the ground appears.      |
|  8                   | push the 'd' key continuously  | The character moves to the right, and once it hits the right side of the screen, a message appears saying, "Catch the frogs!".      |
|  9                   | push the 'w', 'a', or 'd' keys until the character has collided with all of the green blocks | The character moves or jumps around the screen. When all of the "frogs" have been caught, the text changes to "WIN!" and the character moves to the right. The screen then changes to a new background without text    |
|  10                   | push the 'd' key continuously  | The character moves to the right, and once it hits the right side of the screen, a message appears saying, "Don't fall in the water!".      |
|  11                   | press the 'w' key when the character is near the edge of one of the grassy platforms  | The character jumps. If the character collides with the side of one of the blocks, a screen will appear with three buttons reading "Replay," "Main Menu," and "Quit." When the character makes it to the end of the game, the text will change to "WIN!" and the screen will change to one with a blue text box.  |
|  11                   | click on the text box and enter the name of a pokemon  | The pokemon will appear below the screen.  |
|  12                   | continue to enter pokemon  | The screen will change to the main menu.  |
|  13                   | click "start" button   | The screen changes to a new background, and a character and the ground appears.      |
|  14                   | press the "q" key  | The program quits.   |