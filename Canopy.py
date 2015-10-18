# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 10:28:08 2015

@author: Administrator
"""

import numpy as np
from math import sqrt

def canopy(data,t1,t2):
    l = len(data)
    canopy_list = {}
    distance =cal_dis(data)
    judge = [True for i in xrange(l)]
    center_list = []
    c = 0
    for i in xrange(l):
        if judge[i] == False:
            continue
        center_list.append(i)
        idx = [x[0] for x in filter(lambda x:x[1] <= t1,enumerate(distance[i]))]
        idx2 = [x[0] for x in filter(lambda x:x[1] <= t2,enumerate(distance[i]))]
        canopy_list[c]=[data[j] for j in idx2]
        c += 1
        for j in idx:
            judge[j] = False
        
    return center_list, canopy_list
        
        
def cal_dis(data):
    l = len(data)
    data = np.array(data)
    dis_matrix = [[] for i in xrange(l)]
    for i in xrange(l):
        for j in xrange(l):
            dis_matrix[i].append(sqrt(sum((data[i]-data[j])**2)))
    return np.array(dis_matrix)

if __name__=='__main__':
    X = [[1,0],[3,0],[5,0],[6,0]]
    print cal_dis(X)
    center_list, canopy_list = canopy(X,1,2)
    