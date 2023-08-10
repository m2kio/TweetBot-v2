from requests_oauthlib import OAuth1Session
from prayer import get_random_prayer
from logger import logger
import os

consumer_key = os.environ.get('CONSUMER_KEY')
consumer_secret = os.environ.get('CONSUMER_SECRET')
access_token = os.environ.get('ACCESS_TOKEN_KEY')
access_token_secret = os.environ.get('ACCESS_TOKEN_SECRET')

def post_tweet():
  '''
  Post a random prayer
  '''
  oauth = OAuth1Session(
    # get them from https://developer.twitter.com
    client_key=consumer_key,
    client_secret=consumer_secret,
    resource_owner_key=access_token,
    resource_owner_secret=access_token_secret,
  )

  # whatever you want to tweet
  prayer = get_random_prayer()
  payload = {"text": prayer}

  # create the tweet
  response = oauth.post(
    "https://api.twitter.com/2/tweets",
    json=payload,
  )

  # check the response 
  if response.status_code == 201:
    logger.info('Tweet posted')
  else:
    raise Exception(f'Posting tweet returned an error: {response.status_code} {response.text}')

if __name__ == '__main__':
  try:
    post_tweet()
  except Exception as e:
    logger.error(f'Exception occured while posting the tweet, trying again: {e}')
    post_tweet()
