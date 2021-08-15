#!/usr/bin/env python
# coding: utf-8

# # Economic Dispatch

# In[1]:


import numpy as np
import pandas as pd
header = ['iteration','Inc_loss_1','Inc_loss_2','Penfac_1','Penfac_2','Plosses', 'Pdemand', 'Lambda', 'P1','P2']
values = []


# ## Iteration 1

# In[2]:


p1, p2 = [500, 500]
incloss1 = 0.0004*p1
incloss2 = 0.0002*p2
penfact1 = 1/(1-incloss1)
penfact2 = 1/(1-incloss2)
ploss = 0.0002*p1*p1 + 0.0001*p2*p2
pdemand = ploss + 1000
#solve kkt
A = np.array([[1, 1, 0], [0.05, 0, incloss1-1], [0, 0.04, incloss2-1]])
B = np.array([pdemand, -25, -11])
X = np.linalg.solve(A,B)
print(X)


# ## P2 max limit is hit, setting to Pmax1

# In[3]:


#Checking for lambda
11+0.04*800
# conditions met as Lambda at Pmax = 43 < 48


# ## Starting from iteration 2

# In[4]:


p1, p2 = [275, 800]
for i in range(8):
    incloss1 = 0.0004*p1
    incloss2 = 0.0002*p2
    penfact1 = 1/(1-incloss1)
    penfact2 = 1/(1-incloss2)
    ploss = 0.0002*p1*p1 + 0.0001*p2*p2
    pdemand = ploss + 1000
    #solve kkt
    A = np.array([[1, 1, 0], [0.05, 0, incloss1-1], [0, 0.04, incloss2-1]])
    B = np.array([pdemand, -25, -11])
    X = np.linalg.solve(A,B)
    #update power values
    p1, p2, lamb = X 
    #append to dict
    values.append([i+2,incloss1,incloss2,penfact1,penfact2,ploss,pdemand,lamb,p1,p2])
pd.DataFrame(values,columns=header)

