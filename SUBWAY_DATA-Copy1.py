#!/usr/bin/env python
# coding: utf-8

# In[7]:


import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt


# This program is made to visualize the amount of subway entrances 
# for each train line in new york city. 
# Dataset retrieved courtesy of NYC Open Data


# read data using pandas
df=pd.read_csv('DOITT_SUBWAY_ENTRANCE_01_13SEPT2010.csv')

# separate elements in LINE column into separate rows
df['LINE']=df['LINE'].str.split('-')
df=df.explode('LINE')
#print(df.head())

# fixing typo
df['LINE'] = df['LINE'].str.replace('e', 'E')

# series of counts
print(df['LINE'].value_counts())



# storing value count of entrances to a dictionary
counts = df['LINE'].value_counts().to_dict()


# Testing dictionary
print(counts['G'])

# input results into graphs 
matplotlib.style.use('fivethirtyeight')
ax=df.LINE.value_counts().plot.bar(x="LINE", y='counts', rot=0, figsize=(20, 8))
plt.title('Number of Subway Entrances per Train Line', fontsize=20)
plt.xlabel("Train Line")
plt.ylabel("Number of Entrances")



# In[2]:


#Now make a pie chart

df2 = df.value_counts('LINE')


colors=['lightblue','lightsteelblue','silver']
explode=(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.1,0.1,0.5,0.7,0.9,1)
ax=df2.plot.pie(explode=explode, figsize=(10,10),startangle=15, shadow=True, 
                                   colors=colors,pctdistance=0.8)
plt.title('Number of Entrances per Line', color='black', size=18)


plt.show()


# In[ ]:





# In[3]:


counts = df['LINE'].value_counts().to_dict()

# Get the keys from dictionary and store them in a list
labels = list(counts.keys())

# Get the values from dictionary and store them in a list
values = list(counts.values())

# Make pie chart bigger
plt.figure(figsize=(8,10))

# plot another pie chart with percents
plt.pie(values, labels=labels, explode=explode, startangle=15, shadow=True, 
                                   autopct='%1.1f%%',pctdistance=0.8)
explode=(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.1,0.1,0.5,0.7,0.9,1)
plt.title('Number of Entrances per Line', color='black', size=18)
plt.show()


# In[ ]:





# In[ ]:




