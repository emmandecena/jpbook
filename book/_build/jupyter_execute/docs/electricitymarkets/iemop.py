#!/usr/bin/env python
# coding: utf-8

# # IEMOP data exporation

# In[1]:


# Libraries
import pandas as pd
import numpy as np


# In[2]:


#import os
#os.system("""awk '(NR == 1) || !/^EOF/ && (FNR > 1)' /Volumes/data/projects/django-mms/tempdata/20210704/RTD*.csv > /Volumes/data/projects/django-mms/tempdata/20210704/bigfile.csv""")


# In[2]:


fname = "/Volumes/data/projects/django-mms/tempdata/RTD-2021-07-13.csv"


# In[11]:


date_columns = ['RUN_TIME','TIME_INTERVAL']
df = pd.read_csv(fname, parse_dates=date_columns)


# In[12]:


df.dtypes


# In[14]:


df


# In[5]:


df.to_json ("/Volumes/data/projects/django-mms/tempdata/20210704/bigfile.json")


# In[5]:


df.groupby(['REGION_NAME']).count()


# In[6]:


df.groupby(['RESOURCE_NAME']).count()


# In[10]:


df[df['REGION_NAME']=='CVIS'].groupby(['RESOURCE_NAME']).count()


# In[13]:


import seaborn as sns


# In[24]:



PLANTS = ['05CEDC_U01', '05CEDC_U02', '05CEDC_U03']

df[df['RESOURCE_NAME'].isin(PLANTS)]


# In[30]:


df.groupby(['RUN_TIME', 'REGION_NAME']).mean().reset_index()


# In[36]:


from matplotlib import pyplot
dims = (25, 10)


# In[37]:


fig, ax = pyplot.subplots(figsize=dims)
sns.lineplot(data=df.groupby(['RUN_TIME', 'REGION_NAME']).mean().reset_index(), x="RUN_TIME", y="LMP", hue="REGION_NAME")


# In[ ]:




