#!/usr/bin/env python
#
# user_info.py
# Author: Zex <top_zlynch@yahoo.com>

config = {}

def create_html(xlsname, sheetname):

    data = {}
    data['userid'] = [23,4,36,14,1,63,123]
    data['useremail'] = [
        'x3sd@sfsf.com',
        'x5sd@sfsf.com',
        'x2sd@sfsf.com',
        'x4sd@sfsf.com',
        'xasd@sfsf.com',
        'x35sd@sfsf.com',
        'x234sd@sfsf.com',
    ]

    from pandas import DataFrame
    ret = ''

    ret += "<label>helo</label>"
    xls = DataFrame(data)
    #xls.to_excel(xlsname, sheetname, index=False)
    return xls.to_html(index=False)

def reply(cherry):

    global config
    config = cherry.config
    req = cherry.request

    title = "User Info"
    
    ret = "<!DOCTYPE html>"
    ret += "<html>"
    
    ret += "<head>"
    ret += "<title>" + title + "</title>"
    ret += "<link href=\"/css/basic.css\" rel=\"stylesheet\" type=\"text/css\">"
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

    buf = create_html(config['/res']['tools.staticdir.dir'] + '/' + 'all-log-pandas.xls', 'user-info')
    for tag in ['table', 'th', 'tr', 'td']:
        buf = buf.replace('<' + tag + ' ', '<' + tag + ' class=\"normal\" ')
    ret += buf
    
    ret += "</div>"
    ret += "</body>"
    ret += "</html>"

    return ret

