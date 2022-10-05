from cmath import exp
from ctypes import alignment
from logging import root
from textwrap import fill
import tkinter as tk
from tkinter import E, HORIZONTAL, LEFT, messagebox
import re
from turtle import width
from controller import Controller


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
                new_room = Room(self, number=i*2+j+1)
                new_room.grid(row=i,
                              column=j, sticky="nesw", pady=10)
                self.rooms.append(new_room)

        self.nav_frame = NavBar(self).grid(column=0, row=2, columnspan=5)

    def set_controller(self, controller):
        self.controller = controller

    def raise_error(self, msg: str):
        messagebox.showerror(msg)

    def load_config(self, rooms: list):

        for i, obj in self.children.items():
            if isinstance(obj, Room):
                target_temp = rooms[obj.number-1].get("target_temp")
                cooling = rooms[obj.number-1].get("cooling")

                # obj.target_temp_label.config(
                #     text=f"Target temperature {target_temp}°C")
                obj.target_temp_scale.set(target_temp)
                obj.cooling_radio_var.set(cooling)
                if cooling:
                    obj.cooling_radio_no.deselect()
                    obj.cooling_radio_yes.select()
                else:
                    obj.cooling_radio_no.select()
                    obj.cooling_radio_yes.deselect()


class Room(tk.LabelFrame):
    def __init__(self, parent, number):
        super().__init__(parent)
        self.number = number

        self.columnconfigure(index=0, weight=1, pad=20)
        self.columnconfigure(index=1, weight=1)
        self.rowconfigure(index=0, weight=1, pad=10)
        self.rowconfigure(index=1, weight=1, pad=5)

        # Room no
        self.target_temp_var = tk.StringVar()
        self.room_nr_label = tk.Label(
            self, text=f"Room {number}", justify=tk.CENTER)
        self.room_nr_label.grid(
            column=0, row=0, columnspan=5, sticky="w",padx=10)

        # Target temp
        self.target_temp_container = tk.Frame(self)
        self.target_temp_container.grid(column=0, row=1, sticky=tk.W)
        self.target_temp_scale = tk.Scale(
            self.target_temp_container, from_=15.0, to=30.0, resolution=0.5, orient=HORIZONTAL)
        self.target_temp_scale.grid(column=1, row=0)
        self.target_temp_scale.bind(
            "<ButtonRelease-1>", self.on_set_target_temp)
        self.target_temp_label = tk.Label(
            self.target_temp_container, text="Target temperature °C")
        self.target_temp_label.grid(
            column=0, row=0, padx=10)

        # Cooling Radiobuttons
        self.cooling_radio_container = tk.Frame(self)
        self.cooling_radio_container.grid(column=0,row=2,sticky=tk.W,padx=10)
        self.cooling_radio_var = tk.StringVar()
        self.cooling_radio_var.set(0)
        self.cooling_label = tk.Label(self.cooling_radio_container, text="Cooling:")
        self.cooling_label.grid(column=0, row=0, sticky=tk.W)
        self.cooling_radio_yes = tk.Radiobutton(
            self.cooling_radio_container, value=1, variable=self.cooling_radio_var, text="yes", command=self.on_cooling_radio_change)
        self.cooling_radio_yes.grid(column=1, row=0, sticky=tk.E)
        self.cooling_radio_no = tk.Radiobutton(
            self.cooling_radio_container, value=0, variable=self.cooling_radio_var, text="no", command=self.on_cooling_radio_change)
        self.cooling_radio_no.grid(column=2, row=0, sticky=tk.W)
        self.cooling_radio_no.select()

    def on_cooling_radio_change(self):
        if int(self.cooling_radio_var.get()) == 1:
            messagebox.showinfo(title="Attention", message=f"In case the temperature goes above "
                                f"{self.target_temp_var.get()[-6:]}"
                                f" cooling is going to start in Room#{self.number}")
        self.master.controller.cooling_radio_change(number=self.number-1,
                                                    val=self.cooling_radio_var.get())

    def on_set_target_temp(self, event):
        value = self.target_temp_scale.get()
        if not value:
            messagebox.showerror(title="Bad value", message="The temperature format is incorrect."
                                 "\nThe correct format is 'xx.x'")
            return

        # set the label
        self.target_temp_var.set(
            f"Target temperature: {self.target_temp_scale.get()}")

        self.master.controller.set_target_temp(self.number-1, value)


class NavBar(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.save_config_button = tk.Button(
            master=self, text="Save config", command=self.save_config)
        self.save_config_button.pack(side=tk.RIGHT, anchor=tk.SE)

        # self.load_config_btn = tk.Button(
        #     master=self, text="Load config", command=self.load_config
        # )
        # self.load_config_btn.pack(side=LEFT)

    def save_config(self):
        self.master.controller.save_configuration()

    # def load_config(self):
    #     self.master.controller.load_view_config()
