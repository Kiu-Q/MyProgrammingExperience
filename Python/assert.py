# -*- coding: utf-8 -*-
"""
Created on Wed Jan 26 15:25:06 2022

@author: user
"""

class siufa():
    def __init__(self, weight):
        self.w = weight
        print('origial weight: '+str(self.w))
    def wei(self, inc):
        assert self.w >= 0
        self.w += inc
        print('new weight: '+str(self.w))
cat=siufa(-1)
cat.wei(1)