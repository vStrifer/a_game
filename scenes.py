import narration
import character
import combat
import global_
import datetime as dt


# TODO: Pull out and put as its own 'thing' just as character?

class Scene(object):
    # add more status effects as necesary.
    def __init__(self):
        self.freezing = None
        self.burning = None
        self.toxic = None

    def enter(self):
        pass

    def forward_time(hours, minutes, seconds):
        time_to_add = dt.timedelta(hours = hours, minutes = minutes,
                                    seconds = seconds)
        global_.world_time = global_.world_time + time_to_add

        print(global_.world_time)


class Introduction(Scene):
    def __init__(self):
        self.room_name = 'introduction'

    def enter(self):
        self.freezing = True
        print(narration.scenes['rooms'][self.room_name]['s1'])
        print(f"The room is freezing?: {self.freezing}")
        return 'cell'

class Cell(Scene):
    def __init__(self):
        self.room_name = 'cell'

    def enter(self):
        print(narration.scenes['rooms'][self.room_name]['s1'])

        Scene.forward_time(2, 30, 0)

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

# TODO: Make more generic, or remove completely putting the print statement
# as part of the parent scene, then pass in enemy. Checks of player status
# should probably be an event (global based on time?)

class Fight(Scene):
    def __init__(self):
        self.room_name = 'fight'

    def enter(self):
        print(narration.scenes['rooms'][self.room_name]['s1'])

        Scene.forward_time(10, 0, 0)

        # container test
        print(f"You find a Knife!")
        global_.player.items.append("Knife")
        print(global_.player.items)

        gru = character.Character('Gru', 50)
        # TODO: Clean up this call?
        # Pass in victory condition text as part of the function call to make
        # it more generic. Text can be fetched from narration.
        combat.Combat.combat(self, gru)

        if global_.player.get_hp() <= 0:
            return 'death'

        if gru.get_hp() <= 0:
            return 'escape'
