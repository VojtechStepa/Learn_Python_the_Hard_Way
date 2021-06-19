print("""You enter a dark room with two doors.
Do you go through door #1 or door #2?""")

door = input("> ")

if door == "1":
    print("There is a giant bear here eating  a cheese cake.")
    print("What do you do?")
    print("1. take the cake")
    print("2. scream at the bear")

    bear = input("> ")

    if bear == "1":
        print("The bear eats you face off. Good job!")
    elif bear == "2":
        print("The bear eats your leg off. Good job!")
    else:
        print(f"Well, doing {bear} is probably better.")
        print("Bear runs away.")

elif door == "2":
    print("You stare into endless abyss at Chutlun's retina")
    print("1. Blueberries.")
    print("2. yellow jacket clothespins")
    print("3. Understanding revolvers yelling melodies.")

    insanity = input("> ")

    if insanity == "1":
        print("Your body survives powered by mind of jello.")
        print("Good job!")
    else:
        print("The insanity rots your eyes into a pool of muck.")
        print("Good job!")

else:
    print("You stumble around and fall a knife and die. Good job!")