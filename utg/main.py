import tkinter
from model import Model
from view import View
from controller import Controller
import tkinter as tk


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("UART Thermostat")
        self.attributes("-zoomed",True)
        model = Model()
        view = View(self)
        view.pack(fill="both")

        controller = Controller(model=model,view=view)

        view.set_controller(controller=controller)

        controller.load_view_config()




if __name__ == "__main__":
    app = App()

    app.mainloop()
