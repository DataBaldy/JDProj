__author__ = 'Jon'

import twitter

consumer_key = '7zHknYNJt0kO7brrxlKAHOvvv'

consumer_secret = 'uZAvp0guiUsPPkeRYrFOsxWFErj0HJfLAcYGah48t1Yv0HRIbH'

oauth_token = '19970000-X9DopJ9ItK7ve7e8v5htSx3LKcQ2dN1i9HwZKobSF'

oauth_token_secret = 'icUR0gHdI9492KSqTz8QgdIX2NpDFTzb6662i6XLWdVUy'

auth = twitter.oauth.OAuth(oauth_token,oauth_token_secret,consumer_key,consumer_secret)

twitter_api = twitter.Twitter(auth=auth)

print(twitter_api)

WORLD_WOE_ID = 1
US_WOE_ID = 23424977

world_trends = twitter_api.trends.place(_id=WORLD_WOE_ID)
us_trends = twitter_api.trends.place(_id=US_WOE_ID)

print(world_trends)
print(us_trends)

import json

records = [json.loads(line) for line in open(world_trends)]