#!/usr/bin/env python
#
# ranseq.py
# Author: Zex <top_zlynch@yahoo.com>

from random import randint#, choice
from string import digits

def ranseq(length):
#    print "--------------------------------------------------------->"
#    ancient_a = [int(choice(digits)) for i in xrange(int(length))]
#    ancient_b = [int(choice(digits)) for i in xrange(int(length))]
    ancient_a = [randint(1, 1000) for i in xrange(int(length))]
    ancient_b = [randint(1, 1000) for i in xrange(int(length))]

    print "<label>Ancient a: </label><p><span contenteditable=\"false\">", ancient_a, "</span></p>"
    print "<label>Ancient b: </label><p><span contenteditable=\"false\">", ancient_b, "</span></p>"

    ancient_a.extend(ancient_b)
    ancient_a.sort()

    print "<label>Ancient a: </label><p><span contenteditable=\"false\">", ancient_a, "</span></p>"

    child_min = ancient_a[:(len(ancient_a)-2)/2]
    child_max = ancient_a[(len(ancient_a)-2)/2:-2]

    print "<label>child_min: </label><p><span contenteditable=\"false\">", child_min, "</span></p>"
    print "<label>child_max: </label><p><span contenteditable=\"false\">", child_max, "</span></p>"

    child_min.append(ancient_a[-1])
    child_max.append(ancient_a[-2])

    print "<label>child_min sum: </label><p><span contenteditable=\"false\">", reduce(lambda x,y:x+y, child_min), "</span></p>"
    print "<label>child_max sum: </label><p><span contenteditable=\"false\">", reduce(lambda x,y:x+y, child_max), "</span></p>"
#    print "---------------------------------------------------------+"

def reply():
    import cgi
    title = "Random Seq"
    
    print "Content-Type: text/html\n\n"
    print "<!DOCTYPE html>"
    print "<html>"
    
    print "<head>"
    print "<title>", title, "</title>"
    print "<link href=\"/css/basic.css\" rel=\"stylesheet\" type=\"text/css\">"
    print "<meta charset=\"UTF-8\">"
    print "</head>"
    
    print "<body>"
    
    print "<table>"
    for i in [100, 10, 1000, 999, 3]:
        print "<tr><td>"
        ranseq(i)
        print "</td></tr>"
    print "</table>"
    
    print "</body>"
    print "</html>"

reply()
