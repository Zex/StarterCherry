#!/usr/bin/python

def reply(req, kwargs = {}):

    title = "Motion Trigger"
    ret  = ''
    
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
    
    for k in kwargs.items():
    	ret += "<b>" + k[0].upper() + ": " + k[1] + "</b><br>"
    
    ret += "</body>"
    ret += "</html>"
    
    return ret
