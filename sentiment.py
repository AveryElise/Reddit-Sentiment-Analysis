import praw
import pandas as pd
from datetime import datetime
from pandas.io import sql
from sqlalchemy import create_engine
import config as cf
import nltk
from datetime import datetime
import redditscraper as rs
from nltk.sentiment.vader import SentimentIntensityAnalyzer as SIA

nltk.download('vader_lexicon')

#Create praw instance
reddit = praw.Reddit(client_id = cf.praw_client_id, 
					client_secret = cf.praw_client_secret, 
					user_agent = cf.praw_user_agent, 
					username = cf.praw_username, 
					password = cf.praw_password)

def main():

	#subreddits
	subreddit_csv = pd.read_csv('subreddits.csv')
	topsubreddits = subreddit_csv['Subreddits'].tolist()

	#get top posts for this month from each subreddit
	toppostsdata = rs.getTopPosts(25, topsubreddits, "month")

	#include sentiment analysis in toppostsdata dictionary
	sia = SIA()
	for x in toppostsdata:
		text = x['title']
		pol_score = sia.polarity_scores(text)
		for i, j in zip(pol_score, ['neg', 'neu', 'pos', 'compound']):
			x[j] = pol_score[i]

	#insert into dataframe
	df = pd.DataFrame.from_dict(toppostsdata)
	print(df.head())

	#append date pulled to df
	today = (datetime.today().strftime('%Y/%m/%d'))
	df['date_pulled'] = today

	#put results in databse
	#Create SQL connection
	engine = create_engine('mysql+mysqlconnector://%s:%s@%s:%s/scraping_data' % (cf.user, cf.passw, cf.host, cf.port), echo=False)

	#push to mySQL - creating the temp table allows us to then INSERT IGNORE to ignore duplicate entries to subreddit_data_sentiment table
	df.to_sql(name='temp_table', con=engine, if_exists = 'replace', index=False)
	connection = engine.connect()
	connection.execute("INSERT IGNORE INTO subreddit_data_sentiment SELECT * FROM temp_table")
	connection.close()
	#If we just pushed it directly:
	#df.to_sql(name='SUBREDDIT_DATA_SENTIMENT', con=engine, if_exists = 'append', index=False)

	#Push subscriber count df to SQL
	sub_count = rs.get_subscriber_count(topsubreddits)
	sub_count_df = pd.DataFrame.from_dict(sub_count)
	sub_count_df['date_pulled'] = today
	print(sub_count_df.head())
	sub_count_df.to_sql(name='subscriber_count', con=engine, if_exists='append', index=False)

	#alternatively, save data as csv
	#df.to_csv(r'csv_scrapes/%s_scrape.csv' % today ,index=False)
	#sub_count_df.to_csv(r'csv_scrapes/%s_subscriber_count_scrape.csv' % today ,index=False)

if __name__ == '__main__':
	main()

