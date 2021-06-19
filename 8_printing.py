formater = "{} {} {} {}"  # varieble with wait to fill with else 4 variebles
print(formater.format(1, 2, 3, 4)) 
print(formater.format("one", "two", "three", "four")) # I use funciton format to add on the varieble formater something - number, text, Booledom or more complex text
print(formater.format(True, False, False, True))
print(formater.format(formater, formater, formater, formater))
print(formater.format(
    "Try your",
    "own text here",
    "Maybe a poeam",
    "Or a song about fear"
))