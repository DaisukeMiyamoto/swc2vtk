# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 15:52:38 2016

@author: nebula
"""

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
        self.data = []

        if (filename != ''):
            self.filename = filename
            self.loadswc()
        else:
            pass
        
    def loadswc(self):
        with open(self.filename, 'r') as f:
            for line in f:
                if line[0] == '#':
                    self.header += line                    

                elif len(line) > 1:
                    record = line.strip().split(' ')
                    
                    one_data = {'id':int(record[0]), 
                                'type':int(record[1]),
                                'pos':[float(record[2]), float(record[3]), float(record[4])],
                                'radius':float(record[5]),
                                'parent':int(record[6])}
                    self.data.append(one_data)

if __name__ == '__main__':
    swc = Swc('simple.swc')
    print swc.data
    

            