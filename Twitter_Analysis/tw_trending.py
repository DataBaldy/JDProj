import twitter

CONSUMER_KEY = '7zHknYNJt0kO7brrxlKAHOvvv'
CONSUMER_SECRET = 'uZAvp0guiUsPPkeRYrFOsxWFErj0HJfLAcYGah48t1Yv0HRIbH'

OAUTH_TOKEN = '19970000-X9DopJ9ItK7ve7e8v5htSx3LKcQ2dN1i9HwZKobSF'
OAUTH_TOKEN_SECRET = 'icUR0gHdI9492KSqTz8QgdIX2NpDFTzb6662i6XLWdVUy'

auth = twitter.oauth.OAuth(OAUTH_TOKEN,OAUTH_TOKEN_SECRET,CONSUMER_KEY,CONSUMER_SECRET)

twitter_api = twitter.Twitter(auth=auth)

print(twitter_api)

WORLD_WOE_ID = 1
US_WOE_ID = 23424977

world_trends = twitter_api.trends.place(_id=WORLD_WOE_ID)
us_trends = twitter_api.trends.place(_id=US_WOE_ID)

print(world_trends)
print
print(us_trends)

world_trends_set = set([trend['name'] for trend in world_trends[0]['trends']])
us_trends_set = set([trend['name'] for trend in us_trends[0]['trends']])

common_trends = world_trends_set.intersection(us_trends_set)

print(common_trends)