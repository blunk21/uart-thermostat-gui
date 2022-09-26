import json
from dataclasses import dataclass

MAX_NO_OF_ROOMS = 4


@dataclass
class Room():
    nr: int
    target_temp: float


class Model():
    def __init__(self) -> None:
        self.rooms = list()
        existing_config: bool = self.check_for_existing_config()
        if not existing_config:
            self.initialize_config()

    def check_for_existing_config(self) -> bool:
        pass

    def initialize_config(self) -> None:
        create_room_objects(self.rooms)
        self.write_config_to_json(self.rooms)

    def set_room_target_temp(self,room_no:int) -> None:
        pass

    def write_config_to_json(self):
        jsonstring: str = ""
        for room in self.rooms:
            pass


def create_room_objects(roomlist: list):
    for nr in range(MAX_NO_OF_ROOMS):
        new_room: dict = {"Room{nr}":{"nr":str(nr),"target_temp": "22.5"}}
        roomlist.append(new_room)
