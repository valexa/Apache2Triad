<html>
<head>
<link rel="stylesheet" href="style.css">
<title>Apache2Triad Update Check</title>
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
            <p>&nbsp;
</p>
            <p align="center">
<?php
$available = file ('http://apache2triad.net/txt/edge.txt');
$my = file ('version.txt');
if (!$available){ echo "<font color=red>Coud not get new version number</font><br>";
}else{
	if (rtrim($my[0])==rtrim($available[0])) {
	echo "<b>Installed version of Apache2Triad is the latest (edge).<br>You don't need to update it.</b><br>";
	}else{
	echo "<b>New version of Apache2Triad is available!</b><br><br>";
	echo "New version: $available[0]<br>";
	echo "Installed version: $my[0]<br><br>";
	echo "<form action=\"http://apache2triad.net\" method=post>";
	echo "<input class=button type=submit name=act value=\"Get new version : $available[0]\"></form>";
	}
}
?>
            </p>
            <p>&nbsp;</p>
            <p>&nbsp;</p>
            <p>&nbsp;</p>
            <p>&nbsp;</p>
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