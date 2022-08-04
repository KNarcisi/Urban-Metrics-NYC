
import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import datetime

# Exploring Monkey Pox NYC Data
# Dataset From NYC Department of Health and Mental Hygiene

# read url data using pandas
url='https://raw.githubusercontent.com/nychealth/monkeypox-data/main/trends/cases-by-day.csv'
df=pd.read_csv(url,delimiter=',')
url2='https://raw.githubusercontent.com/nychealth/monkeypox-data/main/totals/summary-cases.csv'
df2=pd.read_csv(url2,delimiter=',')
url3='https://raw.githubusercontent.com/nychealth/coronavirus-data/master/trends/cases-by-day.csv'
df3=pd.read_csv(url3,delimiter=',')



# assign variable to column
x=df['diagnosis_date']

# plot line graph of case rate 
plt.subplots(figsize=(20, 8))
plt.plot(df['diagnosis_date'],df['count'],color='red',marker='o')
plt.title('Monkey Pox NYC Rate', fontsize=20)
plt.xlabel('Date', fontsize=15)
plt.ylabel('Case Rate', fontsize=15)

# edit x axis labels to make room
plt.xticks(rotation=20, ha='right')
plt.margins(x=0, y=0.05)

# Use slice notation to slice list x to set ticks every 3rd entry to make room on x axis
plt.xticks(x[::3])
plt.grid(True)
plt.show()



# fill in missing dates  
# Convert string to datetime     
df['diagnosis_date'] = pd.to_datetime(df['diagnosis_date'])

# reindex date using min and max, rename diagnosis date to date
new_df = (df.set_index('diagnosis_date')
      .reindex(pd.date_range(min(df.diagnosis_date), max(df.diagnosis_date), freq='D'))
      .rename_axis(['date'])
      .fillna(0)
      .reset_index())

print(new_df)

# count how many days we have on record
print(len(new_df.date))



# Creating new column Day to both datasets to plot
new_df = new_df.reset_index()
new_df['Day'] = new_df.index + 1
print(new_df)

df3=df3.reset_index()
df3['Day']=df3.index + 1
print(df3)


# assigning variables to columns day and daily total to plot
# for both COVID and Monkey POX NYC data
# using iloc function to slice the dataframes and have equal specific rows

x1=new_df['Day'].iloc[0:75]
y1=new_df['count'].iloc[0:75]

x2=df3['Day'].iloc[0:75]
y2=df3['CASE_COUNT'].iloc[0:75]

plt.plot(x1, y1, label = "Monkey Pox" ,marker='o', color='purple')
plt.plot(x2, y2, label = "COVID", marker='o')
plt.legend(fontsize=20)
plt.title('Monkey Pox VS COVID case rate first 76 days reported NYC ', fontsize=25,pad=20)
plt.xlabel('Per Day', fontsize=20)
plt.ylabel('Case Rate', fontsize=20)
plt.grid(True)

plt.show()






