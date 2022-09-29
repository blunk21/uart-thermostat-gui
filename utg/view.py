from cmath import exp
from ctypes import alignment
from logging import root
from textwrap import fill
import tkinter as tk
from tkinter import messagebox
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
                new_room = Room(self, number=i+j+1).grid(row=i,
                                                         column=j, sticky="nesw", pady=10)
                self.rooms.append(new_room)

        self.nav_frame = NavBar(self).grid(column=0, row=2, columnspan=5)

    def set_controller(self, controller):
        self.controller = controller

    def raise_error(self, msg: str):
        messagebox.showerror(msg)


class Room(tk.Frame):
    def __init__(self, parent, number):
        super().__init__(parent)
        self.number = number

        self.columnconfigure(index=0, weight=1, pad=20)
        self.columnconfigure(index=1, weight=1)
        self.rowconfigure(index=0, weight=2, pad=10)
        self.rowconfigure(index=1, weight=1, pad=5)

        # Title and target temp label
        self.target_temp_var = tk.StringVar()
        self.target_temp_var.set("Target temperature: 22.0")
        self.room_nr_label = tk.Label(self, text=f"Room {number}", justify=tk.CENTER).grid(
            column=0, row=0, columnspan=5, sticky="w")
        self.target_temp_label = tk.Label(self, textvariable=self.target_temp_var).grid(
            column=0, row=1, columnspan=2, sticky="w")
        self.target_temp_entry = tk.Entry(self)
        self.target_temp_entry.grid(column=1,row=1,columnspan=3)
        self.target_temp_btn = tk.Button(self,text="Set",command=self.on_set_target_temp)
        self.target_temp_btn.grid(column=2,row=1)

        # Cooling Radiobuttons
        self.cooling_radio_var = tk.StringVar()
        self.cooling_radio_var.set(0)
        self.cooling_radio_yes = tk.Radiobutton(
            self, value=1, variable=self.cooling_radio_var, text="yes", command=self.on_cooling_radio_change)
        self.cooling_radio_yes.grid(column=0, row=2)
        self.cooling_radio_no = tk.Radiobutton(
            self, value=0, variable=self.cooling_radio_var, text="no", command=self.on_cooling_radio_change)
        self.cooling_radio_no.grid(column=1, row=2)

    def on_cooling_radio_change(self):
        if int(self.cooling_radio_var.get()) == 1:
            messagebox.showinfo(title="Attention", message=f"In case the temperature falls below "
                                f"{self.target_temp_var.get()[-4:]}°C"
                                f" cooling is going to start in Room#{self.number}")
        self.master.controller.cooling_radio_change(number=self.number-1,
                                                    val=self.cooling_radio_var.get())

    def on_set_target_temp(self):
        value = re.fullmatch("[1-9][0-9]\.[0-9]",self.target_temp_entry.get())
        if not value:
            messagebox.showerror(title="Bad value",message="The temperature format is incorrect."
            "\nThe correct format is 'xx.x'")
            return

        self.master.controller.set_target_temp(self.number-1,value[0])


class NavBar(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.save_config_button = tk.Button(
            master=self, text="Save config", command=self.save_config)
        self.save_config_button.pack(side=tk.RIGHT, anchor=tk.SE)

    def save_config(self):
        self.master.controller.save_configuration()
