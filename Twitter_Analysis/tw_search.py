import twitter, json

CONSUMER_KEY = '7zHknYNJt0kO7brrxlKAHOvvv'
CONSUMER_SECRET = 'uZAvp0guiUsPPkeRYrFOsxWFErj0HJfLAcYGah48t1Yv0HRIbH'

OAUTH_TOKEN = '19970000-X9DopJ9ItK7ve7e8v5htSx3LKcQ2dN1i9HwZKobSF'
OAUTH_TOKEN_SECRET = 'icUR0gHdI9492KSqTz8QgdIX2NpDFTzb6662i6XLWdVUy'

auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET)

twitter_api = twitter.Twitter(auth=auth)

print(twitter_api)

q = '#coys'

count = 100

search_results = twitter_api.search.tweets(q=q, count=count)

statuses = search_results['statuses']

for _ in range(5):
    print('length of statuses', len(statuses))

try:
    next_results = search_results['search_metadata']['next_results']
except KeyError as e:

    kwargs = dict([kv.split('=') for kv in next_results[1:].split("&")])
    search_results = twitter_api.search.tweets(**kwargs)
    statuses += search_results['statuses']

print(json.dumps(statuses[0], indent=1))
