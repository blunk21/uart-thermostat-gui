import serial


class Controller():
    def __init__(self, model, view):
        self. model = model
        self.view = view
        self.ser = serial.Serial(port="/dev/ttyUSB1", baudrate=115200)

    def cooling_radio_change(self, number: int, val: int):
        try:
            self.model.rooms["Rooms"][number]["cooling"] = int(val)

            self.send_cooling_command(room_nr=number, value=val)
        except TypeError or ValueError:
            self.view.raise_error(
                "An error occured. Could not change cooling status.")

    def save_configuration(self):
        self.model.write_config_to_json()

    def set_target_temp(self, number: int, val: float):
        self.model.set_target_temp(room_nr=number, val=float(val))

        self.send_temp_command(room_nr=number, value=val)

    def load_view_config(self):
        roomlist = self.model.rooms.get("Rooms")
        self.view.load_config(roomlist)

    def send_temp_command(self, room_nr, value):
        commandstring: str = f":st{room_nr+1}{int(value*10)}!"
        self.ser.write(bytes(commandstring, "ascii"))
        print("sent:" + commandstring)

    def send_cooling_command(self, room_nr, value):
        commandstring: str = f":sc{room_nr+1}00{value}!"
        self.ser.write(bytes(commandstring, "ascii"))
        print("sent:" + commandstring)
