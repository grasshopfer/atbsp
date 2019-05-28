#! python3

import webbrowser, sys, requests

# TODO get search keywords from command line args
args = sys.argv
keyword = 'poop'
# TODO retrieve and parse search results page
searchURL = 'https://duckduckgo.com/?q=%s&ia=web' % (keyword)
print(searchURL)
# TODO open a browser tab for the top three results


