#!/usr/bin/env python
#
# cgi-bin/youout.py
# Solution to the YouOut game
#
# Author: zex <top_zlynch@yahoo.com>

import cgi

def youout(total, n):

    cur = 0
    n -= 1
    a = range(1, total+1)

    while len(a) > 1:

        cur = (cur + n) % len(a)
        a.pop(cur)

    return str(a)

if __name__ == '__main__':

    fields = cgi.FieldStorage()
    title = "YouOut!"
    
    print "Content-Type: text/html\n\n"
    print "<!DOCTYPE html>"
    print "<html>"
    
    print "<head>"
    print "<title>", title, "</title>"
    print "<link href=\"/css/basic.css\" rel=\"stylesheet\" type=\"text/css\">"
    print "<meta charset=\"UTF-8\">"
    print "</head>"
    
    print "<body>"
    
    print "<div>"
    print "<label for=total_player><b>Total player: </b></label>"
    print "<input type=text name=\"total_player\" readonly=\"true\" value=\""+fields['total_player'].value+"\"/><br>"
    print "</div>"
    print "<div>"
    print "<label for=\"unlucky_n\"><b>Unlucky N: </b></label>"
    print "<input type=text name=\"unlucky_n\" readonly=\"true\" value=\""+fields['unlucky_n'].value+"\"/><br>"
    print "</div>"
    print "<div>"
    print "<label><b>Lucky Dog: </b><label>"
    print "<label><b>", youout(int(fields['total_player'].value), int(fields['unlucky_n'].value)), "</b></label><br>"
    print "</div>"
    
    print "</body>"
    print "</html>"

#if __name__ == '__main__':
#    youout(15, 3)
#    print ":----------------------------------"
#    youout(15, 4)
#    print ":----------------------------------"
#    youout(20, 7)
#    print ":----------------------------------"
#    youout(177, 11)
#    print ":----------------------------------"
#    youout(3, 11)

