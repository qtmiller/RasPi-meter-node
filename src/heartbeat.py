import time

from inputBlock import InputBlock
from tagPoint import TagPoint
from timedCallback import TimedCallback

class Heartbeat(InputBlock):

    def __init__(self, seconds):
        self.tag_name = 'HeartBeat'
        super().__init__(self.tag_name)
        self.seconds = seconds
        tc = TimedCallback(seconds,self.log_status)
        tc.start()
        return None

    def log_status(self):
        self.hbeat_tag_point = TagPoint(
            self.tag_name,
            time.localtime(time.time()),
            1)
        self.recv_tag_point(self.hbeat_tag_point)
        self.send_tag_point()
