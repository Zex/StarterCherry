#!/usr/bin/env python
#
# cgi-bin/whereyoulive_sum.py
# Survay of where my colleagues live
#
# Author: zex <top_zlynch@yahoo.com>
#
# http://localhost:8080/whereyoulive_sum

#TODO: store in redis db

# addr -> count

addresses = {}

def preset(sample):

    global addresses

    with open(sample, 'r') as fd:
        addresses = { p:0 for p in fd.readlines() }

    addresses[''] = 0;

def whereyoulive(addr):

    if addresses.has_key(addr):

        addresses[addr] += 1

    else:
        addresses[addr] = 1

def whereyoulive_sum():

    ret = '<table>'
    ret += '<th>' + "Address" + '</th>'
    ret += '<th>' + "Total" + '</th>'

    for a in addresses.items():
        if len(a[0]) == 0: continue
        ret += "<tr>"
        ret += "<td>" + str(a[0]) + "</td>"
        ret += "<td><span>" + str(a[1]) + "</span></td>"
        ret += "</tr>"

    ret += '</table>'

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

    if len(kwargs['addr']) == 0:
        whereyoulive(kwargs['elseaddr'])
    else:
        whereyoulive(kwargs['addr'])

    ret += whereyoulive_sum()

    ret += "</body>"
    ret += "</html>"

    return ret

preset("../res/Addrs.Sample")
