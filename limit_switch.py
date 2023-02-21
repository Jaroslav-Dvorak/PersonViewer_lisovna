from gpiozero import Button
from gpiozero.pins.pigpio import PiGPIOFactory
from is_rpi import is_rpi

if is_rpi():
    pin_factory = PiGPIOFactory(host='127.0.0.1')
else:
    pin_factory = PiGPIOFactory(host='10.110.30.3')


class LimitSwitch:

    def __init__(self, pin):
        self.switch = Button(pin, pin_factory=pin_factory, pull_up=False)
        self.switch.when_activated = self.rising
        self.switch.when_deactivated = self.falling

    def rising(self):
        pass

    def falling(self):
        pass
