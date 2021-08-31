CREATE TABLE SUBREDDIT_DATA
(subreddit VARCHAR(100), post_rank INT, title VARCHAR(500), title_length INT, score INT, postID VARCHAR(10) UNIQUE, date_pulled DATE);

CREATE TABLE subreddit_data_sentiment
(subreddit VARCHAR(100), post_rank INT, title VARCHAR(500), title_length INT, score INT, postID VARCHAR(10) UNIQUE, neg FLOAT, neu FLOAT, pos FLOAT, compound FLOAT, date_pulled DATE);

DROP table SUBREDDIT_DATA_SENTIMENT;
DROP table subscriber_count;

SELECT subreddit, AVG(pos), AVG(neg), AVG(neu) FROM SUBREDDIT_DATA_SENTIMENT
GROUP BY subreddit
ORDER BY AVG(neg) DESC;

select * from subreddit_data_sentiment;
select * from subscriber_count;

SELECT COUNT(*) FROM SUBREDDIT_DATA_SENTIMENT;

SELECT * FROM SUBREDDIT_DATA_SENTIMENT
ORDER BY pos DESC
LIMIT 10;
