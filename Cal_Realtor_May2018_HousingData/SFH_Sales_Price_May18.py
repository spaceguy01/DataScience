
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')


# In[2]:


file = '2018MayHousingSales.xlsx'


# In[3]:


df = pd.read_excel(file)
dfSFBay = df.iloc[11:21]
dfSFBay.columns = dfSFBay.iloc[0]
dfSFBay


# In[4]:


dfSFBay= dfSFBay.dropna(axis=1)
dfSFBay= dfSFBay.drop(dfSFBay.index[0])
dfSFBay.columns = 'SF Bay County','May-18($)','Apr-18($)','May-17($)','Price MTM % Chg','Price YTY % Chg','May-18(#)','Apr-18(#)','May-17(#)','Sales MTM % Chg','Sales YTY % Chg' 


# In[5]:


dfSFBay[['Price MTM % Chg', 'Price YTY % Chg','Sales MTM % Chg', 'Sales YTY % Chg']] = dfSFBay[['Price MTM % Chg', 'Price YTY % Chg','Sales MTM % Chg', 'Sales YTY % Chg']].applymap("{0:.2f}".format)


# In[6]:


dfSFBay


# In[7]:


dfSFBay.index = np.arange(1, len(dfSFBay)+1)


# In[8]:


dfSFBay['Price MTM % Chg'] = pd.to_numeric(dfSFBay['Price MTM % Chg'])
dfSFBay['Price YTY % Chg'] = pd.to_numeric(dfSFBay['Price YTY % Chg'])
dfSFBay['Sales MTM % Chg'] = pd.to_numeric(dfSFBay['Sales MTM % Chg'])
dfSFBay['Sales YTY % Chg'] = pd.to_numeric(dfSFBay['Sales YTY % Chg'])

dfSFBay.loc[:,'Price MTM % Chg'] = dfSFBay['Price MTM % Chg'] * 100
dfSFBay.loc[:,'Price YTY % Chg'] = dfSFBay['Price YTY % Chg'] * 100
dfSFBay.loc[:,'Sales MTM % Chg'] = dfSFBay['Sales MTM % Chg'] * 100
dfSFBay.loc[:,'Sales YTY % Chg'] = dfSFBay['Sales YTY % Chg'] * 100


# In[9]:


mediansoldprice = dfSFBay.loc[:,:'Price YTY % Chg']


# In[10]:


mediansoldsales = dfSFBay.loc[:,'May-18(#)':'Sales YTY % Chg']


# In[11]:


sfheader = {'Median Sold Price ($) of Existing Single Family Homes':mediansoldprice, 'Number (#) of Existing Single Family Homes Sales':mediansoldsales}


# In[12]:


SFcategory = pd.concat(sfheader.values(), axis=1, keys=sfheader.keys())


# In[13]:


SFcategory


# ****SF BAY AREA : Year to Year Median Sold Price of Existing Single Family Homes (May-2017 / May-2018)****

# In[14]:


May17Price = dfSFBay.loc[:,['SF Bay County','May-17($)']]
May18Price = dfSFBay.loc[:,['SF Bay County','May-18($)']]
YTYPriceDiff = pd.merge(May17Price,May18Price, how='inner',on=['SF Bay County']).set_index('SF Bay County').plot.bar(figsize=(13,6),cmap='Paired')
plt.title('Year to Year Median Sold Price of Existing Single Family Homes (May-2017 / May-2018)')
plt.ylabel('Median Sold Price ($)')
plt.xlabel('SF Bay Area County')
plt.xticks(rotation='horizontal')


# ***SF BAY AREA : Year to Year Price Change % in Existing Single Family Homes (May-2017 / May-2018)***

# In[15]:


dfSFBay[['Price YTY % Chg']] = dfSFBay[['Price YTY % Chg']].astype(float)
fig = plt.figure(figsize=(13,6))
sns.barplot(x='SF Bay County',y='Price YTY % Chg', data=dfSFBay,palette="RdBu_r")
plt.title('Year to Year Price Change Percentage (%) in Existing Single Family Homes (May-2017 / May-2018)')
plt.ylabel('YTY Price Change Percentage (%)')
plt.xlabel('SF Bay Area County')


