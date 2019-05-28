#! python3

import webbrowser

html = '<strong>Hello</strong> world!'
outfile = 'some.html'

writer = open(outfile,'w')
writer.write(html)
writer.close()

webbrowser.open(outfile)
