#! python3

# not really curl, but using python to pull webpages

import requests, logging
logging.basicConfig(level=logging.DEBUG, format= '%(asctime)s - %(levelname)s - %(message)s')

rjUrl = 'https://automatetheboringstuff.com/files/rj.txt'

logging.debug('Trying url: ' + rjUrl)
romeo = requests.get(rjUrl)                 # pull down file at url
logging.debug('Status code: ' + str(romeo.status_code))

# save http response to file
outFile = 'Romeo and Juliet.txt'
logging.debug(outFile + ': opening wb')
webFile = open('Romeo and Juliet.txt', 'wb')# wb == write binary. Used to preserve unicode encoding
for block in romeo.iter_content(100000):    # string.iter_content() helps with mem management
    webFile.write(block)                    # more at requests.readthedocs.org/

webFile.close()
