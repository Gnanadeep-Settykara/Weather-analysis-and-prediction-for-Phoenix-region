#processing
#!/usr/bin/env python
# coding: utf-8


import pandas as pd


we = pd.read_csv("data_original/weather_data.csv",index_col="DATE")

#print(we)

df = we[["PRCP", "SNOW", "SNWD", "TMAX", "TMIN"]].copy()
df.columns = ["Precipitation", "Snow", "Snow_depth", "Temp_max", "Temp_min"]

#print(df)

# Finding and replacing the missing values
df.apply(pd.isnull).sum()
df["Snow"].value_counts()
df["Snow_depth"].value_counts()
df[pd.isnull(df["Precipitation"])]


df["Precipitation"] = df["Precipitation"].fillna(0)
df["Snow"] = df["Snow"].fillna(0)
df["Snow_depth"] = df["Snow_depth"].fillna(0)
df.apply(pd.isnull).sum()
df[pd.isnull(df["Temp_min"])]

# usinf ffill to replace with the previous value for temperature
df = df.fillna(method="ffill")
df.apply(pd.isnull).sum()
df.apply(lambda x: (x == 9999).sum())

#print(df.dtypes)

#converting date column to datetime
df.index = pd.to_datetime(df.index)

#df.describe()


# Adding a new column 'weather' with categorical data
df['Weather'] = pd.cut(df['Temp_min'],
                            bins=[0,32,42,50],
                            labels=['Freezing','Cold', 'Chilly'])

if df['Weather'].isnull:
    df['Weather'] = pd.cut(df['Temp_max'],
                            bins=[50,60,84,100,130 ],
                            labels=['Cool','Warm','Hot','Sweltering'])

#print(df.dtypes)
#Summary Statistics of Quantitative data
#df.describe()

#df.apply(pd.isnull).sum()

#df['Weather'].value_counts()

df = df.fillna(method="ffill")

# Summary Statistics of Qualitative data
#df['Weather'].value_counts()
df.to_csv('data_processed\weather_data_processed.csv')







