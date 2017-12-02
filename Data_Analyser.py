#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 11:09:50 2017

@author: pi
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
inp = pd.read_csv('/home/ashish/Desktop/Imp Codes/Cog Sci Visual Cocktail Output/Murtu_trial1.txt',header = None)
inp = inp.iloc[1:,:]
sep = np.array(inp[31])
result1 = np.array(inp[33])
result2 = np.array(inp[35])
sep_unique = np.unique(sep)
seq_result = []
for i in sep_unique:
    j, = np.where(sep==i)
    count = 0
    count_two = count_mone = count_one = count_mtwo = 0
    for k in j:
        if result1[k]==1 and result2[k]==1:
            count+=1
            count_one+=1
        if result1[k]==1 and result2[k]==-1:
            count+=1
            count_mone+=1
        if result1[k]==1 and result2[k]==2:
            count+=1
            count_two+=1
        if result1[k]==1 and result2[k]==-2:
            count+=1
            count_mtwo+=1
    seq_result.append((i,count,count_two, count_mtwo, count_one, count_mone))

for k in range(2,3):
    x_axis = []
    y_axis = []
    for i in seq_result:
        x_axis.append(i[0])
        y_axis.append(i[k]/i[1] * 100)
    plt.plot(x_axis, y_axis)
plt.show()
    
    



