#! python3

import webbrowser, sys, requests, bs4

# TODO get search keywords from command line args

# TODO retrieve and parse search results page
#print('DuckDuckGo...ing...')       # this returns 418 :(
#res = requests.get('http://duckduckgo.com/?q=' + '+'.join(keywords))
res.raise_for_status()

# retrieve top search results
soup = bs4.BeautifulSoup(res.text, "html.parser")
print(soup.text)

linkElems = soup.select('.r a')
# TODO open a browser tab for the top three results

numOpen = min(5, len(linkElems))
print(len(linkElems))
for i in range(numOpen):
    print(numOpen)
    webbrowser.open('http://google.com' + linkElems[i].get('href'))

