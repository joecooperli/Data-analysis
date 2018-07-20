# -*- coding: utf-8 -*-
"""
Created on Mon Jul 16 20:22:04 2018

@author: joe01.cooper
"""

import pandas as pd
import numpy as np
import os
#聚类函数库
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import time

#定位工作路径（电脑桌面）
os.chdir(r"D:\Users\joe01.cooper\Desktop")

#读取RFM模型数据表（含拒退）
data = pd.read_csv('RFM_model_with_rejected_order.csv', header = 0)
#过滤掉离群值（monetary>50000）
new_data = data[data['monetary'] <= 50000]
new_data.to_csv('new_data.csv',index = False)
#延迟5秒再执行时间
time.sleep(5)
data = pd.read_csv('new_data.csv', header = 0)

#打散数据
data = data.reindex(np.random.permutation(data.index))
#取需要进行聚类的三个字段RFM
data_analysis = data[['recency', 'frequency', 'monetary']]

# 实现标准化变换 z-score标准化方法，均值为0，方差为1
data_Density = (data_analysis - data_analysis.mean(axis = 0))/(data_analysis.std(axis = 0))

#类簇的数量
k = 4
#聚类最大循环次数（迭代次数）
iteration = 500

#初始化质心
init_values = np.array([[-0.86109,3.118033,3.716422],#111 重要价值用户
[-0.86109,0.118033,0.716422],#110 潜力用户
[-0.86109,-0.68391,-0.82591],#100 新客（半年以内）
[1.672845,-0.68391,-0.62591]])#000 流失用户(采取措施尽力找回)

#对数据进行聚类;聚类函数KMeans()
#n_init: 设置选择质心种子次数，默认为10次。返回质心最好的一次结果（好是指计算时长短），若自定义聚类质心点，n_init需设为一次
#n_jobs 使用进程的数量，与电脑的CPU有关
#random_state 随机生成器的种子 ，和初始化中心有关
clf = KMeans(n_clusters = k,init = init_values, n_init = 1, max_iter = iteration, random_state= k) 
#拟合模型
clf = clf.fit(data_Density)

data_analysis['label']= clf.labels_

#统计各个类别的数目
r1 = data_analysis["label"].value_counts()
#找出聚类中心
r2 = pd.DataFrame(clf.cluster_centers_)
print(clf.cluster_centers_)
#横向连接（0是纵向），得到聚类中心对应的类别下的数目
r = pd.concat([r2, r1], axis = 1)
#重命名表头
r.columns = list(data_Density.columns) + [u'类别数目']
print(r)

 #详细输出每个样本对应的类别
data1 = pd.concat([data, pd.Series(clf.labels_, index = data.index)], axis = 1) 
 #重命名表头
data1.columns = list(data.columns) + [u'聚类类别']
print(data1)
#保存分类结果
data1.to_csv('RFM模型聚类分析03.csv', index = False) 
'''
color = ['b', 'y', 'r', 'g', 'b', 'y', 'r', 'g']
markers = ['^','x','o','*','+','1','2','3']

def scatter(data, color, markers):
    #存在三维数据，需要3D绘图
    ax = plt.subplot(111, projection='3d')
    #散点图
    ax.scatter(data.iloc[:,0], data.iloc[:,1], data.iloc[:,2], c=color, marker=markers)
    #给轴线设置标签
    ax.set_xlabel('recency')
    ax.set_ylabel('frequency')
    ax.set_zlabel('monetary')

#遍历4个类别的散点图
for i in range(k):
    print('分群%s的概率密度函数图：\n'%i)
    scatter(data_Density[data1[u'聚类类别']==i], color[i], markers[i])
    plt.savefig(u'3%s.png' %i, dpi = 500)
    plt.show()
'''