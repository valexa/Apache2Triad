#!C:/apache2triadpath/perl/bin/perl.exe

print "Content-type: text/html\n\n";


$ENV{'SERVER_ADMIN'} =~ m/^.*?@(.*)$/ ;
$curdomain = $1;
$windir = $ENV{'WINDIR'};

$phpini = "$windir/php.ini";
$httpdconf = "C:/apache2triadpath/conf/httpd.conf";
$sslconf = "C:/apache2triadpath/conf/ssl.conf";
$serversphp = "C:/apache2triadpath/htdocs/phpxmail/servers.php";
$configphp = "C:/apache2triadpath/htdocs/uebimiau/inc/config.php";
$domainstab = "C:/apache2triadpath/mail/domains.tab";
$mailuserstab = "C:/apache2triadpath/mail/mailusers.tab";
$servertab = "C:/apache2triadpath/mail/server.tab";

$admintab = "C:/apache2triadpath/mail/domains/$curdomain/admin/user.tab";
$postmastertab = "C:/apache2triadpath/mail/domains/$curdomain/postmaster/user.tab";
$awstats = "C:/apache2triadpath/htdocs/awstats/awstats.$curdomain.conf";

#if ($curdomain ne "localhost"){$disabled = disabled;}

$FORM{'act'} = '';

&parseform();

