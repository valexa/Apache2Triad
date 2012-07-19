#!C:/apache2triadpath/perl/bin/perl.exe

print "Content-type: text/html\n\n";

$file = 'count.txt';

$cunt = 0;
open(FILE,"<$file") or die "cant read $file";
$cunt = <FILE>;
close(FILE);
$cunt += 1;
open(FILE,">$file") or die "cant write $file";
print FILE $cunt;
close(FILE);
print "$cunt";
exit;
