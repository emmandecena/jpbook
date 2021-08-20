#!/usr/bin/env python
# coding: utf-8

# # Regional Electricity Demand Data

# {badge}`python3,badge-success` {badge}`exploratory data analysis,badge-secondary` {badge}`energy market,badge-warning` 

# This post explores the 5-min regional electricity demand data from the Electricity Market of the Philippines.

# ## Setup

# ### Libraries

# In[1]:


import glob
import pandas as pd
import os


# ### Functions

# In[2]:


def concatenate_csv_local(file_dir, dest_dir, output_filename="output"):
    """
    Conatenates multiple hourly csv into one daily file. 
    """
    try:
        files = glob.glob(os.path.join(file_dir, "RTDREG_*.csv")) 
        
        date_columns = ['RUN_TIME','TIME_INTERVAL']
            
        df = pd.concat((pd.read_csv(f, header = 0, error_bad_lines=False, skipfooter=1, engine='python', parse_dates=date_columns) for f in files))
        df.drop(df.columns[df.columns.str.contains('unnamed',case = False)],axis = 1, inplace = True)
        df.to_csv(os.path.join(dest_dir, "Combined-{}.csv".format(output_filename)), index=False)
        print("Concatenate sucess: RTD-{}.csv".format(output_filename))
        
    except ValueError:
        print("File not found: {}".format(output_filename))


# ### DataFrame html format

# In[3]:


t_props = [
  ('font-size', '80%')
  ]
   
styles = [
  dict(selector="th", props=t_props),
  dict(selector="td", props=t_props)
  ]


# ### Paths

# In[4]:


dir = "/Volumes/data/projects/django-mms/data/demand_daily"


# ## The Regional Electricity Demand Dataset
# 
# This post uses regional electricity demand time series dataset from the Independent Electricity Market Operator of the Philippines (www.iemop.ph). 
# 
# The dataset contains several features such as 'Time Interval', 'Market Type', 'Region Name', 'Commodity Type', 'Market Requirment', 'Generation' and 'Losses' among others.
# 
# For simplicity we will only consider the following: 'Time Interval', 'Region Name' with corresponds to the three major subgrids, and 'Market Requirment' with is the electricity demand required for the current interval.

# ### Loading

# In[5]:


concatenate_csv_local(dir,dir,"regional-demand")


# In[44]:


filename = os.path.join(dir, "Combined-regional-demand" + "." + "csv")
df = pd.read_csv(filename)


# ### Inspection and Cleanup
# 

# In[45]:


df.head().style.set_table_styles(styles)


# In[46]:


df.describe().style.set_table_styles(styles)


# In[47]:


df.isnull().sum()


# In[48]:


df = df.fillna(0)


# ### Commodity Type
# 
# The commodity type refers to either energy or to the type of ancilliary service reserve. For this post we will only consider the 'En' commodity.

# In[49]:


df['COMMODITY_TYPE'].unique()


# ### Data cleanup
# 
# Need to do per region to give unique index

# In[50]:


# Removing AM/PM from RUN_TIME
df['TIME_INTERVAL'] = df['TIME_INTERVAL'].str.replace(r'[^\W\d_]', '')

# Setting RUN_TIME to datetime
df['TIME_INTERVAL'] = pd.to_datetime(df['TIME_INTERVAL'])


# ### Create separate dataframe for each region and En commodity type
# 
# So that we can use unique datetime index

# In[51]:


df_luz = df[df['REGION_NAME']=='CLUZ'].copy()
df_min = df[df['REGION_NAME']=='CMIN'].copy()
df_vis = df[df['REGION_NAME']=='CVIS'].copy()


# ### Data cleanup and indexing
# 
# Need to do per region to give unique index

# In[52]:


# Setting RUN_TIME as sorted index
df_luz = df_luz.set_index('TIME_INTERVAL')
df_luz = df_luz.sort_index()

df_vis = df_vis.set_index('TIME_INTERVAL')
df_vis = df_vis.sort_index()

df_min = df_min.set_index('TIME_INTERVAL')
df_min = df_min.sort_index()


# ### Resampling

# In[53]:


df_luz_hr = df_luz[df_luz['COMMODITY_TYPE']=='En'].resample('1H').mean()
df_luz_day = df_luz[df_luz['COMMODITY_TYPE']=='En'].resample('1D').mean()

df_vis_hr = df_vis[df_vis['COMMODITY_TYPE']=='En'].resample('1H').mean()
df_vis_day = df_vis[df_vis['COMMODITY_TYPE']=='En'].resample('1D').mean()

df_min_hr = df_min[df_min['COMMODITY_TYPE']=='En'].resample('1H').mean()
df_min_day = df_min[df_min['COMMODITY_TYPE']=='En'].resample('1D').mean()


# ### Data cleanup and indexing
# 
# Need to do per region to give unique index

# # Plotting

# ### Stacked plot
# 
# Luzon takes up majority of the demand

# In[90]:


fig, ax = plt.subplots(figsize=(25,15))
plt.stackplot(df_min_hr.index, df_min_hr.MKT_REQT, df_vis_hr.MKT_REQT, df_luz_hr.MKT_REQT, labels=['Mindanao','Visayas','Luzon'])
plt.legend(loc='upper left')
fig.suptitle(f'Electricity Demand from {start} to {end}', size=20)


# In[84]:


df_luz_hr.index


# ### Series plot

# In[91]:


import matplotlib.pyplot as plt

start, end = '2021-06-26', '2021-07-14'

fig, ax = plt.subplots(3,1, figsize=(25,15))

ax[0].plot(df_luz_hr.loc[start:end, 'MKT_REQT'], marker='.', linestyle='-', linewidth=0.5, label='5-Min')
ax[0].plot(df_luz_day.loc[start:end, 'MKT_REQT'], marker='o', markersize=5, linestyle='-', label = 'Daily mean price')
ax[0].set_title('Luzon')

ax[1].plot(df_vis_hr.loc[start:end, 'MKT_REQT'], marker='.', linestyle='-', linewidth=0.5, label='5-Min')
ax[1].plot(df_vis_day.loc[start:end, 'MKT_REQT'], marker='o', markersize=5, linestyle='-', label = 'Daily mean price')
ax[1].set_title('Visayas')

ax[2].plot(df_min_hr.loc[start:end, 'MKT_REQT'], marker='.', linestyle='-', linewidth=0.5, label='5-Min')
ax[2].plot(df_min_day.loc[start:end, 'MKT_REQT'], marker='o', markersize=5, linestyle='-', label = 'Daily mean price')
ax[2].set_title('Mindanao')


ax[0].set_ylabel('Market Requirement')
fig.suptitle(f'Electricity Demand from {start} to {end}', size=20)

ax[0].legend()

