#!/usr/bin/python

import cgi

fields = cgi.FieldStorage()
title = fields["file_name"].value

print "Content-Type: text/html\n\n"
print "<!DOCTYPE html>"
print "<html>"

print "<head>"
print "<title>", title,"</title>"
print "<link href=\"/css/basic.css\" rel=\"stylesheet\" type=\"text/css\">"
print "<meta charset=\"UTF-8\">"
print "</head>"

print "<body>"

#filebuf = fields["file_name"].file.read()
#lines = filebuf.split('\n')

while line = fields["file_name"].file.read():
	print "<p><b>", line,"</b></p>"



print "</body>"
print "</html>"

