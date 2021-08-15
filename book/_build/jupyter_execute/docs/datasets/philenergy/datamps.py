#!/usr/bin/env python
# coding: utf-8

# # Market Prices and Schedules Data

# In[1]:


def concatenate_csv_local(file_dir, dest_dir, output_filename="output"):
    """
    Conatenates multiple hourly csv into one daily file. 
    """
    try:
        files = glob.glob(os.path.join(file_dir, "RTD_*.csv")) 
        
        date_columns = ['RUN_TIME','TIME_INTERVAL']
            
        df = pd.concat((pd.read_csv(f, header = 0, error_bad_lines=False, skipfooter=1, engine='python', parse_dates=date_columns) for f in files))
        df.drop(df.columns[df.columns.str.contains('unnamed',case = False)],axis = 1, inplace = True)
        for file in files:
            os.remove(file)
        df.to_csv(os.path.join(dest_dir, "RTD-{}.csv".format(output_filename)), index=False)
        print("Concatenate sucess: RTD-{}.csv".format(output_filename))
        
    except ValueError:
        print("File not found: {}".format(output_filename))


# In[ ]:





# In[ ]:




