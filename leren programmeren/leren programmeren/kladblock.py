from ctypes.wintypes import PCHAR
from tkinter.messagebox import QUESTION


#Vraag: console of PC
#bereken de prijs pc: 45
# console: 55

pc_or_console =input("game je op pc of op de console? ")

if pc_or_console == "pc" :
    print ("prijs is 45 euro" )
else: 
    membership = input("ben je een member? ")
    if membership == ("ja"):
        print ("prijs is 40 euro")
    else:
       print ("prijs is 55 euro")
