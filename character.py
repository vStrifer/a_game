class Character(object):
    # TODO: Handle status effects 
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
        self.sanity = None
        self.bleeding = None

        self.items = []

    def add_hp(self, change_in_hp):
        self.hp = self.hp + change_in_hp

    def reduce_hp(self, change_in_hp):
        self.hp = self.hp - change_in_hp

    def set_hp(self, hp):
        self.hp = hp

    def get_hp(self):
        return self.hp
