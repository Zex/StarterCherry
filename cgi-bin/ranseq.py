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
    ret = "<table>"

    ancient_a = [randint(1, 1000) for i in xrange(int(length))]
    ancient_b = [randint(1, 1000) for i in xrange(int(length))]

    ret += "<tr>"
    ret += "<td>Ancient a: </td><td><span contenteditable=\"false\">" + str(ancient_a) + "</span></td>"
    ret += "</tr>"
    ret += "<tr>"
    ret += "<td>Ancient b: </td><td><span contenteditable=\"false\">" + str(ancient_b) + "</span></td>"
    ret += "</tr>"

    ancient_a.extend(ancient_b)
    ancient_a.sort()

    ret += "<tr>"
    ret += "<td>Ancient a: </td><td><span contenteditable=\"false\">" + str(ancient_a) + "</span></td>"
    ret += "</tr>"

    child_min = ancient_a[:(len(ancient_a)-2)/2]
    child_max = ancient_a[(len(ancient_a)-2)/2:-2]

    ret += "<tr>"
    ret += "<td>child_min: </td><td><span contenteditable=\"false\">" + str(child_min) + "</span></td>"
    ret += "</tr>"
    ret += "<tr>"
    ret += "<td>child_max: </td><td><span contenteditable=\"false\">" + str(child_max) + "</span></td>"
    ret += "</tr>"

    child_min.append(ancient_a[-1])
    child_max.append(ancient_a[-2])

    ret += "<tr>"
    ret += "<td>child_min sum: </td><td><span contenteditable=\"false\">" + str(reduce(lambda x,y:x+y, child_min)) + "</span></td>"
    ret += "</tr>"
    ret += "<tr>"
    ret += "<td>child_max sum: </td><td><span contenteditable=\"false\">" + str(reduce(lambda x,y:x+y, child_max)) + "</span></td>"
    ret += "</tr>"
#    ret += "---------------------------------------------------------+"
    ret += "</table>"

    return ret

def reply(req):

    title = "Random Seq"
    ret = ''
 
    ret += "<!DOCTYPE html>"
    ret += "<html>"
    
    ret += "<head>"
    ret += "<title>" + title + "</title>"
    ret += "<link href=\"/css/basic.css\" rel=\"stylesheet\" type=\"text/css\">"
    ret += "<link href=\"/img/badsmile.jpg\" rel=\"icon\" type=\"image/jpg\">"
    ret += "<meta charset=\"UTF-8\">"
    ret += "</head>"
    
    ret += "<body>"
    
    ret += "<h2>Welcome, " + req.headers["Remote-Addr"] + "!</h2>"
    ret += "<span>" + req.headers["User-Agent"] + "</span><br>"

#    for item in req.headers.items():
#        ret += "<span>" + item[0] + ": </span>"
#        ret += "<span>" + item[1] + "</span><br>"

    for i in [100, 10, 1000, 999, 3]:
        ret += "<h2>" + "Ranseq with " + str(i) + "</h2>"
        ret += ranseq(i)
    
    ret += "</body>"
    ret += "</html>"

    return ret

