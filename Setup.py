from time import sleep
import sys

sys.path.append('src')
from pulseDetect import PulseDetect
from accumulator import Accumulator
from ftpLocalSave import FtpLocalSave

##  Fortis natural gas pulse detection
L1B1 = PulseDetect('WLK_NatGas_MainMeter',7)
L1B2 = Accumulator()
L1B3 = FtpLocalSave()
L1B1.connect_output(L1B2)
L1B2.connect_output(L1B3)

while (True):
    sleep(1)

