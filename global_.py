import character
import datetime as dt
import yaml
from yaml.loader import SafeLoader
from yaml.loader import BaseLoader

# Open at launch and then  we have access to narration globaly.
narration_file = open('narration.yaml', 'r')
narrator = yaml.load(narration_file, Loader=SafeLoader)

player = character.Character('Strifer', 100)
world_time = dt.datetime(2254, 1, 1, 12, 0, 0)
