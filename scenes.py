import character
import action
import global_
import datetime as dt
import yaml
from yaml.loader import BaseLoader

class Scene(object):
    # add more status effects as necesary.
    def __init__(self):
        self.freezing = None
        self.burning = None
        self.toxic = None
        self.container = []

    def enter(self):
        pass

    def forward_time(hours, minutes, seconds):
        time_to_add = dt.timedelta(hours = hours, minutes = minutes,
                                    seconds = seconds)

        global_.world_time = global_.world_time + time_to_add

class Introduction(Scene):
    def __init__(self):
        self.room_name = 'introduction'

    def enter(self):
        print(global_.narrator['scenes']['rooms'][self.room_name]['s1'])
        return 'cell'

class Cell(Scene):
    def __init__(self):
        self.room_name = 'cell'

    def enter(self):
        print(global_.narrator['scenes']['rooms'][self.room_name]['s1'])

        Scene.forward_time(2, 30, 0)

        print("Left or Right?")
        print("1. Left")
        print("2. Right")

        player_input = input('> ')

        if player_input == '1':
            return 'escape'
        else:
            return Fight.set_up(self, 's1', 'Gru', 50, 'd2', 'v1')


class Escape(Scene):
    def __init__(self):
        self.room_name = 'escape'

    def enter(self):
        print(global_.narrator['scenes']['rooms'][self.room_name]['s1'])
        exit(1)

class Death(Scene):
    def __init__(self):
        self.room_name = 'death'

    def enter(self):
        print(global_.narrator['scenes']['rooms'][self.room_name]['d1'])
        exit(1)

class Fight(Scene):
    def __init__(self):
        pass

    def set_up(self, scene, enemy, hp, defeat, victory):
        self.fight_scene = scene
        self.defeat_scene = defeat
        self.victory_scene = victory

        print(global_.narrator['scenes']['rooms']['fight'][self.fight_scene])

        Scene.forward_time(10, 0, 0)

        enemy = character.Character(enemy, hp)

        action.Combat.attack_flee(self, enemy)

        if global_.player.get_hp() <= 0:
            print(global_.narrator['scenes']['rooms']['death'][self.defeat_scene])
            return 'death'

        if enemy.get_hp() <= 0:
            print(global_.narrator['scenes']['rooms']['fight'][self.victory_scene])
            return 'escape'
