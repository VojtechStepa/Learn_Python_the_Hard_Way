import os
import time
from tkinter import *
from sys import exit
from random import randint

class Fight(object):

    enemy_type = ['common', 'rare', 'strong', 'boss']

    common_enemy = [
        'dwarf', 'goblin', 'wolf', 'orc', 'eagle',
        'drunk', 'warrior', 'zombie', 'dog', 'puma',
        'spiders', 'centipedes', 'wizard\'s disciple',
        'fairy', 'carnivel plant', 'falcon', 'own',
        'snake', 'serpant', 'rats', 'thief',
    ]

    rare_enemy = [
        'giant', 'ghost', 'mummy', 'tiger', 'lion',
        'lioness', 'cubs...and lioness', 'warrior on horse',
        'cheetah', 'jaguar', 'cobra',
        ]

    strong_enemy = [
        'werewolf', 'elite dwarf warrior', 'vampire',
        'dragonling', 'warlock', 'murder',
    ]

    boss_enemy = [
        'lead wizard', 'brother\'s best assasin',
        'dragon',
    ]

    adjective_enemy = [
        'cross', 'furious', 'mean', 'bad-tempered',
        'shocked', 'proud', 'starving', 'slim',
        'bad-looking',
    ]

    def __init__(self):
        self.c_en = len(self.common_enemy)
        self.r_en = len(self.rare_enemy)
        self.s_en = len(self.strong_enemy)
        self.b_en = len(self.boss_enemy)
        self.a_en = len(self.adjective_enemy)

    def left_down(self, event):
        os.system('cls')
        self.click += 1
        self.end = time.time()
        # self.end is time of last click
        # self.start is time when was thinker window made
        if self.end - self.start > self.time:
            self.root.destroy()
    
    def choose_enemy(self):
        """
        Choose random enemy from prepared lists, if list exist.
        If not create enemy of this name, if string. In both cases
        enemy has got random HP.
        """
        self.adj = randint(0, self.a_en - 1)

        if self.enemy == 'random':
            a = randint(0,2)
            self.enemy = self.enemy_type[a]

        if self.enemy == 'common':
            self.monster = randint(0, self.c_en - 1)
            self.min_click = randint(20, 55)
            self.time = 10
            self.enemy_HP = randint(10, 30)
            print(f"You spot a {self.adjective_enemy[self.adj]}", end="")
            print(f" {self.common_enemy[self.monster]}.")
            print("It look's like an invintation to fight.")

        elif self.enemy == 'rare':
            self.monster = randint(0, self.r_en - 1)
            self.min_click = randint(60, 80)
            self.time = 15
            self.enemy_HP = randint(35, 65)
            print(f"You spot a {self.adjective_enemy[self.adj]}", end="")
            print(f"{self.rare_enemy[self.monster]}.")
            print("It look's like an invintation to fight.")

        elif self.enemy == 'strong':
            self.monster = randint(0, self.s_en - 1)
            self.min_click = randint(85, 105)
            self.time = 20
            self.enemy_HP = randint(70, 110)
            print(f"You spot a {self.adjective_enemy[self.adj]}", end="")
            print(f"{self.strong_enemy[self.monster]}.")
            print("It look's like an invintation to fight.")

        elif self.enemy == 'boss':
            self.monster = randint(0, self.b_en - 1)
            self.min_click = randint(90, 130)
            self.time = 20
            self.enemy_HP = randint(120, 180)
            print(f"You spot a {self.adjective_enemy[self.adj]}", end="")
            print(f"{self.boss_enemy[self.monster]}.")
            print("It look's like an invintation to fight.")

        # Sometimes is usefull to create enemy of specific name
        elif type(self.enemy) == str:
            self.monster = self.enemy
            self.min_click = randint(40, 65)
            self.time = 15
            print(f"You spot a {self.adjective_enemy[self.adj]} {self.monster}.")
            print("It look's like an invintation to fight.")
            self.enemy_HP = randint(30, 45)

        else:
            print("Something wrong with enemy type")
            print("Fatal mistake")
            exit(1)

    def clicking(self):
        # Make window, where I could count clicks
        self.root = Tk()
        self.root.title('Click Here')
        self.root.minsize(
            height=self.root.winfo_screenheight(),
            width=self.root.winfo_screenwidth(),
        )
        self.start = time.time()
        self.root.bind('<Button-1>', self.left_down)
        self.click = 0
        self.root.mainloop()
        
    def match(self, type_enemy, HP, player_damage):
        self.enemy = type_enemy
        self.HP = HP
        self.attack = player_damage
        self.choose_enemy()
        input("Ready?")
        
        while self.HP > 0:
            self.clicking()

            if self.click > self.min_click:
                self.enemy_HP -= self.attack
                print("Nice hit, that's must be a bad injury.")
            elif self.click == self.min_click:
                # Higher time value is for stronger enemy, which are more dangerous
                self.HP -= randint(10, 30) * self.time / 10
                self.enemy_HP -= self.attack
                print("Nice hit, that's must be a bad injury.")
                print("Unfortunately you was hitted to.")
                print("Your HP", self.HP)
            else:
                self.HP -= randint(10, 30) * self.time / 10
                print("You are so clunch.")
                print("And too slow, your opponent hit you.")
                print("Your HP", self.HP)

            if (self.HP < 1) or (self.enemy_HP < 1): 
                return self.HP
            
            input("Ready for next round?")