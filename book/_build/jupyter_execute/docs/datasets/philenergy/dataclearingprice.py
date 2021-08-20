#!/usr/bin/env python
# coding: utf-8

# # Market Clearing Price Data

# {badge}`python3,badge-success` {badge}`exploratory data analysis,badge-secondary` {badge}`energy market,badge-warning` 

# **Market clearing price** is calculated every 5-min interval and is the intersection between the generation supply offers and the forecasted demand per region. If there is no line congestion between regions, then there will be only one market clearing price for the whole market. However, if there is line congestion, this results in market separation causing two clearing prices for each region.

# ## Imports

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
        files = glob.glob(os.path.join(file_dir, "MP_*.csv")) 
        
        date_columns = ['RUN_TIME']
            
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


dir = "/Volumes/data/projects/django-mms/data/market_clearing"


# ### Loading data

# In[5]:


concatenate_csv_local(dir,dir,"market-clearing-price")
filename = os.path.join(dir, "Combined-market-clearing-price" + "." + "csv")
df = pd.read_csv(filename)


# ## Data wrangling
# 
# Dataset consists of 5-min market clearing prices from July 26, 2021, start of the 5-Min market up to Aug 14. 'RESOURCE_NAME' indicates the clearing plant.

# In[6]:


df.head().style.set_table_styles(styles)


# In[7]:


df.tail().style.set_table_styles(styles)


# ### Removing CMIN since it is a separate market
# For now only Luzon and Visayas grids are connected

# In[8]:


df = df[df["REGION_NAME"] != "CMIN"]


# CLUZ and CVIZ markets not equal in length. During congestion, CVIS goes to market separation and clears its own price 

# In[9]:


df.groupby(df['REGION_NAME']).count().style.set_table_styles(styles)


# ### Create new dataframe for mean clearing price

# In[10]:


df_price = df.groupby(df['RUN_TIME']).mean()

# Resetting the index
df_price = df_price.reset_index()

# Removing AM/PM from RUN_TIME
df_price['RUN_TIME'] = df_price['RUN_TIME'].str.replace(r'[^\W\d_]', '')

# Setting RUN_TIME to datetime
df_price['RUN_TIME'] = pd.to_datetime(df_price['RUN_TIME'])

# Setting RUN_TIME as sorted index
df_price = df_price.set_index('RUN_TIME')

df_price = df_price.sort_index()


# In[11]:


df_price.head().style.set_table_styles(styles)


# ### Resampling time series for plotting

# In[12]:


df_price_hr = df_price.resample('1H').mean()
df_price_day = df_price.resample('1D').mean()
df_price_7d = df_price.rolling('7D').mean()


# ## Plotting

# In[13]:


import matplotlib.pyplot as plt

start, end = '2021-06-26', '2021-07-14'

fig, ax = plt.subplots(figsize=(25,15))

ax.plot(df_price_hr.loc[start:end, 'MARGINAL_PRICE'], marker='.', linestyle='-', linewidth=0.5, label='5-Min')
ax.plot(df_price_day.loc[start:end, 'MARGINAL_PRICE'], marker='o', markersize=5, linestyle='-', label = 'Daily mean price')
ax.plot(df_price_7d.loc[start:end, 'MARGINAL_PRICE'], marker='.', linestyle='-', label='7d Rolling Average price')
ax.set_ylabel('Marginal Price')

ax.legend()


# In[14]:


# #import calendar
# #all_month_year_df = pd.pivot_table(df_price, values="MARGINAL_PRICE",
# #                                   index=["RUN_TIME"],
# #                                   columns=["RUN_TIME"],
# #                                   fill_value=0,
# #                                   margins=True)
# named_index = [[calendar.month_abbr[i] if isinstance(i, int) else i for i in list(all_month_year_df.index)]] # name months
# all_month_year_df = all_month_year_df.set_index(named_index)
# all_month_year_df


# In[ ]:




