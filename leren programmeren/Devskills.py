from operator import truediv


gastheer = True
gasten = False
drank = True
chips = True

if (gastheer and drank) or (gasten and drank and chips) or (gasten and gastheer and drank and chips):
    print ("Start the party")
else:
    print ("No party")