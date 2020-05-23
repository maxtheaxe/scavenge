# nwf_testing.py for backyard-hacks-2020 by max
import requests

# cookies = {'ZipCode': '04901'}
cookies = {'npfUser':'ZipCode=07940'}

s = requests.Session()

r = s.get('https://www.nwf.org/nativePlantFinder/plants', cookies=cookies)
# print(r.text)
# '{"cookies": {"from-my": "browser"}}'

# r = s.get('https://www.nwf.org/nativePlantFinder/plants')
print(r.text)
# '{"cookies": {}}'