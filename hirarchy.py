# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 10:23:51 2020

@author: neshragh
"""


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


##################################################################

##open a dataset
df = pd.read_csv('week1_all.csv')
x = df.iloc[:, []].values

#import scipy.cluster.hierarchy as sch
#dengram = sch.dendrogram(sch.linkage(x, method= 'ward'))
#plt.title('Dendrogram')
#plt.xlabel('number of people')
#plt.ylabel('count')
#plt.show()

from sklearn.cluster import AgglomerativeClustering
hc = AgglomerativeClustering(n_clusters=3, affinity='euclidean', linkage='ward')
y_hc = hc.fit_predict(x)


plt.scatter(x[y_hc == 0,0], x[y_hc ==0,1], s =100, c= 'cyan', label ='1cluster')
plt.scatter(x[y_hc == 1,0], x[y_hc ==1,1], s =100, c= 'red', label ='2cluster')
plt.scatter(x[y_hc == 2,0], x[y_hc ==2,1], s =100, c= 'yellow', label ='3cluster')

plt.title('clusster of levels')
plt.xlabel('num of people')
plt.ylabel('NOT')
plt.legend()
plt.show()