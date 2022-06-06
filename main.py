import json
import narration

class Character(object):

    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def add_hp(self, change_in_hp):
        self.hp = self.hp + change_in_hp

    def reduce_hp(self, change_in_hp):
        self.hp = self.hp - change_in_hp

    def set_hp(self, hp):
        self.hp = hp

    def get_hp(self):
        return self.hp


class Scene(object):
    # will do stuff later, pass for now
    def enter(self):
        pass

class Engine(object):
    # stores scene_map(a map object) in self.scene_map
    def __init__(self, scene_map):
        self.scene_map = scene_map

    # stores the return value from the opening_scene method from the
    # scene_map(a map object) in current_scene
    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('escape')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        # enters the current scene from the scene map object
        current_scene.enter()

class Introduction(Scene):
    def __init__(self):
        self.room_name = 'introduction'

    def enter(self):
        print(narration.scenes['rooms'][self.room_name]['s1'])
        return 'cell'

# each of the 'rooms' will most likely have to be their own file for organization
class Cell(Scene):
    def __init__(self):
        self.room_name = 'cell'

    def enter(self):
        print(narration.scenes['rooms'][self.room_name]['s1'])

        print("Left or Right?")
        print("1. Left")
        print("2. Right")

        player_input = input('> ')

        if player_input == '1':
            return 'escape'
        else:
            return 'fight'


class Escape(Scene):
    def __init__(self):
        self.room_name = 'escape'

    def enter(self):
        print(narration.scenes['rooms'][self.room_name]['s1'])
        exit(1)

class Death(Scene):
    def __init__(self):
        self.room_name = 'death'

    def enter(self):
        print(narration.scenes['rooms'][self.room_name]['s1'])
        exit(1)

class Fight(Scene):
    def __init__(self):
        self.room_name = 'fight'

    def enter(self):
        print(narration.scenes['rooms'][self.room_name]['s1'])

        gru = Character('Gru', 50)
        Combat.combat(self, gru)

        if player.get_hp() <= 0:
            return 'death'

        if gru.get_hp() <= 0:
            return 'escape'

class Combat(object):

    def combat(self, enemy):

        print("Attack or Flee?")
        print("1. Attack")
        print("2. Flee")

        while player.get_hp() > 0 and enemy.get_hp() > 0:

            player_input = input('> ')

            if player_input == '1':
                print(narration.scenes['rooms']['player']['a1'])
                enemy.reduce_hp(20)
            else:
                print(narration.scenes['rooms']['enemy']['a1'])
                player.reduce_hp(20)


class Map(object):
    # scenes avaliable on the map
    scenes = {
        'introduction': Introduction(),
        'cell': Cell(),
        'death': Death(),
        'escape': Escape(),
        'fight': Fight()
    }

    # stores the passed scene in start_scene
    def __init__(self, start_scene):
        self.start_scene = start_scene

    # returns the scene corresponding to the start_scene variable
    # via the get() function
    def next_scene(self, scene_name):
        scene = self.scenes.get(scene_name)
        return scene

    def opening_scene(self):
        return self.next_scene(self.start_scene)

player = Character('Strifer', 100)

# creates a_map, Passes the introduction variable to the created object
a_map = Map('introduction')
# creates a_game object, passes the a_map object to the Engine class
a_game = Engine(a_map)
a_game.play()
