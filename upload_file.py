#!/usr/bin/python

import cgi

fields = cgi.FieldStorage()

print "Content-Type: text/html"
print

print "<html>"
print "<title>",fields["file_name"].value,"</title>"

print "<body>"

#filebuf = fields["file_name"].file.read()
#lines = filebuf.split('\n')

while line = fields["file_name"].file.read():
	print "<p><b>", line,"</b></p>"



print "</body>"
print "</html>"

