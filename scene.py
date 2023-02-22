from time import time
from datetime import timedelta
from tkinter import *
from db import DB

GREEN = "green"
ORANGE = "orange"
RED = "red"

DB = DB()


class Scene:
    def __init__(self, root, logic):

        self.frame = Frame(root,
                           bg=GREEN,
                           # height=1080,
                           # width=960,
                           # border=10,
                           # highlightbackground="black",
                           # borderwidth=1,
                           # relief=SOLID
                           )
        self.door = Label(self.frame,
                          text="VRATA UZAVŘENA",
                          font=("Verdana", 100, "bold"),
                          bg=GREEN
                          )
        self.door.pack(pady=20)
        self.person = Label(self.frame, font=("Verdana", 100, "bold"), bg=GREEN)
        self.person.pack(side=TOP, expand=YES)
        self.time = Label(self.frame, font=("Verdana", 140), bg=GREEN)
        self.time.pack(side=BOTTOM, pady=20)

        self.logic = logic

        self.update()

    def update(self):
        status = self.logic.scan()

        if status == "opened_correctly":
            self.frame.configure(bg=ORANGE)
            self.door.configure(text="VRATA OTEVŘENA")
            person_name = DB.read(self.logic.last_rfid)
            self.person.configure(text="ZODPOVĚDNÁ OSOBA:\n"+person_name)

        elif status == "opened_no_rfid":
            self.frame.configure(bg=RED)
            self.door.configure(text="VRATA OTEVŘENA\nBEZ ČIPU!")

        elif status == "no_opening":
            self.frame.configure(bg=ORANGE)
            self.door.configure(text="VRATA SE NEOTEVŘELA")
            self.person.configure(text="")
            self.time.configure(text="")

        elif status == "closed":
            self.frame.configure(bg=GREEN)
            self.door.configure(text="VRATA UZAVŘENA")
            self.person.configure(text="")
            self.time.configure(text="")

        if "opened" in status:
            t = time() - self.logic.open_time
            t = str(timedelta(seconds=t)).split('.', 2)[0]
            self.time.configure(text="DOBA OTEVŘENÍ:\n"+t)

        self.door.configure(bg=self.frame["background"])
        self.person.configure(bg=self.frame["background"])
        self.time.configure(bg=self.frame["background"])
