a = int(input("A: "))
b = int(input("B: "))

if a > b:
    max = a
    min = b
    print("A is het grootste getal: " + str(max))
elif a < b:
    min = a
    max = b
    print("A is het kleinste getal: " + str(min))
else:
    min = a
    max = a
    print("A en B zijn even groot")

print("Het minimum is: " + str(min))
print("Het maximum is: " + str(max))
