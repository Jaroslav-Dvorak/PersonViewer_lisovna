from tkinter import *
from scene import Scene
from logic import Logic
from is_rpi import is_rpi

if is_rpi():
    dev_door_outside = "/dev/ttyUSB0"
    dev_door_inside = "/dev/ttyUSB1"
else:
    dev_door_outside = "COM2"
    dev_door_inside = "COM1"


class GUI:
    def __init__(self):
        self.root = Tk()
        self.root.attributes("-fullscreen", True)
        self.root.configure(background='black')
        # l_frame_logic = Logic(door_sw_pin=21, rfid_device_1=dev_door_outside, rfid_device_2=dev_door_outside)
        # r_frame_logic = Logic(door_sw_pin=26, rfid_device=dev_door_2)
        # self.l_frame = Scene(self.root, l_frame_logic)
        # self.r_frame = Scene(self.root, r_frame_logic)
        # self.l_frame.frame.pack(expand=True, fill=BOTH, side=LEFT, padx=10, pady=10)
        # self.l_frame.frame.pack_propagate(0)
        # self.r_frame.frame.pack(expand=True, fill=BOTH, side=LEFT, padx=10, pady=10)
        # self.r_frame.frame.pack_propagate(0)
        frame_logic = Logic(door_sw_pin=26,
                            rfid_device_1=dev_door_inside,
                            rfid_device_2=dev_door_outside)
        self.frame = Scene(self.root, frame_logic)
        self.frame.frame.pack(expand=True, fill=BOTH, side=LEFT, padx=10, pady=10)
        self.frame.frame.pack_propagate(0)

        self.update()
        self.root.mainloop()

    def update(self):
        # self.l_frame.update()
        # self.r_frame.update()
        self.frame.update()
        self.root.after(100, self.update)
