#!/usr/bin/python
#
# Starter.py
# Author: Zex <top_zlynch@yahoo.com>
#

import time

print "Content-Type: text/html\n\n"
print "<!DOCTYPE html>"
print "<html>"

print "<head>"
print "<title>Starter</title>"
print "<link href=\"/css/basic.css\" rel=\"stylesheet\" type=\"text/css\">"
print "<meta charset=\"UTF-8\">"
print "</head>"

print "<body>"
print "<div>"
print "<img src=\"/img/cattail.jpg\" border=0>"
print "</div>"

print "<div>"
print "<form action=\"hello_baby.py\" method=get>"
print "<label><b>Action: </b></label>"
print "<input type=text name=fr_name/>"
print "<input type=\"submit\" value=\"Do IT!\"/><br>"
print "</form>"
print "</div>"

print "<div>"
print "<form action=\"upload_file.py\" method=post enctype=\"multipart/form-data\">"
print "<label><b>Select file: </b></label>"
print "<input type=file name=file_name/>"
print "<input type=\"submit\" value=\"Upload!\"/><br>"
print "</form>"
print "</div>"

print "<table>"

print "<tr>"
print "<td>"
icecreams = [ "Milk", "Chocolate", "Strawberry", "Coconut", "Peanut" ]

print "<form action=\"icecream_box.py\" method=post>"
print "<label><b>Icecream: </b></label><br>"

for i in icecreams:
    print "<input type=checkbox name=\"", i,"\" value=\"1\"/> <b>", i, "</b><br>"

print "<input type=\"submit\" value=\"Done!\"/><br>"
print "</form>"
print "</td>"
print "<td>"

flowers = [ "Almond Blossom", "Balsam", "Anther", "Camellia", "Azalea" ]

print "<form action=\"flower_man.py\" method=post>"
print "<label><b>Flower: </b></label><br>"

for f in flowers:
    print "<input type=radio name=flower value=\"", f,"\"/> <b>", f,"</b><br>"

print "<input type=\"submit\" value=\"Done!\"/><br>"
print "</form>"
print "</td>"
print "</tr>"
print "</table>"

options = [ "Go", "Walk Away", "Close", "Laught" ]
print "<div>"
print "<form action=\"motion_trigger.py\" method=post>"
print "<label for=option><b>Motions: </b></label><br>"
print "<select name=option>"

for o in options:
    print "<option>" + o

print "</select>"
print "<input type=\"submit\" value=\"Done!\"/><br>"
print "</form>"
print "</div>"

print "<div>"
print "<label><b>Current time: </b><label>"
print "<input id=\"cur_time\" type=text rows=30 cols=100 readonly=\"true\" value=\"",time.strftime(time.asctime()), "\"/><br>"
print "</form>"
print "</div>"

print "<div>"
print "<form action=\"leave_message.py\" method=post>"
print "<label for=msgbox><b>Leave a Message: </b></label><br>"
print "<textarea name=\"msgbox\"></textarea><br>"
print "<input type=\"submit\" value=\"Submit\"/><br>"
print "</form>"
print "</div>"

print "</body>"
print "</html>"

