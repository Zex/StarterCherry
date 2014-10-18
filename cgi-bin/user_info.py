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

def reply(req):

    global config
    config = req.config

    title = "User Info"
    
    ret = "<!DOCTYPE html>"
    ret += "<html>"
    
    ret += "<head>"
    ret += "<title>" + title + "</title>"
    ret += "<link href=\"/css/basic.css\" rel=\"stylesheet\" type=\"text/css\">"
    ret += "<meta charset=\"UTF-8\">"
    ret += "</head>"
    
    ret += "<body>"
    
    ret += create_html(config['/res']['tools.staticdir.dir'] + '/' + 'all-log-pandas.xls', 'user-info')
    
    ret += "</body>"
    ret += "</html>"

    return ret