# ***SF BAY AREA : Month to Month Median Sold Price of Existing Single Family Homes (Apr-2018 / May-2018)***

# In[16]:


Apr18Price = dfSFBay.loc[:,['SF Bay County','Apr-18($)']]
May18Price = dfSFBay.loc[:,['SF Bay County','May-18($)']]
MTMPriceDiff = pd.merge(Apr18Price,May18Price, how='inner',on=['SF Bay County']).set_index('SF Bay County').plot.bar(figsize=(13,6),cmap='Accent')
plt.ylabel('Median Sold Price ($)')
plt.title('Month to Month Median Sold Price of Existing Single Family Homes (Apr-2018 / May-2018)')
plt.xlabel('SF Bay Area County')
plt.xticks(rotation='horizontal')


# ***SF BAY AREA : Month to Month Median Sold Price % Change in Existing Single Family Homes (Apr-2018 / May-2018)***

# In[17]:


dfSFBay[['Price MTM % Chg']] = dfSFBay[['Price MTM % Chg']].astype(float)
fig = plt.figure(figsize=(13,6))
sns.barplot(x='SF Bay County',y='Price MTM % Chg', data=dfSFBay,palette="RdBu_r")
plt.ylabel('MTM Price % Change')
plt.title('Month to Month Median Sold Price Change Percentage (%) of Existing Single Family Homes (Apr-2018 / May-2018)')
plt.xlabel('SF Bay Area County')


# ***SF BAY AREA : Year to Year Number of Existing Single Family Homes Sales (Apr-2018 / May-2018)***

# In[18]:


May17Sales = dfSFBay.loc[:,['SF Bay County','May-17(#)']]
May18Sales = dfSFBay.loc[:,['SF Bay County','May-18(#)']]
YTYSalesDiff = pd.merge(May17Sales,May18Sales, how='inner',on=['SF Bay County']).set_index('SF Bay County').plot.bar(figsize=(13,6),cmap='Paired')
plt.title('Year to Year Number of Existing Single Family Homes Sales (May-2017 / May-2018)')
plt.ylabel('Number of Existing Home Sales')
plt.xlabel('SF Bay Area County')
plt.xticks(rotation='horizontal')


# ***SF BAY AREA : Year to Year % Change in Number of Existing Single Family Homes Sales (Apr-2018 / May-2018)***

# In[19]:


dfSFBay[['Sales YTY % Chg']] = dfSFBay[['Sales YTY % Chg']].astype(float)
fig = plt.figure(figsize=(13,6))
sns.barplot(x='SF Bay County',y='Sales YTY % Chg', data=dfSFBay,palette="RdBu_r")
plt.title('Year to Year Percentage (%) Change in Number of Existing Single Family Homes Sales (May-2017 / May-2018)')
plt.ylabel('YTY Number of Sales % Change')
plt.xlabel('SF Bay Area County')


# ***SF BAY AREA : Month to Month Number of Existing Single Family Homes Sales (Apr-2018 / May-2018)***

# In[20]:


Apr18Sales = dfSFBay.loc[:,['SF Bay County','Apr-18(#)']]
May18Sales = dfSFBay.loc[:,['SF Bay County','May-18(#)']]
MTMSalesDiff = pd.merge(Apr18Price,May18Price, how='inner',on=['SF Bay County']).set_index('SF Bay County').plot.bar(figsize=(12,6),cmap='Accent')
plt.ylabel('Number of Existing Home Sales')
plt.title('Month to Month Number of Existing Single Family Homes Sales (Apr-2018 / May-2018)')
plt.xlabel('SF Bay Area County')
plt.xticks(rotation='horizontal')


# ***SF BAY AREA : Month to Month % Change in Number of Existing Single Family Homes Sales (Apr-2018 / May-2018)***

# In[21]:


dfSFBay[['Sales MTM % Chg']] = dfSFBay[['Sales MTM % Chg']].astype(float)
fig = plt.figure(figsize=(13,6))
MTMperc = sns.barplot(x='SF Bay County',y='Sales MTM % Chg', data=dfSFBay,palette="RdBu_r")
plt.title('Month to Month Percentage (%) Change in Number of Existing Single Family Homes Sales (Apr-2018 / May-2018)')
plt.ylabel('MTM Number of Sales % Change')
plt.xlabel('SF Bay Area County')


