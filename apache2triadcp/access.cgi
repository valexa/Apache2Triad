#!C:/apache2triadpath/perl/bin/perl.exe

$show = 100;

$log1 = "C:/apache2triadpath/logs/access.log";
$log2 = "C:/apache2triadpath/logs/ssl_access.log";
$log3 = "C:/apache2triadpath/mysql/logs/myaccess.log";

print "Content-type: text/html\n\n";
print "<html><head><title>Apache2Triad access logs</title>\n";
print "<link rel=stylesheet href=style.css></head><body>\n";
print "<hr>";

#http access log 

$line = 0;
$start = clines($log1) - $show;
open (LOG1, $log1)|| die "Can't open $log1\n";
while (<LOG1>){
	$line++;
	if ($line >= $start){
		push(@log1,$_);	
	}
}
close (LOG1);
@log1=reverse(@log1);
print "<b><center>The Apache server on $ENV{'SERVER_NAME'}:80 last $show access log lines:</center></b><br><textarea class=input rows=10 style='width:100%'>\n";
foreach $log1 (@log1) {
        $log1 =~ m/^(\S*\s)(.*)(\".*\")$/ or print"<b>can not show this line</b>";
        print "$1 $2\n";
}
print "</textarea><hr>";

#https access log

$line = 0;
$start = clines($log2) - $show;
open (LOG2, "$log2")|| die "Can't open $log2\n";
while (<LOG2>){
	$line++;
	if ($line >= $start){
		push(@log2,$_);	
	}
}
close (LOG2);
@log2=reverse(@log2);
print "<b><center>The SSL server on $ENV{'SERVER_NAME'}:443 last $show access log lines:</center></b><br><textarea class=input rows=10 style='width:100%'>\n";
foreach $log2 (@log2) {
        $log2 =~ m/^(\S*\s)(.*)$/ or print"<b>can not show this line</b>";
        print "$1 $2\n";
}
print "</textarea><hr>";

#mysql access log

$line = 0;
$start = clines($log3) - $show;
open (LOG3, "$log3")|| die "Can't open $log3\n";
while (<LOG3>){
	$line++;
	if ($line >= $start){
		push(@log3,$_);	
	}
}
close (LOG3);
@log3=reverse(@log3);
print "<b><center>The Mysql server on $ENV{'SERVER_NAME'}:3306 last $show access log lines:</center></b><br><textarea class=input rows=10 style='width:100%'>\n";
foreach $log3 (@log3) {
        if ($log3 =~ m/^(.*)(Connect)(.*)(on)(.*)$/){
        	print "Connected - $3\n";
	}	
}
print "</textarea><hr>";

print "</center>Written by Vlad Alexa Mancini</html>\n";

sub clines {
    my ($filename) = @_;
    $lines = 0;
    open(FILE, $filename) or die "Can't open `$filename': $!";
    while (sysread FILE, $buffer, 4096) {
	$lines += ($buffer =~ tr/\n//);
    }
    close FILE;
    return $lines
}

exit;