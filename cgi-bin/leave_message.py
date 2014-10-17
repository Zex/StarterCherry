#!/usr/bin/python

import time

def reply(req, kwargs = {}):

    title = "Message Box"
    
    ret = "<!DOCTYPE html>"
    ret += "<html>"
    
    ret += "<head>"
    ret += "<title>" + title + "</title>"
    ret += "<link href=\"/css/basic.css\" rel=\"stylesheet\" type=\"text/css\">"
    ret += "<meta charset=\"UTF-8\">"
    ret += "</head>"
    
    ret += "<body>"
    
    ret += "<span>" + "Message from " + req.remote.ip + ": " + str(req.remote.port)
    ret += " " + time.strftime(time.asctime())
    ret += "</span>"

    ret += "<textarea readonly=\"true\">"
    ret += kwargs['msgbox']
    ret += "</textarea>"

    ret += "</body>"
    ret += "</html>"

    return ret
