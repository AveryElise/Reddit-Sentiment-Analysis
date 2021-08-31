import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import random
import seaborn as sns


#create pandas dataframe
df = pd.read_csv(r'scrapes\2021.01.08_scrape - Copy.csv')

creepy_df =df[df['subreddit']=='creepy']

print(creepy_df.head())

sns.scatterplot(x='rank', y='score', data=creepy_df)
sns.displot(creepy_df['rank'])
plt.savefig('save_as_a_png.png')
