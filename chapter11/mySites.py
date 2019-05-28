#! python 3

# mySites.py    - opens custom URLs in the web browser.
#               - new URLs can be added by appending them
#                 as command line arguments

import webbrowser, sys, shelve, requests, logging

# logging
logging.basicConfig(level=logging.DEBUG, format= '%(asctime)s - %(levelname)s - %(message)s')
logging.propagate = False

# default URLs:
#urls = ['https://beta.protonmail.com/login','https://github.com/grasshopfer','https://old.reddit.com']

# create save file with shelve
cache = shelve.open('mySites.dat')
args = sys.argv

# load urls from save file
urls = list(cache.values())
logging.debug('got list from cache: ' + str(urls))

# evaluate arguments
#   TODO add support for deleting single or all URLs from shelf
if len(args) > 1:
    newUrls = []
    for url in args[1:]:
        if not url.startswith('https'):
            # prepend https to provided URL
            url = 'https://' + url
            logging.debug('appended https:// to arg url: ' + url)
        if url in urls:
            # url provided on cmdline already on shelf
            logging.debug('found ' + url + ' in url list, continuing')
            continue
        # test provided URL
        r = requests.get(url)
        if r.status_code == 200:
            newUrls.append(url)
        else:
            print('URL provided: (' + url + ') did not respond to http request. The URL was not added') 
    for url in newUrls:
        # add new URL to URL list
        urls.append(url)
        logging.debug('appended arg url: ' + url + ' to urls')

# store urls on shelf
for url in urls:
    if not url in cache.values():
        logging.debug('new value stored to shelf: cache[' + str(len(cache)+1) + '] = ' + url)
        cache[str(len(cache)+1)] = url

# open pages in browser
logging.debug('got list from cache: ' + str(urls))
for url in urls:
    webbrowser.open(url)

cache.close()
