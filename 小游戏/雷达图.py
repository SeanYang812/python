#coding=gbk
import pandas as pd#Python Data Analysis Library 或 pandas 是基于NumPy 的一种工具，
             #该工具是为了解决数据分析任务而创建的。Pandas 纳入了大量库和一些标准的数据模型
import numpy as np#NumPy 是一个 Python 包。 它代表 “Numeric Python”。 
                  #它是一个由多维数组对象和用于处理数组的例程集合组成的库。
import matplotlib.pyplot as plt
#Matplotlib 是一个 Python 的 2D绘图库，它以各种硬拷贝格式和跨平台的交互式环境生成出版质量级别的图形
#matplotlib.pyplot是一些命令行风格函数的集合，使matplotlib以类似于MATLAB的方式工作。每个pyplot函数对一幅图片(figure)做一些改动
plt.rcParams['font.sans-serif'] = ['KaiTi']  # 显示中文
labels = np.array([u'唱歌', u'吃鸡', u'淘宝',u'微信',u'抖音']) # 标签
dataLenth = 5  # 数据长度
data_radar = np.array([20, 10, 20, 20,30]) # 数//据
angles = np.linspace(0, 2*np.pi, dataLenth, endpoint=False)  # 分割圆周长
data_radar = np.concatenate((data_radar, [data_radar[0]]))  # 闭合
angles = np.concatenate((angles, [angles[0]]))  # 闭合
plt.polar(angles, data_radar, 'bo-', linewidth=1)  # 做极坐标系
plt.thetagrids(angles * 180/np.pi, labels)  # 做标签
plt.fill(angles, data_radar, facecolor='r', alpha=0.25)# 填充
plt.ylim(0, 70)
plt.title(u'时间占比')
plt.show()
