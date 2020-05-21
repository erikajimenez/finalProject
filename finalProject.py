'''
Created on Mar 7, 2020

@author: ITAUser
'''
#set variable keepPlaying to True
keepPlaying = True
#while keepPlaying is True:
while (keepPlaying):
    tries = 0
    while(tries < 3):
        #print statement welcoming players to the game
            print("welcome to guess the number")
        #print statement stating the rules
            print("guess the number in 3 or less tries and win, press q to quit game.")
        #import random function the makes its choice randomly from this function
        import random
        #computer's choice = random number between 1 and 15 (random functions gets used here)
        def pick_random_integer():
            integer = random.randint(1,15)
            return integer
        computer_pick = random.randint(1,15)
        #player's choice = input(ask player to guess a number)
        player_pick = random.randint(1,15)
        
        playerChoice = input("guess a number between 1 and 15")
        #start checking user guesses
        #else if (if player inputs number between 1 and 15 and computer choose same number)
        #print that they win
        if player_pick == computer_pick:
            print("you win")
        #else if (if player inputs number between 1 and 15 and computer chooses different number)
        #print that they need to guess again
        else:
            print("that's incorrect, guess again")
            tries += 1
        #tell the user their input was not valid
        else:
            print("that input was invalid")
            
        if pick_random_integer not in range(1,15):
            print("not an option")
        
        
