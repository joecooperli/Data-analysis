# -*- coding: utf-8 -*-
"""
Created on Fri Jun 29 10:27:34 2018

@author: joe01.cooper
"""

#编写数学函数进行相关系数的计算

import pandas as pd
import os
# 用来计算标准差（需要开根）
import math

# 定位工作路径
os.chdir(r"D:\Users\joe01.cooper\Desktop")
# 读取excel数据
data = pd.read_excel('detail_page.xlsx', header = 0)

# data1点击收藏pv，data2点击加购pv
data1 = data['like_sku_click_pv']
data2 = data['add_cart_pv']

# 期望（平均值）：针对离散随机变量的公式计算
def mean(x):
  return sum(x) / len(x)

# 计算每一项数据与均值的差
def de_mean(x):
  x_bar = mean(x)
  return [x_i - x_bar for x_i in x]

# 辅助计算函数 dot product 、sum_of_squares
def dot(v, w):
  return sum(v_i * w_i for v_i, w_i in zip(v, w)) # 数据与均值差的平方和
def sum_of_squares(v):
  return dot(v, v) #为该值的平方做准备：v * v

# 方差：针对离散随机变量的公式计算
def variance(x):
  n = len(x)
  deviations = de_mean(x)
  return sum_of_squares(deviations) / (n - 1) # 实际上，我们计算样本方差的时候一般会使用 n-1(分母)

# 标准差
def standard_deviation(x):
  return math.sqrt(variance(x))

# 协方差
def covariance(x, y):
  n = len(x)
  return dot(de_mean(x), de_mean(y)) / (n -1)

# 相关系数：由协方差除以两个变量的标准差而得，
# 相关系数的取值会在 [-1, 1] 之间，-1 表示完全负相关，1 表示完全相关，例如 0.18 则为弱正相关
def correlation(x, y):
  stdev_x = standard_deviation(x)
  stdev_y = standard_deviation(y)
  if stdev_x > 0 and stdev_y > 0:
    return covariance(x, y) / stdev_x / stdev_y
  else:
    return 0

# 计算 data1 和 data2 两组数据的相关系数
corr = correlation(data1, data2)
print('用户点击收藏行为与加购行为的相关系数：')
print(corr)

# 判断data1 和 data2 两组数据的相关程度（或者 <0.4显著弱相关; 0.4-0.75中等相关; 大于0.75强相关）
if corr == 1.0:
    print("相关性程度：\n'完全正相关'")
elif corr > 0.8 and corr < 1.0:
    print("相关性程度：\n'极强正相关'")
elif corr > 0.6 and corr <= 0.8:
    print("相关性程度：\n'强正相关'")
elif corr > 0.4 and corr <= 0.6:
    print("相关性程度：\n'中等程度正相关'")
elif corr > 0.2 and corr <= 0.4:
    print("相关性程度：\n'弱正相关'")
elif corr > 0 and corr <= 0.2:
    print("相关性程度：\n'极弱正相关'")
elif corr == 0:
    print("相关性程度：\n'无相关'")
elif corr >= -0.2 and corr < 0:
    print("相关性程度：\n'极弱负相关'")
elif corr >= -0.4 and corr < -0.2:
    print("相关性程度：\n'弱负相关'")
elif corr >= -0.6 and corr < -0.4:
    print("相关性程度：\n'中等程度负相关'")
elif corr >= -0.8 and corr < -0.6:
    print("相关性程度：\n'强负相关'")
elif corr > -1.0 and corr < -0.8:
    print("相关性程度：\n'极强负相关'")
else:
    print("相关性程度：\n'完全负相关'")




