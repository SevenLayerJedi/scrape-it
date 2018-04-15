import tweepy


def get_api(cfg):
  auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
  auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
  return tweepy.API(auth)


cfg = { 
"consumer_key"        : "XXXXXXXXXXXXXXXXX",
"consumer_secret"     : "XXXXXXXXXXXXXXXXX",
"access_token"        : "XXXXXXXXXXXXXXXXX-XXXXXXXXXXXXXXXXX",
"access_token_secret" : "XXXXXXXXXXXXXXXXX" 
}

api = get_api(cfg)


def tweet_it(tweetString):
    status = api.update_status(status=tweetString)
