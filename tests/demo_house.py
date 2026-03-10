from pathlib import Path
import sys

sys.path.append(str(Path().parent.absolute()))

from smarthouse.domain import *

DEMO_HOUSE = SmartHouse()

DEMO_HOUSE.register_floor(1)
DEMO_HOUSE.register_floor(2)

# rooms floor 1
DEMO_HOUSE.register_room(1,39.75,'LivingRoomKitchen')
DEMO_HOUSE.register_room(1,6.3,'Bathroom')
DEMO_HOUSE.register_room(1,13.5,'Entrance')
DEMO_HOUSE.register_room(1,8,'Guest Room 1')
DEMO_HOUSE.register_room(1,19,'Garage')

# rooms floor 2
DEMO_HOUSE.register_room(2,11.75,'Office')
DEMO_HOUSE.register_room(2,9.25,'Bathroom 2')
DEMO_HOUSE.register_room(2,8,'Guest Room 2')
DEMO_HOUSE.register_room(2,10,'Guest Room 3')
DEMO_HOUSE.register_room(2,4,'Dressing Room')
DEMO_HOUSE.register_room(2,17,'Master Bedroom')
DEMO_HOUSE.register_room(2,10,'Hallway')

smart_lock = SmartLock('4d5f1ac6-906a-4fd1-b4bf-3a0671e4c4f1','MythicalTech', 'Guardian Lock 7000')
co2_sensor = CO2Sensor('8a43b2d7-e8d3-4f3d-b832-7dbf37bf629e', 'ElysianTech', 'Smoke Warden 1000')
#eletricity_meter = ('a2f8690f-2b3a-43cd-90b8-9deea98b42a7', 'MysticEnergy Innovations', 'Volt Watch Elite')

#ground_floor = DEMO_HOUSE.register_floor(1)
#entrance = DEMO_HOUSE.register_room(ground_floor, 13.5, "Entrance")
# TODO: continue registering the remaining floor, rooms and devices