if ($FORM{'act'} eq 'Change domain' && $FORM{'newdomain'} ne ''){
print "<title>Apache2Triad domain name change tool</title>";
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
<title>Apache2Triad domain name change tool</title><body><center>
<p><font size=5>Domain name change tool</font></p>
This script will change the domain name in the configs from localhost to your domainname or hostname. (localhost to domain.dom)<br>
It will also change the serveradmin email adress , and the xmail default mail account. (admin\@localhost to admin\@domain.dom)<br>
<font color=red>You must own the domain name to wich you are changing to and the DNS records for that domain must point to this computer's IP</font></p>
<font color=red>After running the script you should restart apache and xmail for changes to take place</font></p>
";

if (open (FILE,"$phpini")){
@data=<FILE>;
$line = 0;
foreach $d (@data){
        $line++;
        while ($d =~ m/^sendmail_from = admin@(\S*)/g){if ($1 eq $curdomain){ print "$phpini line $line good ($1)<br>"; }else{ print "<font color=red>$phpini line $line bad ($1)</font><br>"; }}
}
close (FILE);
}else{ print "<font color=red>Did not find <b>$phpini</b></font><br>"; $disabled = disabled; }


if (open (FILE,"$httpdconf")){
@data=<FILE>;
$line = 0;
foreach $d (@data){
        $line++;
        while ($d =~ m/^ServerName (\S*):80/g){if ($1 eq $curdomain){ print "$httpdconf line $line good ($1)<br>"; }else{ print "<font color=red>$httpdconf line $line bad ($1)</font><br>"; }}
        while ($d =~ m/^ServerAdmin admin@(\S*)/g){if ($1 eq $curdomain){ print "$httpdconf line $line good ($1)<br>"; }else{ print "<font color=red>$httpdconf line $line bad ($1)</font><br>"; }}
}
close (FILE);
}else{ print "<font color=red>Did not find <b>$httpdconf</b></font><br>"; $disabled = disabled; }


if (open (FILE,"$sslconf")){
@data=<FILE>;
$line = 0;
foreach $d (@data){
        $line++;
        while ($d =~ m/^ServerName (\S*):443/g){if ($1 eq $curdomain){ print "$sslconf line $line good ($1)<br>"; }else{ print "<font color=red>$sslconf line $line bad ($1)</font><br>"; }}
        while ($d =~ m/^ServerAdmin admin@(\S*)/g){if ($1 eq $curdomain){ print "$sslconf line $line good ($1)<br>"; }else{ print "<font color=red>$sslconf line $line bad ($1)</font><br>"; }}
}
close (FILE);
}else{ print "<font color=red>Did not find <b>$sslconff</b></font><br>"; $disabled = disabled; }


if (open (FILE,"$serversphp")){
@data=<FILE>;
$line = 0;
foreach $d (@data){
        $line++;
        while ($d =~ m/^Apache2Triad Xmail Server\t(\S*)\t/g){if ($1 eq $curdomain){ print "$serversphp line $line good ($1)<br>"; }else{ print "<font color=red>$serversphp line $line bad ($1)</font><br>"; }}
}
close (FILE);
}else{ print "<font color=red>Did not find <b>$serversphp</b></font><br>"; $disabled = disabled; }

if (open (FILE,"$configphp")){
@data=<FILE>;
$line = 0;
foreach $d (@data){
        $line++;
        while ($d =~ m/smtp_server = "(\S*)"/g){if ($1 eq $curdomain){ print "$configphp line $line good ($1)<br>"; }else{ print "<font color=red>$configphp line $line bad ($1)</font><br>"; }}
        while ($d =~ m/"domain" => "(\S*)",#change/g){if ($1 eq $curdomain){ print "$configphp line $line good ($1)<br>"; }else{ print "<font color=red>$configphp line $line bad ($1)</font><br>"; }}
        while ($d =~ m/"server" => "(\S*)",#change/g){if ($1 eq $curdomain){ print "$configphp line $line good ($1)<br>"; }else{ print "<font color=red>$configphp line $line bad ($1)</font><br>"; }}
}
close (FILE);
}else{ print "<font color=red>Did not find <b>$configphp</b></font><br>"; $disabled = disabled; }

if (open (FILE,"$domainstab")){
@data=<FILE>;
$line = 0;
foreach $d (@data){
        $line++;
        while ($d =~ m/^"(\S*)"$/g){if ($1 eq $curdomain){ print "$domainstab line $line good ($1)<br>"; }else{ print "<font color=red>$domainstab line $line bad ($1)</font><br>"; }}
}
close (FILE);
}else{ print "<font color=red>Did not find <b>$domainstab</b></font><br>"; $disabled = disabled; }

if (open (FILE,"$mailuserstab")){
@data=<FILE>;
$line = 0;
foreach $d (@data){
        $line++;
        while ($d =~ m/^"(\S*)"/g){if ($1 eq $curdomain){ print "$mailuserstab line $line good ($1)<br>"; }else{ print "<font color=red>$mailuserstab line $line bad ($1)</font><br>"; }}
}
close (FILE);
}else{ print "<font color=red>Did not find <b>$mailuserstab</b></font><br>"; $disabled = disabled; }

if (open (FILE,"$servertab")){
@data=<FILE>;
$line = 0;
foreach $d (@data){
        $line++;
        while ($d =~ m/"RootDomain"\s*"(\S*)"/g){if ($1 eq $curdomain){ print "$servertab line $line good ($1)<br>"; }else{ print "<font color=red>$servertab line $line bad ($1)</font><br>"; }}
        while ($d =~ m/"SmtpServerDomain"\s*"(\S*)"/g){if ($1 eq $curdomain){ print "$servertab line $line good ($1)<br>"; }else{ print "<font color=red>$servertab line $line bad ($1)</font><br>"; }}
        while ($d =~ m/"POP3Domain"\s*"(\S*)"/g){if ($1 eq $curdomain){ print "$servertab line $line good ($1)<br>"; }else{ print "<font color=red>$servertab line $line bad ($1)</font><br>"; }}
        while ($d =~ m/"HeloDomain"\s*"(\S*)"/g){if ($1 eq $curdomain){ print "$servertab line $line good ($1)<br>"; }else{ print "<font color=red>$servertab line $line bad ($1)</font><br>"; }}
        while ($d =~ m/"PostMaster"\s*"postmaster@(\S*)"/g){if ($1 eq $curdomain){ print "$servertab line $line good ($1)<br>"; }else{ print "<font color=red>$servertab line $line bad ($1)</font><br>"; }}
        while ($d =~ m/"Pop3SyncErrorAccount"\s*"psync@(\S*)"/g){if ($1 eq $curdomain){ print "$servertab line $line good ($1)<br>"; }else{ print "<font color=red>$servertab line $line bad ($1)</font><br>"; }}
        while ($d =~ m/"ErrorsAdmin"\s*"errors@(\S*)"/g){if ($1 eq $curdomain){ print "$servertab line $line good ($1)<br>"; }else{ print "<font color=red>$servertab line $line bad ($1)</font><br>"; }}
        while ($d =~ m/"TempErrorsAdmin"\s*"send-failures@(\S*)"/g){if ($1 eq $curdomain){ print "$servertab line $line good ($1)<br>"; }else{ print "<font color=red>$servertab line $line bad ($1)</font><br>"; }}
}
close (FILE);
}else{ print "<font color=red>Did not find <b>$servertab</b></font><br>"; $disabled = disabled; }

if (open (FILE,"$admintab")){
@data=<FILE>;
$line = 0;
foreach $d (@data){
        $line++;
        while ($d =~ m/^"RealName"\s*"admin@(\S*) account"/g){if ($1 eq $curdomain){ print "$admintab line $line good ($1)<br>"; }else{ print "<font color=red>$admintab line $line bad ($1)</font><br>"; }}
        while ($d =~ m/^"HomePage"\s*"http:\/\/(\S*)\/~admin"/g){if ($1 eq $curdomain){ print "$admintab line $line good ($1)<br>"; }else{ print "<font color=red>$admintab line $line bad ($1)</font><br>"; }}
}
close (FILE);
}else{ print "<font color=red>Did not find <b>$admintab</b></font><br>"; $disabled = disabled; }

if (open (FILE,"$postmastertab")){
@data=<FILE>;
$line = 0;
foreach $d (@data){
        $line++;
        while ($d =~ m/^"RealName"\s*"postmaster@(\S*) account"/g){if ($1 eq $curdomain){ print "$postmastertab line $line good ($1)<br>"; }else{ print "<font color=red>$postmastertab line $line bad ($1)</font><br>"; }}
        while ($d =~ m/^"HomePage"\s*"http:\/\/(\S*)\/~postmaster"/g){if ($1 eq $curdomain){ print "$postmastertab line $line good ($1)<br>"; }else{ print "<font color=red>$postmastertab line $line bad ($1)</font><br>"; }}
}
close (FILE);
}else{ print "<font color=red>Did not find <b>$postmastertab</b></font><br>"; $disabled = disabled; }

if (open (FILE,"$awstats")){
@data=<FILE>;
$line = 0;
foreach $d (@data){
        $line++;
        while ($d =~ m/^SiteDomain="(\S*)"/g){if ($1 eq $curdomain){ print "$awstats line $line good ($1)<br>"; }else{ print "<font color=red>$awstats line $line bad ($1)</font><br>"; }}
}
close (FILE);
}else{ print "<font color=red>Did not find <b>$awstats</b></font><br>"; $disabled = disabled; }


print "
<form name=form action=$ENV{SCRIPT_NAME} method=post>
New domain : <input class=input type=text size=24 maxlength=50 name=newdomain>&nbsp;(curent is $curdomain)<br><br>
<input class=button type=submit name=act value=\"Change domain\" $disabled></form>";

print "</center>Written by Vlad Alexa Mancini</html>";

}


sub action {

$newdomain = $FORM{'newdomain'};

if (open (FILE,"+< $phpini")){
@data=<FILE>;
truncate (FILE,0);
close (FILE);
open (FILE,"+< $phpini");
foreach $d (@data){
        $d =~ s/sendmail_from = admin\@$curdomain/sendmail_from = admin\@$newdomain/g ;
        print FILE $d;
}
close (FILE);
}

if (open (FILE,"+< $httpdconf")){
@data=<FILE>;
truncate (FILE,0);
close (FILE);
open (FILE,"+< $httpdconf");
foreach $d (@data){
        $d =~ s/ServerName $curdomain:80/ServerName $newdomain:80/g ;
        $d =~ s/ServerAdmin admin\@$curdomain/ServerAdmin admin\@$newdomain/g ;
        print FILE $d;
}
close (FILE);
}

if (open (FILE,"+< $sslconf")){
@data=<FILE>;
truncate (FILE,0);
close (FILE);
open (FILE,"+< $sslconf");
foreach $d (@data){
        $d =~ s/ServerName $curdomain:443/ServerName $newdomain:443/g ;
        $d =~ s/ServerAdmin admin\@$curdomain/ServerAdmin admin\@$newdomain/g ;
        print FILE $d;
}
close (FILE);
}

if (open (FILE,"+< $serversphp")){
@data=<FILE>;
truncate (FILE,0);
close (FILE);
open (FILE,"+< $serversphp");
foreach $d (@data){
        $d =~ s~Apache2Triad Xmail Server\t$curdomain\t~Apache2Triad Xmail Server\t$newdomain\t~g ;
        print FILE $d;
}
close (FILE);
}

if (open (FILE,"+< $configphp")){
@data=<FILE>;
truncate (FILE,0);
close (FILE);
open (FILE,"+< $configphp");
foreach $d (@data){
        $d =~ s~smtp_server = "$curdomain"~smtp_server = "$newdomain"~g ;
        $d =~ s~"domain" => "$curdomain",#change~"domain" => "$newdomain",#change~g ;
        $d =~ s~"server" => "$curdomain",#change~"server" => "$newdomain",#change~g ;
        print FILE $d;
}
close (FILE);
}

if (open (FILE,"+< $domainstab")){
@data=<FILE>;
truncate (FILE,0);
close (FILE);
open (FILE,"+< $domainstab");
foreach $d (@data){
        $d =~ s~"$curdomain"~"$newdomain"~g ;
        print FILE $d;
}
close (FILE);
}

if (open (FILE,"+< $mailuserstab")){
@data=<FILE>;
truncate (FILE,0);
close (FILE);
open (FILE,"+< $mailuserstab");
foreach $d (@data){
        $d =~ s~"$curdomain"~"$newdomain"~g ;
        print FILE $d;
}
close (FILE);
}

if (open (FILE,"+< $servertab")){
@data=<FILE>;
truncate (FILE,0);
close (FILE);
open (FILE,"+< $servertab");
foreach $d (@data){
        $d =~ s~"RootDomain"\s*"$curdomain"~"RootDomain"\t"$newdomain"~g ;
        $d =~ s~"SmtpServerDomain"\s*"$curdomain"~"SmtpServerDomain"\t"$newdomain"~g ;
        $d =~ s~"POP3Domain"\s*"$curdomain"~"POP3Domain"\t"$newdomain"~g ;
        $d =~ s~"HeloDomain"\s*"$curdomain"~"HeloDomain"\t"$newdomain"~g ;
        $d =~ s~"PostMaster"\s*"postmaster\@$curdomain"~"PostMaster"\t"postmaster\@$newdomain"~g ;
        $d =~ s~"Pop3SyncErrorAccount"\s*"psync\@$curdomain"~"Pop3SyncErrorAccount"\t"psync\@$newdomain"~g ;
        $d =~ s~"ErrorsAdmin"\s*"errors\@$curdomain"~"ErrorsAdmin"\t"errors\@$newdomain"~g ;
        $d =~ s~"TempErrorsAdmin"\s*"send-failures\@$curdomain"~"TempErrorsAdmin"\t"send-failures\@$newdomain"~g ;
        print FILE $d;
}
close (FILE);
}

if (open (FILE,"+< $admintab")){
@data=<FILE>;
truncate (FILE,0);
close (FILE);
open (FILE,"+< $admintab");
foreach $d (@data){
        $d =~ s~"RealName"\s*"admin\@$curdomain account"~"RealName"\t"admin\@$newdomain account"~g ;
        $d =~ s~"HomePage"\s*"http:\/\/$curdomain\/\~admin"~"HomePage"\t"http:\/\/$newdomain\/\~admin"~g ;
        print FILE $d;
}
close (FILE);
}

if (open (FILE,"+< $postmastertab")){
@data=<FILE>;
truncate (FILE,0);
close (FILE);
open (FILE,"+< $postmastertab");
foreach $d (@data){
        $d =~ s~"RealName"\s*"postmaster\@$curdomain account"~"RealName"\t"postmaster\@$newdomain account"~g ;
        $d =~ s~"HomePage"\s*"http:\/\/$curdomain\/\~postmaster"~"HomePage"\t"http:\/\/$newdomain\/\~postmaster"~g ;
        print FILE $d;
}
close (FILE);
}

if (open (FILE,"+< $awstats")){
@data=<FILE>;
truncate (FILE,0);
close (FILE);
open (FILE,"+< $awstats");
foreach $d (@data){
        $d =~ s~SiteDomain="$curdomain"~SiteDomain="$newdomain"~g ;
        print FILE $d;
}
close (FILE);
}

rename("C:/apache2triadpath/htdocs/awstats/awstats.$curdomain.conf", "C:/apache2triadpath/htdocs/awstats/awstats.$newdomain.conf");
rename ("C:/apache2triadpath/mail/domains/$curdomain/", "C:/apache2triadpath/mail/domains/$newdomain/");

print "<br>All done<br>";
print "<a href=javascript:history.go(-2)>Go Back</a>";
}
exit;