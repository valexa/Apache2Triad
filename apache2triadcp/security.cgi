#!C:/apache2triadpath/perl/bin/perl.exe

$http_error = "C:/apache2triadpath/logs/error.log";
$http_access = "C:/apache2triadpath/logs/access.log";
$ssl_error = "C:/apache2triadpath/logs/ssl_error.log";
$ssl_access = "C:/apache2triadpath/logs/ssl_access.log";

use Socket;

print "Content-type: text/html\n\n";
print "<html><head><title>Apache2Triad secuity log</title>\n";
print "<link rel=stylesheet href=style.css></head><body>\n";
print "<hr><center>";

open (HTTP_ACCESS, "$http_access")|| die "Can't open $http_access\n";
@http_access = <HTTP_ACCESS>;
close (HTTP_ACCESS);
print "<b><center>The Apache server on $ENV{'SERVER_NAME'}:80 list of hosts that performed actions as root or attempted to:</center></b><br>\n";
foreach $http_access (@http_access) {
        if ($http_access =~ m/(\d+\.\d+\.\d+\.\d+) - root.*?/){$all3{$1} += "1";}
        if ($http_access =~ m/([\w\d\.-]*?) - .* \[(.*)\].*?chr\(.*?/){$requests1{"by $1 on $2"}= "Double-encoded special characters attack (santy)";}
        if ($http_access =~ m/([\w\d\.-]*?) - .* \[(.*)\].*?sumthin.*?/){$requests1{"by $1 on $2"}= "404 headers acquiring attack (slapper)";}
        if ($http_access =~ m/([\w\d\.-]*?) - .* \[(.*)\].*?-{10,}?/){$requests1{"by $1 on $2"}= "Unknown HTTP method (30 minuses and stamp) attack";}
        if ($http_access =~ m/([\w\d\.-]*?) - .* \[(.*)\] "-" /){$requests1{"by $1 on $2"}= "Unknown HTTP method (one minus sign) attack";}
        if ($http_access =~ m/([\w\d\.-]*?) - .* \[(.*)\] "CONNECT /){$requests1{"by $1 on $2"}= "Multiple Vendor HTTP CONNECT TCP Tunnel attack";}
        if ($http_access =~ m/([\w\d\.-]*?) - .* \[(.*)\] "PUT /){$requests1{"by $1 on $2"}= "HTTP PUT attack";}
        if ($http_access =~ m/([\w\d\.-]*?) - .* \[(.*)\] "DELETE /){$requests1{"by $1 on $2"}= "HTTP DELETE attack";}
        if ($http_access =~ m/([\w\d\.-]*?) - .* \[(.*)\] ".*?\\x/){$requests1{"by $1 on $2"}= "Unknown HTTP method (hex encoded) attack";}
}
foreach $key (sort { $all3{$a} <=> $all3{$b} } keys %all3) {
        push(@all3,"<b>$key </b>$all3{$key} times<br>\n");
}
@all3 = reverse(@all3);
foreach $all3 (@all3) {
        print "<center>$all3</center>";
}
print "<br>";

open (HTTP_ERROR, "$http_error")|| die "Can't open $http_error\n";
@http_error = <HTTP_ERROR>;
close (HTTP_ERROR);
print "<b><center>The Apache server on $ENV{'SERVER_NAME'}:80 hackers top ten and their attempts:</center></b><br>\n";
foreach $http_error (@http_error) {
        if ($http_error =~ m/\[(.*)\] \[error\] \[client (.*)\].*?Attempt to serve directory/){$attempts1{"by $2 on $1"}= "Attempt to serve directory";}
        if ($http_error =~ m/\[(.*)\] \[error\] \[client (.*)\].*?Invalid URI in request GET/){$attempts1{"by $2 on $1"}= "Attempt to use malformed URI";}
        if ($http_error =~ m/\[(.*)\] \[error\] \[client (.*)\].*?URI too long/){$attempts1{"by $2 on $1"}= "Attempt to overflow with huge URI";}
        if ($http_error =~ m/\[(.*)\] \[error\] \[client (.*)\].*?The given path contained wildcard characters/){$attempts1{"by $2 on $1"}= "Attempt to use wildcard path";}
        if ($http_error =~ m/\[(.*)\] \[error\] \[client (.*)\].*?client denied by server configuration/){$attempts1{"by $2 on $1"}= "Attempt to perform denied action";}
        if ($http_error =~ m/\[(.*)\] \[error\] \[client (.*)\].*?Directory index forbidden by rule/){$attempts1{"by $2 on $1"}= "Attempt to directory index forbidden dir";}
        if ($http_error =~ m/\[(.*)\] \[error\] \[client (.*)\].*?Options ExecCGI is off in this directory/){$attempts1{"by $2 on $1"}= "Attempt to execute CGI in forbidden dir";}
        if ($http_error =~ m/\[(.*)\] \[error\] \[client (.*)\].*?Invalid method in request LINK/){$attempts1{"by $2 on $1"}= "Attempt to use invalid LINK request";}
        if ($http_error =~ m/\[(.*)\] \[error\] \[client (.*)\].*?Invalid method in request UNLINK/){$attempts1{"by $2 on $1"}= "Attempt to use invalid UNLINK request";}
        if ($http_error =~ m/\[(.*)\] \[error\] \[client (.*)\].*?cmd\.exe/){$attempts1{"by $2 on $1"}= "Attempt to exploit cmd.exe";}
        if ($http_error =~ m/\[(.*)\] \[error\] \[client (.*)\].*?boot\.ini/){$attempts1{"by $2 on $1"}= "Attempt to get boot.ini";}
        if ($http_error =~ m/\[(.*)\] \[error\] \[client (.*)\].*?win\.ini/){$attempts1{"by $2 on $1"}= "Attempt to get win.ini";}
        if ($http_error =~ m/\[(.*)\] \[error\] \[client (.*)\].*?etc\/passwd/){$attempts1{"by $2 on $1"}= "Attempt to get etc/passwd";}
        if ($http_error =~ m/\[(.*)\] \[error\] \[client (.*)\].*?iisadmpwd/){$attempts1{"by $2 on $1"}= "Attempt to get iisadmpwd";}
        if ($http_error =~ m/\[(.*)\] \[error\] \[client (.*)\].*?vti_pvt/){$attempts1{"by $2 on $1"}= "Attempt to exploit vti_pvt";}
        if ($http_error =~ m/\[(.*)\] \[error\] \[client (.*)\].*?vti_bin/){$attempts1{"by $2 on $1"}= "Attempt to exploit vti_bin";}
        if ($http_error =~ m/\[(.*)\] \[error\] \[client (.*)\].*?vti_cnf/){$attempts1{"by $2 on $1"}= "Attempt to exploit vti_cnf";}
        if ($http_error =~ m/\[(.*)\] \[error\] \[client (.*)\].*?vti_inf/){$attempts1{"by $2 on $1"}= "Attempt to exploit vti_inf";}
        if ($http_error =~ m/\[(.*)\] \[error\] \[client (.*)\].*?MSOffice/){$attempts1{"by $2 on $1"}= "Attempt to exploit MSOffice";}
        if ($http_error =~ m/\[(.*)\] \[error\] \[client (.*)\].*?default.ida/){$attempts1{"by $2 on $1"}= "Attempt to exploit default.ida";}
        if ($http_error =~ m/\[(.*)\] \[error\] \[client (.*)\].*?NULL.printer/){$attempts1{"by $2 on $1"}= "Attempt to exploit NULL.printer";}
        if ($http_error =~ m/\[(.*)\] \[error\] \[client (.*)\].*?erroneous characters/){$attempts1{"by $2 on $1"}= "Attempt to use erroneous characters";}
}

##print hackers
while (($key, $value) = each %attempts1) {
        $key =~ m/by (.*?) on /;
        $hackers1{"$1"} += "1";
}
while (($key, $value) = each %requests1) {
        $key =~ m/by (.*?) on /;
        $hackers1{"$1"} += "1";
}
$c = 0;
foreach $hacker1 (sort( { $hackers1{$b} <=> $hackers1{$a} } keys %hackers1)){
        if ($hackers1{$hacker1} >= 2 && $c < 10){
         print "$hacker1<b> $hackers1{$hacker1}</b> attempts<br>\n";
        }
        $c += 1;
        $total_hosts1 += "1";
}
print "<br>";

## print attacks
while (($key, $value) = each %requests1) {
        $attacks1{$value} += "1";
        $total_tries1 += "1";
}
foreach $attack1 (sort( { $attacks1{$b} <=> $attacks1{$a} } keys %attacks1)){
        print "$attack1 <b>$attacks1{$attack1}</b> times<br>\n";
}
print "<br>";

## print exploits
while (($key, $value) = each %attempts1) {
        $exploits1{$value} += "1";
        $total_tries1 += "1";
}
foreach $exploit1 (sort( { $exploits1{$b} <=> $exploits1{$a} } keys %exploits1)){
        print "$exploit1 <b>$exploits1{$exploit1}</b> times<br>\n";
}
print "<br>";

## print totals
print "<h3>There were a total of $total_tries1 attempts by $total_hosts1 persons/hosts , list follows : </h3>\n";

## print details
print "<br><textarea class=input rows=10 style='width:100%'>";
while (($key, $value) = each %attempts1) {
        print "$value $key\n";
}
while (($key, $value) = each %requests1) {
        print "$value $key\n";
}
print "</textarea><hr>";

open (SSL_ACCESS, "$ssl_access")|| die "Can't open $ssl_access\n";
@ssl_access = <SSL_ACCESS>;
close (SSL_ACCESS);
print "<b><center>The SSL server on $ENV{'SERVER_NAME'}:443 list of hosts that performed actions as root or attempted to:</center></b><br>\n";
foreach $ssl_access (@ssl_access) {
        if ($ssl_access =~ m/(\d+\.\d+\.\d+\.\d+) - root.*?/){$all4{$1} += "1";}
        if ($ssl_access =~ m/([\w\d\.-]*?) - .* \[(.*)\].*?chr\(.*?/){$requests2{"by $1 on $2"}= "Double-encoded special characters attack";}
        if ($ssl_access =~ m/([\w\d\.-]*?) - .* \[(.*)\].*?sumthin.*?/){$requests2{"by $1 on $2"}= "404 headers acquiring attack (slapper)";}
        if ($ssl_access =~ m/([\w\d\.-]*?) - .* \[(.*)\].*?-{10,}?/){$requests2{"by $1 on $2"}= "Unknown HTTP method (30 minuses and stamp) attack";}
        if ($ssl_access =~ m/([\w\d\.-]*?) - .* \[(.*)\] "-" /){$requests2{"by $1 on $2"}= "Unknown HTTP method (one minus sign) attack";}
        if ($ssl_access =~ m/([\w\d\.-]*?) - .* \[(.*)\] "CONNECT /){$requests2{"by $1 on $2"}= "Multiple Vendor HTTP CONNECT TCP Tunnel attack";}
        if ($ssl_access =~ m/([\w\d\.-]*?) - .* \[(.*)\] "PUT /){$requests2{"by $1 on $2"}= "HTTP PUT attack";}
        if ($ssl_access =~ m/([\w\d\.-]*?) - .* \[(.*)\] "DELETE /){$requests2{"by $1 on $2"}= "HTTP DELETE attack";}
        if ($ssl_access =~ m/([\w\d\.-]*?) - .* \[(.*)\] ".*?\\x/){$requests2{"by $1 on $2"}= "Unknown HTTP method (hex encoded) attack";}
}
foreach $key (sort { $all4{$a} <=> $all4{$b} } keys %all4) {
        push(@all4,"<b>$key </b>$all4{$key} times<br>\n");
}
@all4 = reverse(@all4);
foreach $all4 (@all4) {
        print "<center>$all4</center>";
}
print "<br>";

open (SSL_ERROR, "$ssl_error")|| die "Can't open $ssl_error\n";
@ssl_error = <SSL_ERROR>;
close (SSL_ERROR);
print "<b><center>The SSL server on $ENV{'SERVER_NAME'}:443 hackers top ten and their attempts:</center></b><br>\n";
foreach $ssl_error (@ssl_error) {
        if ($ssl_error =~ m/\[(.*)\] \[error\] \[client (.*)\].*?Attempt to serve directory/){$attempts2{"by $2 on $1"}= "Attempt to serve directory";}
        if ($ssl_error =~ m/\[(.*)\] \[error\] \[client (.*)\].*?Invalid URI in request GET/){$attempts2{"by $2 on $1"}= "Attempt to use malformed URI";}
        if ($ssl_error =~ m/\[(.*)\] \[error\] \[client (.*)\].*?URI too long/){$attempts2{"by $2 on $1"}= "Attempt to overflow with huge URI";}
        if ($ssl_error =~ m/\[(.*)\] \[error\] \[client (.*)\].*?The given path contained wildcard characters/){$attempts2{"by $2 on $1"}= "Attempt to use wildcard path";}
        if ($ssl_error =~ m/\[(.*)\] \[error\] \[client (.*)\].*?client denied by server configuration/){$attempts2{"by $2 on $1"}= "Attempt to perform denied action";}
        if ($ssl_error =~ m/\[(.*)\] \[error\] \[client (.*)\].*?Directory index forbidden by rule/){$attempts2{"by $2 on $1"}= "Attempt to directory index forbidden dir";}
        if ($ssl_error =~ m/\[(.*)\] \[error\] \[client (.*)\].*?Options ExecCGI is off in this directory/){$attempts2{"by $2 on $1"}= "Attempt to execute CGI in forbidden dir";}
        if ($ssl_error =~ m/\[(.*)\] \[error\] \[client (.*)\].*?Invalid method in request LINK/){$attempts2{"by $2 on $1"}= "Attempt to use invalid LINK request";}
        if ($ssl_error =~ m/\[(.*)\] \[error\] \[client (.*)\].*?Invalid method in request UNLINK/){$attempts2{"by $2 on $1"}= "Attempt to use invalid UNLINK request";}
        if ($ssl_error =~ m/\[(.*)\] \[error\] \[client (.*)\].*?cmd\.exe/){$attempts2{"by $2 on $1"}= "Attempt to exploit cmd.exe";}
        if ($ssl_error =~ m/\[(.*)\] \[error\] \[client (.*)\].*?boot\.ini/){$attempts2{"by $2 on $1"}= "Attempt to get boot.ini";}
        if ($ssl_error =~ m/\[(.*)\] \[error\] \[client (.*)\].*?win\.ini/){$attempts2{"by $2 on $1"}= "Attempt to get win.ini";}
        if ($ssl_error =~ m/\[(.*)\] \[error\] \[client (.*)\].*?etc\/passwd/){$attempts2{"by $2 on $1"}= "Attempt to get etc/passwd";}
        if ($ssl_error =~ m/\[(.*)\] \[error\] \[client (.*)\].*?iisadmpwd/){$attempts2{"by $2 on $1"}= "Attempt to get iisadmpwd";}
        if ($ssl_error =~ m/\[(.*)\] \[error\] \[client (.*)\].*?vti_pvt/){$attempts2{"by $2 on $1"}= "Attempt to exploit vti_pvt";}
        if ($ssl_error =~ m/\[(.*)\] \[error\] \[client (.*)\].*?vti_bin/){$attempts2{"by $2 on $1"}= "Attempt to exploit vti_bin";}
        if ($ssl_error =~ m/\[(.*)\] \[error\] \[client (.*)\].*?vti_cnf/){$attempts2{"by $2 on $1"}= "Attempt to exploit vti_cnf";}
        if ($ssl_error =~ m/\[(.*)\] \[error\] \[client (.*)\].*?vti_inf/){$attempts2{"by $2 on $1"}= "Attempt to exploit vti_inf";}
        if ($ssl_error =~ m/\[(.*)\] \[error\] \[client (.*)\].*?MSOffice/){$attempts2{"by $2 on $1"}= "Attempt to exploit MSOffice";}
        if ($ssl_error =~ m/\[(.*)\] \[error\] \[client (.*)\].*?default.ida/){$attempts2{"by $2 on $1"}= "Attempt to exploit default.ida";}
        if ($ssl_error =~ m/\[(.*)\] \[error\] \[client (.*)\].*?NULL.printer/){$attempts2{"by $2 on $1"}= "Attempt to exploit NULL.printer";}
        if ($ssl_error =~ m/\[(.*)\] \[error\] \[client (.*)\].*?erroneous characters/){$attempts2{"by $2 on $1"}= "Attempt to use erroneous characters";}
}

##print hackers
while (($key, $value) = each %attempts2) {
        $key =~ m/by (.*?) on /;
        $hackers2{"$1"} += "1";
}
while (($key, $value) = each %requests2) {
        $key =~ m/by (.*?) on /;
        $hackers2{"$1"} += "1";
}
$c = 0;
foreach $hacker2 (sort( { $hackers2{$b} <=> $hackers2{$a} } keys %hackers2)){
        if ($hackers2{$hacker2} >= 2 && $c < 10){
         print "$hacker2<b> $hackers2{$hacker2}</b> attempts<br>\n";
        }
        $c += 1;
        $total_hosts2 += "1";
}
print "<br>";

## print attacks
while (($key, $value) = each %requests2) {
        $attacks2{$value} += "1";
        $total_tries2 += "1";
}
foreach $attack2 (sort( { $attacks2{$b} <=> $attacks2{$a} } keys %attacks2)){
        print "$attack2 <b>$attacks2{$attack2}</b> times<br>\n";
}
print "<br>";

## print exploits
while (($key, $value) = each %attempts2) {
        $exploits2{$value} += "1";
        $total_tries2 += "1";
}
foreach $exploit2 (sort( { $exploits2{$b} <=> $exploits2{$a} } keys %exploits2)){
        print "$exploit2 <b>$exploits2{$exploit2}</b> times<br>\n";
}
print "<br>";

## print totals
print "<h3>There were a total of $total_tries2 attempts by $total_hosts2 persons/hosts , list follows : </h3>\n";

## print details
print "<br><textarea class=input rows=10 style='width:100%'>";
while (($key, $value) = each %attempts2) {
        print "$value $key\n";
}
while (($key, $value) = each %requests2) {
        print "$value $key\n";
}
print "</textarea><hr>";
print "</center>Written by Vlad Alexa Mancini</html>\n";
exit;