import character
import datetime as dt
import yaml
from yaml.loader import SafeLoader

file = open('narration.yaml', 'r')
narrator = yaml.load(file, Loader=SafeLoader)


player = character.Character('Strifer', 100)
world_time = dt.datetime(2254, 1, 1, 12, 0, 0)
