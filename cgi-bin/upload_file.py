#!/usr/bin/env python

config = {}

def reply(cherry, kwargs = {}):

    global config
    config = cherry.config
    req = cherry.request

    title = kwargs["file_name"].filename
    ret = ''

    ret += "<!DOCTYPE html>"
    ret += "<html>"
    
    ret += "<head> "
    ret += "<title>" + str(title) + "</title>"
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

    ret += "<div class=\"content\">"
    
    for k in kwargs.items():

    	ret += "<b>" + "File Name: " + str(k[1].filename) + "</b><br>"
        ret += "<span contenteditable=\"false\">"

        with open(str(config['/uploads']['tools.staticdir.dir'] + '/' + k[1].filename), 'w') as fd:

            for line in k[1].file.readlines():
             	ret +=  line + "<br>"
                fd.write(line)

        ret += "</span>"

    ret += "div"    
    ret += "</body>"
    ret += "</html>"

    return ret

