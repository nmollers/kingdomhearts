import sys
import random
import time
import cmd
import os

stats = {"kracht":50,
         "HP": 100,
         "XP": 0}



inventory = {"potions":0,
             }
             
chestFound = 0


sword = {"sword" : 1}
shield = {"shield" : 1}
magic_wand = {"magic_wand" : 1}

inventory["potions"] += chestFound



def travelers_town():
    print('')

def after_first_fight():
    print('After defeating the weird creatures on the platform you see a door appearing on the platform')
    choice = input('Do you want to go through the door or do you want to look around on the platform?> ')
    if choice == 'go':
        print('You decided to go through the door')
        travelers_town()#Placeholder for travelers town *1st world
    elif choice == 'look':
        print('You decided to look on the platform and find a christmas tree with presents underneath it.')
        # Chest spawn needs to come here

### First fight with Heartless on the glass platform
def first_fight():
    print(f"After choosing the {'start_choice moet hier komen'} some weird creatures start appearing on the platform")
    print(f"You don't have a chance to run away so you need to fight them!")
    quit #Placeholder for fight system
    after_first_fight()# If player defeats the Heartless the story goes further
    first_fight()# If player gets killed in the fight he needs fight them again

### Intro of the game where player needs to make a choice between 3 items
def start_game():
    print("""You'r floating from the sky into a large glass platform where you see three different items
You see a Sword, Shield and a Magic Wand and are thinking what you should pick""")
    print("Make your choice between a sword, shield and magic wand")
    start_choice = input("Whats gonna be your choice?> ")
    if start_choice == 'sword':
        sure = input("You picked the 'sword' are you sure?> ")
        if sure == 'yes':
            stats["kracht"] = 1
            print("You'r stats have been changed to: --")
            print(inventory)
            print(stats)
            first_fight() #Placeholder for first fight
        elif sure == 'no':
            start_game()
    if start_choice == 'shield':
        sure = input("You picked the 'shield' are you sure?> ")
        if sure == 'yes':
            stats["kracht"] = 1                                                         #   needs specification 
            print("You'r stats have been changed to: --")
            print(inventory)
            print(stats)
            first_fight() #Placeholder for first fight
        elif sure == 'no':
            start_game()
        ### Change stats to sword stats
    if start_choice == 'magic wand':
        sure = input("You picked the 'magic wand' are you sure?> ")
        if sure == 'yes':
            stats["kracht"] = 1
            print("You'r stats have been changed to: --")
            print(inventory)
            print(stats)                                                                #   needs specification 
            first_fight() #Placeholder for first fight
        elif sure == 'no':
            start_game()
        ### Change stats to sword stats
    else:
        print("please make a valid choice")
        start_game()

### Intro if the player want's to start the game or get some help ###
def intro_kingdomhearts():
    print('Welcome to Text-Based Kingdom Hearts!')
    keuze1 = input("Do you wan't to start playing the game, quit or do you want some help?> ")
    if keuze1 == 'play':
        start_game()    
    elif keuze1 == 'help':
        print("---")
        intro_kingdomhearts()
    elif keuze1 == 'quit':
        quit
    else:
        print('Please make a valid choice')
        keuze1 = input("Do you wan't to start paying the game or do you want some help?> ")

intro_kingdomhearts()