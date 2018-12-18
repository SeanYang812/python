#coding=gbk
import pandas as pd#Python Data Analysis Library �� pandas �ǻ���NumPy ��һ�ֹ��ߣ�
             #�ù�����Ϊ�˽�����ݷ�������������ġ�Pandas �����˴������һЩ��׼������ģ��
import numpy as np#NumPy ��һ�� Python ���� ������ ��Numeric Python���� 
                  #����һ���ɶ�ά�����������ڴ�����������̼�����ɵĿ⡣
import matplotlib.pyplot as plt
#Matplotlib ��һ�� Python �� 2D��ͼ�⣬���Ը���Ӳ������ʽ�Ϳ�ƽ̨�Ľ���ʽ�������ɳ������������ͼ��
#matplotlib.pyplot��һЩ�����з�����ļ��ϣ�ʹmatplotlib��������MATLAB�ķ�ʽ������ÿ��pyplot������һ��ͼƬ(figure)��һЩ�Ķ�
plt.rcParams['font.sans-serif'] = ['KaiTi']  # ��ʾ����
labels = np.array([u'����', u'�Լ�', u'�Ա�',u'΢��',u'����']) # ��ǩ
dataLenth = 5  # ���ݳ���
data_radar = np.array([20, 10, 20, 20,30]) # ��//��
angles = np.linspace(0, 2*np.pi, dataLenth, endpoint=False)  # �ָ�Բ�ܳ�
data_radar = np.concatenate((data_radar, [data_radar[0]]))  # �պ�
angles = np.concatenate((angles, [angles[0]]))  # �պ�
plt.polar(angles, data_radar, 'bo-', linewidth=1)  # ��������ϵ
plt.thetagrids(angles * 180/np.pi, labels)  # ����ǩ
plt.fill(angles, data_radar, facecolor='r', alpha=0.25)# ���
plt.ylim(0, 70)
plt.title(u'ʱ��ռ��')
plt.show()
