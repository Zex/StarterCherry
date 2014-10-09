#!/usr/bin/python

import cgi

fields = cgi.FieldStorage()
title = "Hello Baby"

print "Content-Type: text/html"
print

print "<html>"
print "<title>", title, "</title>"

print "<body>"

for k in fields.keys():
	print k, fields[k].value

print "</body>"
print "</html>"

