#!/usr/bin/env python
#
# cgi-bin/whereyoulive_sum.py
# Survay of where my colleagues live
#
# Author: zex <top_zlynch@yahoo.com>
#
# http://localhost:8080/whereyoulive

from redis import Redis#Connection
from socket import gethostname, gethostbyname

# addr -> count
addresses = {}

addr_prefix = 'staff.address'

def preset(sample):

    global addresses

    conn = Redis(host=gethostbyname(gethostname()), port=6379)
#    conn = Redis(host=gethostname(), port=6379)

    if conn.zcard(addr_prefix) == 0:
        with open(sample, 'r') as fd:
            addresses = { p.split('\n')[0]:0 for p in fd.readlines() }

        for k, v in addresses.items():
            conn.zadd(addr_prefix, k, v)

    else:
        for x in conn.zrange(addr_prefix, 0, conn.zcard(addr_prefix)):
            addresses[x] = int(conn.zscore(addr_prefix, x))

    conn.save()

def whereyoulive(addr):

    conn = Redis(host=gethostname(), port=6379)

    if addresses.has_key(addr):
        addresses[addr] += 1
        conn.zincrby(addr_prefix, addr)

    else:
        addresses[addr] = 1
        conn.zadd(addr_prefix, addr, 1)
        
    conn.save()

def whereyoulive_sum():

    ret = "<table class=\"normal\">"
    ret += "<th class=\"normal\">" + "Address" + "</th>"
    ret += "<th class=\"normal\">" + "Total/Address" + "</th>"

    conn = Redis(host=gethostname(), port=6379)
    vals = []

    for x in conn.zrange(addr_prefix, 0, conn.zcard(addr_prefix)):
        ret += "<tr class=\"normal\">"
        ret += "<td class=\"normal\">" + x + "</td>"
        vals.append(int(conn.zscore(addr_prefix, x)))
        ret += "<td class=\"normal\"><span>" + str(vals[-1]) + "</span></td>"
        ret += "</tr>"

    ret += "<tr align=\"center\"><td class=\"normal\">" + "Sum" + "</td>"
    if len(vals) == 0:
        ret += "<td class=\"normal\">" + "0" + "</td></tr>"
    else:
        ret += "<td class=\"normal\">" + str(reduce(lambda i, j : i+j, [i for i in vals])) + "</td></tr>"
    ret += "</table>"

    return ret

def reply(kwargs = {}):

    title = "WhereYouLive"
    
    ret = "<!DOCTYPE html>"
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

    if kwargs.has_key('addr'):
        whereyoulive(kwargs['addr'])
    elif kwargs.has_key('elseaddr'):
        whereyoulive(kwargs['elseaddr'])
    else:
        ret += "<span>No address selected. <span>Previous Result</span><br>"

    ret += whereyoulive_sum()

    ret += "</div>"
    ret += "</body>"
    ret += "</html>"

    return ret

preset("../res/Addrs.Sample")
