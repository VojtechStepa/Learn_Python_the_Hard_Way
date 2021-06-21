from sys import exit
from os import remove, system

from textwrap3 import dedent

import battlesystem as bs
import gamesave as gs
import magicpower as mp

# load the game dats first
a_save = gs.GameSaver()
save_dat = a_save.load('save1.txt', 'Prolog', 100, 15, 30).split('\n')
print(save_dat)

class Scene(object):

    live = float(save_dat[1])
    damage = float(save_dat[2])
    mana = float(save_dat[3])

class Prolog(Scene):

    def enter(self):
        print(dedent("""
            Your dad, king Char V, passed away and you like
            first-born boy should become a new king. But
            your arrogant brother didn't allow this. He
            decided to try a takeover. And unfortunately
            he succeeded.\n
            He sent you out of the capital city to castle 
            belonged one of his loylest friend Kalmak. This 
            castle is located near the north border of the
            kindom, almost in wilderness.\n
            You are now sitting on the jail floor. You haven't
            got any idea what plans your brother has with you.
            But probalby nothing kind.It's time to take things
            on your hands and shows everyone, who is the real 
            king. Otherwise the jail is spectacular place to
            spend rest of your live, isn't it?
        """))
        return 'Tutorial'

class Tutorial(Scene):

    def enter(self):
        print(dedent("""
            In your cell is quite dark, so you can meke out
            only the nearest surroudings. What do you want to do?
            Explore the cell (type E)
            Sit quietly, may you hear something (type S) 
        """))
        answer = input(">")
        while not(answer == 'E' or answer == 'e' or answer == 'S' or answer == 's'):
            answer = input("That wasn't right, type S or E.\n>")
        system('cls')

        if (answer == 'E') or (answer == 'e'):
            print(dedent("""
                You stand up and go belong wall. You're
                disappointed, cuz your cell is small (2 to 3m)
                and without excetpion of metal door, you
                didn't found nothing interesting.
                Would you like to 
                just sit, may you hear something (S)
                get a closer look on wall(W)
            """))
            answer = input(">")
            while not(answer == 'W' or answer == 'w' or answer == 'S' or answer == 's'):
                answer = input("That wasn't right, type S or W.\n>")
            system('cls')

        if (answer == 'W') or (answer == 'w'):
            print(dedent("""
                You're preciously searching for something
                usefull, but you're now touching the door
                and you haven't found anything.
                Would you like to 
                just sit, because it's hopeless (S)
                continue to search for something interesting (I)
            """))
            answer = input(">")
            while not(answer == 'I' or answer == 'i' or answer == 'S' or answer == 's'):
                answer = input("That wasn't right, type S or I.\n>")
            system('cls')
        
            if (answer == 'I' or answer == "i"):
                print(dedent("""
                    Unfortunatlly you have been finding nothing.
                    You feel hopeless, so yo just sit down. 
                """))
                answer = 'S'
            elif (answer == 'S') or (answer == 's'):
                print(dedent("""
                    You gave up finding and you go back
                    to you original sitting place. When you
                    was in middle of room, you steped on something
                    sharp. You took it and discoverd that it is a
                    fork.
                    Stupid fork! That's like an awful joke. Your're
                    very depressed. If you weren't so stupid, you would 
                    becomea king. Instead you're sitting in Jail. This 
                    live is miserable and you haven't gog any chance to
                    make it better. You can do only one thing - suicide.

                    Are you enought strong to get your feelings under
                    control? Well we'll see.
                    Remember about your first real fight as a child. 
                    It was akward. May this was the moment, when a lot 
                    of people've began thing that you wouldn't be 
                    a good king.
                    Did you deal with this?

                    It's time for your first combat. If you want to prove,
                    that you are enough strong, you must win. Press enter and
                    click with left button on your mouse as fast as you can.
                    Cuz now is going about your life.
                """))
                Scene.live -= 5     # Injury caused by fork
                Scene.live = a_fight.match('common', self.live, self.damage)
                if self.live < 1:
                    return 'Death'
                print(dedent("""
                    Congratulation! Yours feeling are under control. And on time,
                    because you hear clumsy steps. Moment later the door was 
                    opened and a guard entry. You don't wait and sting the guard
                    with fork. He quietly pass away, of course with your little
                    help.
                """))
                answer =  None

        if (answer == 'S') or (answer == 's'):
            print(dedent("""
                The prison is completly quiet, only
                falling water dips disturb the silence.
                You're bored and slowly falling asleep...

                You dream about your chilhood, about dad
                and mum, your horse Tim. However the 
                dream is immediatelly turn into nightmare.

                It's time for your first combat. If you want to prove,
                that you are enough strong, you must win. Press enter and
                click with left button on your mouse as fast as you can.
                Cuz now is going about your life.
            """))
            Scene.live = a_fight.match('common', self.live, self.damage)
            if self.live < 1:
                return 'Death'
            print("First enemy is down, but next dreadful enemy is approaching.")
            Scene.live = a_fight.match('rare', self.live, self.damage)
            if self.live < 1:
                return 'Death'
            print(dedent("""
                That was much more challenging. And  a new creatur is 
                comming.It look' like an agressive werewolf. But you're 
                prepared to cause fisrt hit. You jump and...

                And your wrist is touched something cold and hard. You 
                wake up, before a guard. Your real-looking dreams were
                been causing that you suprisingly attack on a guard,
                who thought that you sleep. And your attack again
                werewolf (in dream) charged him a sword.

                But his suprised is disseapered. You don't hesitate
                and jump on him.
            """))
            Scene.live = a_fight.match('guard', self.live, self.damage)
            if self.live < 1:
                return 'Death'
            print(dedent("""
                    Congratulation! Your are a combat monster. Or at least
                    you now know, how some combats look like. 
                    Guard quietly pass away, of course with your little
                    help.
                """))
            answer = None
        
        print(dedent("""
                    What would you like to do?
                    Sit down and try to face up to the reality (F)
                    Disappear from cell as fast as you can (D)
                    Take his sword (T)
                    Take his key and lock the jail (K)
                """))
        answer = input("> ")
        while not(
            answer == 'F' or answer == 'f' 
            or answer == 'D' or answer == 'd'
            or answer == 'T' or answer == 't'
            or answer == 'K' or answer == 'k'
            ):
            answer = input("That wasn't right, type F, D, T or K.\n>")
            system('cls')

        system('cls')
        if (answer == 'T') or (answer == 't'):
            print("You feel much more better with the sword in your hand.")
            Scene.damage += 10
            print(dedent("""
                What would you like to do?
                Sit down and try to face up to the reality (F)
                Disappear from cell as fast as you can (D)
                Take his key and lock the jail (K)
                """))
            answer = input("> ")
            while not(
                answer == 'F' or answer == 'f' 
                or answer == 'D' or answer == 'd'
                or answer == 'K' or answer == 'k'
                ):
                answer = input("That wasn't right, type F, D or K.\n>")
                system('cls')

        system('cls')
        if (answer == 'F') or (answer == 'f'):
            print(dedent("""
                You feel upset, because you take him whole life.
                You're not a God. You never be. Why is this
                word so spoiled? What I would do?

                Your thoughts interupt a scream:
                'Hey, our almost-king killed one of use.'
                'It's time to solve succession problem for ever.'

                You're upset. Why so much people hate you.
                I don'tvwant be a corpse. But four madden guards
                are to strong. You haven't got any chance.

                You yell somethikng and...miracle was happen.
                From you hands fly away a
            """))
            a_spell.shot_fire()
            print(dedent("""
                The guards can't make it. The heat was terrible.
                'I'm wizard'.
                You hear a lot of about magic. Mostly than is very
                rare and unbeliable powerful. But is very dangerous
                too. If wizard overrated his skill, he can easily
                destroy himself.
                And you feel very tired. It would be better to don't
                try it again. May you meet someone, who tell you more.
            """))
        elif (answer == 'd') or (answer == 'd'):
            print(dedent("""
                You hurry up to get away from this place.
                But on the next corner you met four guards,
                who's probably hear something. You kill the 
                firts one, but others are ready. Hopefully
                the corridor is there really thin. Only one 
                of the guards could fight with you at the same
                time. 
            """))
            for i in range(3):
                Scene.live = a_fight.match('guard', self.live, self.damage)
                if self.live < 1:
                    return 'Death'
            print(dedent("""
                You kill them all. And now you have a really good 
                reason to hurry up. You're running far away from
                this place.
            """))  
        else:
            # story to be an ultimate theef
            print(dedent("""
                You took the keys and find out if the guard
                has some other usefull things. Nothing.
                You hear steps three or might fourth guards.
                What would you like to do?
                Lock the cell from inside (I)
                Lock the cell from outside (U)
                Leave the cell and diseaper on other side of 
                cordor that the steps is approaching (L)
                Suprising attack (A)
            """))
            answer = input("> ")
            while not(answer == 'I' or answer == 'i' 
                      or answer == 'U' or answer == 'u'
                      or answer == 'L' or answer == 'l'
                      or answer == 'A' or answer == 'a'
                ):
                answer = input("That wasn't right, type U, L, I or A.\n>")
                system('cls')
            system('cls')
            if (answer == 'I') or (answer == 'i'):
                print(dedent("""
                    You hurry up and lock the door from inside.
                    You are waiting next to the door prepared to
                    kill everyone, who'll come on.

                    But the guards now, how important prisoner they
                    have to keep an eye. So they first want to take look
                    on you cell. The door was opened and you kill first
                    guard with appreciate hit. When the others guards saw
                    your madness, they close the door and call it for more 
                    tropse.

                    You can't get out of this. It's hopeless. But you want
                    take with you as mamy mans as you can.
                """))
                for i in range(20):
                    Scene.live = a_fight.match(f'guard ({i+1})', self.live, self.damage)
                    if self.live < 1:
                        return 'Death'
                print(dedent("""
                    You're a real monster. You kill twenty guards.
                    Their blood is everywhere, on walls, on your
                    hands, in your eyes.
                    Now is no-one who try to stop you. But you
                    don't think that this was all guards of this
                    castle. Never mind.
                """))
            elif (answer == 'U') or (answer == 'u'):
                print(dedent("""
                    You locked the cell from outside. Than you
                    jumped to doors opposite the first one, opened
                    them and as quit as you could you close them. Moment
                    later the guards opened your original cell. When they
                    notice, that you aren't there they run out to catch you.
                    You wait a moment and than go out of the cell.
                """))
            elif (answer == 'L') or (answer == 'l'):
                print(dedent("""
                    You hurry up to get on the arch of the corridor on
                    time. You mist sometking because there are guards too.
                    You haven't got any chance with eight guards on such 
                    broad corridor. They kill you.
                """))
                return 'Death'
            else:
                print(dedent("""
                    Are you really thing that you can surprised professionals
                    guards, even if they got alert?
                """))
        print("Your jorney to freedom is started.")
        return 'Jail'

