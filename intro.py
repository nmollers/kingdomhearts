import sys
import random
import time
import cmd
import os

def travelers_town():
    print('After going through the door you random wake up by a dog thats licking your face')
    print('You look up and see goofy licking your face so you wake up')
    print("After waking up you'r in a random ally in a town where you don't know the name of")
    print("You only have the choice to go straight forward")
    movement = input("Make you'r choice> ")
    if movement == 'forward':
        print("You walked out of the ally and see you'r in the middle of the town")
        print("You see 2 little shops and 3 big doors around you")
        choice = input("you have the choice to go to the 2 shops or the first big door> ")
        if choice == 'first shop':
            print('You walk in the first shop and you see a man behind the counter')
            talk_leave = input("Want to speak to the man behind the counter or leave the shop?> ")
            if talk_leave == 'talk':
                print('Man: Hello there how can I help you?')
                choice1 = input("talk or buy?> ")
                if choice1 == 'talk':
                    print("You: Hello there what's your name?")
                    print("Man: I'm z")
        elif choice == 'second shop':
            print('You walk in the second shop where you see Huey, Dewey, and Louie standing behind the counter')
        elif choice == 'first big door':
            print('You decided to go through the first big door and are now in the second district of the town')
            print("After arriving in the second district you see a man running towards you but you don't know why he is running")
            print("After the man has run past you you see the weird creatures you defeated earlier appearing from the shadows of the town")
            # Fight with Heartless 
        # If player defeats the Heartless he can go with exploring the second district
        

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
            print("You'r stats have been changed to: --")
            first_fight() #Placeholder for first fight
        elif sure == 'no':
            start_game()
    if start_choice == 'shield':
        sure = input("You picked the 'shield' are you sure?> ")
        if sure == 'yes':
            print("You'r stats have been changed to: --")
            first_fight() #Placeholder for first fight
        elif sure == 'no':
            start_game()
        ### Change stats to sword stats
    if start_choice == 'magic wand':
        sure = input("You picked the 'magic wand' are you sure?> ")
        if sure == 'yes':
            print("You'r stats have been changed to: --")
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