import cmd
import textwrap
import sys
import os
import time
import random
from tkinter import *


inventory = {"potions":0,
             "sword": None,
             "shield": None,
             "magic wand":None}
             
print(inventory)

chest = 0
chestFound = 2

inventory["potions"] += chestFound

print(inventory)







window = Tk()
window.geometry("1500x1000")





window.mainloop()