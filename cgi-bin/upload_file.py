#!/usr/bin/env python

config = {}

def reply(req, kwargs = {}):

    global config
    config = req.config

    title = kwargs["file_name"].filename
    ret = ''

    ret += "<!DOCTYPE html>"
    ret += "<html>"
    
    ret += "<head> "
    ret += "<title>" + str(title) + "</title>"
    ret += "<link href=\"/css/basic.css\" rel=\"stylesheet\" type=\"text/css\">"
    ret += "<meta charset=\"UTF-8\">"
    ret += "</head>"
    
    ret += "<body>"
    
    for k in kwargs.items():

    	ret += "<b>" + "File Name: " + str(k[1].filename) + "</b><br>"
        ret += "<span contenteditable=\"false\">"

        with open(str(config['/uploads']['tools.staticdir.dir'] + '/' + k[1].filename), 'w') as fd:

            for line in k[1].file.readlines():
             	ret +=  line + "<br>"
                fd.write(line)

        ret += "</span>"
    
    ret += "</body>"
    ret += "</html>"

    return ret

