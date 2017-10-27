

from accumulator import Accumulator as accu
from ftpLocalSave import FtpLocalSave as fls
from tagPoint import TagPoint as tp

# create instances
y = accu()
z = fls()
t = tp('test_tag','fake datetime', 100)

# connect blocks
y.connect_output(z)

# test data path
for i in range(5):
    y.recv_tag_point(t)
