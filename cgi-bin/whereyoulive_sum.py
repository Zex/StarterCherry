#!/usr/bin/env python
#
# cgi-bin/whereyoulive_sum.py
# Survay of where my colleagues live
#
# Author: zex <top_zlynch@yahoo.com>
#
# http://localhost:8080/whereyoulive

#TODO: store in redis db

from redis import Connection
from socket import gethostname

# addr -> count
addresses = {}

addr_prefix = 'staff.address.'

def preset(sample):

    global addresses

    conn = Connection(host=gethostname(),port=6379)

    conn.send_command('keys', addr_prefix+'*')
    keys = conn.read_response()
    vals = []

    if len(keys) == 0:
        with open(sample, 'r') as fd:
            addresses = { p.split('\n')[0]:0 for p in fd.readlines() }

        for k, v in addresses.items():
            conn.send_command('set', addr_prefix+k, v)
            conn.read_response()
    else:
        conn.send_command('mget', *keys)
        vals = conn.read_response()

        for k, v in zip(keys, vals):
            addresses[k.split('.')[-1]] = int(v)

    conn.disconnect()


def whereyoulive(addr):

    if addresses.has_key(addr):
        addresses[addr] += 1

    else:
        addresses[addr] = 1

    Connection(host=gethostname(),port=6379).send_command('set', addr_prefix+addr, addresses[addr])

def whereyoulive_sum():

    ret = "<table>"
    ret += "<th>" + "Address" + "</th>"
    ret += "<th>" + "Total/Address" + "</th>"

# with redis
    conn = Connection(host=gethostname(),port=6379)

    conn.send_command('keys', addr_prefix+'*')
    keys = conn.read_response()

    conn.send_command('mget', *keys)
    vals = conn.read_response()

    conn.disconnect()

    vks = zip(vals, keys)
    vks.sort()

    for item in vks:
        ret += "<tr>"
        ret += "<td>" + str(item[1]).split('.')[-1] + "</td>"
        ret += "<td><span>" + str(item[0]) + "</span></td>"
        ret += "</tr>"

    ret += "<tr align=\"center\"><td>" + "Sum" + "</td>"
    ret += "<td>" + str(reduce(lambda i, j : i+j, [int(i) for i in vals])) + "</td></tr>"
    ret += "</table>"

# with file
#   for item in addresses.items():
#        if len(item[0]) == 0: continue
#        ret += "<tr>"
#        ret += "<td>" + str(item[0]) + "</td>"
#        ret += "<td><span>" + str(item[1]) + "</span></td>"
#        ret += "</tr>"
#    ret += '</table>'


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
