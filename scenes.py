import narration
import character
import combat
import global_

class Scene(object):
    # will do stuff later, pass for now
    def enter(self):
        pass

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

        gru = character.Character('Gru', 50)
        combat.Combat.combat(self, gru)

        if global_.player.get_hp() <= 0:
            return 'death'

        if gru.get_hp() <= 0:
            return 'escape'
