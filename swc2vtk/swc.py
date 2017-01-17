# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 15:52:38 2016

@author: nebula
"""
import os

'''
from neuromorpho.org

The three dimensional structure of a neuron can be represented in a SWC format (Cannon et al., 1998). SWC is a simple Standardized format. Each line has 7 fields encoding data for a single neuronal compartment:
an integer number as compartment identifier
type of neuronal compartment 
   0 - undefined
   1 - soma
   2 - axon
   3 - basal dendrite
   4 - apical dendrite
x coordinate of the compartment
y coordinate of the compartment
z coordinate of the compartment
radius of the compartment
parent compartment
'''


class Swc():
    
    def __init__(self, filename=''):
        self.header = ''
        self.data = {}
        self.scale = [1.0, 1.0, 1.0]

        if not (len(filename) == 0):
            self.filename = filename
            self.load_swc(filename)
        else:
            pass
        
    def load_swc(self, filename):
        with open(filename, 'r') as f:
            for line in f:
                if line[0] == '#':
                    self.header += line
                    if 'SCALE' in line:
                        record = line.split(' ')
                        if record[1] == 'SCALE':
                            self.scale[0] = float(record[2])
                            self.scale[1] = float(record[3])
                            self.scale[2] = float(record[4])
                        else:
                            self.scale[0] = float(record[1])
                            self.scale[1] = float(record[2])
                            self.scale[2] = float(record[3])

                elif len(line) > 1:
                    record = line.strip().split(' ')

                    one_data = {'id': int(record[0]),
                                'type': int(record[1]),
                                'pos': [float(record[2]) * self.scale[0], float(record[3]) * self.scale[1],
                                        float(record[4]) * self.scale[2]],
                                'radius': float(record[5]),
                                'parent': int(record[6])}
                    self.data[int(record[0])] = one_data

    def shift(self, x=0.0, y=0.0, z=0.0):
        for k, val in self.data.items():
            val['pos'][0] += x
            val['pos'][1] += y
            val['pos'][2] += z

    def invert(self, x=False, y=False, z=False):
        for k, val in self.data.items():
            if x is True:
                val['pos'][0] *= -1.0
            if y is True:
                val['pos'][1] *= -1.0
            if z is True:
                val['pos'][2] *= -1.0

if __name__ == '__main__':
    swc = Swc(os.path.join('..', 'swc', 'simple.swc'))
    swc.invert(True, False, False, )
    swc.shift(100.0, 0, 0)
    print(swc.data)
