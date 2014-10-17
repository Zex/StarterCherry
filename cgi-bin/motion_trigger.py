#!/usr/bin/python

def reply(kwargs = {}):

    title = "Motion Trigger"
    ret  = ''
    
    ret += "<!DOCTYPE html>"
    ret += "<html>"
    
    ret += "<head>"
    ret += "<title>" + title + "</title>"
    ret += "<link href=\"/css/basic.css\" rel=\"stylesheet\" type=\"text/css\">"
    ret += "<meta charset=\"UTF-8\">"
    ret += "</head>"
    
    ret += "<body>"
    
    for k in kwargs.items():
    	ret += "<b>" + k[0].upper() + ": " + k[1] + "</b><br>"
    
    ret += "</body>"
    ret += "</html>"
    
    return ret
