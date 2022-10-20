score = 0

# 7 Landen keuze programma
#Dubai Vragen:
#vraag1_Dubai = "Welke taal spreken ze in Dubai? " #Engels
#vraag2_Dubai = "Denk je dat het leven in Dubai duur is? " #nee
#vraag3_Dubai = "Welke kleur is het water Dubai? " #blauw
###########################################################
# Ierland vragen:
#vraag1_Ierland = "Welk dier loopt niet in het wild in Ierland? " #Slangen
#vraag2_Ierland = "Wat is de hoofdstad van Ierland? " #Dublin
#vraag3_Ierland = "Sinds wanneer is Ierland lid van de Europese Unie? " #1973
###########################################################
# Amerika vragen:
#vraag1_Amerika = "Wat is de meest bekende supermarkt in Amerika? " #Wallmart
#vraag2_Amerika = "Wat is de andere naam voor Amerika? " #verenigde staten
#vraag3_Amerika = "Wie is de president van Amerika? " #joe biden
###########################################################
# Japan Vragen:
# vraag1_Japan = "Welke taal spreken ze in Japan? " #Japanese
# vraag2_Japan = "Hoe heten stripboeken in het Japans? " #manga
# vraag3_Japan = "Wat is de hoofdstad van Japan? " #Tokyo
###########################################################
# Frankrijk Vragen:
# vraag1_Frankrijk = "Wanneer heeft Frankrijk de World Cup gewonnen? " #2018
# vraag2_Frankrijk = "Wat is het meest gegeten brood in Frankrijk? " #Stokbrood
# vraag3_Frankrijk = "In welke stad ligt de Eiffeltoren? " #Parijs
###########################################################
# brazilie Vragen:
# vraag1_Brazilie = "In welke stad ligt het Cristo Redentor? " #Rio de Janeiro
# vraag2_brazilie = "Hoeveel sterren heeft de braziliaanse vlag? " #Cristo Redentor
# vraag3_brazilie = "Wanneer heeft brazilie voor het laast een world cup gewonnen? " #2002
###########################################################
# Zuid-Afrika Vragen:
# vraag1_Afrika = "Heeft Zuid Afrika veel natuur? " #ja
# vraag2_Afrika = "Wat is 1 van de populairste dieren in Zuid Afrika? " #Leeuw
# vraag3_Afrika = "Heeft Zuid Afrika tap water? " #ja

klaar_voor = input("Ben je klaar om jouw ideale vakantie bestemming te vinden? ")
if klaar_voor == ("ja"):
    print ("succes! ")
else:
    print ("Ga je dan maar eens goed voorbereiden! ")
    exit()

keuze_landen = input("""Welke bestemming denk je dat geschikt is voor jouw? Kies uit:
Dubai
Ierland
Amerika
Japan
Frankrijk
Brazilie
Zuid Afrika 
""")
if keuze_landen == "Dubai":
    print ("maak je klaar voor de opkomende vragen over Dubai. ")
    vraag1_Dubai = input("Welke taal spreken ze in Dubai? ")
    if vraag1_Dubai == "engels":
        vraag2_Dubai = input("Denk je dat het leven in Dubai duur is? ")
        score += 1
    else:
        print (f"je bent helaas net niet geschikt om naar deze bestemming te reizen, kies een andere bestemming! je hebt {score} uit de 3 goed. ")
        exit()
        
    if vraag2_Dubai == "nee":
        vraag3_Dubai = input("Welke kleur is het water Dubai? ")
        score += 1
    else:
        print (f"je bent helaas net niet geschikt om naar deze bestemming te reizen, kies een andere bestemming! je hebt {score} uit de 3 goed. ")
        exit()

    if vraag3_Dubai == "blauw":
        print("Je hebt alle vragen goed! Gefeliciteerd en veel plezier in Dubai! ")
        score += 1
    else:
        print (f"je bent helaas net niet geschikt om naar deze bestemming te reizen, kies een andere bestemming! je hebt {score} uit de 3 goed.")
        exit()

if keuze_landen == "Ierland":
    print ("maak je klaar voor de opkomende vragen over Ierland. ")
    vraag1_Ierland = input("Welk dier loopt niet in het wild in Ierland? ")
    if vraag1_Ierland == "slangen":
        vraag2_Ierland = input("Wat is de hoofdstad van Ierland? ")
        score += 1
    else:
        print (f"je bent helaas net niet geschikt om naar deze bestemming te reizen, kies een andere bestemming! je hebt {score} uit de 3 goed. ")
        exit()

    if vraag2_Ierland == "dublin":
        vraag3_Ierland = input("Sinds wanneer is Ierland lid van de Europese Unie? ")
        score += 1
    else:
        print (f"je bent helaas net niet geschikt om naar deze bestemming te reizen, kies een andere bestemming! je hebt {score} uit de 3 goed. ")
        exit()

    if vraag3_Ierland == "1973":
         print("Je hebt alle vragen goed! Gefeliciteerd en veel plezier in Ierland! ")
         score += 1
    else:
        print (f"je bent helaas net niet geschikt om naar deze bestemming te reizen, kies een andere bestemming! je hebt {score} uit de 3 goed. ")
        exit()

