#!/usr/bin/python

def reply(cherry, kwargs = {}):

    req = cherry.request
    title = "Icecream Box"
    ret = ''

    ret += "<!DOCTYPE html>"
    ret += "<html>"
    
    ret += "<head>"
    ret += "<title>" + title + "</title>"
    ret += "<link href=\"/css/basic.css\" rel=\"stylesheet\" type=\"text/css\">"
    ret += "<link href=\"/img/badsmile.jpg\" rel=\"icon\" type=\"image/jpg\">"
    ret += "<meta charset=\"UTF-8\">"
    ret += "</head><body>"
    
    ret += "<div class=\"navigator\">"
    ret += "<a name=\"Navigator\"><ul>Navigator</ul></a>"
    ret += "<ul>"
    ret += "<li><a href=\"index#Motions\" title=\"Motions\">Motions</a></li>"
    ret += "<li><a href=\"index#RandomSeq\" title=\"Random Seq\">Random Seq</a></li>"
    ret += "<li><a href=\"index#LeaveMessage\" title=\"Leave a Message\">Leave a Message</a></li>"
    ret += "</ul>"
    ret += "</div>"

    ret += "<div id=\"content\">"

    ret += "<h2>Welcome, " + req.headers["Remote-Addr"] + "!</h2>"
    ret += "<span>" + req.headers["User-Agent"] + "</span><br>"
    
    for k in kwargs.items():
    	ret += "<b>" + str(k[0]) + "</b><br>"
    ret += "</div>"
    ret += "</body>"
    ret += "</html>"

    return ret
