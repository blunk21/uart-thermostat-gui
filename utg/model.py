import json
from dataclasses import dataclass
from os.path import exists

MAX_NO_OF_ROOMS = 4
CONFIG_FILE_NAME = "room_configs.json"


@dataclass
class Room():
    nr: int
    target_temp: float


class Model():
    def __init__(self) -> None:
        self.rooms: dict = {"Rooms": []}
        if self.check_for_existing_config():
            self.load_config()
        else:
            self.initialize_config()

    def check_for_existing_config(self) -> bool:
        if exists(CONFIG_FILE_NAME):
            return True
        else:
            return False

    def initialize_config(self) -> None:
        self.create_room_objects()
        self.write_config_to_json()

    def set_room_target_temp(self, room_no: int, target_temp: float) -> None:
        pass

    def load_config(self):
        print("Loading configuration")
        fo = open(CONFIG_FILE_NAME, "r")
        self.rooms = json.load(fo)
        fo.close()

    def write_config_to_json(self):
        """
        with open(CONFIG_FILE_NAME, "w") as fo:
            fo.write('')
            for room in self.rooms:
                json.dump(room, fo, indent=4)"""
        print("Saving configuration")
        fo = open(CONFIG_FILE_NAME, "w")
        fo.truncate(0)
        json.dump(self.rooms, fo, indent=4)
        fo.close()

    def create_room_objects(self) -> None:
        print("Creating room objects")
        for nr in range(MAX_NO_OF_ROOMS):
            new_room: dict = {
                "nr": nr+1, "target_temp": 22.5, "cooling": 0}
            self.rooms["Rooms"].append(new_room)

    def get_target_temp(self, room_nr: int) -> float:
        return self.rooms["Rooms"][room_nr-1]["target_temp"]

    def set_target_temp(self,room_nr:int,val:float):
        self.rooms["Rooms"][room_nr]["target_temp"] = val
