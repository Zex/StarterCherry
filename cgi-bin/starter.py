#!/usr/bin/env python
#
# Starter.py
# Author: Zex <top_zlynch@yahoo.com>
#

# python -c 'for x in dir(__builtins__):print "<"+x+">\n["+x.__doc__+"]\n"' 
# 
# xfile.py
# if __name__ == '__main__':
#    print __file__
# python < xfile.py

#with open('res/Addrs.Sample', 'w') as fd:
#  for x in xrange(50):
#    fd.write(''.join(random.choice(string.ascii_letters+string.digits+' .@') for x in xrange(random.randint(10, 30)))+'\n')

import time
import os
import cherrypy as cherry

import ranseq
import hello_baby
import plotting
import icecream_box
import flower_man
import motion_trigger
import upload_file
import roman_number
import leave_message
import user_info
import youout
import whereyoulive
import whereyoulive_sum

class Starter(object):

    @cherry.expose
    def ranseq(self):
        return ranseq.reply(cherry.request)

    @cherry.expose
    def hello_baby(self, fr_name=''):
        return hello_baby.reply(cherry.request, fr_name)

    @cherry.expose
    def user_info(self):
        return user_info.reply(cherry.request)

    @cherry.expose
    def plotting(self):
        return plotting.reply(cherry.request)

    @cherry.expose
    def icecream_box(self, **kwargs):
        return icecream_box.reply(cherry.request, kwargs)

    @cherry.expose
    def flower_man(self, **kwargs):
        return flower_man.reply(cherry.request, kwargs)

    @cherry.expose
    def motion_trigger(self, **kwargs):
        return motion_trigger.reply(cherry.request, kwargs)

    @cherry.expose
    def upload_file(self, **kwargs):
        return upload_file.reply(cherry.request, kwargs)

    @cherry.expose
    def roman_number(self, **kwargs):
        return roman_number.reply(cherry.request, kwargs)

    @cherry.expose
    def leave_message(self, **kwargs):
        return leave_message.reply(cherry.request, kwargs)

    @cherry.expose
    def youout(self, **kwargs):
        return youout.reply(kwargs)

    @cherry.expose
    def whereyoulive(self, **kwargs):
        return whereyoulive.reply(cherry.request, kwargs)

    @cherry.expose
    def whereyoulive_sum(self, **kwargs):
        return whereyoulive_sum.reply(kwargs)

    @cherry.expose
    @cherry.tools.gzip()
    def index(self):

        ret = ''
        ret += "<!DOCTYPE html>"
        ret += "<html>"
        
        ret += "<head>"
        ret += "<title>Starter</title>"
        ret += "<link href=\"/css/basic.css\" rel=\"stylesheet\" type=\"text/css\">"
        ret += "<meta charset=\"UTF-8\">"
        ret += "</head>"
        
        ret += "<body>"
        ret += "<div>"
        ret += "<img src=\"/img/cattail.jpg\" height=200px>"
        ret += "</div>"
        
        ret += "<div>"
        ret += "<form action=\"hello_baby\" method=get>"
        ret += "<label><b>Action: </b></label>"
        ret += "<input type=\"text\" name=\"fr_name\"/>"
        ret += "<input type=\"submit\" value=\"Do IT!\"/><br>"
        ret += "</form>"
        ret += "</div>"
        
        ret += "<div>"
        ret += "<form action=\"upload_file\" method=post enctype=\"multipart/form-data\">"
        ret += "<label><b>Select file: </b></label>"
        ret += "<input type=\"file\" name=\"file_name\"/>"
        ret += "<input type=\"submit\" value=\"Upload!\"/><br>"
        ret += "</form>"
        ret += "</div>"
        
        ret += "<table>"
        
        ret += "<tr>"
        ret += "<td>"
        icecreams = [ "Milk", "Chocolate", "Strawberry", "Coconut", "Peanut" ]
        
        ret += "<form action=\"icecream_box\" method=post>"
        ret += "<label><b>Icecream: </b></label><br>"
        
        for i in icecreams:
            ret += "<input type=checkbox name=\"" + str(i) + "\" value=\"1\"/> <b>" + str(i) + "</b><br>"
        
        ret += "<input type=\"submit\" value=\"Done!\"/><br>"
        ret += "</form>"
        ret += "</td>"
        ret += "<td>"
        
        flowers = [ "Almond Blossom", "Balsam", "Anther", "Camellia", "Azalea" ]
        
        ret += "<form action=\"flower_man\" method=post>"
        ret += "<label><b>Flower: </b></label><br>"
        
        for f in flowers:
            ret += "<input type=\"radio\" name=\"flower\" value=\"" + str(f) + "\"/> <b>" + str(f) + "</b><br>"
        
        ret += "<input type=\"submit\" value=\"Done!\"/><br>"
        ret += "</form>"
        ret += "</td>"
        ret += "</tr>"
        ret += "</table>"
        
        options = [ "Go", "Walk Away", "Close", "Laught" ]
        ret += "<div>"
        ret += "<form action=\"motion_trigger\" method=post>"
        ret += "<label for=option><b>Motions: </b></label><br>"
        ret += "<select name=option>"
        
        for o in options:
            ret += "<option>" + o
        
        ret += "</select>"
        ret += "<input type=\"submit\" value=\"Done!\"/><br>"
        ret += "</form>"
        ret += "</div>"
        
        ret += "<div>"
        ret += "<label><b>Current time: </b><label>"
        ret += "<input id=\"cur_time\" type=text rows=30 cols=100 readonly=\"true\" value=\"" + time.strftime(time.asctime()) + "\"/><br>"
        ret += "</form>"
        ret += "</div>"
        
        ret += "<div>"
        ret += "<form action=\"leave_message\" method=post>"
        ret += "<label for=msgbox><b>Leave a Message: </b></label><br>"
        ret += "<textarea id=\"msgbox\" name=\"msgbox\"></textarea><br>"
        ret += "<input type=\"submit\" value=\"Submit\"/><br>"
        ret += "</form>"
        ret += "</div>"
        
        ret += "<table>"
        ret += "<tr>"
        ret += "<td>"
        ret += "<form action=\"user_info\" method=get>"
        ret += "<input type=\"submit\" value=\"User Info\"/><br>"
        ret += "</form>"
        ret += "</td>"
        
        ret += "<td>"
        ret += "<form action=\"ranseq\" method=get>"
        ret += "<input type=\"submit\" value=\"Random Seq\"/><br>"
        ret += "</form>"
        ret += "</td>"
        
        ret += "<td>"
        ret += "<form action=\"roman_number\" method=get>"
        ret += "<span>Arabic/Roman Number </span><input name=\"rnum\" type=\"text\"/><br>"
        ret += "</form>"
        ret += "</td>"
        
        ret += "<td>"
        ret += "<form action=\"plotting\" method=post>"
        ret += "<input type=\"submit\" value=\"Plot\"/><br>"
        ret += "</form>"
        ret += "</td>"
        
        for i in xrange(1):
            ret += "<td>"
            ret += "<form action=\"hello_baby.py\" method=get>"
            ret += "<input type=\"submit\" value=\"TOBE CONTINUE...\"/><br>"
            ret += "</form>"
            ret += "</td>"
        
        ret += "</tr>"
        ret += "</table>"
        
        ret += "</body>"
        ret += "</html>"

        return ret

if __name__ == '__main__':

    conf = {
        '/': {
            'tools.sessions.on': True,
            'tools.staticdir.root': os.path.abspath(os.getcwd()),
        },
        '/css': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': '../css'
        },
        '/img': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': '../img'
        },
        '/res': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': '../res'
        },
        '/uploads': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': '../uploads'
        }
    }

    from socket import gethostname

#    cherry.server.bind_addr = (gethostname(), 7777)
    cherry.server.bind_addr = ('192.168.0.116', 7777)
    cherry.quickstart(Starter(), '/', conf)

#    server1 = cherry._cpwsgi.CPWSGIServer()
#    server1.bind_addr = (gethostname(), 7777)
#
#    server2 = cherry._cpwsgi.SCPWSGIServer()
#    server2.bind_addr = (gethostname(), 11119)
#
#    cherry.server.httpservers = {
#        server1 : (gethostname(), 7777),
#        server2 : (gethostname(), 11119)
#    }
#
#    cherry.server.start()
