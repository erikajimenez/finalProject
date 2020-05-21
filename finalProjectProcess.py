'''
Created on Mar 7, 2020

@author: ITAUser
'''
OBJECTIVE:
This program will alllow user to play guess the number against the computer
-we will...    
-create code that takes the input from the user 
-create code that takes "input" form the computer 
-check if the user wants to quit OR does not enter one of the options
-loop each round of the game
-add statements at the beginning and end of the game welcoming the player to the game and thanking them for playing 
-loop game so they can keep playing until they choose to quit

PSEUDOCODE:
#set variable keepPlaying to True
#while keepPlaying is True:
    #print statement welcoming players to the game
    #print statement stating the rules
    #import random function the makes its choice randomly from this function
    #computer's choice = random number between 1 and 15 (random functions gets used here)
    #player's choice = input(ask player to guess a number)
    #start checking user guesses
    #if player inputs 'q': --player wants to end the game
    #else if (if player inputs number between 1 and 15 and computer choose same number)
    #print that they win
    #else if (if player inputs number between 1 and 15 and computer chooses different number)
    #print that they need to guess again
    #print number of guesses they have left
    #else:
        #tell the user their input was not valid
    #print statement thanking the player for playing
    #if (player guesses number in 3 or less guesses)
    #print that they win
    #else:
        #print that they lost
    #