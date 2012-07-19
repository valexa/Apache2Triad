#!C:/apache2triadpath/perl/bin/perl.exe

print "Content-type: text/html\n\n";


$ENV{'SERVER_ADMIN'} =~ m/^.*?@(.*)$/ ;
$curdomain = $1;
$windir = $ENV{'WINDIR'};

$servertab = "C:/apache2triadpath/mail/server.tab";
$myini = "$windir/my.ini";
$phpini = "$windir/php.ini";

$FORM{'act'} = '';

&parseform();

if ($FORM{'act'}eq'Use Recomended Settings'){
print "<title>Apache2Triad server protect tool</title>";
&action;
}else{
&entry;
}
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
print "<link rel=stylesheet href=style.css>
<title>Apache2Triad server protect tool</title><body><center>
<p><font size=5>Apache2Triad server protect tool</font></p>
This script will look for common misconfigurations of the settinng of the servers within Apache2Triad and recomend changes<br>
<p><font color=red>After running the script you should restart your computer or all the servers for changes to take place</font></p>
";

if (open (FILE,"$servertab")){
@data=<FILE>;
$line = 0;
foreach $d (@data){
        $line++;
        while ($d =~ m/^\"EnableAuthSMTP-POP3\"\s*\"(\d*)\"/g){
               if ($1 eq "1"){
                         print "EnableAuthSMTP-POP3 = $1 in $servertab (Recomended = 1)<br>"; $disabled = disabled;
               }else{
                         print "<font color=blue>EnableAuthSMTP-POP3 = $1 in $servertab (Recomended = 1)</font><br>"; $disabled = "";
               }
        }
}
close (FILE);
}else{ print "<font color=red>Did not find <b>$servertab</b></font><br>"; $disabled = disabled; }

if (open (FILE,"$myini")){
@data=<FILE>;
$line = 0;
foreach $d (@data){
        $line++;
        while ($d =~ m/^bind-address\s*=\s*(\S*)/g){
               if ($1 eq "127.0.0.1"){
                         print "bind-address = $1 in $myini (Recomended = 127.0.0.1)<br>"; $disabled = disabled;
               }else{
                         print "<font color=blue>bind-address = $1 in $myini (Recomended = 127.0.0.1)</font><br>"; $disabled = "";
               }
        }
}
close (FILE);
}else{ print "<font color=red>Did not find <b>$myini</b></font><br>"; $disabled = disabled; }

if (open (FILE,"$phpini")){
@data=<FILE>;
$line = 0;
foreach $d (@data){
        $line++;
        while ($d =~ m/cgi\.force_redirect\s*=\s*(\S*)/g){
               if ($1 eq "1"){
                         print "cgi.force_redirect = $1 in $phpini (Recomended = 1)<br>"; $disabled = disabled;
               }else{
                         print "<font color=blue>cgi.force_redirect = $1 in $phpini (Recomended = 1)</font><br>"; $disabled = "";
               }
        }
}
close (FILE);
}else{ print "<font color=red>Did not find <b>$phpini</b></font><br>"; $disabled = disabled; }


print "
<form name=form action=$ENV{SCRIPT_NAME} method=post>
<input class=button type=submit name=act value=\"Use Recomended Settings\" $disabled></form>";

print "</center>Written by Vlad Alexa Mancini</html>";

}


sub action {

if (open (FILE,"+< $servertab")){
@data=<FILE>;
truncate (FILE,0);
close (FILE);
open (FILE,"+< $servertab");
foreach $d (@data){
        $d =~ s~"EnableAuthSMTP-POP3"\s*"0"~"EnableAuthSMTP-POP3"\t"1"~g ;
        print FILE $d;
}
close (FILE);
}

if (open (FILE,"+< $myini")){
@data=<FILE>;
truncate (FILE,0);
close (FILE);
open (FILE,"+< $myini");
foreach $d (@data){
        $d =~ s~bind-address.*?$~bind-address = 127\.0\.0\.1~g ;
        print FILE $d;
}
close (FILE);
}

if (open (FILE,"+< $phpini")){
@data=<FILE>;
truncate (FILE,0);
close (FILE);
open (FILE,"+< $phpini");
foreach $d (@data){
        $d =~ s~cgi\.force_redirect = 0$~cgi\.force_redirect = 1~g ;
        print FILE $d;
}
close (FILE);
}

print "<br>All done<br>";
print "<a href=javascript:history.go(-2)>Go Back</a>";
}
exit;