
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



#Now make a pie chart

df2 = df.value_counts('LINE')


colors=['lightblue','lightsteelblue','silver']
explode=(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.1,0.1,0.5,0.7,0.9,1)
ax=df2.plot.pie(explode=explode, figsize=(10,10),startangle=15, shadow=True, 
                                   colors=colors,pctdistance=0.8)
plt.title('Number of Entrances per Line', color='black', size=18)


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

# edit column of geological location for easier mapping by 
# removing characters with known positions using lamda function

df['the_geom'] = df['the_geom'].map(lambda x: str(x)[7:-1])
df.head()



# add two new columns to the existing dataframe
# by default splitting is done on the basis of single space

df[['longitude','latitude']]=df.the_geom.str.split(" ",expand=True)
print(df.info)

# creating a map of NYC
map_nyc=folium.Map(location=[40.730610,-73.935242],zoom_start=12,control_scale=True)

# convert geological info into float
df['latitude'] = df['latitude'].astype(float)
df['longitude'] = df['longitude'].astype(float)

# create a list
heat_df = df[['latitude', 'longitude']]

# plot list into heat map
HeatMap(heat_df).add_to(map_nyc)

map_nyc

# make another map
map_nyc2=folium.Map(location=[40.730610,-73.935242],zoom_start=12,control_scale=True)


# use for loop to plot stations 
for i in range(0, len(df)):
    folium.Marker([df.iloc[i]['latitude'], df.iloc[i]['longitude']],
                 popup=df.iloc[i]['LINE'],icon=folium.Icon(color='green')).add_to(map_nyc2)
   
map_nyc2



