import datetime
from enum import Enum

class Measurement:
    """
    This class represents a measurement taken from a sensor.
    """

    def __init__(self, timestamp, value, unit):
        self.timestamp = timestamp
        self.value = value
        self.unit = unit

class Device:

    def __init__(self, id, device_type, supplier, model_name):
        self.id = id
        self.device_type = device_type
        self.supplier = supplier
        self.model_name = model_name
        self.room = None # when installed device will learn what room it is in

    def is_sensor(self):
        pass

    def is_actuator(self):
        pass

    def get_device_type(self):
        pass

class Sensor(Device):

    def __init__(self, id, device_type, supplier, model_name):
        super().__init__(id, device_type, supplier, model_name)

    def is_actuator(self):
        return False

    def is_sensor(self):
        return True

    def last_measurement(self):
        return Measurement(datetime.datetime.now(), 84.0, "°C") # TODO: generalize

class CO2Sensor(Sensor):

    def last_measurement(self):
        return Measurement(datetime.datetime.now(),84,"PPM")

class ElectricityMeter(Sensor):

    def last_measurement(self):
        return Measurement(datetime.datetime.now(),84,"kWh")

class ActuatorState(Enum):
    ACTIVE = 1
    INACTIVE = 2

class Actuator(Device):

    def __init__(self, id, device_type, supplier, model_name):
        super().__init__(id, device_type, supplier, model_name)
        self.state = ActuatorState.INACTIVE

    def is_sensor(self):
        return False

    def is_actuator(self):
        return True

    def turn_on(self):
        self.state = ActuatorState.ACTIVE

    def turn_off(self):
        self.state = ActuatorState.INACTIVE

    def is_active(self):
        return self.state == ActuatorState.ACTIVE

# TODO: need further subclasses for some of the sensor/actuators

class SmartLock(Actuator):

    def __init__(self, id, supplier, model_name):
        super().__init__(id, supplier, model_name)

class Room:

    def __init__(self, name, area):
        self.room_name = name
        self.area = area
        self.devices = []

    def register_device(self,device):
        self.devices.append(device)
        device.room = self

    def find_device(self,device_id):

        for device in self.devices:
            if device.id == device_id:
                return device

        return None

    def deregister_device(self, device):

        if device in self.devices:
            self.devices.remove(device)
            device.room = None

class Floor:

    def __init__(self, level):
        self.level = level
        self.rooms = []

    def register_room(self, room):
        self.rooms.append(room)

    def get_rooms(self):
        return self.rooms

    def get_area(self):

        area = 0
        for room in self.rooms:
            area += room.area

        return area

    def find_device(self,device_id):

        for room in self.rooms:

            device = room.find_device(device_id)

            if device:
                return device

        return None

    def get_devices(self):

        devices = []
        for room in self.rooms:
            devices += room.devices

        return devices

class SmartHouse:
    """
    This class serves as the main entity and entry point for the SmartHouse system app.
    Do not delete this class nor its predefined methods since other parts of the
    application may depend on it (you are free to add as many new methods as you like, though).

    The SmartHouse class provides functionality to register rooms and floors (i.e. changing the 
    house's physical layout) as well as register and modify smart devices and their state.
    """

    def __init__(self):
        self.floors = []

    def register_floor(self, level):
        """
        This method registers a new floor at the given level in the house
        and returns the respective floor object.
        """
        floor = Floor(level)
        self.floors.append(floor)

    def get_floor(self,level):

        for floor in self.floors:
            if floor.level == level:
                return floor

        return None

    def register_room(self, level, room_size, room_name = None):
        """
        This methods registers a new room with the given room areal size 
        at the given floor. Optionally the room may be assigned a mnemonic name.
        """

        floor = self.get_floor(level)

        room = None

        if floor is not None:
            room = Room(room_name, room_size)
            floor.register_room(room)

        return room

    def get_floors(self):
        """
        This method returns the list of registered floors in the house.
        The list is ordered by the floor levels, e.g. if the house has 
        registered a basement (level=0), a ground floor (level=1) and a first floor 
        (leve=1), then the resulting list contains these three floors in the above order.
        """
        return list.sort(self.floors, key= lambda f: f.level)


    def get_rooms(self):
        """
        This methods returns the list of all registered rooms in the house.
        The resulting list has no particular order.
        """
        rooms = []

        for floor in self.floors:
            rooms += floor.get_rooms()

        return rooms

    def get_area(self):
        """
        This methods return the total area size of the house, i.e. the sum of the area sizes of each room in the house.
        """
        area = 0
        for floor in self.floors:
            area += floor.get_area()

        return area

    def register_device(self, room, device):
        """
        This methods registers a given device in a given room.
        """
        current_room = device.room
        if current_room is not None:
            current_room.deregister_device(device)

        room.register_device(device)

    # FIXME: seems from the tests to have been called get_device_by_id earlier
    def get_device(self, device_id):
        """
        This method retrieves a device object via its id.
        """
        for floor in self.floors:
            device = floor.find_device(device_id)

            if device:
                return device

        return None

    # FIXME: had to add this one to make the test pass
    def get_devices(self):

        devices = []

        for floor in self.floors:
            devices +=floor.get_devices()

        return devices


