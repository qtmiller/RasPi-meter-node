import RPi.GPIO as GPIO

from inputBlock import InputBlock

class pulseDetect(InputBlock):
    pin_id = None
    active_high = None

    def __init__(self, tagname, pin, active_high=True):
        super().__init__(tagname)
        GPIO.setmode(GPIO.BOARD)
        self.pin_id = pin
        self.active_high = active_high
        configureInput(self)
        return None

    def setPinId(self, pin):
        self.pin_id = pin
        self._configureInput()
        return None

    def clearPinId(self):
        # clear GPIO config
        self.pin_id = None
        return None

    def setMode(self, mode):
        self.input_mode = mode
        return None

    def configureInput(self):
        if (self.pin_id == None 
            or self.active_high == None):
            return None
        else:
            if (self.active_high):
                resist_type = GPIO.PUD_DOWN
            else:
                resist_type = GPIO.PUD_UP
            GPIO.setup(self.pin_id, GPIO.IN, resist_type)
        return None

    def pulseCallback(self):
        # send tagpoint with 1
        return None

    def contCallback(self, channel):
        # send tagpoint with value
        # set timer for next callback
        return None
