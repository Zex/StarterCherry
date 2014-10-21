#!/usr/bin/env python
#
# cgi-bin/whereyoulive_sum.py
# Survay of where my colleagues live
#
# Author: zex <top_zlynch@yahoo.com>
#
# http://localhost:8080/whereyoulive

#TODO: store in redis db

from redis import Redis#Connection
from socket import gethostname

# addr -> count
addresses = {}

addr_prefix = 'staff.address'

def preset(sample):

    global addresses

    conn = Redis(host=gethostname(), port=6379)

    if conn.zcard(addr_prefix) == 0:
        with open(sample, 'r') as fd:
            addresses = { p.split('\n')[0]:0 for p in fd.readlines() }

        for k, v in addresses.items():
            conn.zadd(addr_prefix, k, v)

    else:
        for x in conn.zrange(addr_prefix, 0, conn.zcard(addr_prefix)):
            addresses[x] = int(conn.zscore(addr_prefix, x))


def whereyoulive(addr):

    conn = Redis(host=gethostname(), port=6379)

    if addresses.has_key(addr):
        addresses[addr] += 1
        conn.zincrby(addr_prefix, addr)

    else:
        addresses[addr] = 1
        conn.zadd(addr_prefix, addr, 1)

def whereyoulive_sum():

    ret = "<table>"
    ret += "<th>" + "Address" + "</th>"
    ret += "<th>" + "Total/Address" + "</th>"

    conn = Redis(host=gethostname(), port=6379)
    vals = []

    for x in conn.zrange(addr_prefix, 0, conn.zcard(addr_prefix)):
        ret += "<tr>"
        ret += "<td>" + x + "</td>"
        vals.append(int(conn.zscore(addr_prefix, x)))
        ret += "<td><span>" + str(vals[-1]) + "</span></td>"
        ret += "</tr>"

    ret += "<tr align=\"center\"><td>" + "Sum" + "</td>"
    if len(vals) == 0:
        ret += "<td>" + "0" + "</td></tr>"
    else:
        ret += "<td>" + str(reduce(lambda i, j : i+j, [i for i in vals])) + "</td></tr>"
    ret += "</table>"

    return ret

def reply(kwargs = {}):

    title = "WhereYouLive"
    
    ret = "<!DOCTYPE html>"
    ret += "<html>"
    
    ret += "<head>"
    ret += "<title>" + title + "</title>"
    ret += "<link href=\"/css/basic.css\" rel=\"stylesheet\" type=\"text/css\">"
    ret += "<meta charset=\"UTF-8\">"
    ret += "</head>"
    
    ret += "<body>"

    if kwargs.has_key('addr'):
        whereyoulive(kwargs['addr'])
    elif kwargs.has_key('elseaddr'):
        whereyoulive(kwargs['elseaddr'])
    else:
        ret += "<span>No address selected. <span>Previous Result</span><br>"

    ret += whereyoulive_sum()

    ret += "</body>"
    ret += "</html>"

    return ret

preset("../res/Addrs.Sample")
