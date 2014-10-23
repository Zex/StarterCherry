#!/usr/bin/python

def reply(req, fr_name = ''):

    title = "Hello Baby"

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
    
    ret += "<p>" + fr_name + "</p>"
    
    ret += "</body>"
    ret += "</html>"

    return ret

