import tweepy

auth = tweepy.OAuthHandler('Tk2JmDprFZtPd0IA9kZlnm6RJ', 'Ie2Ewf5n87gcYBKPn6Qip8M2GrVyW0L8of4qWALfFDEhWIGFS2')
auth.set_access_token('1252233736931827728-F0p29PBwr7g4FbiNdsqYOIlUM6F5yt', '1pdNgJwimuCwClpbh4lb9HJaRRJCial5NedAWRo1rqABX')

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)