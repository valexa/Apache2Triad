<html>
<link rel=stylesheet href=style.css>
<center>
<span class=span0><span class=span1>

<b><% $Response->Write("ASP is working fine") %></b>

<br><br>
<b>server software : </b><%= $Request->ServerVariables("SERVER_SOFTWARE") %>
<br><br>
<b>client software : </b><%= $Request->ServerVariables("HTTP_USER_AGENT") %>
<br><br>
<b>http referer : </b><%= $Request->ServerVariables("HTTP_REFERER") %>
<br><br>
<b>opened file : </b><%= $Request->ServerVariables("SCRIPT_FILENAME") %>
<br><br>
<b>server adress :</b><%= $Request->ServerVariables("HTTP_HOST") %>
<br><br>
<b>your adress : </b><%= $Request->ServerVariables("REMOTE_ADDR") %>
</span></span>
<br>

<table width=88% class=table border=0 cellpadding=4 cellspacing=1>
<tr><td class=tdark ><b>Server Variable</b></td><td class=tdg ><b>Value</b></td></tr>

<% 
$env = $Request->ServerVariables();
foreach $var (sort(keys(%{$env}))) {
    $val = $ENV{$var};
    $val =~ s|\n|\\n|g;
    $val =~ s|"|\\"|g;
print "<tr><td class=tdd><font size=-1>${var}</font></td>\n";
print "<td class=tdl><font size=-1>\"${val}\"&nbsp;</font></td></tr>\n";
}
%>

</table></p></font>

</center>Written by Vlad Alexa Mancini</html>