import time

from pulseDetect import PulseDetect as pd
from accumulator import Accumulator as accu
from ftpLocalSave import FtpLocalSave as fls
from tagPoint import TagPoint as tp

# create instances

x = pd('test_pulse_detect',29)
y = accu()
z = fls()
t = tp('test_tag',time.localtime(time.time()), 1)

# connect blocks
x.connect_output(y)
y.connect_output(z)

# test data path
