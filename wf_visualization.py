#!/usr/bin/env python
# coding: utf-8



import pandas as pd
import matplotlib.pyplot as plt



df = pd.read_csv("data_processed/weather_data_processed.csv")



#Summary Statistics of Quantitative data
df.describe()

df.median()

df.apply(pd.isnull).sum()


# Summary Statistics of Qualitative data
df['Weather'].value_counts()

# Summary Statistics of Qualitative data 
# Most Frequent 
df['Weather'].value_counts().idxmax()

#most frequent alternate way
df['Weather'].mode()

# No. of categories
df['Weather'].unique()

# Least Frequent
df['Weather'].value_counts().idxmin()


#pairwise correlation

corr=df.corr()

corr



#plots of distribution

plt.scatter(df['Precipitation'],df['Snow'],alpha=0.8)
plt.title("ScatterPlot #1")
plt.xlabel("Precipitation (mm or inches)")
plt.ylabel("Snowfall (mm or inches)")
plt.savefig('visuals/scatterplot1.png')


plt.scatter(df['Precipitation'],df['Temp_max'],alpha=0.8)
plt.title("ScatterPlot #2")
plt.xlabel("Precipitation (mm or inches)")
plt.ylabel("Maximum temperature recorded (F)")
plt.savefig('visuals/scatterplot2.png')





plt.scatter(df['Snow'],df['Temp_max'],alpha=0.8)
plt.title("ScatterPlot #3")
plt.xlabel("Snowfall (mm or inches)")
plt.ylabel("Maximum temperature recorded (F)")
plt.savefig('visuals/scatterplot3.png')




plt.scatter(df['Precipitation'],df['Temp_min'],alpha=0.8)
plt.title("ScatterPlot #4")
plt.xlabel("Precipitation (mm or inches)")
plt.ylabel("Minimum temperature recorded (F)")
plt.savefig('visuals/scatterplot4.png')




plt.scatter(df['Snow'],df['Temp_min'],alpha=0.8)
plt.title("ScatterPlot #5")
plt.xlabel("Snowfall (mm or inches)")
plt.ylabel("Minimum temperature recorded (F)")
plt.savefig('visuals/scatterplot5.png')





plt.scatter(df['Temp_max'],df['Temp_min'],alpha=0.8)
plt.title("ScatterPlot #6")
plt.xlabel("Maximum temperature recorded (F)")
plt.ylabel("Minimum temperature recorded (F)")
plt.savefig('visuals/scatterplot6.png')



plt.hist(df['Weather'],alpha=1)
plt.title("Histogram for Qualitative features")
plt.xlabel("Weather")
plt.ylabel("No.of days (Frequency)")
plt.savefig('visuals/histogram.png')






