#!/usr/bin/env python
# coding: utf-8



import pandas as pd
import matplotlib.pyplot as plt
#import numpy as np


df = pd.read_csv("data_processed/weather_data_processed.csv")



out= '#Summary Statistics of Quantitative data\n'
out= out+ '\n'+ df.describe().to_string()
text_file = open("data_processed/summary.txt","w")
text_file.write(out)
text_file.close()

#df.median()

df.apply(pd.isnull).sum()



out= '\n\n#Summary Statistics of Qualitative data\n'
out= out+ '\n'+ df['Weather'].value_counts().to_string()
text_file = open("data_processed/summary.txt","a")
text_file.write(out)
text_file.close()


out= '\n\nMost Frequent-- Warm'
text_file = open("data_processed/summary.txt","a")
text_file.write(out)
text_file.close()

out= '\nNo of categories-- 4 (Hot, Sweltering, Warm, Cool)'
text_file = open("data_processed/summary.txt","a")
text_file.write(out)
text_file.close()

out= '\nLeast frequent-- Cool'
text_file = open("data_processed/summary.txt","a")
text_file.write(out)
text_file.close()


# Summary Statistics of Qualitative data 
# Most Frequent 
df['Weather'].value_counts().idxmax()

#most frequent alternate way
df['Weather'].mode()

# No. of categories
df['Weather'].unique()

# Least Frequent
df['Weather'].value_counts().idxmin()


co= '#pairwise correlation'

corr=df[['Precipitation','Snow','Temp_max','Temp_min']].corr()

co= co+ '\n'+ corr.to_string()

text_file = open("data_processed/correlations.txt","w")
text_file.write(co)
text_file.close()

#plots of distribution

fig,ax = plt.subplots()
plt.scatter(df['Precipitation'],df['Snow'],alpha=0.8)
plt.title("ScatterPlot #1 Precipitation vs Snowfall")
plt.xlabel("Precipitation (mm or inches)")
plt.ylabel("Snowfall (mm or inches)")
#plt.savefig('visuals/scatterplot1.png')
fig.savefig('visuals/scatterplot1.png',facecolor='w')

import matplotlib.pyplot as plt

fig,ax = plt.subplots()
plt.scatter(df['Precipitation'],df['Temp_max'],alpha=0.8)
plt.title("ScatterPlot #2 Precipitation vs Max Temp")
plt.xlabel("Precipitation (mm or inches)")
plt.ylabel("Maximum temperature recorded (F)")
#plt.savefig('visuals/scatterplot2.png')
fig.savefig('visuals/scatterplot2.png',facecolor='w')


import matplotlib.pyplot as plt

fig,ax = plt.subplots()
plt.scatter(df['Snow'],df['Temp_max'],alpha=0.8)
plt.title("ScatterPlot #3 Snowfall vs Max Temp")
plt.xlabel("Snowfall (mm or inches)")
plt.ylabel("Maximum temperature recorded (F)")
#plt.savefig('visuals/scatterplot3.png')
fig.savefig('visuals/scatterplot3.png',facecolor='w')

import matplotlib.pyplot as plt

fig,ax = plt.subplots()
plt.scatter(df['Precipitation'],df['Temp_min'],alpha=0.8)
plt.title("ScatterPlot #4 Precipitation vs Min Temp")
plt.xlabel("Precipitation (mm or inches)")
plt.ylabel("Minimum temperature recorded (F)")
#plt.savefig('visuals/scatterplot4.png')
fig.savefig('visuals/scatterplot4.png',facecolor='w')

import matplotlib.pyplot as plt

fig,ax = plt.subplots()
plt.scatter(df['Snow'],df['Temp_min'],alpha=0.8)
plt.title("ScatterPlot #5 Snowfall vs Min Temp")
plt.xlabel("Snowfall (mm or inches)")
plt.ylabel("Minimum temperature recorded (F)")
#plt.savefig('visuals/scatterplot5.png')
fig.savefig('visuals/scatterplot5.png',facecolor='w')


import matplotlib.pyplot as plt

fig,ax = plt.subplots()
plt.scatter(df['Temp_max'],df['Temp_min'],alpha=0.8)
plt.title("ScatterPlot #6 Max Temp vs Min Temp")
plt.xlabel("Maximum temperature recorded (F)")
plt.ylabel("Minimum temperature recorded (F)")
#plt.savefig('visuals/scatterplot6.png')
fig.savefig('visuals/scatterplot6.png',facecolor='w')

import matplotlib.pyplot as plt

fig,ax = plt.subplots()
plt.hist(df['Weather'],alpha=1)
plt.title("Histogram for Qualitative features")
plt.xlabel("Weather")
plt.ylabel("No.of days (Frequency)")
#plt.savefig('visuals/histogram.png')
fig.savefig('visuals/histogram.png',facecolor='w')





