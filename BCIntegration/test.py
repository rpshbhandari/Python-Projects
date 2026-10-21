import requests
import config

res = requests.get(config.BASE_URL + config.PATH, auth=(config.USER, config.PASSWORD), params=config.PARAM)
print(res.json())


