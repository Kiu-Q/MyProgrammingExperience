# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 17:21:16 2022

@author: user
"""

import random as r
draw=r.sample(range(1,51), 10)
specDraw=draw.pop()
draw.sort()
print('draw number is %d, %d, %d, %d, %d, %d, %d, %d, %d'%(draw[0],draw[1],draw[2],draw[3],draw[4],draw[5],draw[6],draw[7],draw[8]))
print('special number is: '+str(specDraw))