#!/usr/bin/env python
# coding: utf-8

# In[122]:


import pandas as pd
import scipy
from numpy import mean
from numpy import std
from matplotlib import pyplot
from scipy import stats
import matplotlib.pyplot as plt
import numpy as np

#read data on vaccines from file
df= pd.read_csv('doses-by-day.csv', sep=',',na_values='')

# get column names in dataset
df.info()

#checking how many days are in dataset
print(len(df['DATE']))

#making sure the rows within the vaccine dataset match the case rate dataset
start_date = '2021-01-01'
end_date = '2022-04-26'
mask = (df['DATE'] >= start_date) & (df['DATE'] <= end_date)
df_vaccine = df.loc[mask]
display(len(df_vaccine))








# In[137]:



# read second dataset on case rate
df2 = pd.read_csv('https://raw.githubusercontent.com/nychealth/coronavirus-data/master/trends/cases-by-day.csv', sep=',',na_values='')

# getting column names in dataset
df2.info()


#checking how many days in dataset
print(len(df2['date_of_interest']))

# extract rows from dates of interest column
df_case=df2.iloc[307:788, 0:2]


#select data on cumulative total of vaccines admimistered per day
vaccine_total=df_vaccine['ADMIN_ALLDOSES_DAILY']
print(vaccine_total.sum())
case_total=df_case['CASE_COUNT']
print(case_total.sum())
vaccine_dose1=df_vaccine['ADMIN_DOSE1_DAILY']
vaccine_dose2=df_vaccine['ADMIN_DOSE2_DAILY']

# find correlation values between data
print(vaccine_total.corr(case_total))
print(vaccine_dose1.corr(vaccine_dose2))


#plot 
ax=df_vaccine.plot(x='DATE', y='ADMIN_ALLDOSES_DAILY',fontsize=15, color='orange', label='Vaccines 1 and 2')
df_case.plot(ax=ax, x='date_of_interest', y='CASE_COUNT', color='red', label='Cases',figsize=(20, 8))
df_vaccine.plot(ax=ax, x='DATE', y='ADMIN_DOSE1_DAILY', color='green', label='Vaccine1')
df_vaccine.plot(ax=ax, x='DATE', y='ADMIN_DOSE2_DAILY', color='darkblue', label='Vaccine2')
plt.title("Case Rate and Vaccine Rate Trends in NYC", fontsize=20)
plt.xlabel('Days', fontsize=20)
plt.ylabel('Rate', fontsize=20)
plt.legend(fontsize=15)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




