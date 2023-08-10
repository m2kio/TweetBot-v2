from logger import logger
import requests

def get_random_prayer(length: int = 280) -> str:
  '''
  Get a random prayer from https://api.du3aa.rest
  '''
  try:
    # request
    response = requests.get('https://api.du3aa.rest')
    data = response.json()['prayer']

    # check data length, return prayer if all is good
    if(len(data) > length or len(data) == 0 or data is None):
      logger.info('Re-requesting a random prayer')
      get_random_prayer(length)
    else:
      return data

  except Exception as e:
    logger.error(f'Exception occured while requesting prayer from https://api.du3aa.rest, trying again: {e}')
    get_random_prayer(length)