# ****SOUTHERN CALIFORNIA DATA****

# ***Setting up the Pandas DataFrame***

# In[22]:


dfSoCal = df.iloc[21:27]
dfSoCal


# In[23]:


dfSoCal= dfSoCal.dropna(axis=1)
dfSoCal= dfSoCal.drop(dfSoCal.index[0])
dfSoCal.columns = 'SoCal Counties','May-18($)','Apr-18($)','May-17($)','Price MTM % Chg','Price YTY % Chg','May-18(#)','Apr-18(#)','May-17(#)','Sales MTM % Chg','Sales YTY % Chg' 
dfSoCal[['Price MTM % Chg', 'Price YTY % Chg','Sales MTM % Chg', 'Sales YTY % Chg']] = dfSoCal[['Price MTM % Chg', 'Price YTY % Chg','Sales MTM % Chg', 'Sales YTY % Chg']].applymap("{0:.2f}".format)
dfSoCal.index = np.arange(1, len(dfSoCal)+1)


# In[24]:


dfSoCal['Price MTM % Chg'] = pd.to_numeric(dfSoCal['Price MTM % Chg'])
dfSoCal['Price YTY % Chg'] = pd.to_numeric(dfSoCal['Price YTY % Chg'])
dfSoCal['Sales MTM % Chg'] = pd.to_numeric(dfSoCal['Sales MTM % Chg'])
dfSoCal['Sales YTY % Chg'] = pd.to_numeric(dfSoCal['Sales YTY % Chg'])

dfSoCal.loc[:,'Price MTM % Chg'] = dfSoCal['Price MTM % Chg'] * 100
dfSoCal.loc[:,'Price YTY % Chg'] = dfSoCal['Price YTY % Chg'] * 100
dfSoCal.loc[:,'Sales MTM % Chg'] = dfSoCal['Sales MTM % Chg'] * 100
dfSoCal.loc[:,'Sales YTY % Chg'] = dfSoCal['Sales YTY % Chg'] * 100
dfSoCal


# In[25]:


mediansoldprice = dfSoCal.loc[:,:'Price YTY % Chg']
mediansoldsales = dfSoCal.loc[:,'May-18(#)':'Sales YTY % Chg']
socalheader = {'Median Sold Price ($) of Existing Single Family Homes':mediansoldprice, 'Number (#) of Existing Single Family Homes Sales':mediansoldsales}
socalcategory = pd.concat(socalheader.values(), axis=1, keys=socalheader.keys())
socalcategory


# ****Southern California : Year to Year Median Sold Price of Existing Single Family Homes (May-2017 / May-2018)****

# In[26]:


May17Price = dfSoCal.loc[:,['SoCal Counties','May-17($)']]
May18Price = dfSoCal.loc[:,['SoCal Counties','May-18($)']]
YTYPriceDiff = pd.merge(May17Price,May18Price, how='inner',on=['SoCal Counties']).set_index('SoCal Counties').plot.bar(figsize=(13,6),cmap='Paired')
plt.title('Year to Year Median Sold Price of Existing Single Family Homes (May-2017 / May-2018)')
plt.ylabel('Median Sold Price ($)')
plt.xlabel('SoCal Counties')
plt.xticks(rotation='horizontal')


# ***Southern California : Year to Year Price Change % in Existing Single Family Homes (May-2017 / May-2018)***

# In[27]:


dfSoCal[['Price YTY % Chg']] = dfSoCal[['Price YTY % Chg']].astype(float)
fig = plt.figure(figsize=(13,6))
sns.barplot(x='SoCal Counties',y='Price YTY % Chg', data=dfSoCal,palette="RdBu_r")
plt.title('Year to Year Price Change Percentage (%) in Existing Single Family Homes (May-2017 / May-2018)')
plt.ylabel('YTY Price Change Percentage (%)')
plt.xlabel('SoCal Counties')


# ***Southern California : Month to Month Median Sold Price of Existing Single Family Homes (Apr-2018 / May-2018)***

