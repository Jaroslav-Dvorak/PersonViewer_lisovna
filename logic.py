from time import time
from rfid import RFID
from limit_switch import LimitSwitch


class Logic(LimitSwitch):
    def __init__(self, door_sw_pin, rfid_device):
        super().__init__(door_sw_pin)

        self.inst_rfid = RFID(rfid_device)
        self.last_rfid = None
        self.door_opened = False
        self.open_time = None
        self.rfid_time = None

    def scan(self):
        status = str()

        rfid = self.inst_rfid.read()
        if rfid is not None:
            self.last_rfid = rfid
            self.rfid_time = time()

        if self.switch.value:
            self.door_opened = True
            if self.open_time is None:
                self.open_time = time()

            if self.last_rfid is not None and self.door_opened:
                status = "opened_correctly"
                self.rfid_time = time()
            else:
                status = "opened_no_rfid"
        else:
            self.open_time = None
            if self.rfid_time is not None and (time() - self.rfid_time) > 3:
                status = "no_opening"
                self.rfid_time = None
            elif self.door_opened:
                status = "closed"
                self.last_rfid = None
                self.door_opened = False
                self.rfid_time = None

        return status

    def rising(self):
        pass

    def falling(self):
        pass
