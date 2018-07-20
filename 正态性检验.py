# -*- coding: utf-8 -*-
"""
Created on Tue Jul 10 10:59:17 2018

@author: joe01.cooper
"""
#源数据不符合正态分布

import pandas as pd
#import numpy as np
import os
from scipy.stats import kstest #kstest 是检验模块,包括正态性检验
from scipy.stats import anderson #anderson 是修改版的 kstest，也可以做多种分布的检验，默认的检验时正态性检验
from scipy.stats import normaltest #normaltest 也是专门做正态性检验的模块
from scipy.stats import shapiro #专门用来做正态性检验的模块 

#定位工作路径（电脑桌面）
os.chdir(r"D:\Users\joe01.cooper\Desktop")

#读取RFM模型数据表（含拒退）
data = pd.read_csv('RFM_model_with_rejected_order.csv', header = 0)
data_analysis = data[['recency', 'frequency', 'monetary']]

#rvs：待检验的数据
#cdf：检验方法，这里我们设置为‘norm’，即正态性检验
#alternative：默认为双尾检验，可以设置为‘less’或‘greater’作单尾检验
#输出结果中第一个为统计数，第二个为P值
Normal_test1 = kstest(data_analysis['recency'], 'norm', alternative='two_sided')
print('kstest检验:\n', Normal_test1)

#anderson 有三个输出值，第一个为统计数，第二个为评判值，第三个为显著性水平，评判值与显著性水平对应 
#对于正态性检验，显著性水平为：15%, 10%, 5%, 2.5%, 1%
Normal_test2 = anderson(data_analysis['recency'], 'norm')
print('\nanderson检验:\n', Normal_test2)

#a：待检验的数据
#axis：默认为0，表示在0轴上检验，即对数据的每一行做正态性检验，我们可以设置为 axis=None 来对整个数据做检验
#nan_policy：当输入的数据中有空值时的处理办法。默认为 ‘propagate’，返回空值；设置为 ‘raise’ 时，抛出错误；设置为 ‘omit’ 时，在计算中忽略空值。
Normal_test3 = normaltest(data_analysis['recency'], axis=None)
print('\nnormaltest检验:\n', Normal_test3)

#shapiro 不适合做样本数＞5000的正态性检验，检验结果的P值可能不准确
Normal_test4 = shapiro(data_analysis['recency'])
print('\nshapiro检验:\n', Normal_test4)


#正态分布的偏度和峰度均为 0
#标准正态分布的偏度应该是0，峰度是3
u = data_analysis['recency'].mean()#均值
std = data_analysis['recency'].std()#标准差
var = data_analysis['recency'].var()#方差
skew = data_analysis['recency'].skew()#偏度
kurtosis = data_analysis['recency'].kurtosis()#峰度
print('均值：%s\n标准差：%s\n方差：%s\n偏度：%s\n峰度：%s\n'%(u,std,var,skew,kurtosis))