class Jail(Scene):

    def enter(self):
        return 'Castle'

class Castle(Scene):
    
    def enter(self):
        return 'Garden'

class Garden(Scene):

    def enter(self):
        return 'Bush'

class Bush(Scene):

    def enter(self):
        return 'LoyalArmy'

class LoyalArmy(Scene):

    def enter(self):
        return 'Battle'

class Battle(Scene):
     
     def enter(self):
        return 'TwinsDuel'

class  TwinsDuel(Scene):

    def enter(self):
        return 'Win'

class Win(Scene):

    def enter(self):
        print("You win!")
        remove("save1.txt")
        exit(1)

class Death(Scene):

    def enter(self):
        print("Thas's a shame.")
        print("Bye corpse!")
        exit(1)


class Engine(object):

    scenes = {  
        'Prolog'    : Prolog(),
        'Tutorial'  : Tutorial(),
        'Jail'      : Jail(),
        'Castle'    : Castle(),
        'Garden'    : Garden(),
        'Bush'      : Bush(),
        'LoyalArmy' : LoyalArmy(),
        'Battle'    : Battle(),
        'TwinsDuel' : TwinsDuel(),
        'Win'       : Win(),
        'Death'     : Death(),      
        }

    def __init__(self, first_scene):
        self.starting_scene = first_scene

    def play(self):
        current_scene = self.opening_scene(self.starting_scene)
        final_scene = Win()

        while current_scene != final_scene:
            next_scene = current_scene.enter()
            current_scene = self.opening_scene(next_scene)

        current_scene.enter()

    def next_scene(self, scene_name):
        pass

    def opening_scene(self, scene_name):
        #a_save.save('save1.txt', scene_name, str(Scene.live), str(Scene.damage), str(a_spell.mana))
        place = Engine.scenes.get(scene_name)
        a_spell.increase_mana(5)
        return place

a_game = Engine(save_dat[0])
a_spell = mp.Magic(float(save_dat[3]))
a_fight = bs.Fight()
a_game.play()