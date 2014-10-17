#!/usr/bin/env python
#
# cgi-bin/youout.py
# Solution to the YouOut game
#
# Author: zex <top_zlynch@yahoo.com>
#
# http://localhost:8080/youout?total_player=15&unlucky_n=3
# http://localhost:8080/youout?total_player=710&unlucky_n=43

def youout(total, n):

    cur = 0
    n -= 1
    a = range(1, total+1)

    while len(a) > 1:

        cur = (cur + n) % len(a)
        a.pop(cur)

    return str(a)

def reply(kwargs = {}):

    title = "YouOut!"
    
    ret = "<!DOCTYPE html>"
    ret += "<html>"
    
    ret += "<head>"
    ret += "<title>" + title + "</title>"
    ret += "<link href=\"/css/basic.css\" rel=\"stylesheet\" type=\"text/css\">"
    ret += "<meta charset=\"UTF-8\">"
    ret += "</head>"
    
    ret += "<body>"
    
    ret += "<div>"
    ret += "<label for=total_player><b>Total player: </b></label>"
    ret += "<input type=text name=\"total_player\" readonly=\"true\" value=\"" + kwargs['total_player'] + "\"/><br>"
    ret += "</div>"
    ret += "<div>"
    ret += "<label for=\"unlucky_n\"><b>Unlucky N: </b></label>"
    ret += "<input type=text name=\"unlucky_n\" readonly=\"true\" value=\"" + kwargs['unlucky_n'] + "\"/><br>"
    ret += "</div>"
    ret += "<div>"
    ret += "<label><b>Lucky Dog: </b><label>"
    ret += "<label><b>" + youout(int(kwargs['total_player']), int(kwargs['unlucky_n'])) + "</b></label><br>"
    ret += "</div>"
    
    ret += "</body>"
    ret += "</html>"

    return ret

#if __name__ == '__main__':
#    youout(15, 3)
#    ret += ":----------------------------------"
#    youout(15, 4)
#    ret += ":----------------------------------"
#    youout(20, 7)
#    ret += ":----------------------------------"
#    youout(177, 11)
#    ret += ":----------------------------------"
#    youout(3, 11)

