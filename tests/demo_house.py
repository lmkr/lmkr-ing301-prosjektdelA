from pathlib import Path
import sys

sys.path.append(str(Path().parent.absolute()))

from smarthouse.domain import *

DEMO_HOUSE = SmartHouse()

DEMO_HOUSE.register_floor(1)
DEMO_HOUSE.register_floor(2)

# rooms floor 1
living_room_kitchen = DEMO_HOUSE.register_room(1,39.75,'LivingRoomKitchen')
bathroom_1 = DEMO_HOUSE.register_room(1,6.3,'Bathroom 1')
entrance = DEMO_HOUSE.register_room(1,13.5,'Entrance')
guest_room_1 = DEMO_HOUSE.register_room(1,8,'Guest Room 1')
garage = DEMO_HOUSE.register_room(1,19,'Garage')

# rooms floor 2
office = DEMO_HOUSE.register_room(2,11.75,'Office')
bathroom_2 = DEMO_HOUSE.register_room(2,9.25,'Bathroom 2')
guest_room_2 = DEMO_HOUSE.register_room(2,8,'Guest Room 2')
guest_room_3 = DEMO_HOUSE.register_room(2,10,'Guest Room 3')
dressing_room = DEMO_HOUSE.register_room(2,4,'Dressing Room')
master_bedroom = DEMO_HOUSE.register_room(2,17,'Master Bedroom')
hallway = DEMO_HOUSE.register_room(2,10,'Hallway')

# devices

smart_lock = SmartLock('4d5f1ac6-906a-4fd1-b4bf-3a0671e4c4f1','MythicalTech','Guardian Lock 7000')
co2_sensor = Sensor('8a43b2d7-e8d3-4f3d-b832-7dbf37bf629e','CO2 sensor','lysianTech','Smoke Warden 1000', "PPM")
ele_meter = Sensor('a2f8690f-2b3a-43cd-90b8-9deea98b42a7','Electricity Meter','MysticEnergy Innovations','Volt Watch Elite', "kWh")
heat_pump = HeatPump('5e13cabc-5c58-4bb3-82a2-3039e4480a6d','ElysianTech','Thermo Smart 6000')
motion_sensor = Sensor('cd5be4e8-0e6b-4cb5-a21f-819d06cf5fc5','Motion Sensor','NebulaGuard Innovations','MoveZ Detect 69', "Motion")
hum_sensor = Sensor('3d87e5c0-8716-4b0b-9c67-087eaaed7b45','Humidity Sensor','AetherCorp','Aqua Alert 800', "%")
oven1 = Actuator('8d4e4c98-21a9-4d1e-bf18-523285ad90f6','Smart Oven','AetherCorp	','Pheonix HEAT 333')
garage_door = Actuator('9a54c1ec-0cb5-45a7-b20d-2a7349f1b132','Automatic Garage Door','MythicalTech','Guardian Lock 9000')
oven2 = Actuator('c1e8fa9c-4b8d-487a-a1a5-2b148ee9d2d1','Smart Oven','IgnisTech Solutions','Ember Heat 3000')
temp_sensor = Sensor('4d8b1d62-7921-4917-9b70-bbd31f6e2e8e','Temperature Sensor','AetherCorp','SmartTemp 42', "°C")
air_sensor = Sensor('7c6e35e1-2d8b-4d81-a586-5d01a03bb02c','Air Quality Sensor','CelestialSense Technologies','AeroGuard Pro', "AQI")
smart_plug = Actuator('1a66c3d6-22b2-446e-bf5c-eb5b9d1a8c79','Smart Plug','MysticEnergy Innovations','FlowState X')
dehumidifier = Actuator('9e5b8274-4e77-4e4e-80d2-b40d648ea02a','Dehumidifier','ArcaneTech Solutions	','Hydra Dry 8000')
light_bulp = Actuator('6b1c5f6b-37f6-4e3d-9145-1cfbe2f1fc28','Light Bulp','Elysian Tech','Lumina Glow 4000')

DEMO_HOUSE.register_device(living_room_kitchen, motion_sensor)
DEMO_HOUSE.register_device(living_room_kitchen, heat_pump)
DEMO_HOUSE.register_device(living_room_kitchen, co2_sensor)

DEMO_HOUSE.register_device(bathroom_1,hum_sensor)
DEMO_HOUSE.register_device(guest_room_1,oven1)
DEMO_HOUSE.register_device(entrance,ele_meter)
DEMO_HOUSE.register_device(entrance, smart_lock)

DEMO_HOUSE.register_device(garage, garage_door)

DEMO_HOUSE.register_device(office, smart_plug)
DEMO_HOUSE.register_device(bathroom_2, dehumidifier)
DEMO_HOUSE.register_device(guest_room_2, light_bulp)
DEMO_HOUSE.register_device(guest_room_3, air_sensor)
DEMO_HOUSE.register_device(master_bedroom, temp_sensor)
DEMO_HOUSE.register_device(master_bedroom, oven2)

#smart_lock = SmartLock('4d5f1ac6-906a-4fd1-b4bf-3a0671e4c4f1','MythicalTech', 'Guardian Lock 7000')
#co2_sensor = CO2Sensor('8a43b2d7-e8d3-4f3d-b832-7dbf37bf629e', 'ElysianTech', 'Smoke Warden 1000')
#eletricity_meter = ('a2f8690f-2b3a-43cd-90b8-9deea98b42a7', 'MysticEnergy Innovations', 'Volt Watch Elite')

#ground_floor = DEMO_HOUSE.register_floor(1)
#entrance = DEMO_HOUSE.register_room(ground_floor, 13.5, "Entrance")
# TODO: continue registering the remaining floor, rooms and devices

