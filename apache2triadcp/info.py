#!C:/apache2triadpath/python/bin/python.exe

print "Content-type: text/html"

#
# general info
#

import sys
import platform

print """
      <html><link rel=stylesheet href=style.css>
      <h2 align=center>general info</h2>
      <p>
      <table class=table border=0 cellpadding=4 cellspacing=1 width=100%>
             <tr>
                 <td width=35% class=tdd><b>python version:</b></td>
                 <td width=65% class=tdl>""" , platform._sys_version()[0] , """</td>
             </tr>
             <tr>
                 <td class=tdd><b>python compiled on:</b></td>
                 <td class=tdl>""" , platform.python_compiler() , """</td>
             </tr>
             <tr>
                 <td class=tdd><b>python executable:</b></td>
                 <td class=tdl>""" , sys.executable , """</td>
             </tr>
             <tr>
                 <td class=tdd><b>location of python:</b></td>
                 <td class=tdl>""" , sys.exec_prefix , """</td>
             </tr>
             <tr>
                 <td class=tdd><b>include paths:</b></td>
                 <td class=tdl>""" , sys.prefix , """</td>
             </tr>
"""

print """
      </table>
"""

#
# environment variables
#

import os

print """
        <h2 align=center>environment variables</h2><table class=table border=0 cellpadding=4 cellspacing=1 width=100%>
        <tr><td class=tdark ><b>Server Variable</b></td><td class=tdg ><b>Value</b></td></tr>
"""

keys = os.environ.keys()
for i in keys:
        print "<tr><td width=35% class=tdd><font size=-1>" , i , "<font></td>\n"
        print "<td width=65% class=tdl><font size=-1>" , os.environ[i] , "&nbsp;<font></td></tr>\n"

print """
      </table>
"""

#
# python modules
#

import pydoc
from string import find

modules = {}
def callback(path, modname, desc, modules=modules):
    if modname and modname[-9:] == '.__init__':
        modname = modname[:-9] + ' (package)'
    if find(modname, '.') < 0:
        modules[modname] = 1
pydoc.ModuleScanner().run(callback)
mods = modules.keys()

print """
      <h2 align=center>python modules</h2><table class=table border=0 cellpadding=4 cellspacing=1 width=100%>
"""

count = 0
for i in mods:
      count = count + 1
      if count == 1:
         print "<tr><td class=tdl>" ,i , "</td>\n";
      if count == 2:
         print "<td class=tdl>" ,i , "</td>\n";
      if count == 3:
         print "<td class=tdl>" ,i , "</td></tr>\n";
         count = 0

print """
      </table></html>
"""
