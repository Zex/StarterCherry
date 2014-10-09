#!/usr/bin/python

import socket

print "Content-Type: text/html"
print
print "<html>"
print "<title>Starter</title>"
print "<body>"

print "<img src=\"./img/cattail.jpg\">"

print "<form action=\"hello_baby.py\" method=get>"
print "<b>Action: </b>"
print "<input type=text name=fr_name/>"
print "<input type=submit value=\"Do IT!\"/></br>"
print "</form>"

print "<form action=\"upload_file.py\" method=post enctype=\"multipart/form-data\">"
print "<b>Select file: </b>"
print "<input type=file name=file_name/>"
print "<input type=submit value=\"Upload!\"/></br>"
print "</form>"

icecreams = [ "Milk", "Chocolate", "Strawberry", "Coconut", "Peanut" ]

print "<form action=\"icecream_box.py\" method=post>"
print "<b>Icecream: </b></br>"

for i in icecreams:
	print "<input type=checkbox name=\"", i,"\" value=\"1\"/> <b>", i, "</b></br>"

print "<input type=submit value=\"Done!\"/></br>"
print "</form>"

flowers = [ "Almond Blossom", "Balsam", "Anther", "Camellia", "Azalea" ]

print "<form action=\"flower_man.py\" method=post>"
print "<b>Flower: </b></br>"

for f in flowers:
	print "<input type=radio name=flower value=\"", f,"\"/> <b>", f,"</b></br>"

print "<input type=submit value=\"Done!\"/></br>"
print "</form>"

options = [ "Go", "Walk Away", "Close", "Laugh" ]

print "<form action=\"motion_trigger.py\" method=post>"
print "<b>Motions: </b></br>"
print "<select name=option>"

for o in options:
	print "<option value=\"", o, "\">", o

print "<input type=submit value=\"Done!\"/></br>"
print "</select>"
print "</form>"


print "</body>"
print "</html>"

