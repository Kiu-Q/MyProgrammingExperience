# -*- coding: utf-8 -*-
"""
Created on Thu Jan 27 10:22:02 2022

@author: user
"""
import traceback

def checkWeight(weight):
    if(weight > 10):
        raise Exception('too heavy\n')
    if(weight < 2):
        raise Exception('too light\n')
    else:
        raise Exception('pased\n')
for weight in (1,6,11):
    try:
        checkWeight(weight)
    except Exception as e:
        with open('file (2).txt', 'a') as f:
            f.write(traceback.format_exc())
            f.write('weight: %d kg'%(weight)+'\n'+'\n')
            f.close
        print('weight: %d, '%(weight)+ str(e)+'\n')
        print('weight information entered to: '+str(f)+'\n')