#!/usr/bin/env python
#
# ranseq.py
# Author: Zex <top_zlynch@yahoo.com>

from random import randint#, choice
from string import digits

def ranseq(length):
#    ret += "--------------------------------------------------------->"
#    ancient_a = [int(choice(digits)) for i in xrange(int(length))]
#    ancient_b = [int(choice(digits)) for i in xrange(int(length))]
    ret = "<table class=\"normal\">"

    ancient_a = [randint(1, 1000) for i in xrange(int(length))]
    ancient_b = [randint(1, 1000) for i in xrange(int(length))]

    ret += "<tr class=\"normal\">"
    ret += "<td class=\"normal\">Ancient a: </td><td class=\"normal\"><span contenteditable=\"false\">" + str(ancient_a) + "</span></td>"
    ret += "</tr>"
    ret += "<tr class=\"normal\">"
    ret += "<td class=\"normal\">Ancient b: </td><td class=\"normal\"><span contenteditable=\"false\">" + str(ancient_b) + "</span></td>"
    ret += "</tr>"

    ancient_a.extend(ancient_b)
    ancient_a.sort()

    ret += "<tr class=\"normal\">"
    ret += "<td class=\"normal\">Ancient a: </td><td class=\"normal\"><span contenteditable=\"false\">" + str(ancient_a) + "</span></td>"
    ret += "</tr>"

    child_min = ancient_a[:(len(ancient_a)-2)/2]
    child_max = ancient_a[(len(ancient_a)-2)/2:-2]

    ret += "<tr class=\"normal\">"
    ret += "<td class=\"normal\">child_min: </td><td class=\"normal\"><span contenteditable=\"false\">" + str(child_min) + "</span></td>"
    ret += "</tr>"
    ret += "<tr class=\"normal\">"
    ret += "<td class=\"normal\">child_max: </td><td class=\"normal\"><span contenteditable=\"false\">" + str(child_max) + "</span></td>"
    ret += "</tr>"

    child_min.append(ancient_a[-1])
    child_max.append(ancient_a[-2])

    ret += "<tr class=\"normal\">"
    ret += "<td class=\"normal\">child_min sum: </td><td class=\"normal\"><span contenteditable=\"false\">" + str(reduce(lambda x,y:x+y, child_min)) + "</span></td>"
    ret += "</tr>"
    ret += "<tr class=\"normal\">"
    ret += "<td class=\"normal\">child_max sum: </td><td class=\"normal\"><span contenteditable=\"false\">" + str(reduce(lambda x,y:x+y, child_max)) + "</span></td>"
    ret += "</tr>"
#    ret += "---------------------------------------------------------+"
    ret += "</table>"

    return ret

def reply(cherry):

    req = cherry.request
    title = "Random Seq"
    ret = ''
 
    ret += "<!DOCTYPE html>"
    ret += "<html>"
    
    ret += "<head>"
    ret += "<title>" + title + "</title>"
    ret += "<link href=\"/css/basic.css\" rel=\"stylesheet\" type=\"text/css\">"
    ret += "<link href=\"/img/badsmile.jpg\" rel=\"icon\" type=\"image/jpg\">"
    ret += "<meta charset=\"UTF-8\">"
    ret += "</head><body>"
    
    ret += "<div class=\"navigator\">"
    ret += "<a name=\"Navigator\"><ul>Navigator</ul></a>"
    ret += "<ul>"
    ret += "<li><a href=\"index#Motions\" title=\"Motions\">Motions</a></li>"
    ret += "<li><a href=\"index#RandomSeq\" title=\"Random Seq\">Random Seq</a></li>"
    ret += "<li><a href=\"index#LeaveMessage\" title=\"Leave a Message\">Leave a Message</a></li>"
    ret += "</ul>"
    ret += "</div>"

    ret += "<div id=\"content\">"

    
    ret += "<h2>Welcome, " + req.headers["Remote-Addr"] + "!</h2>"
    ret += "<span>" + req.headers["User-Agent"] + "</span><br>"

    for i in [100, 10, 1000, 999, 3]:
        ret += "<h2>" + "Ranseq with " + str(i) + "</h2>"
        ret += ranseq(i)
    
    ret += "</div>"
    ret += "</body>"
    ret += "</html>"

    return ret

