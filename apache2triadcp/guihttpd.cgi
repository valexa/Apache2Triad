#!C:/apache2triadpath/perl/bin/perl.exe

print "Content-type: text/html\n\n";

$httpdconf = "C:/apache2triadpath/conf/httpd.conf";

$FORM{'act'} = '';

&parseform();

if ($FORM{'act'}eq'Save Changes'){
print "<link rel=stylesheet href=style.css><title>Apache2Triad Apache2 Configuration GUI</title>";
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

open (CONF,"< $httpdconf") or print "Could not open <b>$httpdconf</b><br>";
@data=<CONF>;
foreach $d (@data){
        if ($d =~ m~ServerName (.*)~g) {$servername = $1;}
        if ($d =~ m~Listen (.*)~g) {$listen = $1;}
        if ($d =~ m~ServerAdmin (.*)~g) {$serveradmin = $1;}
        if ($d =~ m~LogLevel (.*)~g) {$loglevel = $1;}
        if ($d =~ m~ServerTokens (.*)~g) {$servertokens = $1;}
        if ($d =~ m~ServerSignature (.*)~g) {$serversignature = $1;}
        if ($d =~ m~DirectoryIndex (.*)~g) {$directoryindex = $1;}
        if ($d =~ m~ThreadsPerChild (.*)~g) {$threadsperchild = $1;}
        if ($d =~ m~HostnameLookups (.*)~g) {$hostnamelookups = $1;}

        if ($d =~ m/^LoadModule include_module modules\/mod_include.so/) {$ssi = "checked";}
        if ($d =~ m/^LoadModule php5_module modules\/mod_php.so/) {$php = "checked";}
        if ($d =~ m/^PerlHandler Apache::ASP/) {$asp = "checked";}
        if ($d =~ m/^LoadModule perl_module modules\/mod_perl.so/) {$perl_mod = "checked";}
        if ($d =~ m/^LoadModule python_module modules\/mod_python.so/) {$python_mod = "checked";}
        if ($d =~ m/^LoadModule cgi_module modules\/mod_cgi.so/) {$cgi = "checked";}
        if ($d =~ m/^PythonHandler mod_python.psp/) {$psp = "checked";}
}
close (CONF) or die "Died while closing $httpdconf with error( $! )";


print "<link rel=stylesheet href=style.css>
<title>Apache2Triad Apache2 Configuration GUI</title><body><center>
<p><font size=5>Apache2Triad Apache2 Configuration</font></p>
Apache::ASP needs mod perl to be loaded in order for it to function<br>
When enabling CGI you are enabling Perl , Python in CGI mode<br>
When enabling Python PSP you are disabling Python Spyce , both need mod_python<br> 
Disabling one of SSI, PHP or CGI will render parts of the Apache2Triad CP inoperable<br>
<font color=red>After running the script you should restart apache for changes to take place<br>
</font><br>";

print "<form  action=$ENV{SCRIPT_NAME} method=post><br>

<table width=100% valign=top border=0 cellspacing=0 cellpadding=0>

<div align=center>
<font color=#0073c7><b>[ Enable CGI (Perl/Python)&nbsp;<input type=checkbox name=cgi value=on $cgi> ]</b><br></font>
<b>[ Enable SSI&nbsp;<input type=checkbox name=ssi value=on $ssi> ]</b>&nbsp;
<b>[ Enable PHP&nbsp;<input type=checkbox name=php value=on $php> ]</b>&nbsp;
<b>[ Enable Apache::ASP&nbsp;<input type=checkbox name=asp value=on $asp> ]</b>&nbsp;
<b>[ Enable Mod Perl&nbsp;<input type=checkbox name=perl_mod value=on $perl_mod> ]</b>&nbsp;
<b>[ Enable Mod Python&nbsp;<input type=checkbox name=python_mod value=on $python_mod disabled> ]</b>&nbsp;
<b>[ Enable Python PSP&nbsp;<input type=checkbox name=psp value=on $psp> ]</b>&nbsp;
<br><br></div>

<tr><td valign=top align=right width=30%><br><b>
The server name and port of the server :
</b></td><td><br>
<input class=input type=text size=75 maxlength=100 name=servername value=$servername><br>
The format must be : hostname:port not ip:port.
</td></tr>

<tr><td valign=top align=right width=30%><br><b>
The ip/port the server will listen on :
</b></td><td><br>
<input class=input type=text size=75 maxlength=100 name=listen value=$listen><br>
You can use ip:port format to prevent apache listening on all interfaces and restrict it to only one ip.
</td></tr>

<tr><td valign=top align=right width=30%><br><b>
The server admin email address  :
</b></td><td><br>
<input class=input type=text size=75 maxlength=100 name=serveradmin value=$serveradmin><br>
This address appears on some server-generated pages, such as error documents.
</td></tr>

<tr><td valign=top align=right width=30%><br><b>
The verbosity level of the log file :
</b></td><td><br>
<input class=input type=text size=75 maxlength=100 name=loglevel value=$loglevel><br>
The valid alternatives are: debug, info, notice, warn, error, crit, alert, emerg, where debug conveys the most information, and emerg the least.
</td></tr>

<tr><td valign=top align=right width=30%><br><b>
The amount of server info made public :
</b></td><td><br>
<input class=input type=text size=75 maxlength=100 name=servertokens value=$servertokens><br>
The valid alternatives are: Full, OS, Minor, Minimal, Major, Prod, where Full conveys the most information, and Prod the least.
</td></tr>

<tr><td valign=top align=right width=30%><br><b>
The server signature configuration :
</b></td><td><br>
<input class=input type=text size=75 maxlength=100 name=serversignature value=$serversignature><br>
The valid alternatives are: On, Off, EMail, where EMail includes a mailto: link to the ServerAdmin.
</td></tr>

<tr><td valign=top align=right width=30%><br><b>
The directory index valid filenames :
</b></td><td><br>
<input class=input type=text size=75 maxlength=100 name=directoryindex value=\"$directoryindex\"><br>
This sets the filenames that Apache will look for and serve if a directory is requested.
</td></tr>

<tr><td valign=top align=right width=30%><br><b>
The number of threads in the process :
</b></td><td><br>
<input class=input type=text size=75 maxlength=100 name=threadsperchild value=$threadsperchild><br>
This is a constant number defining the worker threads in the server process.
</td></tr>

<tr><td valign=top align=right width=30%><br><b>
Log hostnames instead of ip addreses :
</b></td><td><br>
<input class=input type=text size=75 maxlength=100 name=hostnamelookups value=$hostnamelookups><br>
The valid alternatives are: On, Off, the result is at least one lookup request to the nameserver for each client request.
</td></tr>

</table><br><br><input class=button type=submit name=act value=\"Save Changes\"></form>";

print "</center>Written by Vlad Alexa Mancini</html>";

}


