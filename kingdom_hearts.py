#Python Text RPG
#MadeByNoah
import cmd
import textwrap
import sys
import os
import time
import random
screen_width = 100
## Start Sora Player Stats ##
class Sora:
    def __init__(self):
        self.name = ''
        self.hp = 18
        self.mp = 2
        self.str = 6
        self.df = 1
        self.location = 'Dream'
        self.game_over = False
        self.choice = ''
Sora = Sora()
## Title Screen ##
def title_screen_selections():
    option = input("> ")
    if option.lower() == ("play"):
        start_game() #placeholder for the moment
    elif option.lower() == ("help"):
        help_menu() #placeholder for the moment
    elif option.lower() == ("quit"):
        sys.exit()
    while option.lower() not in ["play", "help", "quit"]: 
        print("Place make a valid choise.")
        option = input("> ")

def title_screen():
    os.system("Clear")
    print("#####################################")
    print("Welcome to Text-Based Kingdom Hearts!")
    print("#####################################")
    print("               -Play-                ")
    print("               -Help-                ")
    print("               -Quit-                ")
    print("             MadeByNoah              ")
    title_screen_selections()

def help_menu():
    print("#####################################")
    print("Welcome to Text-Based Kingdom Hearts!")
    print("#####################################")
    print("     Use Words to play the game      ")
    print("             MadeByNoah              ")
    title_screen_selections()

## Game Controlers ##
def start_game():
    print()

## Map ##
"""
a1, a2... #Player starts at b2
-------------
|  |  |  |  | a4
-------------
|  |  |  |  | b4...
-------------
|  |  |  |  | 
-------------
"""
ZONENAME = ''
DESCRIPTION = 'description'
EXAMINATION = 'examine'
SOLVED = False
UP = 'up', 'north'
DOWN = 'down', 'south'
LEFT = 'left', 'west'
RIGHT = 'right', 'east'

solved_places = {'a1': False,'a2': False,'a3': False,'a4': False,
                'b1': False,'b2': False,'b3': False,'b4': False,
                'c1': False,'c2': False,'c3': False,'c4': False,
                'd1': False,'d2': False,'d3': False,'d4': False,}

zonemap = {
    'a1': {,
        ZONENAME: '',
        DESCRIPTION = 'description'
        EXAMINATION = 'examine'
        SOLVED = False
        UP = 'up', 'north'
        DOWN = 'down', 'south'
        LEFT = 'left', 'west'
        RIGHT = 'right', 'east'
    },
    'a2': {
        ZONENAME: '',
        DESCRIPTION = 'description'
        EXAMINATION = 'examine'
        SOLVED = False
        UP = 'up', 'north'
        DOWN = 'down', 'south'
        LEFT = 'left', 'west'
        RIGHT = 'right', 'east'
    },
    'a3': {
        ZONENAME: '',
        DESCRIPTION = 'description'
        EXAMINATION = 'examine'
        SOLVED = False
        UP = 'up', 'north'
        DOWN = 'down', 'south'
        LEFT = 'left', 'west'
        RIGHT = 'right', 'east'
    },
    'a4': {
        ZONENAME: '',
        DESCRIPTION = 'description'
        EXAMINATION = 'examine'
        SOLVED = False
        UP = 'up', 'north'
        DOWN = 'down', 'south'
        LEFT = 'left', 'west'
        RIGHT = 'right', 'east'
    },
    'b1': {
        ZONENAME: '',
        DESCRIPTION = 'description'
        EXAMINATION = 'examine'
        SOLVED = False
        UP = 'up', 'north'
        DOWN = 'down', 'south'
        LEFT = 'left', 'west'
        RIGHT = 'right', 'east'
    },
    'b2': {
        ZONENAME: 'Home',
        DESCRIPTION = 'This is your home'
        EXAMINATION = 'Your home looks old and creepy'
        SOLVED = False
        UP = 'a2',
        DOWN = 'c2',
        LEFT = 'b1',
        RIGHT = 'b3',   
    }
}

## Game Interactivity ##
def print_location():
    print('\n' + ('#' * (4 + len(Sora.location))))
    print('# ' + Sora.location.upper() + ' #')
    print('# ' + zonemap[Sora.position] [DESCRIPTION] + ' #')
    print('\n' + ('#' * (4 + len(Sora.location))))

def prompt():
    print('\n' + '===========================')
    print('What would you like to do?')
    action = input('> ')
    acceptable_actions = ['move', 'go', 'travel', 'walk', 'quit', 'examine', 'inspect', 'interact', 'look']
    while action.lower() not in acceptable_actions:
        print('Unknow action, please try again.\n')
        action = input('> ')
    if action.lower() == 'quit':
        sys.exit()
    elif action.lower() in ['move', 'go', 'travel', 'walk']:
        Sora_move(action.lower())#placeholder
    elif action.lower() in ['examine', 'inspect', 'interact', 'look']:
        Sora_examine(action.lower())#placeholder

def Sora_move(myAction):
    ask = 'Where would you like to move to?\n'
    dest = input(ask)
    if dest in ['up', 'north']:
        destination = zonemap[Sora.location][UP]
        movement_handler(destination)
    elif dest in ['down', 'south']:
        destination = zonemap[Sora.location][DOWN]
        movement_handler(destination)
    elif dest in ['left', 'west']:
        destination = zonemap[Sora.location][LEFT]
        movement_handler(destination)
    elif dest in ['right', 'east']:
        destination = zonemap[Sora.location][RIGHT]
        movement_handler(destination)

def movement_handler(destination):
    print('\n' + 'You have moved to the ' + destination + '.')
    Sora.location = destination
    print_location()

def Sora_examine(action):
    if zonemap[Sora.location][SOLVED]:
        print('You have already exhausted this zone.')
    else:
        print('Triger Fight here')

## Game Functionality ##
def start_game():
    return

def main_game_loop():
    while Sora.game_over is False:
        prompt()
        # handle boss defeated, eplored everthing, etc.

def setup_game():
    os.system('clear')
    #Setup
    question = 'What type of player are you?\n'
    questionadded = "(You can choose between: sword, shield or magic wand)\n"
    for character in question:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    for character in questionadded:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    player_choice = input('> ')
    valid_choices = ['sword', 'shield', 'magic wand']
    if player_choice.lower() is valid_choices:
        Sora.choice = player_choice
        print('You have selected ' + player_choice '!\n')
    while player_choice.lower() not in valid_choices:
        player_choice = input('> ')
        if player_choice.lower() is valid_choices:
            Sora.choice = player_choice
            print('You have selected ' + player_choice '!\n')

## Player Stats deponding on choice
if Sora.choice is 'sword':
    Sora.mp = '3'
    Sora.str = '6'
    Sora.df = '2'
elif Sora.choice is 'shield':
    Sora.mp = '3'
    Sora.str = '5'
    Sora.df = '1'
elif Sora.choice is 'magic wand':
    Sora.mp = '3'
    Sora.str = '3'
    Sora.df = '3'
    
## Introduction
question = 'What type of player are you?\n'
for character in question:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)





title_screen()