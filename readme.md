# Reddit Sentiment Analysis

### What is the popular sentiment in any given Subreddit, and how does that vary across Reddit's most popular subreddits?

This script connects to the Reddit API (PRAW) and collects post data (title, monthly rank, upvotes) from the top 500 subreddits on Reddit. It then performs sentiment analysis using nltk. I have used this data, stored in a MySQL database, to create the below Tableau Dashboards answering my original question.

View the fully interactive Dashboard on Tableau Public: [**Tableau Public Dashboard**](https://public.tableau.com/app/profile/avery.headley/viz/SubredditSentiments/Subredditsvaryintheirpreferred)

![](Visualizations/subreddit_sentiments.gif)

![](Visualizations/Can we predict the type of Subreddit by Title Length and Sentiment.pdf)