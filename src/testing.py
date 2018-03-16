from heartbeat import Heartbeat
from timedCallback import TimedCallback
from readSensorDht import ReadSensorDht
from ftpLocalSave import FtpLocalSave


## Humidity sensor
L4B1 = TimedCallback(delay=600)
L4B2 = ReadSensorDht('Box_humidity',21,read_humid=True)
L4B3 = FtpLocalSave()
L4B2.connect_output(L4B3)
L4B1.callback = L4B2.read
L4B1.start()
