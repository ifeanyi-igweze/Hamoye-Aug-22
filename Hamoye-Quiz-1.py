#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np


# In[25]:


df = pd.read_csv('FoodBalanceSheets_E_Africa_NOFLAG.csv')


# In[3]:


df.columns


# In[6]:


# No. 11

df.groupby('Item')[['Y2014', 'Y2017']].sum()


# In[7]:


# No. 12

df.Y2015.describe()


# In[10]:


# No. 13

df.shape


# In[24]:


print(df.Y2016.isnull().sum())
print(round(((df.Y2016.isnull().sum() / df.shape[0]) * 100), 2))


# In[28]:


# No. 14

df.plot(y='Element Code', x='Y2014', kind='scatter');

df.plot(y='Element Code', x='Y2015', kind='scatter');

df.plot(y='Element Code', x='Y2016', kind='scatter');

df.plot(y='Element Code', x='Y2017', kind='scatter');

df.plot(y='Element Code', x='Y2018', kind='scatter');


# In[32]:


# No. 15

df.query('Element == "Import Quantity"')[['Y2014','Y2015','Y2016','Y2017','Y2018']].sum()


# In[35]:


# No. 16

df.query('Element == "Production"')['Y2014'].sum()


# In[38]:


# No. 17 & 18

df.groupby('Element')['Y2018'].sum()


# In[40]:


# No. 19

df.query('Area == "Algeria" and Element == "Import Quantity"')['Y2018'].sum()


# In[41]:


# No. 20

df.Area.nunique()

