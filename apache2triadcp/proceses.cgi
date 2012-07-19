#!C:/apache2triadpath/perl/bin/perl.exe

print "Content-type: text/html\n\n";

@procs = ("Apache","ApacheSSL","Mysql","Postgresql","Xmail","Slimftpd");

@os = Win32::GetOSVersion();

$FORM{'act'} = '';

&parseform();
if ($FORM{'act'}eq'Proceses'){ &action; }else{ &entry; }
exit;

sub parseform() {
if($ENV{'REQUEST_METHOD'} eq 'GET'){
$buffer=$ENV{'QUERY_STRING'};
}elsif($ENV{'REQUEST_METHOD'} eq 'POST'){
read(STDIN, $buffer, $ENV{'CONTENT_LENGTH'});}
@pairs = split(/&/, $buffer);
foreach $pair (@pairs) {
($name, $value) = split(/=/, $pair);
$value =~ tr/+/ /;
$value =~s/%([a-fA-F0-9][a-fA-F0-9])/pack("c",hex($1))/eg;
$FORM{$name} = $value;}
}


sub entry {

$Apache = Start;
$ApacheSSL = Start;
$Mysql = Start;
$Postgresql = Start;
$Xmail = Start;
$Slimftpd = Start;

if ($os[4] != "2"){
#apache pipe#
#system ("pv.exe");
#@data=<STDOUT>;
#open feature#
#open (PV,"pv.exe|");
#@data=<PV>;
@data = `pv.exe`;
foreach $a (@data){
        if ($a =~ m/httpd.exe/i){ $Apache = Restart; $_ApacheSSL = "disabled";}
        if ($a =~ m/httpd.exe/i){ $ApacheSSL = Restart; $_Apache = "disabled";}
        if ($a =~ m/mysqld.exe/i){ $Mysql = Stop;}
        if ($a =~ m/postgres.exe/i){ $Postgresql = Stop;}
        if ($a =~ m/xmail.exe/i){ $Xmail = Stop;}
        if ($a =~ m/slimftpd.exe/i){ $Slimftpd = Stop;}
}
}

if ($os[4] == "2"){
        $a = `sc query apache2`; if ($a =~ m/RUNNING/i){ $Apache = Restart; $_ApacheSSL = "disabled";}
        $a = `sc query apache2ssl`; if ($a =~ m/RUNNING/i){ $ApacheSSL = Restart; $_Apache = "disabled";}                   
        $a = `sc query mysql`; if ($a =~ m/RUNNING/i){ $Mysql = Stop;}
        $a = `sc query pgsql`; if ($a =~ m/RUNNING/i){ $Postgresql = Stop;}
        $a = `sc query xmail`; if ($a =~ m/RUNNING/i){ $Xmail = Stop;}
        $a = `sc query slimftpd`; if ($a =~ m/RUNNING/i){ $Slimftpd = Stop;}
}

print "
<form class=form action=$ENV{SCRIPT_NAME} method=post>
<input class=button type=submit name=Apache value=\"$Apache Apache\" $_Apache>&nbsp;
<input class=button type=submit name=ApacheSSL value=\"$ApacheSSL ApacheSSL\" $_ApacheSSL>&nbsp;
<input class=button type=submit name=Mysql value=\"$Mysql Mysql\">&nbsp;
<input class=button type=submit name=Postgresql value=\"$Postgresql Postgresql\">&nbsp;
<input class=button type=submit name=Xmail value=\"$Xmail Xmail\">&nbsp;
<input class=button type=submit name=Slimftpd value=\"$Slimftpd Slimftpd\">&nbsp;
<input type=hidden name=act value=\"Proceses\">
</form>
";

}


sub action {

if ($os[4] != "2"){
$apstart = "httpd.exe -f C:/apache2triadpath/conf/httpd.conf -D AEX";
$apstop = "killproc.exe /K httpd.exe";
$apres = 'httpd.exe -n "Apache2" -k restart';
$apsslstart = "httpd.exe -f C:/apache2triadpath/conf/httpd.conf -D AEX -D SSL";
$apsslstop = "killproc.exe /K httpd.exe";
$apsslres = 'httpd.exe -n "Apache2SSL" -k restart';
$mystart = "mysqld.exe";
$mystop = "mysqladmin.exe -u root --password=apache2triadpass shutdown";
$pgstart = "echo Postgres does not work on windows9x";
$pgstop = "echo Postgres does not work on windows9x";
$ftpstart = "C:/apache2triadpath/ftp/slimftpd.exe";
$ftpstop = "killproc.exe /K slimftpd.exe";
$mailstart = "echo Xmail does not work on windows9x";
$mailstop = "echo Xmail does not work on windows9x";
}

if ($os[4] == "2"){
$apstart = "net start Apache2";
$apstop = "net stop Apache2";
$apres = 'httpd.exe -n "Apache2" -k restart';
$apsslstart = "net start Apache2SSL";
$apsslstop = "net stop Apache2SSL";
$apsslres = 'httpd.exe -n "Apache2SSL" -k restart';
$mystart = "net start MySql";
$mystop = "net stop MySql";
$pgstart = "net start PgSQL";
$pgstop = "net stop PgSQL";
$ftpstart = "net start SlimFTPd";
$ftpstop = "net stop SlimFTPd";
$mailstart = "net start Xmail";
$mailstop = "net stop Xmail";
}

if ($FORM{'Apache'} eq "Start Apache") {system($apstart);$msg="Apache has been started";}
if ($FORM{'Apache'} eq "Stop Apache") {system($apstop);$msg="Apache has been stopped";}
if ($FORM{'Apache'} eq "Restart Apache") {system($apres);$msg="Apache has been restarted";}

if ($FORM{'ApacheSSL'} eq "Start ApacheSSL") {system($apsslstart);$msg="ApacheSSL has been started";}
if ($FORM{'ApacheSSL'} eq "Stop ApacheSSL") {system($apsslstop);$msg="ApacheSSL has been stopped";}
if ($FORM{'ApacheSSL'} eq "Restart ApacheSSL") {system($apsslres);$msg="ApacheSSL has been restarted";}

if ($FORM{'Mysql'} eq "Stop Mysql") {system($mystop);$msg="Mysql has been stopped";}
if ($FORM{'Mysql'} eq "Start Mysql") {system($mystart);$msg="Mysql has been started";}

if ($FORM{'Postgresql'} eq "Stop Postgresql") {system($pgstop);$msg="Postgresql has been stopped";}
if ($FORM{'Postgresql'} eq "Start Postgresql") {system($pgstart);$msg="Postgresql has been started";}

if ($FORM{'Xmail'} eq "Stop Xmail") {system($mailstop);$msg="Xmail has been stopped";}
if ($FORM{'Xmail'} eq "Start Xmail") {system($mailstart);$msg="Xmail has been started";}

if ($FORM{'Slimftpd'} eq "Stop Slimftpd") {system($ftpstop);$msg="Slimftpd has been stopped";}
if ($FORM{'Slimftpd'} eq "Start Slimftpd") {system($ftpstart);$msg="Slimftpd has been started";}


print "<br>$msg<br><br>";

print "<br>All done<br>";
print "<a href=javascript:history.go(-1)>Go Back</a>";
}
exit;