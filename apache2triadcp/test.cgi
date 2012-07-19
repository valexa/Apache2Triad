#!C:/apache2triadpath/perl/bin/perl.exe

print "Content-type: text/html\n\n";
print "<link rel=stylesheet href=style.css>";
print "<center>\n";
print "<span class=span0><span class=span1>\n";
print "<b>CGI Perl is working fine</b>\n";
print "<br><br>\n";
print "<b>server software : </b>$ENV{'SERVER_SOFTWARE'}\n";
print "<br><br>\n";
print "<b>client software : </b>$ENV{'HTTP_USER_AGENT'}\n";
print "<br><br>\n";
print "<b>http referer : </b>$ENV{'HTTP_REFERER'}\n";
print "<br><br>\n";
print "<b>opened file : </b>$ENV{'SCRIPT_FILENAME'}\n";
print "<br><br>\n";
print "<b>server adress :</b>$ENV{'HTTP_HOST'}\n";
print "<br><br>\n";
print "<b>your adress : </b>$ENV{'REMOTE_ADDR'}\n";
print "</span></span>\n";
print "<br>\n";

print "<table width=88% class=table border=0 cellpadding=4 cellspacing=1><tr><td class=tdark ><b>Server Variable</b></td><td class=tdg ><b>Value</b></td></tr>\n";
foreach $var (sort(keys(%ENV))) {
    $val = $ENV{$var};
    $val =~ s|\n|\\n|g;
    $val =~ s|"|\\"|g;
print "<tr><td class=tdd><font size=-1>${var}</font></td>\n";
print "<td class=tdl><font size=-1>${val}&nbsp;</font></td></tr>\n";
}
print "</table></p></font>\n";
print "</center>Written by Vlad Alexa Mancini</html>\n";
exit;