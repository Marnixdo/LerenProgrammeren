print ("Pizzaria den Otter")
#pizza calculator

small = 3.99
medium = 6.99
large = 12.49

b = 0

while b < 1:
    try:
        aantal_small = int(input("hoeveel small pizza's "))
        aantal_medium = int(input("hoeveel medium pizza's "))
        aantal_large = int(input("hoeveel large pizza's "))
        b= 2
    except ValueError:
        print("vul een nummer in A.U.B")
        b= 0
    
print (" ")
print (f"{aantal_small} small pizza: {aantal_small* small}")
print (f"{aantal_medium} medium pizza: {aantal_medium * medium}")
print (f"{aantal_large} large pizza {aantal_large *large}")
print (" ")
print ("TOTAAL")
print (aantal_small * small + aantal_medium * medium + aantal_large * large)