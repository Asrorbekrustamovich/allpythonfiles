# import requests
# from pprint import pprint
# response=requests.get('https://api.tirikchilik.uz/api/Product/ProductListByCategory')
# print(response.status_code)
# if response.status_code==200:
#     data=response.json()
#     pprint(data)
#NBU request

import requests
import json
from pprint import pprint
response = requests.get("https://nbu.uz/en/exchange-rates/json/")
data = response.json()
file = open("NBU.json", mode="w")
json.dump(data, file, indent=4)
file.close()

print("Data written to NBU.json successfully.")
