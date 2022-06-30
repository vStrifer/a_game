import global_

class Combat(object):

    def attack_flee(self, enemy):

        print("Attack or Flee?")
        print("1. Attack")
        print("2. Flee")

        while global_.player.get_hp() > 0 and enemy.get_hp() > 0:

            player_input = input('> ')

            if player_input == '1':
                print(global_.narrator['scenes']['rooms']['player']['a1'])
                enemy.reduce_hp(20)
                print(f"Enemy HP:", {enemy.get_hp()})
            else:
                print(global_.narrator['scenes']['rooms']['enemy']['a1'])
                global_.player.reduce_hp(20)
                print(f"Player HP:", {global_.player.get_hp()})

class Items(object):

    # TODO: List of items to pull from based on input
    def inspect(self, item):
        print(f"This is an: ", {item})

    def inventory(self):
        print(f"You have: ", {global_.player.items})

        print("Do you want to use an item?")
        print("1. Yes")
        print("2. No")

        player_input = input('> ')

        if player_input == '1':

            if global_.player.items # contains X
                # print whatever you can do with X depending on Y
                # Use list functions to handle the item interaction
                # Collar is special case

        else:
            return



    def combind(self, item1, item2):
        pass
