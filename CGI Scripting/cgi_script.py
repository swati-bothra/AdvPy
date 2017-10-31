#!/usr/bin/python2
import cgi


print("Content-type:text/html\r\n")
print("<html><body>")
print("<h1>Hey Swati Here!!!</h1>")
form = cgi.FieldStorage()

if form.getvalue("name"):
	print("<p>Name : " + form.getvalue("name")+"</p>")
if form.getvalue("happy"):
	print("<p>m happy!!!!!</p>")
if form.getvalue("sad"):
	print("<p>m Sad!!!!!!</p>")
print("<form method='post' action='cgi_script.py'>")
print("<p>NAME : <input type='text' name='name' /></p>")
print("<input type='checkbox' name='happy'/>Happy")
print("<input  type='checkbox' name='sad'/>Sad")
print("<input type='submit' value='submit'/>")
print("</form>")

print("</body></html>")
