import serial


class RFID:
    def __init__(self, device):

        self.ser = serial.Serial(port=device,
                                 baudrate=9600,
                                 bytesize=8,
                                 parity=serial.PARITY_NONE,
                                 stopbits=1,
                                 xonxoff=0,
                                 rtscts=0
                                 )
        self.ser.timeout = 0.1
        if not self.ser.isOpen():
            self.ser.open()

    def read(self):
        x = self.ser.read(10)
        if len(x) > 0:
            return x.hex()

    @property
    def ended(self):
        return not self.ser.isOpen()
