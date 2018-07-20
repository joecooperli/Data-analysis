# -*- coding: utf-8 -*-
"""
Created on Tue Jul 10 10:19:32 2018

@author: joe01.cooper
"""

import pandas as pd
import numpy as np
from sklearn import preprocessing
import math
import os

#定位工作路径（电脑桌面）
os.chdir(r"D:\Users\joe01.cooper\Desktop")

#读取RFM模型数据表（含拒退）
data = pd.read_csv('RFM_model_with_rejected_order.csv', header = 0)
data_analysis = data[['recency', 'frequency', 'monetary']]

# 实现标准化变换
data_Density = (data_analysis - data_analysis.min(axis = 0))/(data_analysis.max(axis = 0) - data_analysis.min(axis = 0)) 
print(data_Density)

data1 = pd.DataFrame([[1,2,3],
                      [4,5,6],
                      [7,8,9]])
#min-max标准化方法
data_standard = (data1 - data1.min(axis = 0)) / (data1.max(axis = 0) - data1.min(axis = 0))
print('min-max标准化:\n', data_standard)

#z-score标准化方法
data_density = (data1 - data1.mean(axis = 0)) / data1.std(axis = 0)
print('z-score标准化:\n', data_density)

#相当于z-score标准化
data_scale = preprocessing.scale(data1)
print('scale标准化:\n', data_scale)

#min-max标准化
data_MinMaxScaler = preprocessing.MinMaxScaler()
data_minmax = data_MinMaxScaler.fit_transform(data1)
print('MinMaxScaler标准化：\n', data_minmax)

#atan反正切函数标准化
empty_list =[]
for index,row in data1.iterrows():
    for i in row:
        data_atan = (math.atan(i) * 2 / math.pi)
        empty_list.append(data_atan)
data_atanscale = pd.DataFrame(np.array(empty_list).reshape(3,3))     
print(data_atanscale)