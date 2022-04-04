# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 10:21:15 2022

@author: user
"""

def cmToM(cm):
    m=int(cm)/100
    return m
cm=input('enter cm change to m')
print(cm+'cm change to m is %d m'%(cmToM(cm)))