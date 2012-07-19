<html>
<head>
<link rel="stylesheet" href="style.css">
<title>Apache2Triad Feedback</title>
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
<link rel="SHORTCUT ICON" href="favicon.ico">
</head>
<body background="gfx/lines.gif">
<div align="center"><b><span style="font-size: 16.0pt"><a name="Top"></a></span></b>
</div>
<TABLE width="99%" border=0 cellPadding=0 cellSpacing=0 class=ttb>
  <TBODY>
    <TR>
      <TD><IMG alt="" height=12 src="gfx/tt12_l.gif"
      width=10></TD>
      <TD class=tt12bkg><IMG alt="" height=12
      src="gfx/spacer.gif" width=200></TD>
      <TD><IMG alt="" height=12 src="gfx/tt12_r.gif"
      width=10></TD>
    </TR>
  </TBODY>
</TABLE>
<TABLE width="99%" border=0 cellPadding=10 cellSpacing=0 class=bodyline>
  <TR>

    <TD class="logo"><div align="center"><a href="http://apache2triad.net"><img src="http://apache2triad.net/gfx/apache2triad_logo.gif" border="0"></a></div></TD>
  </TR>
  <TBODY>
    <TR>
      <TD width="995">
         <blockquote>
          <blockquote>
            <p>&nbsp;</p>
            <p><font size="4" face="Georgia, Times New Roman, Times, serif">Apache2Triad Feedback/Support</font>
            </p>
            <p>
              <?php
$available = file ('http://apache2triad.net/txt/forums.txt');
if (rtrim($available[0]) == "online"){
      echo  "<p>The forums on <a href=http://apache2triad.net/forums/ target=_blank>http://apache2triad.net/forums/</a> are online </p>";
      echo  "<p>You will get suport on the forums there , and only there while they are online</p>";
}else{
      echo  "<p>The forums on <a href=http://apache2triad.net/forums/ target=_blank>http://apache2triad.net/forums/</a> are offline </p>";
      echo  "<p>You will get suport on the forums at <a href=http://sourceforge.net/forum/forum.php?forum_id=323320>http://sourceforge.net/forum/forum.php?forum_id=323320</a></p>";
}
      echo"
<center>
<p>You can also use the form below to post to the apache2triad users feed but you will get no followups</p>
<form name=feedback action=http://apache2triad.net/form2feed.php method=post>
<p><textarea class=input name=subject cols=100 rows=1 wrap=VIRTUAL></textarea></p>
<p><textarea class=input name=body cols=100 rows=15 wrap=VIRTUAL></textarea><br>
<input type=hidden name=admin value=".$_SERVER['SERVER_ADMIN'].">
<br><input class=button type=submit name=Submit value=Submit></p></form>
       ";
?>
            </p>
            <p>&nbsp;            </p>
          </blockquote>
            </blockquote>
    </TD>
    </TR>
  </TBODY>
</TABLE>
<TABLE width="99%" border=0 cellPadding=0 cellSpacing=0 class=ttb>
  <TBODY>
    <TR>
      <TD><IMG alt="" height=12 src="gfx/tb12_l.gif"
      width=10></TD>
      <TD class=tb12bkg><IMG alt="" height=12
      src="gfx/spacer.gif" width=200></TD>
      <TD><IMG alt="" height=12 src="gfx/tb12_r.gif"
      width=10></TD>
    </TR>
  </TBODY>
</TABLE>
<div>
  <div align="center">
<div align="center">
      <div align="center">
<div align="center"><b><span style="font-size:16.0pt"></span></b></div>
    <div align="center">
</div>
      </div>
    </div>
    <p><font color="#999999" size="1" face="Verdana, Arial, Helvetica, sans-serif">Apache2TriadCP by <a href="http://alexamancini.com" target="_blank">Vlad Alexa Mancini</a><br>

Programming by <a href="http://nextcode.org">NextCode</a>
Graphics by <a href="http://nextdesign.eu.org">NextDesign</a> <br>
      <br>
            </font></p>
  </div>
</div>
</body>
</html>