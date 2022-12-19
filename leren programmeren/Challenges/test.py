mijn_namen_lijst = {}

# loop en een half
while True:
    naam = input("wat is je naam? ")
    if naam == "stop":
        break

    if naam in mijn_namen_lijst:
        if input("wilt u updaten? ja/nee ") != "ja":
            continue

leeftijd = int(input("wat is je leeftijd"))
mijn_namen_lijst[naam] = leeftijd
