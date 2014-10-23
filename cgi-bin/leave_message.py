#!/usr/bin/python

import time
from redis import Connection
from socket import gethostname

msg_prefix = 'custom.message.'

def insert_msg(cust, tm, msg):

    conn = Connection(host=gethostname(),port=6379)
    conn.send_command('set', msg_prefix+cust+'--'+tm, msg)

    conn.disconnect()

def read_msg():

    ret = ''

    conn = Connection(host=gethostname(),port=6379)
    conn.send_command('keys', msg_prefix+'*')
    keys = conn.read_response()
    vals = []

    if len(keys) != 0:
        conn.send_command('mget', *keys)
        vals = conn.read_response()

        ret += "<h2>" + "Message log" + "</h2>"

        for k, v in zip(keys, vals):
            ret += "<span>" + k.replace(msg_prefix, '').replace('--', ' ') + "</span>"
            ret += "<pre readonly=\"true\">" + v + "</pre>"

    conn.disconnect()
    ret += "<br>"

    return ret

def reply(req, kwargs = {}):

    title = "Message Box"
    
    ret = "<!DOCTYPE html>"
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
    
    if kwargs.has_key('msgbox'):
        insert_msg(req.remote.ip, time.strftime(time.asctime()), kwargs['msgbox'])
        #insert_msg(req.remote.ip+':'+str(req.remote.port), time.strftime(time.asctime()), kwargs['msgbox'])

    ret += read_msg()

    ret += "</body>"
    ret += "</html>"

    return ret
