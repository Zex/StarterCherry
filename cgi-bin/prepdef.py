#!/usr/bin/env python
#
# cgi-bin/prepdef.py
# Author: Zex <top_zlynch@yahoo.com>
#

def Page(respcode, hint = None):

    ret = """<!DOCTYPE html>
<!--
This page is generated automaticly by prepdef.py
DO NOT CHANGE IT!
-->
<html><head>
<link href="/css/basic.css" rel="stylesheet" type="text/css">
<link href="/img/badsmile.jpg" rel="icon" type="image/jpg">
<meta charset="UTF-8">
<meta http-equiv="refresh" content="3; url=/"/>
<title>Starter</title>
</head><body>
<div class="default_page">
<span>"""+hint+"""\
</span><br>
<a href="/"><img src="/img/detective-office.jpg" alt="Go Back Home"/></a>
<span>Go back home in 3 seconds</span><br>
<span>or</span><br>
<span>Click the background to go back ASAP</span><br>
</div>
</body></html>
"""

    with open('../default/Starter'+str(respcode)+'.html', 'w') as fd:
        fd.write(ret)