if keuze_landen == "Amerika":
    print ("maak je klaar voor de opkomende vragen over Amerika. ")
    vraag1_Amerika = input("Wat is de meest bekende supermarkt in Amerika? ")
    if vraag1_Amerika == "walmart":
        vraag2_amerika = input("Wat is de andere naam voor Amerika? ")
        score += 1
    else:
        print (f"je bent helaas net niet geschikt om naar deze bestemming te reizen, kies een andere bestemming! je hebt {score} uit de 3 goed. ")
        exit()

    if vraag2_amerika == "verenigde staten":
        vraag3_amerika = input("Wie is de president van Amerika? ")
        score += 1
    else:
        print (f"je bent helaas net niet geschikt om naar deze bestemming te reizen, kies een andere bestemming! je hebt {score} uit de 3 goed. ")
        exit()

    if vraag3_amerika == "joe biden":
         print("Je hebt alle vragen goed! Gefeliciteerd en veel plezier in Amerika! ")
         score += 1
    else:
        print (f"je bent helaas net niet geschikt om naar deze bestemming te reizen, kies een andere bestemming! je hebt {score} uit de 3 goed. ")
        exit()

if keuze_landen == "Japan":
    print ("maak je klaar voor de opkomende vragen over Japan. ")
    vraag1_Japan = input("Welke taal spreken ze in Japan? ")
    if vraag1_Japan == "japanese":
        vraag2_Japan = input("Hoe heten stripboeken in het Japans? ")
        score += 1
    else:
        print (f"je bent helaas net niet geschikt om naar deze bestemming te reizen, kies een andere bestemming! je hebt {score} uit de 3 goed. ")
        exit()

    if vraag2_Japan == "manga":
        vraag3_japan = input("Wat is de hoofdstad van Japan? ")
        score += 1
    else:
        print (f"je bent helaas net niet geschikt om naar deze bestemming te reizen, kies een andere bestemming! je hebt {score} uit de 3 goed. ")
        exit()

    if vraag3_japan == "tokyo":
         print("Je hebt alle vragen goed! Gefeliciteerd en veel plezier in Japan! ")
         score += 1
    else:
        print (f"je bent helaas net niet geschikt om naar deze bestemming te reizen, kies een andere bestemming! je hebt {score} uit de 3 goed. ")
        exit()

if keuze_landen == "Frankrijk":
    print ("maak je klaar voor de opkomende vragen over Frankrijk. ")
    vraag1_Frankrijk = input("Wanneer heeft Frankrijk de World Cup gewonnen? ")
    if vraag1_Frankrijk == "2018":
        vraag2_Frankrijk = input("Wat is het meest gegeten brood in Frankrijk? ")
        score += 1
    else:
        print (f"je bent helaas net niet geschikt om naar deze bestemming te reizen, kies een andere bestemming! je hebt {score} uit de 3 goed. ")
        exit()

    if vraag2_Frankrijk == "stokbrood":
        vraag3_Frankrijk = input("In welke stad ligt de Eiffeltoren? ")
        score += 1
    else:
        print (f"je bent helaas net niet geschikt om naar deze bestemming te reizen, kies een andere bestemming! je hebt {score} uit de 3 goed. ")
        exit()

    if vraag3_Frankrijk == "parijs":
         print("Je hebt alle vragen goed! Gefeliciteerd en veel plezier in Frankrijk! ")
         score += 1
    else:
        print (f"je bent helaas net niet geschikt om naar deze bestemming te reizen, kies een andere bestemming! je hebt {score} uit de 3 goed. ")
        exit()
    
if keuze_landen == "Brazilie":
    print ("maak je klaar voor de opkomende vragen over brazillie. ")
    vraag1_Brazilie = input("In welke stad ligt het Cristo Redentor? ")
    if vraag1_Brazilie == "rio de janeiro":
        vraag2_brazilie = input("Hoeveel sterren heeft de braziliaanse vlag? ")
        score += 1
    else:
        print (f"je bent helaas net niet geschikt om naar deze bestemming te reizen, kies een andere bestemming! je hebt {score} uit de 3 goed. ")
        exit()

    if vraag2_brazilie == "27":
        vraag3_brazilie = input("Wanneer heeft brazilie voor het laast een world cup gewonnen? ")
        score += 1
    else:
        print (f"je bent helaas net niet geschikt om naar deze bestemming te reizen, kies een andere bestemming! je hebt {score} uit de 3 goed. ")
        exit()

    if vraag3_brazilie == "2002":
         print("Je hebt alle vragen goed! Gefeliciteerd en veel plezier in Brazilie! ")
         score += 1
    else:
        print (f"je bent helaas net niet geschikt om naar deze bestemming te reizen, kies een andere bestemming! je hebt {score} uit de 3 goed. ")
        exit()

if keuze_landen == "Zuid Afrika":
    print ("maak je klaar voor de opkomende vragen over Zuid Afrika. ")
    vraag1_Afrika = input("Heeft Zuid Afrika veel natuur? ")
    if vraag1_Afrika == "ja":
        vraag2_Afrika = input("Wat is 1 van de populairste dieren in Zuid Afrika? ")
        score += 1
    else:
        print (f"je bent helaas net niet geschikt om naar deze bestemming te reizen, kies een andere bestemming! je hebt {score} uit de 3 goed. ")
        exit()

    if vraag2_Afrika == "leeuw":
        vraag3_Afrika = input("Heeft Zuid Afrika tap water? ")
        score += 1
    else:
        print (f"je bent helaas net niet geschikt om naar deze bestemming te reizen, kies een andere bestemming! je hebt {score} uit de 3 goed. ")
        exit()

    if vraag3_Afrika == "ja":
         print("Je hebt alle vragen goed! Gefeliciteerd en veel plezier in Zuid-Afrika! ")
         score += 1
    else:
        print (f"je bent helaas net niet geschikt om naar deze bestemming te reizen, kies een andere bestemming! je hebt {score} uit de 3 goed.")
        exit()

if score >2:    
    print (f"Jou score op de quiz is fantastisch, je hebt {score} uit de 3 vragen goed! ")
else:
    print ("")
