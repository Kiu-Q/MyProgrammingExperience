# -*- coding: utf-8 -*-
"""
Created on Wed Jan 26 10:01:13 2022

@author: user
"""

import os
Mdir='dir'
if os.path.exists(Mdir):
    os.rmdir(Mdir)
else:
    os.mkdir(Mdir)