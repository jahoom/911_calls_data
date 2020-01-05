import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("911.csv")

#podstawowe operacje
print("Informacje o pobranych danych: \n", df.info())
print("Nagłówek pobranych danych: \n", df.head())
print("\nNajpopularniejsze kody pocztowe: \n", df['zip'].value_counts().head(5))
print("\nNajpopularniejsze miasta zgłoszeń: \n", df['twp'].value_counts().head(5))
print("\nUnikatowych tytułów jest: ", len(df['title'].unique()))

#modyfikacja danych
df['Reason'] = df['title'].apply(lambda title: str(title).split(":")[0])
print(df['Reason'].value_counts())
sns.set(style='darkgrid')
#cp = sns.countplot(x='Reason',data=df)
print("Typ danych w kolumnie timeStamp ", type(df['timeStamp'][0]))
df['timeStamp']=pd.to_datetime(df['timeStamp'])
print("A po zmianie - typ danych w kolumnie timeStamp ", type(df['timeStamp'][0]))
df['Hour'] = df['timeStamp'].apply(lambda x: x.hour)
df['Month'] = df['timeStamp'].apply(lambda x: x.month)
df['Day'] = df['timeStamp'].apply(lambda x: x.weekday())
print(df['Day'].value_counts())

dmap={0:'Mon',1:'Tue',2:'Wed',3:'Thu',4:'Fri',5:'Sat',6:'Sun'}
df['Day of week']=df['Day'].apply(lambda x: dmap[x])
print(df['Day of week'].value_counts())
f, axes = plt.subplots(2,1)
sns.countplot(x='Day of week', data = df, hue = 'Reason', ax=axes[0])
sns.countplot(x='Month', data = df, hue = 'Reason', ax = axes[1])
byMonth = df.groupby(['Month']).count()
print(byMonth.head())

plt.show()