#!/usr/bin/python

def reply(req, kwargs = {}):

    title = "Flower Man"
    ret = ''
    
    ret += "<!DOCTYPE html>"
    ret += "<html>"
    
    ret += "<head>"
    ret += "<title>" + title + "</title>"
    ret += "<link href=\"/css/basic.css\" rel=\"stylesheet\" type=\"text/css\">"
    ret += "<meta charset=\"UTF-8\">"
    ret += "</head>"
    
    ret += "<body>"
    ret += "<h2>Welcome, " + req.headers["Remote-Addr"] + "!</h2>"
    ret += "<span>" + req.headers["User-Agent"] + "</span><br>"
    
    for k in kwargs.items():
    	ret += "<b>" + str(k[0]).upper() + ': ' + str(k[1]) + "</b><br>"
    
    ret += "</body>"
    ret += "</html>"

    return ret
