#! python3

import requests, bs4

nwsAbq = 'https://forecast.weather.gov/MapClick.php?lat=35.09104490000004&lon=-106.55847219999998'

res = requests.get(nwsAbq)
res.raise_for_status()

abqSoup = bs4.BeautifulSoup(res.text, features="lxml")

pdiv = abqSoup.select('div p')
print(len(pdiv))
for el in pdiv:
        print(el.getText())
