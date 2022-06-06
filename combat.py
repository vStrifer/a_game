import narration
#import character
import global_

class Combat(object):

    def combat(self, enemy):

        print("Attack or Flee?")
        print("1. Attack")
        print("2. Flee")

        while global_.player.get_hp() > 0 and enemy.get_hp() > 0:

            player_input = input('> ')

            if player_input == '1':
                print(narration.scenes['rooms']['player']['a1'])
                enemy.reduce_hp(20)
            else:
                print(narration.scenes['rooms']['enemy']['a1'])
                global_.player.reduce_hp(20)
