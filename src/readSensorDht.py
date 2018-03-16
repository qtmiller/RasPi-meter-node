import Adafruit_DHT
import time

from inputBlock import InputBlock
from tagPoint import TagPoint

class ReadSensorDht(InputBlock):

    def __init__(self, tagname, data_pin, read_humid=False, DHT22=True):
        super().__init__(tagname)
        self.pin = data_pin

        if (read_humid):
            self.data_out = 0
        else:
            self.data_out = 1

        if (DHT22):
            self.sensor = Adafruit_DHT.DHT22
        else:
            self.sensor = Adafruit_DHT.DHT11

        self.configure_sensor()
        return None

    def configure_sensor(self):
        self.reading = Adafruit_DHT.read_retry(
            self.sensor,
            self.pin) \
            [self.data_out]

    def read(self):
        self.configure_sensor()
        tp = TagPoint(self.tagname,
                      time.localtime(time.time()),
                      self.reading)
        self.recent_tag_points.append(tp)
        self.send_tag_point()
