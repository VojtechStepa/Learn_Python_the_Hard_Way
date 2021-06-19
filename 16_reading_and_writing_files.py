from sys import argv

script, filename = argv

print(f"We're going to erase {filename}.")
print("If you don't want to do that, hit CTRL-C (^C)")
print("If you want that, hit return.")

input("?")

print("Opening the file...")
target = open(filename, 'w')

print("Truncking the file. Goodbye!")
target.truncate()

print("Now I'm going to ask you for three lines")

line1 = input("Line 1: ")
line2 = input("Line 2: ")
line3 = input("Line 3: ")

print("I'm going to write these to the file.")

target.write(f'{line1}\n{line2}\n{line3} \n')

print("And finally, we close it")
target.close()

# More on page 52

# This is stuff that I typed into a file.
# It is a really cool stuff.
# Lots and lots of fun to have in here.

