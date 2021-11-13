import praw
import pandas as pd
from datetime import datetime
import config as cf

#PRAW Project : objective is to determine whether or not the word count affects rank of post, & also most popular words in top titles.

#define reddit API connection
reddit = praw.Reddit(client_id = cf.praw_client_id, 
					client_secret = cf.praw_client_secret, 
					user_agent = cf.praw_user_agent, 
					username = cf.praw_username, 
					password = cf.praw_password)


def getTopPosts(n, subreddits, timeframe):
	"""
	Returns a list of dicts of top n non-stickied posts from each subreddit in subreddits.

	"""
	data = []
	for item in subreddits:
		subreddit = reddit.subreddit(item)
		rank = 1
		try:
			for submission in subreddit.top(timeframe, limit= n):
				if not submission.stickied:
					temp={}
					for i, j in zip([item, rank, submission.title, len(submission.title), submission.score, submission.id], ['subreddit', 'post_rank', 'title', 'title_length', 'score', 'postID']):
						temp[j] = i
					rank += 1
					data.append(temp)
		except:
			print(item + " is now defunct")
			continue
	return data


def get_subscriber_count(subreddits):
	"""
	returns a list of dicts of subreddits and their subscriber count

	"""
	sub_count = []
	for subreddit in subreddits:
		try:
			temp = {}
			temp['subreddit'] = subreddit
			temp['subscribers'] = reddit.subreddit(subreddit).subscribers
			sub_count.append(temp)
		except:
			print(subreddit + " is now defunct")
			continue
	return sub_count


def main():

	subreddits = ["aww", "funny"]

	data = getTopPosts(5, subreddits, 'month')

	today = (datetime.today().strftime('%Y.%m.%d'))

	#create pandas dataframe
	df = pd.DataFrame(data, columns = ['subreddit', 'post_rank', 'title', 'title_length', 'score', 'postID'])
	df['date_pulled'] = today

	#save data as csv
	df.to_csv(r'csv_scrapes/%s_scrape.csv' % today ,index=False)



if __name__ == '__main__':
	main()
