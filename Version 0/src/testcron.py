#!/usr/bin/env python3

# testing cron functionality to see if this pops up on startup

import os
import sys

os.chdir(os.path.dirname(os.path.abspath(__file__)))
with open('cron tootally ran.txt','w') as f:
    f.write('test')
