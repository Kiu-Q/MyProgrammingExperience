# -*- coding: utf-8 -*-
"""
Created on Wed Jan 26 09:46:20 2022

@author: user
"""

import os
file='file.txt'
if os.path.exists(file):
    os.remove(file)
else:
    print('file not here')