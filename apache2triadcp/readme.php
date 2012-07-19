<?php

$readmes = array(
           readme => array(title => "The Apache2triad Readme", path => "C:/apache2triadpath/apache2triad_readme.txt"),
           mysql => array(title => "The Apache2triad Mysql Readme", path => "C:/apache2triadpath/mysql/apache2triad_mysql.txt"),
           pgsql => array(title => "The Apache2triad PostgreSQL Readme", path => "C:/apache2triadpath/pgsql/apache2triad_pgsql.txt"),
           openssl => array(title => "The Apache2triad Openssl Readme", path => "C:/apache2triadpath/opssl/apache2triad_openssl.txt"),
           ftp => array(title => "The Apache2triad Slimftpd Readme", path => "C:/apache2triadpath/ftp/apache2triad_ftp.txt"),
           mail => array(title => "The Apache2triad Xmail Readme", path => "C:/apache2triadpath/mail/apache2triad_mail.txt"),
           perl => array(title => "The Apache2triad Perl Readme", path => "C:/apache2triadpath/perl/apache2triad_perl.txt"),
           php => array(title => "The Apache2triad PHP Readme", path => "C:/apache2triadpath/php/apache2triad_php.txt"),
           python => array(title => "The Apache2triad Python Readme", path => "C:/apache2triadpath/python/apache2triad_python.txt"),
           awstats => array(title => "The Apache2triad Awstats Readme", path => "C:/apache2triadpath/htdocs/awstats/apache2triad_awstats.txt"),
           phpmyadmin => array(title => "The Apache2triad PHPMyAdmin Readme", path => "C:/apache2triadpath/htdocs/phpmyadmin/apache2triad_phpmyadmin.txt"),
           phppgadmin => array(title => "The Apache2triad PHPPgAdmin Readme", path => "C:/apache2triadpath/htdocs/phppgadmin/apache2triad_phppgadmin.txt"),
           phpsftpd => array(title => "The Apache2triad PHPsFTPd Readme", path => "C:/apache2triadpath/htdocs/phpsftpd/apache2triad_phpsftpd.txt"),
           phpsqliteadmin => array(title => "The Apache2triad PHPSqliteAdmin Readme", path => "C:/apache2triadpath/htdocs/phpsqliteadmin/apache2triad_phpsqliteadmin.txt"),
           phpxmail => array(title => "The Apache2triad PHPXmail Readme", path => "C:/apache2triadpath/htdocs/phpxmail/apache2triad_phpxmail.txt"),
           uebimiau => array(title => "The Apache2triad Uebimiau Readme", path => "C:/apache2triadpath/htdocs/uebimiau/apache2triad_uebimiau.txt"),
           );

if ($_GET['load']){
        $load = $_GET['load'];
        $mesage = $readmes[$load]['title'];
        $file = $readmes[$load]['path'];
}else{
        $mesage = "The Apache2triad Readme's";
        foreach ($readmes as $r => $e){
                 $file .= "<a href=readme.php?load=$r>".$e['title']."<br>\n";
        }
}

?>

<html>
<head>
<link rel="stylesheet" href="style.css">
<title><?php echo $mesage; ?></title>
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
            <p>&nbsp;</p>
            <p align="center">
<p><font size=5><?php echo $mesage; ?></font></p>
<pre><?php if ($load) {echo file_get_contents($file);}else{echo $file;} ?></pre>
            </p>
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
