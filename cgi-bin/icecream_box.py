#!/usr/bin/python

import cgi

fields = cgi.FieldStorage()
title = "Icecream Box"

print "Content-Type: text/html\n\n"
print "<!DOCTYPE html>"
print "<html>"

print "<head>"
print "<title>", title, "</title>"
print "<link href=\"/css/basic.css\" rel=\"stylesheet\" type=\"text/css\">"
print "<meta charset=\"UTF-8\">"
print "</head>"

print "<body>"

for k in fields.keys():
	print "<b>", k.upper(), "</b>", fields[k].value,"<br>"

print "</body>"
print "</html>"

