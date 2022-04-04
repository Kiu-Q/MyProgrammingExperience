# -*- coding: utf-8 -*-
"""
Created on Wed Jan 26 10:43:52 2022

@author: user
"""

class cat():
    def __init__(self, name,w):
        self.name=name
        self.w = w
    def fight(self):
        print(self.name + ' bom bom, weight: ' + str(self.w))
    def fat(self, inc):
        self.w += inc
    siufa='pig pig B'
index=cat('siufa',30)
index.fat(2)
index.fight()
print(index.siufa)