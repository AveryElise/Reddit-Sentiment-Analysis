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
	topsubreddits = ['funny','askreddit','gaming','aww','music','pics','worldnews','science','todayilearned','movies','videos','news','showerthoughts','earthporn','food','iama','askscience','gifs','jokes','nottheonion','lifeprotips','books','explainlikeimfive','art','diy','mildlyinteresting','sports','space','gadgets','documentaries','blog','photoshopbattles','tifu','getmotivated','upliftingnews','listentothis','television','memes','dataisbeautiful','history','philosophy','internetisbeautiful','futurology','writingprompts','oldschoolcool','nosleep','personalfinance','creepy','twoxchromosomes','technology','wallstreetbets','wholesomememes','adviceanimals','interestingasfuck','fitness','politics','wtf','oddlysatisfying','travel','lifehacks','minecraft','relationship_advice','facepalm','blackpeopletwitter','whatcouldgowrong','leagueoflegends','bestof','natureisfuckinglit','pcmasterrace','me_irl','dankmemes','nextfuckinglevel','tinder','ps4','dadjokes','unexpected','animalsbeingbros','tattoos','photography','buildapc','nba','animalsbeingjerks','trippinthroughtime','bikinibottomtwitter','foodporn','damnthatsinteresting','instant_regret','mademesmile','gardening','reactiongifs','woahdude','animalsbeingderps','watchpeopledieinside','overwatch','pewdiepiesubmissions','mildlyinfuriating','programming','publicfreakout','pokemon','contagiouslaughter','eatcheapandhealthy','gonewild','parenting','boardgames','cryptocurrency','bitcoin','nintendoswitch','pokemongo','itookapicture','malefashionadvice','iphone','woodworking','xboxone','relationships','outdoors','youshouldknow','idiotsincars','drawing','amitheasshole','rarepuppers','nonononoyes','games','stocks','cats','dating_advice','awwducational','cursedcomments','highqualitygifs','loseit','soccer','humor','gifrecipes','europe','askmen','historymemes','gameofthrones','bettereveryloop','historyporn','eyebleach','streetwear','nsfw','netflixbestof','anime','cooking','atheism','apple','makeupaddiction','confession','pcgaming','slowcooking','howto','realgirls','recipes','humansbeingbros','crappydesign','askwomen','backpacking','childrenfallingover','entertainment','teenagers','blackmagicfuckery','wellthatsucks','murderedbywords','socialskills','beamazed','deepintoyoutube','keto','offmychest','cars','trashy','moviedetails','outoftheloop','biology','scifi','horror','youtubehaiku','dnd','trollychromosome','battlestations','frugalmalefashion','learnprogramming','raspberry_pi','nostupidquestions','mac','coronavirus','kidsarefuckingstupid','rickandmorty','holup','android','whitepeopletwitter','starterpacks','coolguides','hardware','roastme','ksi','foodhacks','bodyweightfitness','dogs','nsfw_gif','choosingbeggars','homeimprovement','unpopularopinion','blursedimages','wow','electronicmusic','reallifedoodles','roadcam','therewasanattempt','dogecoin','sneakers','camping','nfl','instantkarma','destinythegame','nintendo','mealprepsunday','natureismetal','likeus','insanepeoplefacebook','astronomy','machinelearning','artefactporn','youseeingthisshit','podcasts','zelda','hiphopheads','hentai','indieheads','design','filmmakers','shittyfoodporn','starwars','femalefashionadvice','whatisthisthing','sex','hacking','frugal','cozyplaces','fiftyfifty','nutrition','homestead','yesyesyesyesno','comicbooks','nasa','writing','marvelstudios','investing','rareinsults','prequelmemes','assholedesign','spaceporn','artisanvideos','thriftstorehauls','nevertellmetheodds','legalteens','porn','graffiti','winstupidprizes','cumsluts','justiceserved','urbanexploration','solotravel','healthyfood','hearthstone','tipofmytongue','astrophotography','physics','justnomil','progresspics','dundermifflin','rule34','pennystocks','hmmm','stockmarket','pubattlegrounds','wallpaper','trees','japantravel','educationalgifs','savedyouaclick','bodybuilding','madlads','technicallythetruth','mealtimevideos','meme','wearethemusicmakers','bustypetite','legaladvice','cinemagraphs','apexlegends','quityourbullshit','crafts','maliciouscompliance','mma','gamephysics','campingandhiking','formula1','asiansgonewild','suggestmeabook','holdmycosmo','audiophile','math','collegesluts','entitledparents','baseball','literature','javascript','comics','animalcrossing','girlsfinishingthejob','doesanybodyelse','casualconversation','economics','sketchdaily','iamverysmart','fortnitebr','google','conspiracy','watches','perfecttiming','mapporn','petitegonewild','ethtrader','shittylifeprotips','atbge','programmerhumor','comedyheaven','ps5','roadtrip','thewalkingdead','compsci','catastrophicfailure','adorableporn','diwhy','collegebasketball','holdthemoan','peoplefuckingdying','techsupport','hiking','breakingbad','edm','chemistry','tittydrop','specart','running','cursedimages','fantasy','terriblefacebookmemes','carporn','memeeconomy','analog','cringetopia','survival','politicalhumor','unresolvedmysteries','rainbow6','vandwellers','metal','iamatotalpieceofshit','somethingimade','tihi','cringepics','childfree','thathappened','kerbalspaceprogram','manga','maybemaybemaybe','nsfw_gifs','softwaregore','marvelmemes','abruptchaos','politicaldiscussion','ass','pussy','freeebooks','askhistorians','niceguys','rpg','exposureporn','globaloffensive','justrolledintotheshop','roomporn','classicalmusic','biggerthanyouthought','machineporn','milf','skincareaddiction','health','abandonedporn','shouldibuythisgame','specializedtools','changemyview','asianbeauty','photocritique','breedingmaterial','mashups','2meirl4meirl','teslamotors','southpark','meirl','confusing_perspective','tooafraidtoask','hockey','cringe','whatswrongwithyourdog','perfectlycutscreams','poetry','anime_irl','shoestring','nsfwhardcore','insaneparents','livestreamfail','sweatypalms','porninfifteenseconds','adhd','unethicallifeprotips','fightporn','iwantout','holdmybeer','marvel','algotrading','homeautomation','oddlyterrifying','4chan','pawg','fuckyoukaren','worldpolitics','privacy','greentext','digitalnomad','awfuleverything','designporn','toptalent','snowboarding','startledcats','motorcycles','perfectfit','amateur','self','skyrim','zoomies','truegaming','iamverybadass','subredditoftheday','anormaldayinrussia','cfb','skiing','genshin_impact','steam','lipsthatgrip','whyweretheyfilming','onoff','gifsthatkeepongiving','twitch','spacex','freefolk','prorevenge','screenwriting','powerwashingporn','shitty_car_mods','wheredidthesodago','blowjobs','tiktoknsfw','gtaonline','pettyrevenge','juicyasians','boxing','fantheories','ethereum','celebnsfw','imgoingtohellforthis','homebrewing','pornhubcomments','makemesuffer','thatsinsane','wiiu','boneappletea','harrypotter','rocketleague','amd','vagabond','valorant','bossfight','oldpeoplefacebook','nude_selfie','tumblr','trueoffmychest','sadcringe','deepfriedmemes','woooosh','bigasses','animemes','modernwarfare','netflix','nudes','canada','instagramreality','westworld','letsnotmeet']

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

