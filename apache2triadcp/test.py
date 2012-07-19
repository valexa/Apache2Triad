#!C:/apache2triadpath/python/bin/python.exe

import os

print "Content-type: text/html\n"

print "<html>"
print "<link rel=stylesheet href=style.css>"
print "<center>"
print "<span class=span0><span class=span1>"

print"<b>CGI Python is working fine</b>"

print"<br><br>"
print"<b>server software : </b>" , os.environ['SERVER_SOFTWARE']
print"<br><br>"
print"<b>client software : </b>" , os.environ['HTTP_USER_AGENT']
print"<br><br>"
print"<b>http referer : </b>" , os.environ['HTTP_REFERER']
print"<br><br>"
print"<b>opened file : </b>" , os.environ['SCRIPT_FILENAME']
print"<br><br>"
print"<b>server adress :</b>" , os.environ['HTTP_HOST']
print"<br><br>"
print"<b>your adress : </b>" , os.environ['REMOTE_ADDR']
print"</span></span>"
print"<br>"

print"<table width=88% class=table border=0 cellpadding=4 cellspacing=1>"
print"<tr><td class=tdark ><b>Server Variable</b></td><td class=tdg ><b>Value</b></td></tr>"

keys = os.environ.keys()
for i in keys:
    keys.sort()
    print "<tr><td class=tdd><font size=-1>" , i , "</font></td>"
    print "<td class=tdl><font size=-1>" , os.environ[i] , "&nbsp;</font></td></tr>"

print"</table></p></font>"

print"</center>Written by Vlad Alexa Mancini</html>"