# In[28]:


Apr18Price = dfSoCal.loc[:,['SoCal Counties','Apr-18($)']]
May18Price = dfSoCal.loc[:,['SoCal Counties','May-18($)']]
MTMPriceDiff = pd.merge(Apr18Price,May18Price, how='inner',on=['SoCal Counties']).set_index('SoCal Counties').plot.bar(figsize=(13,6),cmap='Accent')
plt.ylabel('Median Sold Price ($)')
plt.title('Month to Month Median Sold Price of Existing Single Family Homes (Apr-2018 / May-2018)')
plt.xlabel('SoCal Counties')
plt.xticks(rotation='horizontal')


# ***Southern California : Month to Month Median Sold Price % Change in Existing Single Family Homes (Apr-2018 / May-2018)***

# In[29]:


dfSoCal[['Price MTM % Chg']] = dfSoCal[['Price MTM % Chg']].astype(float)
fig = plt.figure(figsize=(13,6))
sns.barplot(x='SoCal Counties',y='Price MTM % Chg', data=dfSoCal,palette="RdBu_r")
plt.ylabel('MTM Price % Change')
plt.title('Month to Month Median Sold Price Change Percentage (%) of Existing Single Family Homes (Apr-2018 / May-2018)')
plt.xlabel('SoCal Counties')


# ***Southern California : Year to Year Number of Existing Single Family Homes Sales (Apr-2018 / May-2018)***

# In[30]:


May17Sales = dfSoCal.loc[:,['SoCal Counties','May-17(#)']]
May18Sales = dfSoCal.loc[:,['SoCal Counties','May-18(#)']]
YTYSalesDiff = pd.merge(May17Sales,May18Sales, how='inner',on=['SoCal Counties']).set_index('SoCal Counties').plot.bar(figsize=(13,6),cmap='Paired')
plt.title('Year to Year Number of Existing Single Family Homes Sales (May-2017 / May-2018)')
plt.ylabel('Number of Existing Home Sales')
plt.xlabel('SoCal Counties')
plt.xticks(rotation='horizontal')


# ***Southern California : Year to Year % Change in Number of Existing Single Family Homes Sales (Apr-2018 / May-2018)***

# In[31]:


dfSoCal[['Sales YTY % Chg']] = dfSoCal[['Sales YTY % Chg']].astype(float)
fig = plt.figure(figsize=(13,6))
sns.barplot(x='SoCal Counties',y='Sales YTY % Chg', data=dfSoCal,palette="RdBu_r")
plt.title('Year to Year Percentage (%) Change in Number of Existing Single Family Homes Sales (May-2017 / May-2018)')
plt.ylabel('YTY Number of Sales % Change')
plt.xlabel('SoCal Counties')


# ***Southern California : Month to Month Number of Existing Single Family Homes Sales (Apr-2018 / May-2018)***

# In[32]:


Apr18Sales = dfSoCal.loc[:,['SoCal Counties','Apr-18(#)']]
May18Sales = dfSoCal.loc[:,['SoCal Counties','May-18(#)']]
MTMSalesDiff = pd.merge(Apr18Price,May18Price, how='inner',on=['SoCal Counties']).set_index('SoCal Counties').plot.bar(figsize=(12,6),cmap='Accent')
plt.ylabel('Number of Existing Home Sales')
plt.title('Month to Month Number of Existing Single Family Homes Sales (Apr-2018 / May-2018)')
plt.xlabel('SoCal Counties')
plt.xticks(rotation='horizontal')


# ***Southern California : Month to Month % Change in Number of Existing Single Family Homes Sales (Apr-2018 / May-2018)***

# In[33]:


dfSoCal[['Sales MTM % Chg']] = dfSoCal[['Sales MTM % Chg']].astype(float)
fig = plt.figure(figsize=(13,4))
MTMperc = sns.barplot(x='SoCal Counties',y='Sales MTM % Chg', data=dfSoCal,palette="RdBu_r")
plt.title('Month to Month Percentage (%) Change in Number of Existing Single Family Homes Sales (Apr-2018 / May-2018)')
plt.ylabel('MTM Number of Sales % Change')
plt.xlabel('SoCal Counties')

