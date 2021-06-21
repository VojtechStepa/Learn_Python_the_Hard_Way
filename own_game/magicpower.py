from random import randint
from sys import exit

class Magic(object):

    def __init__(self, mana):
        self.mana = mana

    def heal(self):
        self.mana -= 15
        self.check()
        print("Nice, you're out and about")
        return 100

    def shot_fire(self):
        self.mana -= 25
        self.check()
        print("Wow, you shot a huge fire ball.")
        return True

    def invisible(self):
        self.mana -= 20
        self.check()
        print("Now you're invisible.")
        return True

    def unlock(self):
        self.mana -= 10
        self.check()
        print("The door is opened now")
        return True

    def do_a_spell(self):
        print(dedent(""""
            You're very brave (or dumb) if you mess with 
            magic without propert knowledges.
        """))
        # It's possible to mess with magic and make it 
        self.lucky = random(0, 9-(self.mana // 5))
        if self.lucky > 0:
            print(dedent("""
                You've been trying something very sophisticated, 
                however you overrated your skills.You're dead.
                But don't worry, you've been remembered as the 
                biggest fireworks for ages. By corpse.
            """))
            exit(1)
        elif self.lucky == 0:
            print("Lucky man, mess with magic is often risky, but you made it.")
            print("On downside you haven't been acheiving your goal.")
            print("And you feel very tired")

    def increase_mana(self, recovered):
        self.mana += recovered

    def check(self):
        if self.mana > 0:
            print("You're heart is beating fast. You feel the magic.")
        else:
            print("Mess with magic is dangerous fun.")
            print("Even if you know the right words.")
            print("Some times you just isn't enough strong")
            print("But it was a nice firework")
            print("By the way, you're dead.")
            exit(1)