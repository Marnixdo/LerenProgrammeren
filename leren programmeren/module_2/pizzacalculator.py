print ("Pizzaria den Otter")
#pizza calculator

small = 3.99
medium = 6.99
large = 12.49

aantal_small = float(input("hoeveel small pizza's "))
aantal_medium = float(input("hoeveel medium pizza's "))
aantal_large = float(input("hoeveel large pizza's "))

print (" ")
print (f"{aantal_small} small pizza: {aantal_small* small}")
print (f"{aantal_medium} medium pizza: {aantal_medium * medium}")
print (f"{aantal_large} large pizza {aantal_large *large}")
print (" ")
print ("TOTAAL")
print (aantal_small * small + aantal_medium * medium + aantal_large * large)