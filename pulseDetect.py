import RPi.GPIO as GPIO
import time

from inputBlock import InputBlock
from tagPoint import TagPoint

class PulseDetect(InputBlock):

    def __init__(self, tagname, pin, active_high=True):
        super().__init__(tagname)
        GPIO.setmode(GPIO.BOARD)
        self.pin_id = pin
        self.active_high = active_high
        self._configure_input()
        return None

    def set_pin_id(self, pin):
        self.pin_id = pin
        self._configure_input()
        return None

    def clear_pin_id(self):
        GPIO.cleanup(self.pin_id)
        self.pin_id = None
        return None

    def set_mode(self, mode):
        self.input_mode = mode
        return None

    def _configure_input(self):
        resist_type = None
        edge_detect = None
        if (self.pin_id == None 
            or self.active_high == None):
            return None
        else:
            if (self.active_high):
                resist_type = GPIO.PUD_DOWN
                edge_detect = GPIO.RISING
            else:
                resist_type = GPIO.PUD_UP
                edge_detect = GPIO.FALLING
            GPIO.setup(self.pin_id, GPIO.IN, resist_type)
            GPIO.add_event_detect(self.pin_id, edge_detect, self.pulse_callback, bouncetime=300)
        return None

    def pulse_callback(self, channel):
        timestamp = time.localtime(time.time())
        tp = TagPoint(self.tagname, timestamp, 1)
        super().recv_tag_point(tp)
        super().send_tag_point()
        return None
