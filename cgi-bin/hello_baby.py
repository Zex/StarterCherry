#!/usr/bin/python

def reply(fr_name = ''):

    title = "Hello Baby"

    ret = ''
    
    ret += "<!DOCTYPE html>"
    ret += "<html>"
    
    ret += "<head>"
    ret += "<title>" + title + "</title>"
    ret += "<link href=\"/css/basic.css\" rel=\"stylesheet\" type=\"text/css\">"
    ret += "<meta charset=\"UTF-8\">"
    ret += "</head>"
    
    ret += "<body>"
    
    ret += "<p>" + fr_name + "</p>"
    
    ret += "</body>"
    ret += "</html>"

    return ret

