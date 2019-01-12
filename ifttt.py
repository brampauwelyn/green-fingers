import requests
from config import IFTTT_KEY

def notify():
  event_name = 'WaterPlants'
  url = 'https://maker.ifttt.com/trigger/{}/with/key/{}'.format(event_name, IFTTT_KEY)
  request = requests.get(url)
