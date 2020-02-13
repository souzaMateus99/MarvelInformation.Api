import requests
import datetime
import hashlib
import json


today = datetime.datetime.today().utcnow()
date = today.strftime('%b, %d %Y %H:%M:%S GMT')

url_base = 'https://gateway.marvel.com:443'

timestamp = datetime.datetime.timestamp(today)
private_key = '5844d0617fc42fc2cac7fbfb07f2db028e6b3664'
public_key = '060b578530b0a64c9e325b2c90defa42'

generate_hash = str(timestamp) + private_key + public_key
md5_hash = hashlib.md5(generate_hash.encode()).hexdigest()


response = requests.get(
    url = url_base + '/v1/public/characters',
    params=[('ts', timestamp), ('apikey', public_key), ('hash', md5_hash), ('limit', 10), ('orderBy', 'name')],
    headers = {'Content-Type': 'application/json; charset=utf-8', 'Date': date}
)


if response.status_code == 200:
    response_body = json.loads(response.content)['data']['results']
    
    print('id | name')
    
    for item in response_body:
        print(str(item['id']) + ' | ' + item['name'])
else:
    print('error in request')