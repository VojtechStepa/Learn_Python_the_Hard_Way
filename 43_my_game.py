from sys import exit
from textwrap3 import dedent
from random import randint


class Scene(object):
    
    def enter(self):
        pass


class Engine(object):

    def __init__(self, start_navigation):
        self.start_place = start_navigation

    def play(self, list):
        self.name = list[0]
        self.lifes = list[1]
        self.skill = list[2]
        print(dedent(f"""
            Hi {self.name}. Nice to meet you! 
            Your condition has default value {self.lifes} and your skill {self.skill}.
            But I have bad news for you. You are in {self.start_place}.
            Did you really thing that the king allowed you to get away with princess?
        """))

        actual_scene = self.start_place.go_in()
        last_scene = self.start_place.next_scene('win')

        while actual_scene != last_scene:
            next_scene_name = actual_scene.enter()
            actual_scene = self.start_place.next_scene(next_scene_name)

        actual_scene.enter()



class Enemy(object):

    custom_enemies = {  'skeleton' :4}

    rare_enemies = []

    def __init__(self, actual_place):
        pass

    def fight(self, opposing_guy):
        pass


class Player(object):

    def __init__(self, name):
        self.name = name

    def attributes(self):
        hp = randint(0, 6) + randint(0, 6) + 12
        skill = randint(0, 6) + 6
        print(hp, skill)
        return [self.name, hp, skill]


class Jail(Scene):

    def enter(self):
        print("Hola")
        return 'win'

class Pursuit(Scene):

    def enter(Scene):
        pass

class Right_key(Scene):
     
     def enter(self):
         pass

class Fake_key(Scene):

    def enter(self):
        pass

class Pub(Scene):

    def enter(self):
        pass

class Hospital(Scene):
     
     def enter(self):
         pass

class Mountain(Scene):
     
     def enter(self):
         pass

class Tunnel(Scene):
    
    def enter(self):
        pass

class Finnal_battle(Scene):

    def enter(self):
        pass

class Ordinary_place(Scene):

    def __init__(self):
        pass

    def enter(self):
        pass

class Death(Scene):
     
     def enter(self, reason):
         pass

class Win(Scene):
    
    def enter(self):
        print("You won")


class Navigation(object):

    rooms = {   
            'jail'      : Jail(),
            'pursuit'   : Pursuit(),
            'right_key' : Right_key(),
            'fake_key'  : Fake_key(),
            'pub'       : Pub(),
            'hospital'  : Hospital(),
            'mountain'  : Mountain(),
            'tunnel'    : Tunnel(),
            'last'      : Finnal_battle(),
            'win'       : Win(),
            'death'     : Death(),
    }

    def __init__(self, start_place):
        self.start_place = start_place

    def next_scene(self, start_place):
        val = Navigation.rooms.get(start_place)
        return val
        

    def go_in(self):
        return self.next_scene(self.start_place)


a_start = Navigation('jail')
a_character = Player(input("Welcome adventurer in my game. What's your name?\n> "))
a_game = Engine(a_start)
a_game.play(a_character.attributes())







    