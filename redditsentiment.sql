CREATE TABLE SUBREDDIT_DATA
(subreddit VARCHAR(100), post_rank INT, title VARCHAR(500), title_length INT, score INT, postID VARCHAR(10) UNIQUE, date_pulled DATE);

CREATE TABLE subreddit_data_sentiment
(subreddit VARCHAR(100), post_rank INT, title VARCHAR(500), title_length INT, score INT, postID VARCHAR(10) UNIQUE, neg FLOAT, neu FLOAT, pos FLOAT, compound FLOAT, date_pulled DATE);

SELECT subreddit, AVG(pos), AVG(neg), AVG(neu) FROM SUBREDDIT_DATA_SENTIMENT
GROUP BY subreddit
ORDER BY AVG(neg) DESC;

select 'subreddit', 'post_rank', 'title', 'title_length', 'score', 'postID', 'neg', 'neu', 'pos', 'compound', 'date_pulled' UNION select * from subreddit_data_sentiment INTO outfile "c:/ProgramData/MySQL/MySQL Server 8.0/Uploads/sentiment.txt";
select 'subreddit', 'subscribers', 'date_pulled' UNION select * from subscriber_count INTO outfile "c:/ProgramData/MySQL/MySQL Server 8.0/Uploads/subscriber.txt";

SHOW variables like 'secure_file_priv';

SELECT COUNT(DISTINCT subreddit) FROM SUBREDDIT_DATA_SENTIMENT;

SELECT * FROM SUBREDDIT_DATA_SENTIMENT
ORDER BY pos DESC
LIMIT 10;

SELECT DATABASE();
