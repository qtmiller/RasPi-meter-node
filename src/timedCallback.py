import time
import threading

from inputBlock import InputBlock

class TimedCallback(InputBlock):

    def __init__(self, delay=60, callback=None):
        self.delay = delay
        self.callback = callback
        return None

    def loop(self):
        next_call = time.time()
        while True:
            next_call = next_call + self.delay
            self.callback()
            time.sleep(next_call - time.time())

    def start(self):
        timerThread = threading.Thread(target=self.loop)
        timerThread.start()
