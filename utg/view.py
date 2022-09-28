from cmath import exp
from ctypes import alignment
from logging import root
from textwrap import fill
import tkinter as tk


class View(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.columnconfigure(index=0, weight=1)
        self.columnconfigure(index=1, weight=1)
        self.rowconfigure(index=0, weight=1)
        self.rowconfigure(index=1, weight=1)
        self.rooms = []
        for i in range(2):
            for j in range(2):
                new_room = Room(self, i+j+1).grid(row=i,
                                                  column=j, sticky="nesw", pady=10)
                self.rooms.append(new_room)

        self.nav_frame = NavBar(self).grid(column=0, row=2, columnspan=5)

    def set_controller(self, controller):
        self.controller = controller

    def save_config(self):
        pass


class Room(tk.Frame):
    def __init__(self, parent, number):
        super().__init__(parent)
        self.columnconfigure(index=0, weight=1, pad=20)
        self.columnconfigure(index=1, weight=1)
        self.rowconfigure(index=0, weight=2, pad=10)
        self.rowconfigure(index=1, weight=1, pad=5)

        # Title and target temp labewl
        self.target_temp_var = tk.StringVar()
        self.target_temp_var.set("Target temperature: 22.0")
        self.room_nr_label = tk.Label(self, text=f"Room {number}", justify=tk.CENTER).grid(
            column=0, row=0, columnspan=5, sticky="nesw")
        self.target_temp_label = tk.Label(self, textvariable=self.target_temp_var).grid(
            column=0, row=1, columnspan=2, sticky="nesw")

        # Cooling Radiobuttons
        self.cooling_radio_var = tk.StringVar()
        self.cooling_radio_var.set(0)
        self.cooling_radio_yes = tk.Radiobutton(
            self, value=1, variable=self.cooling_radio_var, text="yes")
        self.cooling_radio_yes.grid(column=0, row=2)
        self.cooling_radio_no = tk.Radiobutton(
            self, value=0, variable=self.cooling_radio_var, text="no")
        self.cooling_radio_no.grid(column=1, row=2)


class NavBar(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.save_config_button = tk.Button(
            master=self, text="Save config", command=self.master.save_config)
        self.save_config_button.pack(side=tk.RIGHT, anchor=tk.SE)
