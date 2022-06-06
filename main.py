import json
import narration
import scenes
import character

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

class Map(object):
    # scenes avaliable on the map
    scenes = {
        'introduction': scenes.Introduction(),
        'cell': scenes.Cell(),
        'death': scenes.Death(),
        'escape': scenes.Escape(),
        'fight': scenes.Fight()
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

# creates a_map, Passes the introduction variable to the created object
a_map = Map('introduction')
# creates a_game object, passes the a_map object to the Engine class
a_game = Engine(a_map)
a_game.play()
