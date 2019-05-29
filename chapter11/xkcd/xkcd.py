#! python3

import requests, os, bs4

###<div id="comic">
###<img src="//imgs.xkcd.com/comics/swimming.png" title="&quot;You don't know how high above you the sky goes, but you're not freaking out about that.&quot; &quot;Well, NOW I am!&quot;" alt="Swimming" srcset="//imgs.xkcd.com/comics/swimming_2x.png 2x">
###</div>
#<a rel="prev" href="/2154/" accesskey="p">&lt; Prev</a>

#url = 'http://xkcd.com'


url = 'http://xkcd.com/71'
os.makedirs('xkcd', exist_ok=True)
while not url.endswith('#'):
    # download page
    print('Downloading page %s...' % url)
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text)

    # find URL of comic image in bs
    comicElem = soup.select('#comic img')
    if comicElem == []:
        print('Could not find comic image.')
    else:
        try:
            comicUrl = 'http:' + comicElem[0].get('src')
            # Download the image
            print('Downloading image %s...' % comicUrl)
            res = requests.get(comicUrl)
            res.raise_for_status()
        except requests.exceptions.MissingSchema:
            # Skip the comic
            prevLink = soup.select('a[rel="prev"]')[0]
            url = 'http://xkcd.com' + prevLink.get('href')
            continue
    # save img to ./xkcd
    imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
    for chunk in (res.iter_content(100000)):
        imageFile.write(chunk)
    imageFile.close()

    # get Prev button's URL
    prevLink = soup.select('a[rel="prev"]')[0]
    url = 'http://xkcd.com' + prevLink.get('href')
print('Done.')
