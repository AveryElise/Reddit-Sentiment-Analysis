import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sqlalchemy import create_engine
import config as cf
import seaborn as sns
from sklearn.linear_model import LinearRegression


def rearrange_for_regression(dataframe, column):
	"""
	rearranges a dataframe column for input into the linear regression object
	"""
	return dataframe.iloc[:, column].values.reshape(-1, 1)

engine = create_engine('mysql+mysqlconnector://%s:%s@%s:%s/scraping_data' % (cf.user, cf.passw, cf.host, cf.port), echo=False)

#create df
df = pd.read_sql("SELECT *, (pos+neg) as emotion FROM subreddit_data_sentiment", engine)



#scatterplot of title length vs emotion, with linear regression -------------------------------
plt.scatter(df['title_length'], df['emotion'], alpha=.15)
linear_regressor = LinearRegression()
linear_regressor.fit(rearrange_for_regression(df, 3), rearrange_for_regression(df, 11))
emotion_prediction = linear_regressor.predict(rearrange_for_regression(df, 3))
#r^2 score
print(linear_regressor.score(rearrange_for_regression(df, 3), rearrange_for_regression(df, 11)))
plt.plot(df['title_length'], emotion_prediction, color='red')

plt.show()
# plt.savefig('title_vs_emotion_scatterplot.png')



#What if we just look at the most emotional subreddits? ----------------------------------------
#Cannot do a subquery here because of mySQL limitations, join is a workaround

df = pd.read_sql("""SELECT *, (pos + neg) as emotion From subreddit_data_sentiment s1
INNER JOIN
( SELECT subreddit FROM subreddit_data_sentiment GROUP BY subreddit ORDER BY (pos + neg) DESC LIMIT 10) s2
on s1.subreddit = s2.subreddit;""", engine)

#clear plot
plt.clf()

plt.scatter(df['title_length'], df['emotion'], alpha=.15)

linear_regressor.fit(rearrange_for_regression(df, 3), rearrange_for_regression(df, 12))
emotion_prediction = linear_regressor.predict(rearrange_for_regression(df, 3))
plt.plot(df['title_length'], emotion_prediction, color='red')
print(linear_regressor.score(rearrange_for_regression(df, 3), rearrange_for_regression(df, 12)))
plt.show()


#Now let's do bottom 10 emotional --------------------------------------------------------------
df = pd.read_sql("""SELECT *, (pos + neg) as emotion From subreddit_data_sentiment s1
INNER JOIN
( SELECT subreddit FROM subreddit_data_sentiment GROUP BY subreddit ORDER BY (pos + neg) ASC LIMIT 10) s2
on s1.subreddit = s2.subreddit;""", engine)

plt.clf()

plt.scatter(df['title_length'], df['emotion'], alpha=.15)

linear_regressor.fit(rearrange_for_regression(df, 3), rearrange_for_regression(df, 12))
emotion_prediction = linear_regressor.predict(rearrange_for_regression(df, 3))
plt.plot(df['title_length'], emotion_prediction, color='red')
print(linear_regressor.score(rearrange_for_regression(df, 3), rearrange_for_regression(df, 12)))
plt.show()
