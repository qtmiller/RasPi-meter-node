import time

from block import Block
from pulseDetect import PulseDetect as pd
from accumulator import Accumulator as accu
from ftpLocalSave import FtpLocalSave as fls
from tagPoint import TagPoint as tp

# create instances

x = pd('WLK-natgas',29)
y = accu()
z = fls()
t = tp('test_tag',time.localtime(time.time()), 1)

# connect blocks
x.connect_output(y)
y.connect_output(z)

# test data path
x.pulse_callback(1)

'''
# test block parameter setting
b = Block()
print(b.get_param_dict())
emp_dict = {}
b.set_param_dict(emp_dict)
diff_dict = {'irrelevant':13}
b.set_param_dict(diff_dict)
rel_dict = {'recent_tp_limit':12}
b.set_param_dict(rel_dict)
print(b.recent_tp_limit)
'''
