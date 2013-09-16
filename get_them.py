#!/usr/bin/python
import urllib2
import sys
import HTMLParser

heads = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) \
          AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64',
         'Accept': 'text/html,application/xhtml+xml, \
          application/xml;q=0.9,*/*;q=0.8',
         'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
         'Accept-Encoding': 'none',
         'Accept-Language': 'en-US,en;q=0.8',
         'Connection': 'keep-alive'}
current_quote = 1
html_parser = HTMLParser.HTMLParser()
while current_quote < int(sys.argv[1]):
    request = urllib2.Request('http://bash.org/?' + str(current_quote), headers=heads)
    f = urllib2.urlopen(request)
    # read html from url
    html = f.read()
    # remove multiple spaces (for better looking results)
    html = " ".join(html.split())

    result = html.find('<p class="qt">', 0)
    if result != -1:
        first_found = html[result + 14:result + 400]
        result2 = first_found.find('</td>', 0)
        second_found = first_found[0:result2]
        second_found = "\n".join(second_found.split("<br />"))
        second_found = "".join(second_found.split("</p>"))
        print " Link to post: http://bash.org/?" + str(current_quote)
        print " ============================================"
        print " " + html_parser.unescape(second_found)
        print " ==================================================="
    current_quote += 1
