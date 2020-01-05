import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("911.csv")

print("Informacje o pobranych danych: \n", df.info())
print("Nagłówek pobranych danych: \n", df.head())
print("Najpopularniejsze kody pocztowe: \n", df['zip'].value_counts().head(5))
