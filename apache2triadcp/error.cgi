#!C:/apache2triadpath/perl/bin/perl.exe

$log1 = "C:/apache2triadpath/logs/error.log";
$log2 = "C:/apache2triadpath/logs/ssl_error.log";
$log3 = "C:/apache2triadpath/mysql/logs/myerror.log";
$log4 = "C:/apache2triadpath/php/logs/php_error.log";

print "Content-type: text/html\n\n";
print "<html><head><title>Apache2Triad error logs</title>\n";
print "<link rel=stylesheet href=style.css></head><body>\n";
print "<hr>";

open (LOG1, "$log1")|| die "Can't open $log1\n";
@log1 = <LOG1>;
close (LOG1);
print "<b><center>The Apache server on $ENV{'SERVER_NAME'}:80 most frequent 10 erors:</center></b><br>\n";
foreach $log1 (@log1) {
        if ($log1 =~ m/.*? \[error\] \[client .*?\] (.*)/){$all1{$1} += "1";}
}
foreach $key (sort { $all1{$a} <=> $all1{$b} } keys %all1) {
        push(@all1,"$key <b>$all1{$key} times</b><br>\n");
}
@all1 = reverse(@all1);
splice @all1, 10;
foreach $all1 (@all1) {
        print "<center>$all1</center>";
}
print "<br>";
print "<b><center>The Apache server on $ENV{'SERVER_NAME'}:80 last 100 eror log lines:</center></b><br><textarea class=input rows=10 style='width:100%'>\n";
@log1=reverse(@log1);
splice @log1, 100;
foreach $log1 (@log1) {
        $log1 =~ s/\\r//g;
        print "$log1";
}
print "</textarea><br>";
print "<hr>";

open (LOG2, "$log2")|| die "Can't open $log2\n";
@log2 = <LOG2>;
close (LOG2);
print "<b><center>The Apache server on $ENV{'SERVER_NAME'}:443 most frequent 10 erors:</center></b><br>\n";
foreach $log2 (@log2) {
        if ($log2 =~ m/.*? \[error\] \[client .*?\] (.*)/){$all2{$1} += "1";}
}
foreach $key (sort { $all2{$a} <=> $all2{$b} } keys %all2) {
        push(@all2,"$key <b>$all2{$key} times</b><br>\n");
}
@all2 = reverse(@all2);
splice @all2, 10;
foreach $all2 (@all2) {
        print "<center>$all2</center>";
}
print "<br>";
print "<b><center>The SSL server on $ENV{'SERVER_NAME'}:443 last 100 eror log lines:</center></b><br><textarea class=input rows=10 style='width:100%'>\n";
@log2=reverse(@log2);
splice @log2, 100;
foreach $log2 (@log2) {
        $log2 =~ s/\\r//g;
        print "$log2";
}
print "</textarea><br>";
print "<hr>";

open (LOG3, "$log3")|| die "Can't open $log3\n";
@log3 = <LOG3>;
close (LOG3);
print "<b><center>The MySQL server on $ENV{'SERVER_NAME'}:3306 most frequent 10 erors:</center></b><br>\n";
foreach $log3 (@log3) {
        if ($log3 =~ m/(.*)/){$all3{$1} += "1";}
}
foreach $key (sort { $all3{$a} <=> $all3{$b} } keys %all3) {
        push(@all3,"$key <b>$all3{$key} times</b><br>\n");
}
@all3 = reverse(@all3);
splice @all3, 10;
foreach $all3 (@all3) {
        print "<center>$all3</center>";
}
print "<br>";
print "<b><center>The MySQL server on $ENV{'SERVER_NAME'}:3306 last 100 eror log lines:</center></b><br><textarea class=input rows=10 style='width:100%'>\n";
@log3=reverse(@log3);
splice @log3, 100;
foreach $log3 (@log3) {
         print "$log3";
}
print "</textarea><br>";
print "<hr>";

open (LOG4, "$log4")|| die "Can't open $log4\n";
@log4 = <LOG4>;
close (LOG4);
print "<b><center>The Php server on $ENV{'SERVER_NAME'}:80 most frequent 10 erors:</center></b><br>\n";
foreach $log4 (@log4) {
        if ($log4 =~ m/\[.*?\].*?error: (.*)/i){$all4{$1} += "1";}
}
foreach $key (sort { $all4{$a} <=> $all4{$b} } keys %all4) {
        push(@all4,"$key <b>$all4{$key} times</b><br>\n");
}
@all4 = reverse(@all4);
splice @all4, 10;
foreach $all4 (@all4) {
        print "<center>$all4</center>";
}
print "<br>";
print "<b><center>The Php server on $ENV{'SERVER_NAME'}:80 last 100 eror log lines:</center></b><br><textarea class=input rows=10 style='width:100%'>\n";
@log4=reverse(@log4);
splice @log4, 100;
foreach $log4 (@log4) {
        print "$log4";
}
print "</textarea><br>";
print "</center>Written by Vlad Alexa Mancini</html>\n";
exit;