sub action {

open (CONF,"< $httpdconf") or die "Could not open <b>$httpdconf</b><br>";
@data=<CONF>;
foreach $d (@data){
        if ($d =~ m~ServerName (.*)~g) {$servername = $1;}
        if ($d =~ m~Listen (.*)~g) {$listen = $1;}
        if ($d =~ m~ServerAdmin (.*)~g) {$serveradmin = $1;}
        if ($d =~ m~LogLevel (.*)~g) {$loglevel = $1;}
        if ($d =~ m~ServerTokens (.*)~g) {$servertokens = $1;}
        if ($d =~ m~ServerSignature (.*)~g) {$serversignature = $1;}
        if ($d =~ m~DirectoryIndex (.*)~g) {$directoryindex = $1;}
        if ($d =~ m~ThreadsPerChild (.*)~g) {$threadsperchild = $1;}
        if ($d =~ m~HostnameLookups (.*)~g) {$hostnamelookups = $1;}
        print CONF $d;
}
close (CONF) or die "Died while closing $httpdconf with error( $! )";

if ($FORM{'servername'} ne ''){ $servername1 = $FORM{'servername'}; }else{ die "Fields can not be blank";}
if ($FORM{'listen'} ne ''){ $listen1 = $FORM{'listen'}; }else{ die "Fields can not be blank";}
if ($FORM{'serveradmin'} ne ''){ $serveradmin1 = $FORM{'serveradmin'}; }else{ die "Fields can not be blank";}
if ($FORM{'loglevel'} ne ''){ $loglevel1 = $FORM{'loglevel'}; }else{ die "Fields can not be blank";}
if ($FORM{'servertokens'} ne ''){ $servertokens1 = $FORM{'servertokens'}; }else{ die "Fields can not be blank";}
if ($FORM{'serversignature'} ne ''){ $serversignature1 = $FORM{'serversignature'}; }else{ die "Fields can not be blank";}
if ($FORM{'directoryindex'} ne ''){ $directoryindex1 = $FORM{'directoryindex'}; }else{ die "Fields can not be blank";}
if ($FORM{'threadsperchild'} ne ''){ $threadsperchild1 = $FORM{'threadsperchild'}; }else{ die "Fields can not be blank";}
if ($FORM{'hostnamelookups'} ne ''){ $hostnamelookups1 = $FORM{'hostnamelookups'}; }else{ die "Fields can not be blank";}

if ($FORM{'ssi'} eq "on"){$ssi="on";}else{$ssi="off"}
if ($FORM{'php'} eq "on"){$php="on";}else{$php="off"}
if ($FORM{'asp'} eq "on"){$asp="on";}else{$asp="off"}
if ($FORM{'perl_mod'} eq "on"){$perl_mod="on";}else{$perl_mod="off"}
if ($FORM{'python_mod'} eq "on"){$python_mod="on";}else{$python_mod="off"}
if ($FORM{'cgi'} eq "on"){$cgi="on";}else{$cgi="off"}
if ($FORM{'psp'} eq "on"){$psp="on";}else{$psp="off"}

open (CONF,"+< $httpdconf") or print "Could not open <b>$httpdconf</b><br>";
@data=<CONF>;
truncate (CONF,0) or die "Died while truncating $httpdconf with error( $! )";
close (CONF) or die "Died while closing $httpdconf with error( $! )";
open (CONF,"+< $httpdconf") or print "Could not open <b>$httpdconf</b><br>";

foreach $d (@data){
        $d =~ s~ServerName $servername~ServerName $servername1~g;
        $d =~ s~Listen $listen~Listen $listen1~g;
        $d =~ s~ServerAdmin $serveradmin~ServerAdmin $serveradmin1~g;
        $d =~ s~LogLevel $loglevel~LogLevel $loglevel1~g;
        $d =~ s~ServerTokens $servertokens~ServerTokens $servertokens1~g;
        $d =~ s~ServerSignature $serversignature~ServerSignature $serversignature1~g;
        $d =~ s~DirectoryIndex $directoryindex~DirectoryIndex $directoryindex1~g;
        $d =~ s~ThreadsPerChild $threadsperchild~ThreadsPerChild $threadsperchild1~g;
        $d =~ s~HostnameLookups $hostnamelookups~HostnameLookups $hostnamelookups1~g;

        if ($ssi eq "on"){$d =~ s/^#LoadModule include_module/LoadModule include_module/g;}
        if ($ssi eq "off"){$d =~ s/^LoadModule include_module/#LoadModule include_module/g;}
        if ($php eq "on"){$d =~ s/^#LoadModule php5_module/LoadModule php5_module/g;}
        if ($php eq "off"){$d =~ s/^LoadModule php5_module/#LoadModule php5_module/g;}
        if ($asp eq "on"){$d =~ s/^#PerlHandler Apache::ASP/PerlHandler Apache::ASP/g;}
        if ($asp eq "off"){$d =~ s/^PerlHandler Apache::ASP/#PerlHandler Apache::ASP/g;}
        if ($perl_mod eq "on"){$d =~ s/^#LoadModule perl_module/LoadModule perl_module/g;}
        if ($perl_mod eq "off"){$d =~ s/^LoadModule perl_module/#LoadModule perl_module/g;}
        if ($python_mod eq "on"){$d =~ s/^#LoadModule python_module/LoadModule python_module/g;}
        if ($python_mod eq "off"){$d =~ s/^LoadModule python_module/#LoadModule python_module/g;}
        if ($cgi eq "on"){$d =~ s/^#LoadModule cgi_module/LoadModule cgi_module/g;}
        if ($cgi eq "off"){$d =~ s/^LoadModule cgi_module/#LoadModule cgi_module/g;}

        if ($psp eq "on"){$d =~ s/^#PythonHandler mod_python.psp/PythonHandler mod_python.psp/g;}
        if ($psp eq "on"){$d =~ s/^PythonHandler run_spyceModpy::spyceMain/#PythonHandler run_spyceModpy::spyceMain/g;}
        if ($psp eq "off"){$d =~ s/^PythonHandler mod_python.psp/#PythonHandler mod_python.psp/g;}
        if ($psp eq "off"){$d =~ s/^#PythonHandler run_spyceModpy::spyceMain/PythonHandler run_spyceModpy::spyceMain/g;}

        print CONF $d;
}
close (CONF) or die "Died while closing $httpdconf with error( $! )";

print "<center>SSI is $ssi &nbsp; PHP is $php &nbsp; CGI is $cgi &nbsp; Mod_Perl is $perl_mod &nbsp; ASP is $asp &nbsp; Python is $python_mod <br><br>";

print "
<br>The server name and port of the apache server &nbsp;<input class=input type=text size=38 maxlength=100 name=servername value=$servername1><br>
<br>The port the apache server will listen on &nbsp;<input class=input type=text size=44 maxlength=100 name=listen value=$listen1><br>
<br>The server admin email address for this server &nbsp;<input class=input type=text size=39 maxlength=100 name=serveradmin value=$serveradmin1><br>
<br>The verbosity level of the log file &nbsp;<input class=input type=text size=51 maxlength=100 name=loglevel value=$loglevel1><br>
<br>The amount of server info made public &nbsp;<input class=input type=text size=46 maxlength=100 name=servertokens value=$servertokens1><br>
<br>The server signature configuration &nbsp;<input class=input type=text size=50 maxlength=100 name=serversignature value=$serversignature1><br>
<br>The directory index valid filenames &nbsp;<input class=input type=text size=49 maxlength=100 name=directoryindex value=\"$directoryindex1\"><br>
<br>The number of worker threads in the server process &nbsp;<input class=input type=text size=34 maxlength=100 name=threadsperchild value=$threadsperchild1><br>
<br>Log the hostnames of clients instead of their IP addresses &nbsp;<input class=input type=text size=30 maxlength=100 name=hostnamelookups value=$hostnamelookups1><br>
";

print "<br>Sucesfully written to httpd.conf<br>";
print "<a href=javascript:history.go(-2)>Go Back</a></center>";
}
exit;