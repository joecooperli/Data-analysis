# -*- coding: utf-8 -*-
"""
Created on Sat Jun 30 10:28:31 2018

@author: joe01.cooper
"""

# Python实现正态分布
# 绘制正态分布概率密度函数

import numpy as np
import matplotlib.pyplot as plt
import math

# 均值μ
u = 0   
u01 = -2
# 标准差δ
sig = math.sqrt(0.2)  
sig01 = math.sqrt(1)
sig02 = math.sqrt(5)
sig_u01 = math.sqrt(0.5)

# 对于正态分布随机变量，成立着所谓的‘3δ法则’，即x的取值落在区间（μ-3δ，μ+3δ）内的概率为0.9973.
# 亦即落在这个区间之外的概率不足0.3%，可以认为在一次试验中这是几乎不会发生的事
# x 取值范围
x = np.linspace(u - 3*sig, u + 3*sig, 50)
x_01 = np.linspace(u - 6 * sig, u + 6 * sig, 50)
x_02 = np.linspace(u - 10 * sig, u + 10 * sig, 50)
x_u01 = np.linspace(u - 10 * sig, u + 1 * sig, 50)

# y 概率密度函数
# 圆周率用math.pi表示
y_sig = np.exp(-(x - u) ** 2 /(2* sig **2))/(math.sqrt(2*math.pi)*sig)
y_sig01 = np.exp(-(x_01 - u) ** 2 /(2* sig01 **2))/(math.sqrt(2*math.pi)*sig01) # 标准正态分布
y_sig02 = np.exp(-(x_02 - u) ** 2 / (2 * sig02 ** 2)) / (math.sqrt(2 * math.pi) * sig02)
y_sig_u01 = np.exp(-(x_u01 - u01) ** 2 / (2 * sig_u01 ** 2)) / (math.sqrt(2 * math.pi) * sig_u01)

plt.plot(x, y_sig, "r-", linewidth=2) # "r-" 颜色设置：表示红色， linewidth 线宽
plt.plot(x_01, y_sig01, "g-", linewidth=2)
plt.plot(x_02, y_sig02, "b-", linewidth=2)
plt.plot(x_u01, y_sig_u01, "m-", linewidth=2)
# plt.plot(x, y, 'r-', x, y, 'go', linewidth=2,markersize=8)
# 显示网格线
plt.grid(True)
plt.show()