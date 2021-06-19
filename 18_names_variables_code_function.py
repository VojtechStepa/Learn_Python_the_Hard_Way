def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}\narg2: {arg2}")

def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}\narg2: {arg2}")

def print_one(arg1):
    print(f"arg1: {arg1}")

def print_none():
    print("I got nothin'.")

print_two("Yed", "May")
print_two_again("Ahi","Kub")
print_one("Hola")
print_none()