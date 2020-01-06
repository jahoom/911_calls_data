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
sns.set(style='whitegrid')
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
#f, axes = plt.subplots(2,1)
#sns.countplot(x='Day of week', data = df, hue = 'Reason', ax=axes[0])
#sns.countplot(x='Month', data = df, hue = 'Reason', ax = axes[1])
byMonth = df.groupby(['Month']).count()
print(byMonth.head())
#lp_Month = sns.lineplot(data=byMonth['lat'], linewidth=2)
#lp_Month.set_ylim([7000,14000]); lp_Month.set_xlim([1,12])

#linfit = sns.lmplot(data=byMonth.reset_index(), x='Month', y='lat')
df['Date'] = df['timeStamp'].apply(lambda x: x.date())
byDate_Traffic = df[df['Reason']=='Traffic'].groupby(['Date']).count()
byDate_Fire = df[df['Reason']=='Fire'].groupby(['Date']).count()
byDate_EMS = df[df['Reason']=='EMS'].groupby(['Date']).count()
#f, axes = plt.subplots(3,1)
#lp_Traffic = sns.lineplot(data=byDate_Traffic['lat'], ax=axes[0], linewidth=2)
#lp_Fire = sns.lineplot(data=byDate_Fire['lat'], ax=axes[1] ,linewidth=2)
#lp_EMS = sns.lineplot(data=byDate_EMS['lat'], ax=axes[2] ,linewidth=2)

#heatamap-y

dayHour = df.groupby(by=['Day of week','Hour']).count()['Reason'].unstack()
print(dayHour.head())
#sns.heatmap(dayHour, cmap='magma')
sns.clustermap(dayHour, cmap='coolwarm')
sns.despine()
plt.show()