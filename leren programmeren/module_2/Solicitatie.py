snor = 0
haar = 0

diploma = input("Ben je in bezit van een ondernemen MBO 4 diploma? ")
rijbewijs = input("Ben je in bezit van een geldig vrachtwagen rijbewijs? ")
hoed = input("Ben je in bezit van een hoge hoed? ")
manvrouw = input("Bent u een man of een vrouw m/v? ")
if manvrouw == "m":
    snor = int(input("Hoe lang is uw snor? "))
if manvrouw == "v":
    haar = int(input("hoe lang is uw haar? "))
lengte = input("hoe lang bent u? in cm ")

if lengte == "ik ben kleiner dan 150":
    raise NameError("je bent bijzonder klein! ")

gewicht = input("hoe zwaar bent u? in kilo's ")

if gewicht == "91 kg":
    raise  NameError("u bent zo licht als een veertje! ")

certificaat = input("heeft u een certificaat van Overleven met gevaarlijk personeel? ")

if certificaat == "nee":
    raise NameError("Ga je certificaat halen knoepel")

ervaring_1 = int(input("hoeveel jaar ervaring heeft u met dieren-dressuur? "))
ervaring_2 = int(input("hoeveel jaar ervaring heeft u met jongleren? "))
ervaring_3 = int(input("hoeveel jaar heeft u ervaring met acrobatiek? "))


if diploma == ("ja") and rijbewijs == ("ja") and hoed == ("ja") and (manvrouw == "man" and snor >10) or (manvrouw == "vrouw" and haar >20) and lengte >150 and lengte <220 and gewicht >90 and gewicht <120 and certificaat == ("ja") and (ervaring_1 >4 or ervaring_2 >5 or ervaring_3 >3):
    print("gefeliciteerd, u heeft uw solicitatie fantastisch afgeleverd! ")
else: 
    print("u heeft uw solicitatie helaas niet goed genoeg ingevuld om aangenomen te worden. ")
