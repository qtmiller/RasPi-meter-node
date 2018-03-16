from time import sleep
import sys

sys.path.append('src')
from heartbeat import Heartbeat
from pulseDetect import PulseDetect
from accumulator import Accumulator
from ftpLocalSave import FtpLocalSave
from timedCallback import TimedCallback
from readSensorDht import ReadSensorDht

##  Heartbeat
L2B1 = Heartbeat(300)
L2B2 = FtpLocalSave()
L2B1.connect_output(L2B2)

## Temperature sensor
L3B1 = TimedCallback(delay=600)
L3B2 = ReadSensorDht('Box_temperature',21)
L3B3 = FtpLocalSave()
L3B2.connect_output(L3B3)
L3B1.callback = L3B2.read
L3B1.start()

## Humidity sensor
L4B1 = TimedCallback(delay=600)
L4B2 = ReadSensorDht('Box_humidity',21,read_humid=True)
L4B3 = FtpLocalSave()
L4B2.connect_output(L4B3)
L4B1.callback = L4B2.read
L4B1.start()

##  Fortis natural gas pulse detection
L1B1 = PulseDetect('WLK_NatGas_MainMeter',7)
L1B2 = Accumulator()
L1B3 = FtpLocalSave()
L1B1.connect_output(L1B2)
L1B2.connect_output(L1B3)

while (True):
    sleep(1)
