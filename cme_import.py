
# import modules
import pandas as pd
import numpy as np
import datetime

# import file, DO NOT CHANGE FILE NAME ON DOWNLOAD FROM CME GATEWAY
df = pd.read_csv('CMEgateway.csv')

# drop the non-date and non-credit type and amount columns
df.drop(df.iloc[:, 0:4], inplace=True, axis=1)
df.drop(df.iloc[:,1:7], inplace=True, axis=1)

# parse the year from the date column, needs to be cast to a datetime
df['Date'] = pd.to_datetime(df['Date'])
df['Date'] = df['Date'].dt.year

# reduce to only mpcec credits for analysis, then delete column
mpcec = df['CME Total - Credit Type'] == 'MPCEC'
df = df[mpcec]
df.drop('CME Total - Credit Type', inplace=True, axis=1)

# pivot on year
pivot = pd.pivot_table(data=df, index='Date', aggfunc='sum')

# get the current year to check previous years against
this_year = datetime.datetime.now().year

# TODO: set up bins from current year to the last remaining year, look/fill blanks


# TODO: divide up into 3-year bins, except for the earliest which is a 4-year bin
years = df['Date']


# TODO: sum bins, then check against minimum required (>=75 per 3-year bin)


# TODO: if all bins pass, say user is meeting, otherwise warn them


# TODO ???: show deficits for current and upcoming years and bins?