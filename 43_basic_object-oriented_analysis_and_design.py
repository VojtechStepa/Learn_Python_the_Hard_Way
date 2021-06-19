from sys import exit
from random import randint
from textwrap3 import dedent


class Scene(object):

    def enter(self):
        print("This scene is not yet configured.")
        exit(1)


class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        current_scene.enter()

class Death(Scene):

    quips = [   "Your granny would be better",
                "You are so stupid"
                "I didn't think that someone could be so clumsy...But obviously is possible"
    ]

    def enter(self):
        print(Death.quips[randint(0, len(self.quips) - 1)])
        exit(1)

class CentralCoridor(Scene):

     def enter(self):
        print(dedent("""
            try
        """))
        return 'laser_weapony_armory'

class LaserWeaponyArmory(Scene):

     def enter(self):
       return 'the_Bridge'

class TheBridge(Scene):

     def enter(self):
        return 'escape_Pod'

class EscapePod(Scene):

     def enter(self):
        return "finished"

class Finished(Scene):

    def enter(self):
        print("You win!")
        return 'finished'

class Map(object):

    scenes = {  'central_corridor': CentralCoridor(), 
                'laser_weapony_armory': LaserWeaponyArmory(), 
                'the_Bridge': TheBridge(),
                'escape_Pod': EscapePod(), 
                'death': Death(),
                'finished': Finished(),
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)


a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()