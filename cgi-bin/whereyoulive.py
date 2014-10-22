#!/usr/bin/env python
#
# cgi-bin/whereyoulive.py
# Survay of where colleagues live
#
# Author: zex <top_zlynch@yahoo.com>
#
# http://localhost:8080/whereyoulive

import whereyoulive_sum

def survey(req, kwargs = {}):

    title = "WhereYouLive"
    
    ret = "<!DOCTYPE html>"
    ret += "<html>"
    
    ret += "<head>"
    ret += "<title>" + title + "</title>"
    ret += "<link href=\"/css/basic.css\" rel=\"stylesheet\" type=\"text/css\">"
    ret += "<meta charset=\"UTF-8\">"
    ret += "</head>"
    
    ret += "<body>"
    ret += "<h2>Welcome, " + req.headers["Remote-Addr"] + "!</h2>"
    ret += "<span>" + req.headers["User-Agent"] + "</span><br><br>"
  
    ret += "<form action=\"whereyoulive\" method=\"post\">" 

    for a in whereyoulive_sum.addresses.items():
        ret += "<input type=\"radio\" name=\"addr\" value=\"" + str(a[0]) + "\"/> <b>" + str(a[0]) + "</b><br>"

    ret += "<label for=\"elseaddr\">" + "Somewhere Else ..." + "</label><br>"
    ret += "<input type=\"text\" name=\"elseaddr\"/><br>"
    ret += "</form>"
    
    ret += "</body>"
    ret += "</html>"

    return ret

def reply(req, kwargs = {}):

    if kwargs.has_key('addr') or kwargs.has_key('elseaddr'):
        return whereyoulive_sum.reply(kwargs)
    else:
        return survey(req, kwargs)


