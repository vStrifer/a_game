import narration
import scenes
import character

class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    # starts the 'introduction' and plays until current_scene == 'escape'
    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('escape')

        # while current_scene != 'escape' set current_scene as next_scene
        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        current_scene.enter()

class Map(object):

    # scenes avaliable on the map, return values get mapped to next_scene
    # which in turn is the name of the scene class to be called.
    scenes = {
        'introduction': scenes.Introduction(),
        'cell': scenes.Cell(),
        'death': scenes.Death(),
        'escape': scenes.Escape(),
        'fight': scenes.Fight()
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    # returns the scene corresponding to the start_scene variable
    def next_scene(self, scene_name):
        scene = self.scenes.get(scene_name)
        return scene

    def opening_scene(self):
        return self.next_scene(self.start_scene)

# Starts the game, first scene to be played is 'introduction'
a_map = Map('introduction')
a_game = Engine(a_map)
a_game.play()
