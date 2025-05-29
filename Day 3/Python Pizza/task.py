print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
S = 15
M = 20
L = 25

if size == "S":
    if pepperoni == "Y":
        if extra_cheese == "Y":
            print(f"Your final bill is: ${S + 2 + 1}")
        else:
            print(f"Your final bill is: ${S + 2}")
    else:
        print(f"Your final bill is: ${S}" )

elif size == "M":
    if pepperoni == "Y":
        if extra_cheese == "Y":
            print(f"Your final bill is: ${M + 3 + 1}")
        else:
            print(f"Your final bill is: ${M + 3}")
    else:
        print(f"Your final bill is: ${M}")

elif size == "L":
    if pepperoni == "Y":
        if extra_cheese == "Y":
            print(f"Your final bill is: ${L + 3 + 1}")
        else:
            print(f"Your final bill is: ${L + 3}")
    else:
        print(f"Your final bill is: ${L}")
