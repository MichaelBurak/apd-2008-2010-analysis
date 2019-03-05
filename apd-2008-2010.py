#Importing in libraries

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Importing dataset to base dataframe in pandas
df = pd.read_csv('APD_Incident_Extract_2010.csv')
df.head(5)

# Already seeing NaNs in LOCATION_TYPE, LONGITUDE, LATITUDE, LOCATION 1, but first I'm interested in the type of crimes

df.columns = ['incRepNum', 'crimeType', 'date', 'time',
              'locationType', 'address', 'longitude', 'latitude', 'location1']
df.crimeType.unique()


len(df.crimeType.unique())


# Separating out crimes distinctly involving technology.

techCrimes = ['HIGH TECH CRIME', 'CYBER CRIMES']
dfTech = df[df.crimeType.isin(techCrimes)]


dfTech.info()


# A rather low number of reports to say the least.
dfTech


# Comparatively, what are the most highly reported crimes?

# First get NaNs out of the way.
df = df.dropna(subset=['crimeType'])

# Confirming NaN are dropped.
len(df.crimeType.unique())


val_counts = df.crimeType.value_counts()

val_counts.hist(bins=30)


# Looks like a vast drop off below around 1k, time to grab occurrences equal to and greater than 1k in value count.
oneKPlusVals = df.crimeType.value_counts()[df.crimeType.value_counts() > 999]


oneKPlusVals


len(oneKPlusVals)


len(oneKPlusVals) / len(df.crimeType.unique())
