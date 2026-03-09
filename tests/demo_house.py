from pathlib import Path
import sys

sys.path.append(str(Path().parent.absolute()))

from smarthouse.domain import *

DEMO_HOUSE = SmartHouse()

smart_lock = SmartLock('4d5f1ac6-906a-4fd1-b4bf-3a0671e4c4f1','MythicalTech', 'Guardian Lock 7000')

ground_floor = DEMO_HOUSE.register_floor(1)
entrance = DEMO_HOUSE.register_room(ground_floor, 13.5, "Entrance")
# TODO: continue registering the remaining floor, rooms and devices

