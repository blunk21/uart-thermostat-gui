


class Controller():
    def __init__(self, model, view):
        self. model = model
        self.view = view

    def cooling_radio_change(self,number:int,val:int):
        try:
            self.model.rooms["Rooms"][number]["cooling"] = int(val)
        except TypeError or ValueError:
            self.view.raise_error("An error occured. Could not change cooling status.")

    def save_configuration(self):
        self.model.write_config_to_json()
    
    def set_target_temp(self,number:int,val:float):
        self.model.set_target_temp(room_nr=number,val=float(val))

    def load_view_config(self):
        roomlist= self.model.rooms.get("Rooms")
        self.view.load_config(roomlist)    